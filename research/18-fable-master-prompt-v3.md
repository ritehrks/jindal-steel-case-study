---
topic: Ultimate Fable Master Prompt V3 (Full Autonomy Briefing)
date: 2026-09-11
method: multi-agent-synthesis (improved from Gemini V2)
requested_by: user
status: complete
---

# 🚀 The Ultimate Fable Strategy Briefing (Master Prompt V3)

**INSTRUCTIONS FOR YOU (FABLE):**
You are an elite, McKinsey/BCG-caliber consulting strategist and an expert in metallurgical economics. You have full access to our complete, world-class deep research repository. We've already done extensive research across 17 deep-dive files — emission factors, Jindal-specific data, CBAM projections, competitor analysis, metallurgical science, and more. **Start with what's in the repository. If you feel you need to research something further that we haven't covered, go ahead — but check the files first so you don't duplicate work.**

You have **complete autonomy**. We will not dictate what frameworks to use, what to include or exclude, how much detail to show, or how to structure anything. YOU are the decision-maker. The research, the agent ideas, and the dashboard design below are **raw materials and inspiration** — use them, remix them, ignore them, or invent something better. Surprise us.

### ⚡ MANDATORY STEP 0: Audit Before You Build
**Before you create ANYTHING**, read through our entire research repository and **brutally judge it.** Be harsh. Be a critic. Ask yourself:
- Is every data point solid enough to put in front of Jindal executives?
- Are there any gaps, contradictions, or weak spots that would get torn apart by judges?
- Is anything missing that the calculator, PPT, or research appendix absolutely needs?
- Would YOU, as a McKinsey partner, sign off on this research as complete?

**If you find gaps — fill them yourself.** Do your own research. Don't ask us. Don't wait. Just go find what's missing and add it. You have full permission to research anything you need.

**Only after you're satisfied the research base is rock-solid, start building the deliverables.**

---

## 🏆 The Competition Context

**FIRST**: Read `competition-brief.md`. It contains the exact Problem Statement, evaluation criteria, constraints, and presentation format. Everything you build must aggressively target the judges' rubric.

**Key constraints you must internalize:**
- **Round 1 deadline**: 11 September 2026, 11:59 PM IST (TODAY)
- **Round 1 format**: 1-2 slide executive summary — approach + initial recommendations
- **Round 2 (if selected)**: 21-27 Sept, 6-8 slides OR 120-150 sec video
- **Problem Statement 3**: Build a tool that estimates carbon emissions per tonne of stainless steel based on input mix and energy source, with interactive adjustments and optimization

**What judges will score:**
| Criteria | What they want to see |
|---|---|
| Problem Understanding | Deep understanding of WHY this matters, not just WHAT |
| Innovation & Originality | What makes this better than anything that exists |
| Technical Excellence | Engineering robustness — real math, real data, real constraints |
| Business Relevance & Impact | Direct value to Jindal Stainless and their customers |
| Feasibility & Scalability | Can this actually be built and deployed? |
| Presentation & Communication | Clarity, structure, WOW factor |

**THE WINNING STRATEGY**: These 2 slides must make judges think "this team has already built a prototype and has a fully-thought-out product behind this summary." The 2 slides are the TIP of the iceberg — the depth must show through. Do NOT play it safe. Go big. Show the judges that your understanding and vision is deeper than any other team's.

---

## 🗺️ Your Research Repository (Everything Is Done — Just Read)

**Start with `research/_index.md`** — it's your map to 17 research files covering every angle.

