"""
Talon Trader Funding — Account Data Server
==========================================
Connects to Rithmic via the Order plant (required).
PnL plant is optional — if unavailable, falls back to order-plant polling.

talon_config.json:
{
  "username":    "your-rithmic-username",
  "password":    "your-rithmic-password",
  "system_name": "Rithmic Paper Trading",
  "server_url":  "rprotocol.rithmic.com:443",
  "app_name":    "TradeEcho",
  "app_version": "7.4.8",
  "firm_name":   "BluSky"
}
"""

import json, logging, asyncio, threading, time, os
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_socketio import SocketIO
from async_rithmic import RithmicClient
from async_rithmic.objects import ReconnectionSettings

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
logger = logging.getLogger("talon_server")

# ── Config ───────────────────────────────────────────────────────────────────
CONFIG_FILE = "talon_config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump({
                "username":    "YOUR_RITHMIC_USERNAME",
                "password":    "YOUR_RITHMIC_PASSWORD",
                "system_name": "Rithmic Paper Trading",
                "server_url":  "rprotocol.rithmic.com:443",
                "app_name":    "TradeEcho",
                "app_version": "7.4.8",
                "firm_name":   "BluSky"
            }, f, indent=2)
        logger.warning(f"Created template {CONFIG_FILE} — fill in your credentials")
        return None
    with open(CONFIG_FILE) as f:
        cfg = json.load(f)
    missing = [k for k in ["username", "password", "system_name", "server_url"]
               if not cfg.get(k) or "YOUR_" in str(cfg.get(k, ""))]
    if missing:
        logger.error(f"Config missing or placeholder: {missing}")
        return None
    return cfg

# ── Flask + SocketIO ──────────────────────────────────────────────────────────
app = Flask(__name__, static_folder=".")
app.config["SECRET_KEY"] = "talon-2026"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading",
                    logger=False, engineio_logger=False)

# ── Dedicated async event loop ────────────────────────────────────────────────
_loop = None
def _start_loop():
    global _loop
    _loop = asyncio.new_event_loop()
    asyncio.set_event_loop(_loop)
    _loop.run_forever()
threading.Thread(target=_start_loop, daemon=True, name="AsyncLoop").start()
while _loop is None:
    time.sleep(0.01)

def run_async(coro):
    return asyncio.run_coroutine_threadsafe(coro, _loop).result(timeout=30)

# ── Shared state ──────────────────────────────────────────────────────────────
conn_state = {
    "connected":   False,
    "connecting":  False,
    "error":       None,
    "firm_name":   "",
    "last_update": None,
    # Which plants actually connected (filled after connect)
    "plants_up":   [],
    "pnl_plant_up":   False,
    "order_plant_up": False,
}

# All discovered accounts  { account_id: data_dict }
accounts    = {}
selected_id = None
_client     = None

# ── Account helpers ───────────────────────────────────────────────────────────
def _new_acct(acct_id, acct_name=""):
    return {
        "account_id":       acct_id,
        "account_name":     acct_name,
        "balance":          0.0,
        "equity":           0.0,
        "starting_balance": 0.0,
        "day_pnl":          0.0,
        "day_closed_pnl":   0.0,
        "open_pnl":         0.0,
        "net_qty":          0,
        "altv":             0.0,
        "daily_dd_used":    0.0,
        "margin_balance":   0.0,
        "buying_power":     0.0,
        "equity_history":   [],
        "pnl_history":      [],
        "fills":            [],
        "streaming":        False,
        "last_update":      None,
    }

def safe_float(v, d=0.0):
    try:
        return float(v) if v not in (None, "") else d
    except Exception:
        return d

def _push(acct_id):
    if acct_id not in accounts:
        return
    payload = {
        **accounts[acct_id],
        "connected":  conn_state["connected"],
        "firm_name":  conn_state["firm_name"],
        "timestamp":  datetime.now().isoformat(),
    }
    socketio.emit("account_update", payload)

