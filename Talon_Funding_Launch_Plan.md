# TALON FUNDING — STEP BY STEP LAUNCH PLAN
## Minimum Viable Launch to Revenue Day 1
### Confidential — Version 1.0

---

## CRITICAL PREMISE
Talon Funding is a 100% SIM prop firm.
No real capital is ever deployed for trading.
All "funded" accounts are simulated environments.
Payouts are funded entirely by challenge fee revenue.
This means: ZERO trading capital reserve required.
Total startup spend is technology + legal + marketing ONLY.

---

## PHASE 0 — DECISIONS TO MAKE BEFORE SPENDING A DOLLAR
### Timeline: Week 1 | Cost: $0

These decisions lock in your cost structure. Get them wrong
and you waste money. Get them right and you launch lean.

### Decision 1: White Label vs. Custom Build
ANSWER: White Label — mandatory at launch.
- Custom build: $100,000–$300,000 minimum, 6–12 months
- White label with Rithmic: $1,500–$5,000 setup + $500–$2,000/month
- White label gets you to revenue in 30 days, not 12 months
- Recommended provider: YourPropFirm.com (supports Rithmic natively,
  includes CRM, dashboard, evaluation engine, payment integration,
  automated rule enforcement, and payout system out of the box)

### Decision 2: Business Entity — Where to Register
ANSWER: Wyoming LLC (lowest cost, best protection, no state income tax)
- Wyoming LLC filing fee: $102
- Registered agent (Wyoming): $50/year
- No annual report fee for first year
- DO NOT register in your home state if it has higher fees
- Alternative: Delaware LLC ($90 filing, $50 registered agent)

### Decision 3: SIM Platform — Rithmic vs. Tradovate
ANSWER: Rithmic
- OrderClone is built on Sierra Chart/Rithmic infrastructure
- Rithmic SIM is the industry standard for serious futures prop firms
- Gives you NinjaTrader + Sierra Chart + Quantower + R|Trader Pro
  compatibility — widest platform access in the industry
- Tradovate is Tradovate only (limits OrderClone integration)

### Decision 4: Payment Processor
ANSWER: Stripe (primary) + Crypto option via Coinbase Commerce
- Stripe: 2.9% + $0.30 per transaction
- No monthly fee, no setup cost
- Supports recurring subscriptions for Standard accounts
- International cards accepted automatically
- Crypto option: free to set up, attracts international traders where
  wire transfers are difficult

### Decision 5: Operating Location
ANSWER: Operate as US LLC but consider trader-facing address options.
- A PO Box or virtual office address ($25–50/month) avoids exposing
  home address in public LLC filings
- Wyoming LLC filings are minimal — member names not required

---

## PHASE 1 — LEGAL & BUSINESS FOUNDATION
### Timeline: Week 1–2 | Total Cost: $550–$900

### Step 1.1: Form Wyoming LLC
- Cost: $102 (Wyoming Secretary of State filing fee)
- Method: File online at wyobiz.wyo.gov — takes 24–48 hours
- Entity name: "Talon Funding LLC" (check availability first)
- Registered agent: Wyoming Registered Agent ($50/year)
  Options: Northwest Registered Agent, Registered Agents Inc.
- Total Step 1.1: $152

### Step 1.2: Get EIN (Employer Identification Number)
- Cost: $0 — IRS issues EIN free online at irs.gov
- Takes 10 minutes online
- Required for: bank account, Stripe, Deel/payouts, 1099s to traders
- Total Step 1.2: $0

### Step 1.3: Open Business Bank Account
- Cost: $0 — use Mercury Bank (free business checking, no minimums,
  wire transfers included, built for tech/startup businesses)
- Alternative: Relay Bank ($0 monthly fee, multiple sub-accounts)
- DO NOT use personal bank account — comingles funds, destroys LLC protection
- Total Step 1.3: $0

### Step 1.4: Legal Documents (Non-Negotiable)
You need THREE documents before accepting a single payment:

A) Trader Agreement / Terms of Service
   - This is the most important document in the entire business
   - Must include: sim-only disclaimer, no real capital language,
     all payout rules, V-1 through V-6 prohibitions, account
     activation gate terms, inactivity rule, OrderClone usage policy,
     third-party account trading prohibition with forfeiture clause,
     arbitration clause (prevents class action lawsuits),
     governing law (Wyoming), jurisdiction clause
   - Option 1: Hire a fintech attorney familiar with prop firms: $1,500–3,000
   - Option 2: Purchase a template from PropFirmLegal or similar
     specialized services: $300–600 (then have attorney review)
   - RECOMMENDED: Start with template ($400), have local attorney
     review/customize ($300 for 1hr consultation) = $700 total
   - This document is your primary liability shield

B) Privacy Policy
   - Required by Stripe, required by law (GDPR if you have EU traders)
   - Cost: $0 — use Termly.io or iubenda free tier
   - Generate automatically, customize with Talon name

C) Risk Disclosure Statement
   - One-page document: "Trading futures involves substantial risk of
     loss. Talon Funding accounts are simulated environments. Profits
     and losses in evaluation accounts are not real. Payouts on
     funded accounts are paid from Talon Funding LLC operating revenue."
   - Cost: $0 — write this yourself, have attorney glance at it

- Total Step 1.4: $700–$1,000

### Step 1.5: Virtual Office / Business Address
- Cost: $25–$50/month
- Use for: Stripe business address, website contact, LLC filing
- Options: iPostal1, Regus virtual office, PostScan Mail
- Total Step 1.5: $25–50/month (ongoing)

### PHASE 1 TOTAL: $877–$1,202 one-time + $25–50/month

---

## PHASE 2 — TECHNOLOGY STACK
### Timeline: Week 2–5 | Total Cost: $2,000–$4,500 setup + $800–$1,500/month

### Step 2.1: White Label Platform (YourPropFirm + Rithmic)
YourPropFirm.com is the recommended provider because:
- Native Rithmic integration (required for OrderClone)
- Includes: trader dashboard, CRM, challenge management,
  automated rule enforcement, payout system, affiliate management
- Multi-platform support: NinjaTrader, Sierra Chart, Quantower,
  R|Trader Pro (all Rithmic-compatible platforms)
- Setup time: approximately 10–14 days once contract signed
- Pricing (estimated — must negotiate directly):
  - Setup fee: $1,500–$3,000 one-time
  - Monthly platform fee: $500–$1,000/month
  - Per-account fee OR revenue share (negotiate flat monthly over %)

WHAT YOU GET FROM YourPropFirm:
✅ Automated account creation when trader purchases
✅ Real-time EOD trailing drawdown enforcement
✅ Daily loss limit auto-suspend (account paused, not failed)
✅ Dashboard showing trader P&L, drawdown status, qualifying days
✅ Payout request system with automated eligibility check
✅ CRM for managing all trader accounts
✅ Affiliate tracking (discount codes, referral commissions)
✅ Rithmic SIM account provisioning
✅ API access for OrderClone integration

WHAT YOU NEED TO ADD:
- OrderClone integration via Rithmic API (already built — zero cost)
- Custom rule logic for:
  - Activation gate (3 active funded, queue system)
  - Post-request qualifying day tracking
  - Consistency rule calculator visible on dashboard
  - Inactivity penalty clock
  - Profit reinvestment option at payout
- This custom rule logic = additional development work
  (see Step 2.3)

- Total Step 2.1: $2,000–$3,500 setup + $600–$1,000/month

### Step 2.2: Website
You need a clean, professional website. NOT a complex one.
Required pages: Home, Accounts/Pricing, Rules, Dashboard login,
Blog, Affiliate signup, FAQ, Contact

- Option A (Recommended for launch): Webflow
  - Professional templates available for $50–79 one-time
  - Hosting: $23/month (CMS plan)
  - Connect to custom domain
  - No coding required
  - Looks exactly like a funded firm's site