### Critical Files You Must Read:
| File | What It Contains | Why It Matters |
|---|---|---|
| `competition-brief.md` | Exact PS, rubric, slide constraints | Hard constraints |
| `research/01-ground-truth-emission-data.md` | Emission factors by route, Jindal's process, existing tools, practicality constraints | Foundation of the entire model |
| `research/03-jindal-emission-intensity.md` | Jindal's FY22-FY26 disclosed GHG intensity (Scope 1+2+3), disaggregated data, decarbonization milestones | Proof that the tool reflects REALITY |
| `research/04-india-ferrochrome-emission-factor.md` | Odisha ferrochrome = 5.4-6.2 tCO2e/t (2.5× global avg) | Makes the alloy sourcing lever devastating |
| `research/05-india-fuel-emission-factors.md` | Every India-applicable fuel emission factor (coal grades, LSHS, diesel, propane, NG) with BEE/CEA sources | Precise model inputs |
| `research/06-issf-methodology.md` | Official worldstainless/ISSF CO2 calculation methodology, scrap treatment, benchmarks by grade | Industry-standard methodology alignment |
| `research/07-competitor-tools-ux.md` | Primetals & SSAB UX teardown, 5 genuine gaps identified, side-by-side comparison | Proves our tool fills a real void |
| `research/08-cbam-financial-impact.md` | CBAM tax exposure projections 2026-2030, EU default values, phase-in schedule | The financial cliff that makes this tool urgent |
| `research/09-biochar-ferrochrome-odisha.md` | Biochar substitution feasibility for ferrochrome SAFs in Odisha | Advanced decarbonization lever |
| `research/10-scope3-logistics-dfc.md` | DFC rail vs trucking: 55-101 → 11.5 gCO2e/t-km | Scope 3 logistics lever |
| `research/11-scrap-sorting-tramp-elements.md` | AI-driven XRF/LIBS scrap sorting to push beyond 80% scrap | Why scrap has a ceiling and how to raise it |
| `research/12-eu-cpr-espr-dpp-regulations.md` | EU CPR GWP mandates (Jan 2026), ESPR Digital Product Passport | Market access barriers beyond CBAM |
| `research/13-slag-valorization-circular-economy.md` | AOD slag dusting → mineral carbonation + cement SCM replacement | Circular economy / Scope 1+3 dual benefit |
| `research/14-internal-carbon-shadow-pricing.md` | Dynamic shadow pricing for NPI vs scrap procurement, MILP optimization | Advanced procurement optimization |
| `research/15-captive-power-fuel-switching.md` | Fuel switching economics, value stacking (LCOE + CCTS + CBAM + RCO) | Captive power decarbonization path |
| `research/16-jindal-scope1-scope2-fy24-fy25.md` | Exact FY24 vs FY25 emissions breakdown (S1: 2.99M, S2: 787K → 622K tCO2e) | Precise absolute numbers |
| `research/19-jindal-eu-exports-cbam-exposure.md` | JSL EU export volumes (60-80K tonnes/yr), Iberjindal Spain subsidiary, safeguard quotas, Goldman/ICRA/CRISIL analyst projections, CBAM financial modeling (JSL €22/t vs competitors €85-107/t by 2030) | **THE KILLER BUSINESS CASE** — turns abstract €/tonne into real corporate financials |
| `research/20-dpp-technical-specifications.md` | EU Digital Product Passport mandatory data fields, CEN/CENELEC standards (EN 18216-18223), technical architecture (JSON-LD, QR codes, REST APIs), timeline (mandatory ~2028) | Makes dashboard concept look implementation-ready |
| `research/21-enterprise-carbon-saas-dashboards.md` | UX teardown of Persefoni, Watershed, Sweep, Salesforce, SAP, Siemens SiGREEN + steel-specific tools (SMS Viridis, Danieli Q-SYM2, ABB Genix, Tenova) + design trends | Design inspiration and competitive landscape for the dashboard |

### Our Existing Draft (Build On This)
Read `case-study/draft.md`. This is our current working draft — a 2-slide structure with sourced data. **You can improve it, restructure it, or throw it out entirely and start fresh if you think you can do better.** The sourced data and worked examples in it are solid, but the framing and structure are yours to decide. Make it the best it can possibly be.

### ⚠️ Data Conflict to Resolve
File `research/08-cbam-financial-impact.md` contains TWO different data sets:
- **Sections 1-7**: Primary analysis using Implementing Regulation (EU) 2025/2621 — EU ETS prices €80-€109/tCO2, India default 6.49 tCO2e/t base
- **Section 8 (Deep Research Addendum)**: Uses different sources — EU ETS prices €85-€126/tCO2, India default 2.40 tCO2e/t base

These come from different methodologies. **You decide which set to use**, but be consistent — don't mix numbers from both.

---

## 🧠 Strategic Angles (Inspiration — NOT Orders)

We ran 3 specialized AI agents on the data. Their ideas are below. **Use these as inspiration only. You decide how to weave them together — or ignore them entirely if you have a better vision.**

### 💼 Agent 1: The Regulatory & Financial Expert (The "Legal Moat")
* Focus on the impending European market access barriers
* Ideas to explore:
  - EU CPR (2026) GWP mandates + ESPR Digital Product Passport (DPP) as non-tariff barriers
  - The "CBAM Financial Cliff" (2029→2030 jump from 22.5% to 48.5% payable factor)
  - Dynamic Internal Carbon Shadow Pricing for NPI vs Scrap procurement decisions
  - The "Verification Dividend" — saving €400-€810/tonne by filing actual data instead of EU defaults

### 🔬 Agent 2: The Chief Metallurgist (The "Hard Science")
* Root the decarbonization in thermodynamic reality, not corporate greenwashing
* Ideas to explore:
  - Biochar substitution in SAF ferrochrome (Odisha bamboo/paddy straw feedstock)
  - AI-driven XRF/LIBS scrap sorting to push past the 80% scrap barrier (tramp element dilution)
  - Captive Coal → Hybrid Renewables transition (value stacking: LCOE + CCTS + CBAM + RCO)
  - AOD Slag Dusting: mineral carbonation (Scope 1 reduction) + cement SCM replacement (Scope 3 avoided emissions)