def _push_list():
    socketio.emit("accounts_discovered", {
        "accounts": [
            {"account_id":   aid,
             "account_name": d["account_name"],
             "balance":      d["balance"],
             "day_pnl":      d["day_pnl"],
             "net_qty":      d["net_qty"],
             "streaming":    d["streaming"]}
            for aid, d in accounts.items()
        ],
        "count":     len(accounts),
        "firm_name": conn_state["firm_name"],
    })

def _append_history(acct):
    ts = datetime.now().strftime("%H:%M:%S")
    acct["equity_history"].append({"t": ts, "v": round(acct["equity"],  2)})
    acct["pnl_history"].append(   {"t": ts, "v": round(acct["day_pnl"], 2)})
    if len(acct["equity_history"]) > 60:
        acct["equity_history"] = acct["equity_history"][-60:]
    if len(acct["pnl_history"])   > 60:
        acct["pnl_history"]    = acct["pnl_history"][-60:]

# ── PnL streaming handlers (used when pnl plant is connected) ─────────────────
def setup_pnl_handlers(client):

    async def on_instrument_pnl(r):
        acct_id = getattr(r, "account_id", "") or ""
        if not acct_id:
            return
        if acct_id not in accounts:
            accounts[acct_id] = _new_acct(acct_id)
            logger.info(f"Account discovered via instrument-pnl stream: {acct_id}")
            _push_list()
        a = accounts[acct_id]
        a["open_pnl"]    = safe_float(getattr(r, "open_position_pnl", 0))
        a["day_pnl"]     = safe_float(getattr(r, "day_pnl", 0))
        a["net_qty"]     = int(getattr(r, "net_quantity",  0) or 0)
        a["equity"]      = a["balance"] + a["open_pnl"]
        a["streaming"]   = True
        a["last_update"] = datetime.now().isoformat()
        if acct_id == selected_id:
            _push(acct_id)

    async def on_account_pnl(r):
        acct_id = getattr(r, "account_id", "") or ""
        if not acct_id:
            return
        if acct_id not in accounts:
            accounts[acct_id] = _new_acct(acct_id)
            logger.info(f"Account discovered via account-pnl stream: {acct_id}")
            _push_list()
        a   = accounts[acct_id]
        bal  = safe_float(getattr(r, "account_balance",        0))
        opnl = safe_float(getattr(r, "open_position_pnl",      0))
        dpnl = safe_float(getattr(r, "day_pnl",                0))
        cpnl = safe_float(getattr(r, "closed_position_pnl",    0))
        nqty = int(getattr(r, "net_quantity",                   0) or 0)
        altv = safe_float(getattr(r, "min_account_balance",    0))
        mar  = safe_float(getattr(r, "margin_balance",         0))
        bpow = safe_float(getattr(r, "available_buying_power", 0))

        if a["starting_balance"] == 0.0 and bal > 0:
            a["starting_balance"] = bal
            logger.info(f"[{acct_id}] Starting balance captured: ${bal:,.2f}")

        a.update(balance=bal, equity=bal + opnl, day_pnl=dpnl,
                 day_closed_pnl=cpnl, open_pnl=opnl, net_qty=nqty,
                 margin_balance=mar, buying_power=bpow,
                 streaming=True, last_update=datetime.now().isoformat())

        if altv > 0:
            a["altv"] = altv
            if a["starting_balance"] > 0:
                a["daily_dd_used"] = max(0.0, a["starting_balance"] - bal)

        _append_history(a)
        _push(acct_id)
        _push_list()
        logger.debug(f"[{acct_id}] bal=${bal:,.2f}  dpnl=${dpnl:,.2f}  opnl=${opnl:,.2f}")

    client.on_instrument_pnl_update += on_instrument_pnl
    client.on_account_pnl_update    += on_account_pnl
    logger.info("PnL streaming handlers registered")

# ── Fill handler ──────────────────────────────────────────────────────────────
def setup_fill_handler(client):
    async def on_fill(r):
        acct_id = getattr(r, "account_id", "") or ""
        if not acct_id or acct_id not in accounts:
            return
        fill = {
            "time":    datetime.now().strftime("%H:%M:%S"),
            "symbol":  getattr(r, "symbol",               "?"),
            "side":    "LONG" if getattr(r, "transaction_type", 1) == 1 else "SHORT",
            "qty":     int(getattr(r, "fill_size",    0) or 0),
            "price":   safe_float(getattr(r, "fill_price",    0)),
            "pnl":     safe_float(getattr(r, "closed_position_pnl", 0)),
            "account": acct_id,
        }
        accounts[acct_id]["fills"].insert(0, fill)
        accounts[acct_id]["fills"] = accounts[acct_id]["fills"][:50]
        socketio.emit("new_fill", fill)
    if hasattr(client, "on_exchange_order_notification"):
        client.on_exchange_order_notification += on_fill