- Option B: WordPress + Elementor
  - Domain: $12/year (Namecheap)
  - Hosting: $3.99–7.99/month (Hostinger or SiteGround)
  - Theme: $59 one-time (Astra Pro or similar)
  - Total: ~$100/year

RECOMMENDED: WordPress approach — $100/year + $60 theme = $160 total
Save the Webflow monthly fee for later when scaling.

Content needed for launch (write yourself — you know this industry):
- Homepage: hero with headline, 2 account types, key differentiators
  (5% target, EOD drawdown, no consistency rule in eval, OrderClone free)
- Accounts page: Sprint vs Standard comparison table with pricing
- Rules page: Full transparent rules document (builds trust)
- Dashboard: Link to white label platform
- Affiliates: Signup form + commission structure
- Blog: 3–5 articles minimum at launch for SEO

- Total Step 2.2: $170–$250 setup + $8–25/month

### Step 2.3: OrderClone Custom Integration
This is your exclusive competitive advantage.
Already built — needs to be integrated into the white label platform.

Required integration work:
- OrderClone ↔ Rithmic API: Already done (Sierra Chart connection)
- White label platform ↔ OrderClone account provisioning: Custom work
  (when trader purchases account, system auto-provisions Rithmic SIM
  account AND OrderClone master/sub account relationship)
- Restriction enforcement: OrderClone copies only work between
  accounts on Talon's Rithmic server (not external accounts)
- Activation gate tracking: Platform must track which accounts
  are "active funded" vs "queued" and enforce 3-account max

Development cost options:
- Hire freelance developer (Upwork/Toptal) for Rithmic API work:
  $50–150/hour, estimated 20–40 hours = $1,000–6,000
- Use platform provider's development team (YourPropFirm
  may offer custom development): $1,000–3,000
- Phase the integration: Launch with basic OrderClone (manual
  provisioning by you for first 30 days) and automate later

RECOMMENDED PHASE 1 APPROACH:
Launch without full automation first. Manually provision OrderClone
accounts for the first 30–50 customers while watching revenue come in.
Automate when cash flow supports it.

- Total Step 2.3 at launch: $0 (manual)
- Total Step 2.3 when automating (Month 2–3): $1,500–$3,000

### Step 2.4: Payment Processing Setup
- Stripe account: $0 setup
- Stripe fees: 2.9% + $0.30 per transaction (deducted automatically)
- Stripe subscription billing: Built-in (for Standard recurring accounts)
- Integrate with white label platform via Stripe API (YourPropFirm
  handles this as part of their standard setup)
- Add Coinbase Commerce for crypto: $0 setup, 1% per transaction

- Total Step 2.4: $0 setup, transaction fees only

### Step 2.5: Payout Processing
Talon needs a way to pay traders quickly and internationally.

- Deel (recommended): Handles 1099s automatically for US traders,
  international wire/Wise for foreign traders, ~$49/month for
  contractor payments, handles all compliance paperwork
- Alternative: Wise Business — no monthly fee, pay per transfer
  (~$3–8 per international transfer)
- For very early stage (first 1–10 payouts): Wise Business is cheaper
- Switch to Deel when payout volume justifies it (>20/month)

- Total Step 2.5: $0 (Wise Business) at launch
  Upgrade to Deel (~$49/month) when scaling

### PHASE 2 TOTAL: $2,170–$3,950 setup + $620–$1,075/month

---

## PHASE 3 — PRE-LAUNCH TESTING
### Timeline: Week 4–6 | Cost: $200–$500

### Step 3.1: Internal Account Testing
- Create 3–5 internal test accounts across both Sprint and Standard types
- Trade through them manually: one failure, one pass, one funded
- Test the full lifecycle:
  - Purchase → Rithmic SIM provisioning → trading → DLL trigger
  → EOD drawdown update → qualification → funded activation
  → payout request → consistency check → deduction → processing
