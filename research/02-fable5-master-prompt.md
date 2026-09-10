---
topic: Fable 5 master prompt — complete instructions for generating the case study working document
date: 2026-09-10
method: external-research (Claude-authored prompt with embedded research)
requested_by: user
status: complete
used_in: []
---

# Fable 5 Master Prompt

This is the complete, copy-paste-ready prompt for Fable 5. It contains all ground truth
data embedded inline. The output from Fable 5 should produce the full working document
that the worker agent will use to extract and structure the case study.

## How to Use

Copy everything inside the code block below and paste it to Fable 5 exactly as-is.

```
I'm competing in Jindal Stainless' innovation case challenge — Problem Statement 3:
"Carbon and Energy Calculator for Steelmaking."

PROBLEM STATEMENT:

Business Context: Sustainability and responsible manufacturing are integral to
Jindal Stainless' long-term growth strategy. Increasing transparency around carbon
emissions and energy consumption can help accelerate informed decision-making and
support the industry's transition towards lower-carbon steelmaking.

Background: Stainless steel making is energy- and emissions-intensive, and carbon
intensity per tonne depends heavily on the input mix and energy sources used. With
a Net Zero by 2050 commitment, there is a need for simple tools that make the
emissions impact of different choices visible and help identify lower-carbon
options.

Action Item: Build a tool that estimates carbon emissions per tonne of steel based
on a chosen input mix (for example share of scrap versus virgin input) and energy
source, and let the user adjust these inputs to see the effect on emissions. The
tool should help users find combinations that minimise CO2 per tonne while
remaining practical.

Key Considerations:
- Reasonableness of the emissions model and assumptions
- Clarity of how inputs affect the result
- An interactive, easy-to-understand interface
- The usefulness of the optimisation or comparison feature
- A measurable reduction in estimated emissions

MY CONSTRAINT: Round 1 only requires a 1-2 slide executive summary of my approach
and initial recommendations. I will design the actual slides myself afterward.
Right now I need you to think through and document everything properly so I can
extract the strongest possible 2 slides from it. Treat this as the deep-thinking
and research-synthesis stage, not the slide-writing stage.

Act as a technical + sustainability strategy consultant and produce one detailed
working document covering everything in "WHAT I NEED FROM YOU" below. Use the
verified research data in "GROUND TRUTH DATA" as-is — do not substitute different
numbers unless you explicitly flag a conflict and explain why your number is
better.

===========================================
GROUND TRUTH DATA (verified from public sources — cite these when used)
===========================================

A. EMISSION FACTORS BY STEELMAKING ROUTE
- BF-BOF (virgin, blast furnace route): ~2.2 tCO2 per tonne crude steel (range
  1.8-3.0 depending on system boundary). Source: worldsteel / IEEFA.
- Scrap-EAF: ~0.67 tCO2 per tonne (71% lower than BF-BOF). Source: Columbia
  Business School Center on Global Energy Policy.
- DRI-EAF, natural-gas based: 0.7-1.2 tCO2 per tonne. Source: steelonthenet.
- DRI-EAF, coal-based: 2-3 tCO2 per tonne. Source: steelonthenet.
- EU CBAM official default benchmarks (narrow plant-gate boundary, for reference
  only — not directly comparable to the above cradle-to-gate figures): BF-BOF
  1.370 tCO2e/t, DRI-EAF 0.481 tCO2e/t, Scrap-EAF 0.072 tCO2e/t. Source: EU
  Implementing Regulation 2025/2621.

IMPORTANT NUANCE #1: Different sources use different system boundaries
(cradle-to-gate vs plant-gate vs Scope 1-only vs Scope 1+2+3), which is why
numbers vary 3-10x across sources for the "same" route. Pick ONE boundary, state
it explicitly, and stay consistent throughout the model.

IMPORTANT NUANCE #2: Jindal Stainless is NOT a BF-BOF producer. Confirmed: both
its Jajpur (Odisha) and Hisar (Haryana) plants run an Electric Arc Furnace + AOD
converter route, with captive ferrochrome production via their own submerged arc
furnace, and a captive power plant on-site. So the real "input mix" lever for
this tool is NOT "BF-BOF vs EAF" — it is % scrap vs % virgin/NPI-based alloy
addition within an EAF-AOD process. This directly matches the problem
statement's own example ("share of scrap versus virgin input").

B. STAINLESS-STEEL-SPECIFIC: ALLOYING ELEMENT EMISSIONS (the key differentiator
   vs. a generic carbon-steel calculator)
- High-carbon ferrochrome production: ~2.3 tCO2 per tonne of alloy (global
  average). Source: Metso/Outotec.
- Nickel Pig Iron (NPI) production: 60-85 tCO2 per tonne of contained nickel.
  Source: Stainless Steel World / ISSF data.
- Net effect: for an 8%-nickel grade (e.g. 304), moving from a 40% scrap mix
  (Scope 3 ≈ 2.80 tCO2/t) to NPI-sourced nickel adds another 4-6 tCO2 per tonne
  of stainless steel.
- Scrap-based producer averages: Scope 1 ≈ 0.39 t/t, Scope 2 ≈ 0.49 t/t.
- Real-world "good practice" benchmark: Outokumpu discloses an average carbon
  footprint of 1.8 tCO2 per tonne of crude stainless steel across its entire
  production portfolio. Use this as a credible "target" for what a
  well-optimized combination should approach.

C. ENERGY SOURCE FACTORS (India-specific)
- India's grid emission factor (CEA, Version 21.0, December 2025): 0.710
  tCO2/MWh for FY24-25, down from 0.727 in FY23-24 — trending down as renewable
  capacity scales nationally.
- Renewables (solar/wind): treated as ~0 direct emissions at point of use.
- Jindal's own actual electricity mix (FY26 disclosure): renewables now make up
  ~47% of electricity consumption at Hisar + Jajpur combined.

D. JINDAL STAINLESS — COMPANY-SPECIFIC CONTEXT
- Confirmed process route: EAF + AOD, with captive ferrochrome and captive power
  plants at both major Indian sites.
- Current recycled/scrap input: ~70% (70.12% per FY26 BRSR filing).
- Renewable electricity share: ~47% (Hisar + Jajpur, FY26).
- Stated targets: Net Zero by 2050; 50% cut in emission intensity by FY35 versus
  an FY22 baseline.
- Track record: FY25 delivered a 14% year-on-year emissions cut, avoiding
  approximately 3.18 lakh tonnes of CO2 versus FY24. FY26 delivered a further 5%
  cut in Scope 1+2 emissions (~72,500 tCO2e absolute reduction).
- Concrete decarbonization levers already underway: a ₹700 crore investment plan
  covering Odisha's largest captive solar plant, a green hydrogen plant
  commissioned at Hisar (90 Nm3/hr — first in the Indian stainless industry, with
  a 700 Nm3/hr feasibility study underway at Jajpur), and bio-LDO fuel
  substitution (30% of liquid fossil fuel replaced in Hisar's hot rolling mills,
  saving approximately 17,400 tCO2e per year).

USE THIS to frame the final recommendation as directionally aligned with Jindal's
own real roadmap, not a hypothetical scenario — this is worth a lot on
"Business Relevance & Impact."

E. PRACTICALITY CONSTRAINTS (the "while remaining practical" requirement)
- India's steel scrap use is currently only ~23-25% of national input, against a
  government target of 50% by 2047.
- Roughly 25-40% of India's ferrous scrap is imported, since domestic collection
  and shredding infrastructure is still developing.
- Global scrap availability is tightening, not loosening: 48 countries had scrap
  export restrictions in place as of March 2025, and analysts project the global
  scrap market could flip from a 9 million tonne surplus to a 15 million tonne
  deficit by 2030.

DESIGN IMPLICATION: the optimizer must NOT recommend "100% scrap" as the answer
just because it minimizes CO2 on paper. Cap the scrap % input at a realistic
ceiling (~75-80%) and make that constraint visible in the UI. This single design
choice is what answers "remaining practical" in the problem statement.

F. EXISTING TOOLS (for "Innovation & Differentiation")
- Primetals Technologies' CO2 Calculator: free, interactive tool letting users
  build steelmaking production routes and compare CO2 output across
  configurations.
- SSAB's EcoUpgraded app: calculates weight and CO2 savings from switching to
  higher-strength steel grades.
- worldsteel's CO2 data collection methodology: the industry-standard reference
  methodology for calculating steel emissions.
- A Tata Steel/BCSA-commissioned "Steel Bridges Carbon Calculator": Excel-based,
  not interactive, not stainless-specific.

GAP: none of the above are stainless-specific + India-grid-aware + tied to one
company's own real, disclosed decarbonization roadmap. That combination is this
tool's originality claim.

===========================================
WHAT I NEED FROM YOU
===========================================

1. EMISSIONS MODEL: Define one clear formula:
   CO2/tonne = f(scrap %, virgin/NPI %, alloy grade [e.g. 304 vs 430],
   electricity source mix, captive fuel mix)
   State the system boundary you are using (I recommend: cradle-to-gate,
   Scope 1 + Scope 2 + key Scope 3 from alloying inputs, per tonne of crude
   stainless steel) and justify every coefficient against the ground truth data
   above.

2. ASSUMPTIONS TABLE: One row per assumption — the number, its source, and one
   line on why it is reasonable specifically for an Indian EAF-AOD stainless
   producer (not a generic BF-BOF steelmaker).

3. WORKED EXAMPLE: Build a "baseline" scenario reflecting Jindal's actual current
   mix (~70% scrap, ~47% renewable electricity) and an "optimized" scenario
   (scrap pushed toward the realistic ceiling of ~75-80%, higher renewable
   share, credit for green hydrogen / bio-LDO substitution). Show the resulting
   CO2/tonne for each scenario and the % reduction between them. This is my
   single most important output — I need one real, defensible number for the
   "measurable reduction" judging criterion.

4. TOOL / INTERFACE CONCEPT: Describe, in words plus a simple wireframe/box
   layout I can redraw in PowerPoint, an interactive interface with
   sliders/dropdowns for scrap %, alloy grade, electricity source mix, and fuel
   mix, with a live CO2/tonne output and a "compare to baseline" panel.

5. OPTIMIZATION / COMPARISON FEATURE: Explain precisely how it works. Does it
   scan feasible combinations within realistic constraints (scrap capped at
   ~80%, etc.) and return the lowest-CO2 practical mix? Or does it show a
   sensitivity chart of which lever moves emissions the most? Describe it
   precisely enough that I could confidently explain to a judge how the
   optimizer actually works, step by step.

6. STRUCTURE your full answer under these headers (they match both the Round 1
   judging criteria and the fuller case guidelines I will need for Round 2, so
   this document should be reusable there too):
   - Problem Understanding
   - Objectives & Success Metrics
   - Proposed Solution (model + tool + optimization)
   - Validation (the worked example)
   - Assumptions & Limitations
   - Innovation vs Existing Tools (compare against the Primetals CO2 Calculator
     and SSAB EcoUpgraded app described above)
   - Expected Impact

7. FINALLY, add a "Slide 1" and "Slide 2" section: condense everything above
   into exact bullet points ready to paste into a 2-slide PowerPoint — no more
   than ~6 tight bullets per slide.
```