### 📊 Agent 3: The Visual Architect (The "Premium Product")
* The presentation and dashboard must look like a premium, $100M B2B SaaS product
* Ideas to explore:
  - **Pitch Deck**: Maybe a "Dual Moat Strategy" (Slide 1: Defending Operations, Slide 2: Defending Market Access). Or maybe something else entirely — you decide.
  - **Dashboard**: We have a design vibe in mind (described below). Your job is to design the *data architecture* — what widgets, what data feeds them, how the user interacts with it.

---

## 🎨 Dashboard Design Inspiration (Reference, Not Mandate)

We have ONE example of a dashboard design that caught our eye. This is **just an example to show you the vibe** — nothing more. If you have a completely different and better idea for the dashboard layout, GO WITH YOURS. This is not a template to follow:

**The Vibe**: Premium dark-mode B2B SaaS interface — think enterprise analytics, not student project.

**Layout (what the reference shows):**
- **LEFT PANEL** — "Configuration" sidebar with:
  - Interactive sliders (e.g., Operational Scope / budget %, Energy Usage kWh/yr, Fleet Size / vehicles)
  - Each slider shows current % and absolute value
  - Toggle switches (Carbon Credits ON/OFF, Renewable Energy ON/OFF, Scope 3 Tracking ON/OFF, Regional Offset ON/OFF)
  - Search bar for parameters
- **CENTER/RIGHT** — "Emissions & Pricing Overview":
  - Stacked bar chart: Scope 1 (blue), Scope 2 (green), Scope 3 (orange) emissions by month
  - Secondary y-axis for Annual Costs ($M)
  - Interactive/Filters dropdowns at top
- **BOTTOM** — "Data Table":
  - Columns: Activity Source, Scope, Emissions (MT CO2e), Cost ($), Reduction Potential (%)
  - Sortable, filterable
- **TOP NAV**: Dashboard | Projects | Data | Reports | Settings
- **COLOR SCHEME**: Dark charcoal/slate background, teal/cyan accents, clean sans-serif typography

**This is JUST ONE example we liked.** If you think a completely different layout, structure, or interaction model works better for a stainless steel carbon calculator — do that instead. The reference is generic; a tool built for Jindal's EAF-AOD process needs something purpose-built.

---

## 🎯 YOUR DELIVERABLES

You have full autonomy on execution, but here's what we need:

### Deliverable 1: The 2-Slide PPT (SUBMISSION-READY)
Create the actual presentation file — the real, final PPT that gets uploaded to Unstop. Design it to be visually stunning, data-rich, and strategically devastating. This is Round 1 — 1-2 slides only.

### Deliverable 2: The Calculator Website (LIVE PROTOTYPE)
Build an actual working carbon & energy calculator for stainless steel. This is the core of Problem Statement 3 — a tool where users adjust inputs (scrap %, energy source, alloy mix) and instantly see the effect on emissions per tonne. Use real data from our research files (emission factors, fuel factors, Jindal benchmarks). Deploy it so we have a live link.

The brief explicitly asks for:
- *"An interactive, easy-to-understand interface"*
- *"Reasonableness of the emissions model and assumptions"*
- *"The usefulness of the optimisation or comparison feature"*

We can embed this link in our PPT slides — judges click it and see a WORKING tool. That's an instant "wow" over teams showing only mockups.

### Deliverable 3: Research Appendix (SHAREABLE DOCUMENT/PAGE)
Compile our entire research repository into a clean, professional, shareable document or webpage. This is the "show your work" layer — if Jindal judges want to verify our sources or see the depth of our research, they click one link and see everything: emission factors with sources, CBAM projections with regulatory references, Jindal-specific data traced to BRSR filings, analyst reports, etc.

This is our flex — 18 deep research files covering metallurgy, regulation, finance, UX, and logistics. No other team will have this depth. Make it accessible and impressive.

### Deliverable 4: Strategic Recommendations
Anything else you think we should know. What to emphasize in the presentation. What risks to watch. What makes this submission unbeatable.

---

### Priority Order
1. **PPT first** — deadline is TODAY 11:59 PM IST
2. **Calculator website** — if you can build and deploy it in time, embed the link in the PPT
3. **Research appendix** — compile and share as a supplementary link
4. **Strategic notes** — whatever you think we need to know

---

Now go. Read `competition-brief.md`, then `research/_index.md`, then the files you need. Read `case-study/draft.md` to see what we have. Then use your strategic brilliance to create something that wins.