- Identify any gaps in rule enforcement before going live
- Cost: $0 (internal accounts)

### Step 3.2: Soft Launch with Beta Testers (10–20 traders)
- Offer 5–10 trusted traders access at no cost or deep discount
- Have them trade, attempt payouts, stress-test the system
- You trade your own accounts as the primary test subject
- Document every issue before public launch
- Cost: $200–500 in discounted/free accounts given to beta traders

### Step 3.3: Legal Review of Live System
- Have attorney spot-check one full account lifecycle against the
  Trader Agreement before accepting first paid customer
- Cost: Included in Phase 1 legal budget

### PHASE 3 TOTAL: $200–$500

---

## PHASE 4 — LAUNCH AND DAY 1 REVENUE
### Timeline: Week 6–8 | Marketing Budget: $500–$1,500

This is where money starts coming in.

### Step 4.1: Affiliate Program — Launch This First
Before any paid ads, build the affiliate network.
The prop firm industry runs almost entirely on affiliates.

Structure:
- Affiliates earn 15% of challenge fee revenue from traders
  they refer (ongoing, including retries and renewals)
- Each affiliate gets a unique discount code (50–70% off list price)
- The code is their acquisition tool AND their tracking mechanism
- Affiliates promote through: YouTube reviews, TikTok, Discord servers,
  Twitter/X trading communities, Telegram groups

How to recruit initial affiliates:
- Post in r/Futures, r/FuturesTrading, r/PropFirm on Reddit
- Post in futures trading Discord servers (Apex, Topstep have large ones)
- Contact 10–20 small YouTube traders (5K–50K subscribers)
  who review prop firms — offer them exclusive promo codes
- The top 3 prop firm review channels generate most industry volume
- Cost: $0 upfront — affiliates only paid when they generate sales
  (15% commission paid from incoming fees, not from reserves)

### Step 4.2: Social Media Presence (Organic First)
Required accounts at launch:
- Twitter/X: @TalonFunding
- YouTube: TalonFunding (even 1–2 explainer videos at launch)
- Discord: Talon Funding community server (free to create)
- TikTok: Trading content, challenge results

Content strategy Week 1–4:
- "Why we chose 5% — the only firm brave enough to lower the standard"
- "EOD drawdown explained — why intraday trailing drawdown is killing your accounts"
- "OrderClone: how to run 5 eval accounts from one master"
- "Sprint account — pass in one day or try again for $19.95"

Cost: $0 (your time)

### Step 4.3: Initial Paid Marketing (Optional at Launch)
DO NOT spend on paid ads until organic/affiliate is tested.
If budget allows after platform costs are covered:
- Reddit ads targeting r/Futures, r/DayTrading: $300–500/month
- YouTube pre-roll targeting "prop firm" search terms: $200–400/month
- Google Search: "futures prop firm discount" keywords: $300/month
- Start with $500 total, measure cost per acquisition, scale what works

RECOMMENDED: Hold all paid ad budget until Month 2 when first
organic/affiliate revenue confirms the funnel works.

### Step 4.4: Launch Pricing Structure
Sprint Account:
- List price: $149 (50K) — this is what the website shows
- Standard code (affiliates): 87% off → $19.95
- Promo/flash sale: 90% off → $14.95
- This matches exactly what you paid at Apex/BluSky and felt cheap enough
  to buy 13 times

Standard Account:
- List price: $199/month (50K)
- Month 1 code: 85% off → $29.95 first month
- Renewal: 80% off → $39.95/month
- Reset fee: $24.95

The math on 100 first-month sales (realistic in Month 1 with good affiliates):
- 70 Sprint accounts @ $19.95 = $1,396
- 30 Standard accounts @ $29.95 = $899
- Total Month 1 gross: ~$2,295
- Less: Stripe fees (2.9% + $0.30): ~$100
- Less: Affiliate commissions (15% on referred sales): ~$250
- Net Month 1 revenue: ~$1,945

