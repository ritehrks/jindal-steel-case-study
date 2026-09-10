---
topic: India/Odisha-specific ferrochrome emission factors — SAF producers
date: 2026-09-10
method: agent-search (Gemini 3.8 Flash)
requested_by: orchestrator
status: complete
used_in: []
---

# India & Odisha Ferrochrome Emission Factors

## Key Finding

**Odisha ferrochrome = 5.4-6.2 tCO2e/t HCFeCr — 2.5× the global average of 2.3 tCO2/t**

The global average (Metso/Outotec) reflects closed SAF + preheating + clean power.
Indian producers use open/semi-closed SAFs powered by captive subcritical coal.

## Disaggregated Breakdown (India/Odisha)

| Component | Intensity | Notes |
|---|---|---|
| **Scope 1 (direct process)** | 1.35-1.55 tCO2/t | Carbon reductants, electrode paste, flux calcination |
| **Scope 2 (electricity)** | 4.00-4.60 tCO2/t | 3,950 kWh/t × captive coal ~1.08 tCO2/MWh |
| **Total (Scope 1+2)** | **5.40-6.15 tCO2e/t** | Captive coal dominant |

Scope 2 from captive coal = **~70-75% of total emissions**.

## Producer-Specific Estimates (Odisha)

| Producer | Capacity (tpa) | Power Setup | Estimated S1+2 |
|---|---|---|---|
| **IMFA** | ~284,000 | 204.5 MW captive coal | 5.60-6.10 |
| **Jindal Stainless** | ~250,000 (→450,000) | 264 MW captive coal + grid | **5.40-5.90** |
| **Tata Steel Mining** | ~110,000 | Captive + Tata Power | 5.10-5.50 |
| **Balasore Alloys** | ~160,000 | Captive coal / GRIDCO | 5.50-6.00 |
| **FACOR (Vedanta)** | ~150,000 | 100 MW captive coal | 5.50-5.90 |

## Global Comparison

| Region/Tech | Total S1+2 (tCO2e/t) | vs Global Avg |
|---|---|---|
| **Odisha captive coal** | **5.40-6.15** | **+145% to +170%** |
| India national grid mix | 4.20-4.80 | +82% to +108% |
| Global weighted avg (ICDA) | 2.30-2.80 | Baseline |
| Metso Outotec closed SAF | 2.30-2.70 | ~Par |
| Outokumpu Tornio (Finland) | 1.25-1.40 | -40% to -45% |

## Why Odisha Is So High

1. **Captive coal power** (subcritical, 35-45% ash coal) → 1.05-1.15 tCO2/MWh vs 0.05 for Nordic hydro
2. **Open/semi-closed SAFs** → CO off-gas flared instead of recovered for preheating
3. **Friable Sukinda chromite fines** → extra energy for briquetting/sintering

## Implication for the Calculator

Replace the global 2.3 tCO2/t ferrochrome figure with **5.4-5.9 tCO2e/t** for Jindal's
captive ferrochrome when modeling their actual operations. This makes the alloy sourcing
lever EVEN MORE impactful — switching from virgin ferrochrome to recycled stainless scrap
(which bypasses ferrochrome smelting entirely) saves ~5.5 tCO2 per tonne of alloy avoided.

## Sources
- ICDA LCA of Ferrochrome Production (2020-2024)
- CEA CO2 Baseline Database v19/v20
- IMFA Annual/Sustainability Reports (2022-2025)
- JSL BRSR & Kalinganagar filings
- Metso/Outotec technical papers
- BEE PAT Scheme documentation
