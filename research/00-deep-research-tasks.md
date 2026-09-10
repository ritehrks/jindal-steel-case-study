---
topic: Gemini Deep Research task prompts — 5 research gaps to fill
date: 2026-09-10
method: external-research (Claude-authored research plan)
requested_by: user
status: pending (research tasks not yet executed)
used_in: []
---

# Deep Research Tasks — Run These on Gemini

5 separate Deep Research sessions. Run each as a SEPARATE session (don't combine).
Results should be saved as individual research files (03-xx, 04-xx, etc.).

---

## Task 1 — Jindal's Actual Disclosed Emission Intensity

**Why**: Everything uses global averages as proxies. Jindal's own per-tonne number
would make the worked example a company-specific validation — big credibility jump.

```
Find Jindal Stainless Limited's disclosed greenhouse gas emission intensity,
specifically expressed as tonnes of CO2 (or CO2e) per tonne of crude steel
production (tCO2/tcs), for FY23, FY24, FY25, and FY26 if available. Search their
Business Responsibility and Sustainability Report (BRSR), Integrated Annual
Report, ESG report, and any CDP (Carbon Disclosure Project) filings. Also look
for a separate breakdown between Scope 1 and Scope 2 intensity if disclosed
separately. Report the exact figures with the fiscal year, the exact source
document and page number if possible, and note whether the figure is reported on
a standalone or consolidated basis, and for which plant(s) — Jajpur, Hisar, or
company-wide.
```

**After**: If real number found → replace worked example baseline with actual data.

---

## Task 2 — India-specific Fuel Emission Factors for Captive Power

**Why**: Model only accounts for grid electricity. Jindal uses coal, LSHS, propane,
diesel directly. Need per-fuel factors to add "fuel mix" as a lever.

```
Find official India-applicable greenhouse gas emission factors (in kg CO2 or
tCO2 per unit of fuel, and per unit of energy where available) for the following
fuels used in industrial captive power plants and rolling mills: coal (specify
grade if factors differ), LSHS (low sulphur heavy stock / furnace oil), propane,
diesel oil (HSD), and natural gas. Prioritize sources in this order: India's
Bureau of Energy Efficiency (BEE) PAT scheme documentation, the Ministry of
Environment, Forest and Climate Change's India GHG Program, the IPCC 2006/2019
default emission factor guidelines, and the GHG Protocol's emission factor
database. Present the results in a table with fuel type, unit, emission factor
value, and source.
```

**After**: Add as second lever in emissions model — "fuel mix for captive power."

---

## Task 3 — India/Odisha-specific Ferrochrome Emission Factor

**Why**: 2.3 tCO2/t is a global average. India-specific number is more defensible.

```
Find the greenhouse gas emission factor (tonnes CO2 or CO2e per tonne of
ferrochrome alloy produced) specifically for high-carbon ferrochrome production
in India, and in Odisha if a state-specific figure exists. Search for Indian
Chrome Ore Mining and Ferro Alloys industry data, reports from FICCI or the
Ministry of Mines, life-cycle assessment (LCA) studies of Indian ferrochrome
producers, and any figures published by Jindal Stainless, Tata Steel, or IMFA
(Indian Metals and Ferro Alloys) related to their own captive ferrochrome
operations. Compare this figure against the global average of approximately 2.3
tCO2 per tonne of alloy and note whether the Indian figure is higher (due to
higher grid/coal dependency) or lower.
```

**After**: Swap global 2.3 tCO2/t for India-specific figure in the model.

---

## Task 4 — worldstainless / ISSF Official Calculation Methodology

**Why**: Model built from assembled data points. Industry-standard methodology
would make it citable — big boost to "reasonableness of the emissions model."

```
Find and summarize the official CO2 emissions calculation methodology used by
worldstainless (the International Stainless Steel Forum, ISSF) for stainless
steel life-cycle carbon footprint reporting. Specifically explain: (1) how they
define the system boundary (cradle-to-gate vs cradle-to-grave), (2) how they
allocate Scope 1, Scope 2, and Scope 3 emissions across raw material extraction,
alloy production, melting, and finishing steps, (3) how they treat scrap input
versus virgin/primary raw material in the calculation, and (4) any standard
formula or emission factor table they publish. Cite the specific worldstainless
or ISSF report or methodology document used.
```

**After**: Restructure emissions model to follow this methodology's logic.

---

## Task 5 — Competitor Tool UX Walkthrough

**Why**: Need real interface details for "Innovation vs Existing Tools" section.

```
Find detailed descriptions, screenshots, or user reviews of two existing tools:
(1) the Primetals Technologies CO2 Calculator for steelmaking production routes,
and (2) the SSAB EcoUpgraded app for calculating steel weight and CO2 savings.
For each tool, describe: what inputs the user provides, how results are
displayed (numbers, charts, comparisons), whether it supports side-by-side
scenario comparison, and any usability limitations mentioned by users or
reviewers. The goal is to understand their interface design well enough to
identify a genuine usability gap that a new, simpler, India-specific stainless
steel calculator could fill.
```

**After**: Feed into Innovation vs Existing Tools section.