Platform costs Month 1: ~$1,000 (white label + hosting + legal + misc)
Net profit Month 1: ~$945

Month 2 (with renewals + new sales):
- 30 Standard renewals @ $39.95 = $1,199
- 50 new Sprint @ $19.95 = $998
- 40 new Standard @ $29.95 = $1,198
- 20 Standard resets @ $24.95 = $499
- Total Month 2 gross: ~$3,894
- Less fees + commissions: ~$500
- Net Month 2 revenue: ~$3,394
- Platform costs: ~$1,000
- Net profit Month 2: ~$2,394

Month 3 (compound growth):
- ~$5,000–$7,000 gross expected with normal affiliate growth
- Net profit: ~$3,500–$5,000
- This is the target milestone to invest in OrderClone automation

### PHASE 4 TOTAL MARKETING BUDGET: $0–$1,500

---

## PHASE 5 — OPERATIONS (ONGOING)
### Cost: ~$200/month labor equivalent (your time + 1 part-time support)

### Step 5.1: Trader Support
At launch (0–100 traders): Handle all support yourself
- Discord (free): Primary support channel
- Email ticketing: Use Freshdesk free tier (up to 10 agents free)
- Response time target: Same day for account issues, 24hr for general
- The #1 thing that generates positive Trustpilot reviews is fast,
  human support. This is your cheapest marketing tool.

When to hire first support person:
- When monthly account volume exceeds 200/month
- Hire part-time (15–20hrs/week) at $15–20/hour = $1,200–$1,600/month
- Can be done remotely, hire trading community members

### Step 5.2: Payout Processing
At launch: Handle manually via Wise Business
- When trader submits payout request, verify eligibility manually
  against dashboard data
- Process via Wise: ~$3–8 per transfer
- Target: Same-week processing (Wednesday payments, like Bulenox)
- The 5–7 day processing window gives you float time
- Manual review also gives you additional compliance check opportunity
  (V-1 through V-6 violations sometimes only visible at payout review)

### Step 5.3: Account Monitoring
Key things to watch daily (takes 15–20 min):
- Any accounts approaching DLL (potential suspension to process)
- Any funded accounts with payout requests pending
- Any flagged accounts (style change detection, pattern anomalies)
- OrderClone master account relationships (ensure copy accounts
  are on Talon Rithmic only, no external connections)

### Step 5.4: Trustpilot & Review Management
- Create Trustpilot business account immediately: free
- After every successful payout, send automated email:
  "Your payout has been processed! If you're happy with Talon,
  a quick review on Trustpilot helps us keep improving."
- Respond publicly to every negative review within 24 hours
  (this is visible to prospective traders and matters enormously)
- Target: 4.5+ rating within first 90 days
- Your competitive advantage: You will never do what Apex did —
  reverse platform losses back onto traders. One post about
  "Talon reversed our losses after the platform glitch" is worth
  $10,000 in paid advertising.

---

## COMPLETE COST SUMMARY

### ONE-TIME STARTUP COSTS
| Item | Min | Max |
|------|-----|-----|
| Wyoming LLC formation | $102 | $102 |
| Registered agent (year 1) | $50 | $50 |
| Legal documents (trader agreement + review) | $700 | $1,000 |
| White label platform setup | $1,500 | $3,000 |
| Website (domain + hosting + theme) | $160 | $250 |
| Beta testing accounts | $200 | $500 |
| Initial marketing (optional) | $0 | $1,500 |
| **TOTAL ONE-TIME** | **$2,712** | **$6,402** |

### MONTHLY ONGOING COSTS
| Item | Min | Max |
|------|-----|-----|
| White label platform fee | $500 | $1,000 |
| Website hosting | $8 | $25 |
| Virtual office address | $25 | $50 |
| Registered agent (amortized monthly) | $4 | $4 |
| Stripe fees (variable — ~3% of revenue) | $60* | $200* |
| Payout processing (Wise) | $15 | $50 |
| Affiliate commissions (15% of referred revenue) | $100* | $400* |
| Discord/Freshdesk tools | $0 | $0 |
| **TOTAL MONTHLY FIXED** | **$562** | **$1,129** |

