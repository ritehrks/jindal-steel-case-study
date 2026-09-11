# Case Study Draft — PS3: Carbon & Energy Calculator for Steelmaking
# Round 1: 1-2 Slide Executive Summary

---

## SLIDE 1: Problem Understanding + Proposed Solution

### Title: **StainlessCarbon™ — India's First Stainless-Steel-Specific Carbon & Energy Calculator**

**The Problem:**
- Stainless steel production is energy- and emissions-intensive, with carbon intensity per tonne depending heavily on input mix and energy sources [source: competition-brief.md]
- Jindal Stainless operates an EAF + AOD process route (NOT BF-BOF), meaning the real emission lever is **% scrap vs % virgin/NPI-based alloy addition** — not the "blast furnace vs electric" choice that generic tools model [source: research/01-ground-truth-emission-data.md, Section A/Nuance #2]
- Existing carbon calculators (Primetals CO2 Calculator, SSAB EcoUpgraded, worldsteel methodology) are either carbon-steel-generic, not India-grid-aware, or not tied to any company's real decarbonization roadmap [source: research/01-ground-truth-emission-data.md, Section F]
- **Gap**: No tool exists that is simultaneously stainless-specific + accounts for India's grid emission factor (0.710 tCO2/MWh) + reflects one company's actual disclosed data and Net Zero pathway [source: research/01-ground-truth-emission-data.md, Sections C & F]

**The Solution — StainlessCarbon™:**
- An interactive, web-based carbon calculator purpose-built for **stainless steel** production via the EAF-AOD route
- **Emissions Model**: CO2/tonne = f(scrap %, alloy grade [304/430/duplex], electricity source mix, captive fuel mix) using a consistent Scope 1 + Scope 2 + key Scope 3 system boundary [source: research/01-ground-truth-emission-data.md, Sections A-C]
- **Key differentiator vs generic calculators**: Models the outsized carbon impact of **alloying element sourcing** — Odisha ferrochrome at 5.4-5.9 tCO2/t alloy (2.5× the 2.3 global average) and Nickel Pig Iron at 60-85 tCO2/t contained Ni — which generic carbon-steel tools completely ignore [source: research/04; research/22-canonical-model-v1.md Ruling 4; research/01 Section B]
- **Interactive interface**: Sliders for scrap %, dropdown for alloy grade, toggles for electricity source (grid/renewable/captive mix), with a live CO2/tonne gauge and a "Compare to Baseline" panel
- **Built-in practicality constraints**: Scrap % capped at ~75-80% reflecting India's real scrap availability limitations (only 23-25% of national steel input is scrap today, with global scrap market projected to hit a 15 Mt deficit by 2030) [source: research/01-ground-truth-emission-data.md, Section E]

---

## SLIDE 2: Validation + Innovation + Impact

### Title: **Measurable Impact — 25.2% Reduction Achieved, 37-43% Pathway Ahead**

**Worked Example — Jindal's ACTUAL Disclosed Position (verified from ESG Factsheets & CDP):**

| Parameter | FY24 Peak | FY26 Current | Optimized (FY28-30 Projection) | Source |
|---|---|---|---|---|
| Scrap input | ~60% | 70.12% (BRSR FY26) | 78% (near practical ceiling) | research/03, research/01 |
| Renewable electricity | ~30% | ~47% (FY26) | 65% (₹700 Cr solar + 300MW hybrid) | research/03, Section D |
| Green hydrogen | Not deployed | Pilot: 90 Nm³/hr (Hisar) | Scaled: 700 Nm³/hr (Jajpur) | research/03 |
| Bio-LDO substitution | 0% | 30% at Hisar | 50% across both plants | research/03 |
| **Scope 1+2 Intensity** | **2.15 tCO2e/tcs** | **1.76 tCO2e/tcs** | **~1.35-1.45 tCO2e/tcs** | research/03 (ESG Factsheets) |
| **Scope 3 Intensity** | **1.90 tCO2e/tcs** | **1.27 tCO2e/tcs** | **~0.95-1.05 tCO2e/tcs** | research/03 (ESG Factsheets) |
| **Total (S1+2+3)** | **4.05 tCO2e/tcs** | **3.03 tCO2e/tcs** | **~2.30-2.50 tCO2e/tcs** | Calculated |
| **Reduction from FY24 peak** | — | **-25.2% (S1+2+3 total); -18.1% (S1+2)** | **~37-43% (S1+2)** | Calculated (4.05→3.03 total; 2.15→1.76 S1+2) |

**Key finding**: Jindal's FY26 cradle-to-gate footprint of **3.03 tCO2e/tcs** (S1+2+3) sits in the top global quartile — vs the worldstainless global average of ~3.70 (50% scrap) and Asian NPI-heavy routes at ~6.80. Its S1+2 intensity of **1.76** is best-in-country vs the Indian steel-sector average of ~2.5. The tool's optimizer projects a further pathway to **~1.35-1.45 tCO2e/tcs** (S1+2) — on track for the FY35 target of **0.99 tCO2e/tcs** (50% cut from FY22 baseline of 1.98). [source: research/22-canonical-model-v1.md Ruling 2; research/03; research/06]

*Scope 1 dominates at 79% of combined emissions (FY24 CDP: Scope 1 = 1.70, Scope 2 = 0.45 tCO2e/tcs), confirming that fuel substitution (green H2, bio-LDO) has outsized impact vs grid greening alone.* [source: research/03-jindal-emission-intensity.md]

**Optimization Feature:**
- **Constrained optimizer** scans all feasible combinations within realistic limits (scrap ≤80%, renewable ≤100%, existing technology only) and returns the lowest-CO2 practical mix
- **Sensitivity chart** shows which single lever moves emissions the most — giving Jindal's sustainability team a clear investment priority ranking
- Aligned with Jindal's own stated roadmap: Net Zero by 2050, 50% intensity cut by FY35 vs FY22 [source: research/01-ground-truth-emission-data.md, Section D]

**Innovation vs Existing Tools:**

| Feature | Primetals CO2 Calc | SSAB EcoUpgraded | **StainlessCarbon™** |
|---|---|---|---|
| Stainless-specific (alloy emissions) | ❌ | ❌ | ✅ |
| India grid factor (CEA) | ❌ | ❌ | ✅ |
| Company-specific data (Jindal) | ❌ | ❌ | ✅ |
| Practicality constraints (scrap cap) | ❌ | ❌ | ✅ |
| Constrained optimization | ❌ | ❌ | ✅ |
| Interactive (not Excel) | ✅ | ✅ | ✅ |

[source: research/01-ground-truth-emission-data.md, Section F]

**Expected Impact:**
- **Measurable**: 25.2% total-footprint (S1+2+3) reduction achieved FY24-FY26 (18.1% on S1+2), with S1+2 pathway to 37-43% by FY28-30
- **Financial (CBAM Tax Savings)**: By filing verified direct emissions (~1.5 tCO2/t company-wide Scope 1, realistically 0.9-1.1 for CBAM purposes) instead of the EU default for India (6.49 base → 8.44 tCO2/t with markup), Jindal saves **€370-400 per export tonne by 2030** — **€22-32M (₹200-290 crore) per year** on its 60-80K tonne EU export book. [source: research/22-canonical-model-v1.md Ruling 1; research/08 §1-7; research/19]
- **Business-relevant**: Directly supports Jindal's ₹700 Cr decarbonization investment decisions and FY35 target tracking [source: research/01-ground-truth-emission-data.md, Section D]
- **Scalable**: Model can be extended to any EAF-AOD stainless producer by swapping in their grid factor, scrap ratio, and alloy sourcing data
- **Aligned**: Every recommendation maps to a lever Jindal is ALREADY investing in (solar, green H2, bio-LDO, scrap optimization) — not hypothetical

---

## ASSUMPTIONS & LIMITATIONS

| # | Assumption | Value | Source | Justification |
|---|---|---|---|---|
| 1 | System boundary | Scope 1 + 2 + key Scope 3 (alloy inputs), cradle-to-gate | Model design choice | Most comprehensive while staying comparable to industry benchmarks |
| 2 | EAF base emission | 0.67 tCO2/t crude steel | Columbia CBS/CGEP | Widely cited, applies to scrap-EAF route specifically |
| 3 | Ferrochrome EF | Purchased Odisha: 5.4-5.9 tCO2/t; imported low-carbon: 2.3 | research/04, research/22 Ruling 4 | Captive FeCr is modeled INSIDE JSL's S1+2 boundary (never double-counted as Scope 3) |
| 4 | NPI EF | 60-85 tCO2/t contained Ni | ISSF / Stainless Steel World | Range reflects sourcing variation |
| 5 | India grid EF | 0.710 tCO2/MWh | CEA Version 21.0 (Dec 2025) | Official, FY24-25 |
| 6 | Scrap ceiling | 75-80% | India scrap market data | National avg only 23-25%; global market tightening |
| 7 | Jindal scrap % | 70.12% | FY26 BRSR filing | Company-disclosed |
| 8 | Jindal renewable % | 47% (FY26 full-year, assured) | ESG Factsheet FY26; research/22 Ruling 3 | Hisar + Jajpur combined; 56% by Q3 FY26 may be cited only as momentum footnote with as-of date |
| 8b | Intensity denominator | Tonnes of CRUDE steel (FY24 1.758 / FY25 1.956 / FY26 2.015 Mt, derived) | research/22 Ruling 5 | Sales volumes (2.17-2.56 Mt finished) are never the denominator |
| 9 | Target benchmark | 1.8 tCO2/t | Outokumpu disclosure | Best-in-class global stainless producer |
| 10 | Jindal FY26 Scope 1+2 intensity | 1.76 tCO2e/tcs | ESG Factsheet FY26 | Company-disclosed, consolidated, assured |

---

*This draft is structured to scale: Slide 1 + Slide 2 for Round 1 → expand to 6-8 slides for Round 2 by unpacking each section into its own slide.*