# ── Account discovery (order plant) ──────────────────────────────────────────
async def _discover(client):
    global selected_id
    try:
        plant = client.plants.get("order")
        if not plant:
            logger.warning("Order plant not present — cannot discover accounts")
            return
        if not getattr(plant, "is_connected", False):
            logger.warning("Order plant not connected — cannot discover accounts")
            return
        raw_accounts = getattr(plant, "accounts", None) or []
        if not raw_accounts:
            logger.warning("No accounts in order plant — will discover via PnL stream")
            return
        found = []
        for a in raw_accounts:
            aid   = getattr(a, "account_id",   "") or ""
            aname = getattr(a, "account_name", "") or aid
            if not aid:
                continue
            if aid not in accounts:
                accounts[aid] = _new_acct(aid, aname)
            found.append(aid)
            logger.info(f"  Account found: {aid}  ({aname})")
        if found and selected_id is None:
            selected_id = found[0]
            logger.info(f"  Auto-selected: {selected_id}")
        _push_list()
        socketio.emit("activity_log", {
            "message": f"✓ {len(found)} account(s) found: {', '.join(found)}",
            "level":   "success"})
    except Exception as e:
        logger.error(f"Account discovery error: {e}")

# ── Connect ───────────────────────────────────────────────────────────────────
async def _connect(cfg):
    global _client
    conn_state.update(connecting=True, connected=False, error=None,
                      firm_name=cfg.get("firm_name", "Rithmic"),
                      plants_up=[], pnl_plant_up=False, order_plant_up=False)

    socketio.emit("status_change", {"connecting": True, "connected": False})
    socketio.emit("activity_log", {
        "message": f"Connecting {cfg['username']} → {cfg['server_url']} ...",
        "level":   "info"})

    try:
        client = RithmicClient(
            user        = cfg["username"],
            password    = cfg["password"],
            system_name = cfg["system_name"],
            app_name    = cfg.get("app_name",    "TradeEcho"),
            app_version = cfg.get("app_version", "7.4.8"),
            url         = cfg["server_url"],
            reconnection_settings=ReconnectionSettings(
                max_retries=5, backoff_type="linear", interval=10, max_delay=60))

        # Register handlers before connecting
        setup_pnl_handlers(client)
        setup_fill_handler(client)

        # Pre-warm PnL subscription flag (OrderClone pattern)
        try:
            client.plants["pnl"]._subscriptions["pnl"].add(1)
        except Exception:
            pass

        # Connect — client.py patch makes ticker/pnl/history optional
        await client.connect()

        # ── Inventory which plants actually connected ──────────────────
        plants_up = []
        for pname, plant in client.plants.items():
            up = getattr(plant, "is_connected", False)
            status = "✓" if up else "✗ (skipped)"
            logger.info(f"  Plant '{pname}': {status}")
            if up:
                plants_up.append(pname)

        pnl_up   = "pnl"   in plants_up
        order_up = "order" in plants_up

        if not order_up:
            raise RuntimeError("Order plant did not connect — cannot continue")

        conn_state.update(connected=True, connecting=False,
                          plants_up=plants_up,
                          pnl_plant_up=pnl_up,
                          order_plant_up=order_up)

        _client = client

        logger.info(f"✓ Connected to {cfg.get('firm_name','Rithmic')}  "
                    f"(plants: {', '.join(plants_up)})")

        if not pnl_up:
            logger.warning("PnL plant unavailable — falling back to order-plant polling")
            socketio.emit("activity_log", {
                "message": "⚠ PnL plant unavailable — using order-plant polling for balances",
                "level":   "warning"})

        # Discover accounts from order plant
        await _discover(client)

        socketio.emit("status_change", {
            "connecting": False,
            "connected":  True,
            "firm_name":  cfg.get("firm_name", ""),
            "plants_up":  plants_up,
        })
        return True

    except Exception as e:
        logger.error(f"Connection failed: {e}")
        import traceback; traceback.print_exc()
        conn_state.update(connecting=False, connected=False, error=str(e))
        socketio.emit("status_change", {"connecting": False, "connected": False, "error": str(e)})
        socketio.emit("activity_log", {"message": f"✗ Failed: {e}", "level": "error"})
        return False

