---
topic: Ground truth data — emission factors, Jindal-specific context, practicality constraints, existing tools
date: 2026-09-10
method: external-research (Claude synthesis from verified public sources)
requested_by: user (pre-competition preparation)
status: complete
used_in: []
---

# Ground Truth Data — Compiled Research for Carbon & Energy Calculator

This file contains verified data compiled before the agent tree was started. All
data points below have their sources cited inline. Use these as the baseline for
the emissions model — do not substitute different numbers unless you explicitly
flag a conflict and explain why your number is better.

---

## A. Emission Factors by Steelmaking Route

- **BF-BOF (virgin, blast furnace route)**: ~2.2 tCO2 per tonne crude steel (range 1.8-3.0 depending on system boundary). Source: worldsteel / IEEFA.
- **Scrap-EAF**: ~0.67 tCO2 per tonne (71% lower than BF-BOF). Source: Columbia Business School Center on Global Energy Policy.
- **DRI-EAF, natural-gas based**: 0.7-1.2 tCO2 per tonne. Source: steelonthenet.
- **DRI-EAF, coal-based**: 2-3 tCO2 per tonne. Source: steelonthenet.
- **EU CBAM official default benchmarks** (narrow plant-gate boundary, for reference only — not directly comparable to the above cradle-to-gate figures): BF-BOF 1.370 tCO2e/t, DRI-EAF 0.481 tCO2e/t, Scrap-EAF 0.072 tCO2e/t. Source: EU Implementing Regulation 2025/2621.

### Important Nuance #1: System Boundaries
Different sources use different system boundaries (cradle-to-gate vs plant-gate vs Scope 1-only vs Scope 1+2+3), which is why numbers vary 3-10x across sources for the "same" route. Pick ONE boundary, state it explicitly, and stay consistent throughout the model.

### Important Nuance #2: Jindal's Process Route
Jindal Stainless is NOT a BF-BOF producer. Confirmed: both its Jajpur (Odisha) and Hisar (Haryana) plants run an **Electric Arc Furnace + AOD converter route**, with captive ferrochrome production via their own submerged arc furnace, and a captive power plant on-site. So the real "input mix" lever for this tool is NOT "BF-BOF vs EAF" — it is **% scrap vs % virgin/NPI-based alloy addition within an EAF-AOD process**. This directly matches the problem statement's own example ("share of scrap versus virgin input").

---

## B. Stainless-Steel-Specific: Alloying Element Emissions

This is the key differentiator vs. a generic carbon-steel calculator.

- **High-carbon ferrochrome production**: ~2.3 tCO2 per tonne of alloy (global average). Source: Metso/Outotec.
- **Nickel Pig Iron (NPI) production**: 60-85 tCO2 per tonne of contained nickel. Source: Stainless Steel World / ISSF data.
- **Net effect**: for an 8%-nickel grade (e.g. 304), moving from a 40% scrap mix (Scope 3 ≈ 2.80 tCO2/t) to NPI-sourced nickel adds another 4-6 tCO2 per tonne of stainless steel.
- **Scrap-based producer averages**: Scope 1 ≈ 0.39 t/t, Scope 2 ≈ 0.49 t/t.
- **Real-world benchmark**: Outokumpu discloses an average carbon footprint of 1.8 tCO2 per tonne of crude stainless steel across its entire production portfolio. Use as a credible "target" for what a well-optimized combination should approach.

---

## C. Energy Source Factors (India-specific)

- **India grid emission factor** (CEA, Version 21.0, December 2025): 0.710 tCO2/MWh for FY24-25, down from 0.727 in FY23-24 — trending down as renewable capacity scales nationally.
- **Renewables** (solar/wind): treated as ~0 direct emissions at point of use.
- **Jindal's own electricity mix** (FY26 disclosure): renewables now make up ~47% of electricity consumption at Hisar + Jajpur combined.

---

## D. Jindal Stainless — Company-Specific Context

- **Process route**: EAF + AOD, with captive ferrochrome and captive power plants at both major Indian sites.
- **Current recycled/scrap input**: ~70% (70.12% per FY26 BRSR filing).
- **Renewable electricity share**: ~47% (Hisar + Jajpur, FY26).
- **Targets**: Net Zero by 2050; 50% cut in emission intensity by FY35 versus FY22 baseline.
- **Track record**:
  - FY25: 14% year-on-year emissions cut, avoiding approximately 3.18 lakh tonnes of CO2 versus FY24.
  - FY26: further 5% cut in Scope 1+2 emissions (~72,500 tCO2e absolute reduction).
- **Concrete decarbonization levers already underway**:
  - ₹700 crore investment plan covering Odisha's largest captive solar plant
  - Green hydrogen plant commissioned at Hisar (90 Nm3/hr — first in the Indian stainless industry, with 700 Nm3/hr feasibility study underway at Jajpur)
  - Bio-LDO fuel substitution (30% of liquid fossil fuel replaced in Hisar's hot rolling mills, saving approximately 17,400 tCO2e per year)

**USE THIS** to frame the final recommendation as directionally aligned with Jindal's own real roadmap, not a hypothetical scenario — this is worth a lot on "Business Relevance & Impact."

---

## E. Practicality Constraints

- India's steel scrap use is currently only ~23-25% of national input, against a government target of 50% by 2047.
- Roughly 25-40% of India's ferrous scrap is imported, since domestic collection and shredding infrastructure is still developing.
- Global scrap availability is tightening: 48 countries had scrap export restrictions in place as of March 2025, analysts project global scrap market could flip from 9 million tonne surplus to 15 million tonne deficit by 2030.

**DESIGN IMPLICATION**: the optimizer must NOT recommend "100% scrap" as the answer just because it minimizes CO2 on paper. Cap the scrap % input at a realistic ceiling (~75-80%) and make that constraint visible in the UI.

---

## F. Existing Tools (for "Innovation & Differentiation")

- **Primetals Technologies' CO2 Calculator**: free, interactive tool letting users build steelmaking production routes and compare CO2 output across configurations.
- **SSAB's EcoUpgraded app**: calculates weight and CO2 savings from switching to higher-strength steel grades.
- **worldsteel's CO2 data collection methodology**: industry-standard reference methodology for calculating steel emissions.
- **Tata Steel/BCSA "Steel Bridges Carbon Calculator"**: Excel-based, not interactive, not stainless-specific.

**GAP**: none of the above are stainless-specific + India-grid-aware + tied to one company's own real, disclosed decarbonization roadmap. That combination is this tool's originality claim.
