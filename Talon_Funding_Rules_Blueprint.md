# TALON FUNDING — COMPLETE RULES BLUEPRINT
## Confidential Strategic Document — Version 1.0

---

## ACCOUNT TYPES

### TYPE A — SPRINT (Non-Recurring, One-Time)
**The "nothing to lose" entry point**

- One-time fee, 30-day window, auto-deactivates at month end
- No renewal. Trader must purchase new account to continue.
- List price: $149–$449 depending on account size
- Standard discount: 90% → effective price: **$14.95–$44.95**
- Affiliate/code price: **$9.95–$19.95** (the real volume driver)
- Reset: N/A — account simply deactivates. Buy a new Sprint.
- Design intent: Traders who fail just buy another. $19.95 feels like nothing.
  At 500 Sprint accounts/month at avg $19.95 = $9,975 revenue,
  near zero payout exposure since the 30-day window limits funded conversions.

### TYPE B — STANDARD (Recurring Monthly Subscription)
**The committed trader path**

- Recurring monthly subscription, continues until cancelled or funded
- List price: $199–$599 depending on account size
- Month 1 discount: 90% → effective price: **$19.95–$59.95**
- Renewal months: 80% discount → effective price: **$39.95–$119.95**
- Reset fee: $19.95–$49.95 (cheaper than buying new = encourages retry)
- Design intent: Trader thinks they're saving money by staying subscribed.
  Each renewal month = pure recurring revenue. Average trader fails 3–6 months.

---

## EVALUATION (QUALIFICATION) PHASE RULES

### E-1: Profit Target — 5% (INDUSTRY DIFFERENTIATOR)
- $25K account: $1,250 target
- $50K account: $2,500 target ← ONLY firm at this level industry-wide
- $100K account: $5,000 target
- $150K account: $7,500 target
- Marketing headline: "We're the only prop firm that trusts a 5% proof."
- House mechanic: Target is largely irrelevant — drawdown mechanics kill
  accounts before the target is reached in the majority of cases.

### E-2: Drawdown Structure — EOD Trailing ONLY
- $25K account: $1,250 EOD trailing drawdown
- $50K account: $2,000 EOD trailing drawdown
- $100K account: $3,500 EOD trailing drawdown
- $150K account: $5,000 EOD trailing drawdown
- Stops trailing when locked at initial starting balance + $100
- NO intraday trailing — EOD only (major marketing advantage over Apex)
- House mechanic: $2,000 EOD on $50K is the tightest EOD number in the market.
  One bad CL session wipes the evaluation account.

### E-3: Daily Loss Limit (DLL)
- $25K: $500 DLL
- $50K: $1,000 DLL
- $100K: $2,000 DLL
- $150K: $3,000 DLL
- When DLL hit: account suspended for remainder of trading day. NOT failed.
- Marketing: "We protect you from yourself — we pause you, not punish you."
- House mechanic: CL at 10 contracts = $500 DLL in ~5 adverse price moves.
  A gambler on the one-day Sprint path hits this within minutes.

### E-4: Minimum Trading Days — FLEXIBLE PATHS

**Path A — One-Day Sprint (Sprint accounts only):**
- No minimum trading days. Trader can attempt to pass in a single session.
- Contract limit during One-Day path: 3 contracts maximum.
- Marketing: "Go all-in. Sprint accounts have zero minimum day requirements."
- House mechanic: 3 contracts CL = ~$300/point. The $1,000 DLL is reached
  in approximately 3 adverse ticks. Encourages all-or-nothing behavior.
  Fast blow-up rate generates high-volume Sprint repurchases.

**Path B — Standard Multi-Day (all account types):**
- Minimum 5 trading days required.
- Full contract allowance per scaling plan.
- House mechanic: 5 days of DLL and EOD drawdown exposure.

### E-5: Contract Scaling Plan (Standard Path)
- $25K: 2 contracts (ES/NQ), 1 contract (CL)
- $50K: 5 contracts (ES/NQ), 3 contracts (CL)
- $100K: 10 contracts (ES/NQ), 5 contracts (CL)
- $150K: 15 contracts (ES/NQ), 8 contracts (CL)
- Micros: 10x allowance at all tiers (MES, MNQ, MCL)
- Note: CL intentionally has lower contract limits than ES/NQ at every tier.
  CL is $1,000/tick at standard size. This is necessary CL-specific risk control.
- House mechanic: At 5 CL contracts, the $1,000 DLL is hit in 2 adverse ticks.
  Sounds generous. Is extremely punishing.

### E-6: No Consistency Rule During Evaluation
- Zero consistency restriction during the qualification phase.
- Trader can make 100% of profit in one trade on one day.
- Marketing: "Hit a big NFP move? Keep every dollar. Zero consistency trap."
- House mechanic: Consistency rule activates hard in the funded phase.
  Traders who pass via one large day are the most likely candidates
  to violate the funded-phase consistency rule on their first payout request.