# ── Background PnL poller ─────────────────────────────────────────────────────
def _poll_loop():
    """
    Polls account summary as fallback / supplement to streaming.
    500ms when open positions exist, 5s when flat.
    Tries list_account_summary() (pnl plant) first;
    if pnl plant is down, logs a one-time warning and stops polling.
    """
    FAST, SLOW = 0.5, 5.0
    last_poll  = 0.0
    pnl_warn_shown = False

    while True:
        time.sleep(0.1)
        if not conn_state["connected"] or _client is None:
            continue
        now     = time.time()
        has_pos = any(d["net_qty"] != 0 for d in accounts.values())
        if now - last_poll < (FAST if has_pos else SLOW):
            continue
        last_poll = now

        # If pnl plant is not up, polling via list_account_summary won't work
        if not conn_state.get("pnl_plant_up", False):
            if not pnl_warn_shown:
                logger.warning("PnL plant not up — balance polling unavailable. "
                               "Data will update via order-fill events only.")
                pnl_warn_shown = True
            continue

        try:
            plant = _client.plants.get("order")
            if not plant or not getattr(plant, "accounts", None):
                continue
            raccts = plant.accounts
            for ra in raccts:
                aid = getattr(ra, "account_id", "") or ""
                if not aid:
                    continue
                if aid not in accounts:
                    accounts[aid] = _new_acct(aid)
                    _push_list()
                try:
                    sums = run_async(
                        _client.list_account_summary()
                        if len(raccts) == 1
                        else _client.list_account_summary(account_id=aid))
                    for s in (sums or []):
                        if getattr(s, "account_id", "") != aid:
                            continue
                        a    = accounts[aid]
                        bal  = safe_float(getattr(s, "account_balance",        0))
                        opnl = safe_float(getattr(s, "open_position_pnl",      0))
                        dpnl = safe_float(getattr(s, "day_pnl",                0))
                        cpnl = safe_float(getattr(s, "closed_position_pnl",    0))
                        nqty = int(getattr(s, "net_quantity",                   0) or 0)
                        mar  = safe_float(getattr(s, "margin_balance",         0))
                        bpow = safe_float(getattr(s, "available_buying_power", 0))
                        altv = safe_float(getattr(s, "min_account_balance",    0))

                        if a["starting_balance"] == 0.0 and bal > 0:
                            a["starting_balance"] = bal

                        a.update(balance=bal, equity=bal + opnl,
                                 day_pnl=dpnl, day_closed_pnl=cpnl,
                                 open_pnl=opnl, net_qty=nqty,
                                 margin_balance=mar, buying_power=bpow,
                                 last_update=datetime.now().isoformat())

                        if altv > 0:
                            a["altv"] = altv
                            if a["starting_balance"] > 0:
                                a["daily_dd_used"] = max(0.0, a["starting_balance"] - bal)

                        _append_history(a)
                        _push(aid)
                except Exception as e:
                    logger.debug(f"Poll [{aid}]: {e}")
        except Exception as e:
            logger.debug(f"Poll loop outer: {e}")

threading.Thread(target=_poll_loop, daemon=True, name="PnLPoller").start()

# ── HTTP Routes ───────────────────────────────────────────────────────────────
@app.route("/")
def root():
    return send_from_directory(".", "dashboard.html")

@app.route("/dashboard.html")
def dash():
    return send_from_directory(".", "dashboard.html")

@app.route("/api/status")
def api_status():
    return jsonify({
        **conn_state,
        "account_count":       len(accounts),
        "selected_account":    selected_id,
        "discovered_accounts": list(accounts.keys()),
    })