*Variable — scales with revenue

### ABSOLUTE MINIMUM TO LAUNCH AND TAKE FIRST PAYMENT
| Item | Cost |
|------|------|
| Wyoming LLC | $102 |
| Registered agent | $50 |
| EIN | $0 |
| Mercury bank account | $0 |
| Legal template (trader agreement) | $400 |
| Domain + WordPress hosting + theme | $170 |
| White label setup (YourPropFirm) | $1,500 |
| First month platform fee | $500 |
| Stripe setup | $0 |
| Wise Business | $0 |
| **ABSOLUTE MINIMUM** | **$2,722** |

Under $3,000 to be fully operational and accepting payments.

---

## REVENUE TO BREAK-EVEN TIMELINE

| Month | Accounts Sold | Gross Revenue | Fixed Costs | Net |
|-------|--------------|---------------|-------------|-----|
| 1 | 100 | $2,295 | $2,000 | -$705 |
| 2 | 150 | $3,894 | $1,100 | +$2,794 |
| 3 | 200 | $5,500 | $1,100 | +$4,400 |
| 4 | 300 | $8,200 | $1,300* | +$6,900 |
| 6 | 500 | $13,000 | $1,500* | +$11,500 |

*Includes part-time support hire at Month 4

Cumulative break-even (recovering initial $2,722 investment):
Achieved in Month 2.

---

## THE 30-DAY CRITICAL PATH TO FIRST DOLLAR

| Day | Action | Cost |
|-----|--------|------|
| 1–2 | File Wyoming LLC, apply for EIN | $152 |
| 3–4 | Open Mercury bank account | $0 |
| 5–7 | Purchase + customize legal template | $400 |
| 5–7 | Register domain, set up WordPress | $170 |
| 8–10 | Contact YourPropFirm, sign contract | $1,500–3,000 |
| 8–10 | Set up Stripe + connect to platform | $0 |
| 10–20 | Platform configuration (rules, account types) | $0 |
| 10–20 | Write website content, set up pages | $0 |
| 15–25 | Beta test with 5–10 internal accounts | $0–200 |
| 20–25 | Recruit first 5 affiliates | $0 |
| 25–28 | Soft launch to affiliate audience | $0 |
| 28–30 | First paying customers, first revenue | INCOMING |

---

## WHAT YOU ARE NOT SPENDING MONEY ON
(And why — this is as important as the spending list)

❌ No trading capital reserve — 100% SIM, none needed
❌ No FCM (Futures Commission Merchant) license — not executing real trades
❌ No NFA/CFTC registration — simulated trading, not regulated activity
❌ No exchange membership fees — no real exchange transactions
❌ No clearinghouse fees — no real positions cleared
❌ No custom software development at launch — white label handles it
❌ No office space — 100% remote operation
❌ No employees at launch — 1 founder (you)
❌ No paid marketing at launch — affiliate-first model

The businesses that fail to launch spend $50,000–$100,000 on
technology before generating a single dollar. Talon spends $2,722,
generates revenue in 30 days, and funds all future development
from operating cash flow.

---

## PHASE 6 — SCALE (MONTHS 3–12)
Fund from operating revenue only. No external investment needed.

Month 3 milestone: Automate OrderClone provisioning ($1,500–3,000)
Month 4 milestone: Hire part-time support ($1,200–1,600/month)
Month 5 milestone: Launch paid social media marketing ($1,000/month)
Month 6 milestone: Add $100K and $150K account sizes
Month 9 milestone: Commission custom dashboard enhancements
Month 12 milestone: Evaluate custom platform build vs. continued white label

---

*Talon Funding — Launch Plan v1.0 — Confidential*