### E-7: News Trading — ALLOWED
- All major news events permitted during evaluation.
- No mandatory flat periods before or after high-impact releases.
- DLL remains active during news — a bad NFP trade still hits the daily limit.

### E-8: OrderClone — FREE, RESTRICTED TO TALON/RITHMIC
- OrderClone provided FREE to all Talon account holders.
- Restricted to Talon accounts only via Rithmic data feed.
- Copying FROM any external source is PROHIBITED (see V-3).
- Traders may designate one account as "master" to copy to their
  other Talon evaluation accounts simultaneously.
- Encourages multi-account purchases — each copied account = separate eval fee.
- House mechanic: Execution slippage between master and copy accounts
  (1–3 ticks per trade) creates systematically worse P&L on copies.
  A master account that barely passes will produce copies that blow up
  due to tick-level execution differences, especially on CL.

### E-9: Prohibited Practices
- V-1: External signal copying strictly prohibited.
  If detected: account voided, no refund, permanent ban.
- V-2: Third-party account trading services prohibited.
  Any arrangement where a non-registered trader operates the account
  voids the contract and forfeits all profits and fees paid.
  (Explicitly targets "we'll trade your prop account for 30%" services.)
- V-3: HFT, latency arbitrage, tick scalping: prohibited.
- V-4: Account sharing: prohibited.
- Enforcement: Rithmic trade data reviewed for pattern anomalies.
  Sudden style changes between evaluation and funded phase trigger review.

---

## FUNDED (SIM MASTER) PHASE RULES

### F-1: Activation Gate — 3 Active Accounts Maximum
- Trader may hold unlimited passed evaluations in an inactive queue.
- Maximum 3 active funded (SIM Master) accounts at any time.
- To activate a 4th: one of the 3 active accounts must reach
  starting balance + $500 (profit lock milestone).
- Each subsequent activation requires the same milestone on the most
  recently activated account.
- Marketing: "Earn your way to more capital. Hit milestones, unlock accounts."
- House mechanic: Traders with 5–10 passed evals sitting in queue
  cannot convert them. Queue creates pressure to keep buying Sprint evals
  while waiting — generating ongoing evaluation revenue from the same trader.
  (This is the model you personally experienced with Bulenox — 10 passed,
  only 2 active. Talon adopts and tightens this.)

### F-2: Payout Qualifying Structure
- Minimum qualifying days since last payout: **3 days**
  (vs. industry standard 8–10 — sounds dramatically better)
- Qualifying day definition: net closed profit of **$500 or more** that session.
  (vs. Apex $250, Topstep $200 — buried in the fine print)
- Marketing: "Get paid after just 3 qualifying days. Fastest structure anywhere."
- House mechanic: $500/day threshold means a trader needs $1,500 minimum
  in qualifying-day profits before requesting first payout.
  In a $2,000 EOD account, generating 3 separate $500+ sessions without
  triggering the DLL or breaching the account is genuinely difficult.

### F-3: Consistency Rule — Funded Phase Only (40% Cap)
- No single trading day may account for more than 40% of total net
  profit since the last approved payout at time of withdrawal request.
- Formula: Best Day P&L ÷ Total P&L must be < 40%
- Account stays active if violated — trader must continue trading to comply.
- Marketing: "A fair 40% guideline promotes long-term account health."
- House mechanic: Traders who pass evaluation via one large day (permitted
  under E-6) will almost certainly violate this on the first payout request.
  They must dilute the big day with additional $500+ qualifying sessions.
  Each extra session resets DLL exposure and brings account closer to breach.

### F-4: Immediate Balance Deduction on Payout Request
- Requested amount is immediately deducted from account balance
  the moment the payout is submitted (shown as "pending").
- Processing time: 5–7 business days.
- Trader MAY continue trading during processing.
- If account balance falls below safety threshold BEFORE processing completes:
  payout request is CANCELLED. Trader must rebuild buffer and reapply.
- House mechanic: Balance deduction brings account to near-threshold.
  A bad session during processing simultaneously cancels the payout AND
  potentially breaches the account. Trader loses both.

### F-5: Inactivity Penalty Rule
- After submitting a payout request, trader must log a minimum of
  1 qualifying day ($500+ net) within every 5 calendar days during processing.
- Missing a 5-day window: payout request suspended, requires resubmission.
  Account re-enters the full 3 qualifying day requirement.
- Marketing: "Active traders are funded traders. We keep accounts moving."
- House mechanic: Forces trading during the most financially fragile account
  period — when balance is near threshold following the F-4 deduction.

### F-6: Post-Request Compliance Rule
- Qualifying days logged AFTER payout request must also comply with
  the 40% consistency rule relative to the full profit total.