@app.route("/api/accounts")
def api_accounts():
    return jsonify([
        {"account_id":   aid,
         "account_name": d["account_name"],
         "balance":      d["balance"],
         "equity":       d["equity"],
         "day_pnl":      d["day_pnl"],
         "open_pnl":     d["open_pnl"],
         "net_qty":      d["net_qty"],
         "altv":         d["altv"],
         "streaming":    d["streaming"],
         "last_update":  d["last_update"]}
        for aid, d in accounts.items()])

@app.route("/api/account/<acct_id>")
def api_account(acct_id):
    if acct_id not in accounts:
        return jsonify({"error": "Not found"}), 404
    return jsonify({**accounts[acct_id], "connected": conn_state["connected"]})

@app.route("/api/account/<acct_id>/select", methods=["POST"])
def api_select(acct_id):
    global selected_id
    if acct_id not in accounts:
        return jsonify({"error": "Not found"}), 404
    selected_id = acct_id
    _push(acct_id)
    return jsonify({"success": True, "selected": acct_id})

@app.route("/api/account/summary")
def api_summary():
    if not selected_id or selected_id not in accounts:
        return jsonify({"connected": conn_state["connected"], "account_id": None})
    d = accounts[selected_id]
    return jsonify({
        "connected":  conn_state["connected"],
        "account_id": selected_id,
        **{k: d[k] for k in ["balance", "equity", "day_pnl", "open_pnl",
                               "net_qty", "altv", "daily_dd_used", "last_update"]},
    })

@app.route("/api/account/fills")
def api_fills():
    aid = request.args.get("account_id", selected_id)
    return jsonify(accounts[aid]["fills"] if aid and aid in accounts else [])

@app.route("/api/connect", methods=["POST"])
def api_connect():
    cfg = load_config()
    if not cfg:
        return jsonify({"success": False, "error": "Invalid talon_config.json"}), 400
    threading.Thread(target=lambda: run_async(_connect(cfg)), daemon=True).start()
    return jsonify({"success": True})

@app.route("/api/disconnect", methods=["POST"])
def api_disconnect():
    global _client, selected_id
    if _client:
        try:
            run_async(_client.disconnect())
        except Exception:
            pass
        _client = None
    accounts.clear()
    selected_id = None
    conn_state.update(connected=False, connecting=False,
                      plants_up=[], pnl_plant_up=False, order_plant_up=False)
    socketio.emit("status_change", {"connected": False})
    socketio.emit("accounts_discovered", {"accounts": [], "count": 0})
    return jsonify({"success": True})

# ── SocketIO events ───────────────────────────────────────────────────────────
@socketio.on("connect")
def on_ws_connect():
    socketio.emit("status_change", {
        "connected":  conn_state["connected"],
        "connecting": conn_state["connecting"],
        "firm_name":  conn_state["firm_name"],
        "plants_up":  conn_state.get("plants_up", []),
    })
    if accounts:
        _push_list()
        if selected_id:
            _push(selected_id)

@socketio.on("request_snapshot")
def on_snapshot():
    if selected_id:
        _push(selected_id)
    _push_list()

@socketio.on("select_account")
def on_select(data):
    global selected_id
    aid = data.get("account_id")
    if aid and aid in accounts:
        selected_id = aid
        _push(aid)
        logger.info(f"Dashboard switched to: {aid}")

# ── Auto-connect on startup ───────────────────────────────────────────────────
def _auto_connect():
    time.sleep(1.5)
    cfg = load_config()
    if cfg:
        logger.info("Auto-connecting on startup...")
        run_async(_connect(cfg))
    else:
        logger.warning("Edit talon_config.json then POST /api/connect")

threading.Thread(target=_auto_connect, daemon=True, name="AutoConnect").start()

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  TALON TRADER FUNDING — Account Data Server")
    print("  Dashboard: http://localhost:5100")
    print("  Accounts:  http://localhost:5100/api/accounts")
    print("  Status:    http://localhost:5100/api/status")
    print("=" * 60 + "\n")
    socketio.run(app, host="0.0.0.0", port=5100, debug=False,
                 allow_unsafe_werkzeug=True)