- If post-request trading creates a new largest-day violation,
  payout request goes on hold until compliance is fully restored.
- House mechanic: Prevents traders from simply trading more to dilute
  a big day — new big days extend the compliance requirement indefinitely.

### F-7: Safety Threshold Buffer
- Account balance must remain a minimum of $100 above the drawdown
  threshold floor to be eligible for a payout request.
- Maximum payout per request: 80% of profit above safety threshold.
- Remaining 20% stays as required working capital in the account.
- House mechanic: Trader can never fully empty the account. Working capital
  remains at risk, maintaining ongoing DLL and drawdown exposure.

### F-8: Profit Reinvestment Option — INDUSTRY FIRST
- Optional at time of payout request: trader may elect to dedicate
  10% or 20% of the payout to a "Live Account Credit Pool."
- When credit pool reaches $1,000 (on $50K accounts), trader earns
  an unlock credit toward a future live-capital account tier.
- Marketing: "Build toward real capital by reinvesting your sim profits.
  Talon rewards traders who commit to the long game."
- House mechanic: 10–20% of payout is voluntarily retained per request.
  Reduces actual cash outflow per payout cycle.
  Credits are forfeited upon account breach — the most likely outcome.

### F-9: Profit Split Ladder
- Payouts 1–3: 80% to trader / 20% Talon
- Payouts 4–6: 85% to trader / 15% Talon
- Payouts 7+: 90% to trader / 10% Talon
- Ladder resets to Payout 1 if account is breached and re-funded.

---

## PROHIBITED PRACTICES — FUNDED PHASE

All V-1 through V-4 from evaluation phase remain active, plus:

- V-5: Strategy change detection.
  Trading pattern analyzed across evaluation and funded phases via Rithmic data.
  Significant divergence triggers compliance review and potential suspension.
  (Prevents evaluation farming with one strategy, then funded trading another.)

- V-6: Payout farming detection.
  Mechanical trading patterns designed purely to accumulate qualifying days
  without genuine directional intent will be flagged for review.

---

## MARKETING POSITIONING SUMMARY

### What Talon Says Publicly:
✅ "5% profit target — only firm in the industry at this level"
✅ "EOD drawdown only — intraday swings never count against you"
✅ "No consistency rule during your evaluation — ever"
✅ "Pass in one day on Sprint accounts — zero minimums"
✅ "Get paid after just 3 qualifying days — fastest structure anywhere"
✅ "News trading fully allowed — no restrictions"
✅ "OrderClone included free — run multiple accounts on Rithmic"
✅ "No activation fee when you pass"
✅ "No instrument rug-pulls — your markets are always your markets"
✅ "Reinvest profits toward a live funded account"

### What the Rules Actually Do:
🏦 5% target irrelevant — drawdown ends 85%+ of evals before target
🏦 EOD $2,000/$50K is tighter than most intraday competitors
🏦 No eval consistency = passes by one-day gamblers = funded violations
🏦 One-day Sprint has 3-contract limit = DLL hit in seconds on CL
🏦 3 qualifying days sounds easy; $500/day threshold makes it hard
🏦 Immediate deduction + continued trading = dual breach/cancel risk
🏦 Inactivity rule forces trading during highest-risk account period
🏦 40% consistency + post-request compliance creates moving compliance target
🏦 OrderClone slippage systematically degrades copy account P&L
🏦 Activation gate holds eval inventory — forces more Sprint purchases
🏦 80% payout cap + 20% working capital never leaves the account

---

## ORDERCLONE — STRATEGIC ROLE AT TALON FUNDING

OrderClone is NOT a signal service. It is Talon's proprietary,
Rithmic-native trade copier. Its role in the Talon business model:

1. EVALUATION FEE MULTIPLIER:
   One committed trader with 5 eval accounts = 5 separate fees.
   OrderClone makes running 5 simultaneous accounts trivial for the trader.
   Multi-account purchases become the norm, not the exception.

2. SYSTEMATIC FAILURE RATE ADVANTAGE:
   Execution slippage on copies (1–3 ticks per trade on ES/NQ/CL)
   creates systematically worse P&L on sub-accounts vs master.
   A master account that barely passes will generate copies that
   blow up before reaching the profit target due to cumulative tick drag.

3. PLATFORM STICKINESS / LOCK-IN:
   Free, proprietary, Talon+Rithmic only. Trader cannot take it to
   BluSky or Apex. OrderClone is a retention and acquisition tool simultaneously.

4. PAYOUT THREAT BLOCKER:
   By explicitly prohibiting external copying and third-party account
   trading services in the contract, the primary arbitrage risk is eliminated.
   No professional trading service can run 10 Talon funded accounts
   simultaneously without triggering V-2 contract termination.

---

*Talon Funding — Rules Blueprint v1.0 — Confidential*
