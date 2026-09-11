# StainlessCarbon — Carbon & Energy Calculator for Stainless Steel

Round 1 submission for **"Spark the Rising Curve"** (Jindal Stainless, via Unstop) — **Problem Statement 3:** build a tool that estimates carbon emissions per tonne of stainless steel from the input mix and energy source, and helps users find lower-carbon combinations that remain practical.

**Live calculator:** https://ritehrks.github.io/jindal-steel-case-study/website/

## The idea in one line

Stainless steel's carbon is an **alloy-chain problem** — ferrochrome and nickel drive 60–80% of the footprint — and no existing calculator models it. We built one that does: stainless-specific, calibrated to India's real grid and captive-coal economics, bounded by metallurgical guardrails, and priced per tonne at the EU border (CBAM).

## What's here

| Path | Contents |
|---|---|
| `case-study/StainlessCarbon_Round1.pptx` | The 2-slide Round 1 executive summary (final) |
| `case-study/slide1.html`, `slide2.html` | Editable design sources for the deck (render at 1280×720) |
| `website/` | The live calculator — a single HTML file, no build step; open `index.html` in any browser |
| `research/` | 19 research files behind every number — emission factors, ISSF methodology, CBAM regulation, Jindal disclosures, competitor teardown |
| `research/22-canonical-model-v1.md` | **Start here.** The locked single source of truth: every figure used in the deck and calculator traces to this file |
| `competition-brief.md` | The problem statement and evaluation criteria |

## The model, briefly

```
CO2/t = S1 (fuels, AOD process, captive power)
      + S2 (grid electricity x CEA factor)
      + S3 ((1 - scrap%) x sum of alloy mass x emission factor)
        subject to: scrap <= 80% (Cu/Sn tramp-element limit)
```

- Grade-aware charge chemistry (304 / 316 / 430 / 2205), with nickel-source and ferrochrome-sourcing choices
- India-specific factors: grid 0.710 tCO2/MWh (CEA v21.0), captive subcritical coal 1.045, Odisha ferrochrome 5.4–5.9 tCO2/t (ICDA)
- Boundary discipline: captive power and captive ferrochrome stay inside Scope 1+2; only purchased alloys enter Scope 3
- **Calibration:** with Jindal's disclosed FY26 inputs (70% scrap, 47% renewables), the model returns 1.73 / 2.99 tCO2e/t against the audited 1.76 / 3.03 — within ~2%
- CBAM module: 2026–2030 phase-in, EU default (6.49 → 8.44 tCO2/t with markup) vs verified data — a €372–398/t difference by 2030, worth ₹200–290 crore/yr on Jindal's EU export book
- Constrained optimizer: finds the lowest *feasible* CO2/t, never a fantasy 100%-scrap answer

## Sources

JSL ESG Factsheets, BRSR and CDP disclosures FY22–26 · CEA CO2 Baseline Database v21.0 · BEE PAT · IPCC 2006 · worldstainless/ISSF · ICDA ferrochrome LCA · EU Regulations 2023/956, 2025/2620-21, 2026/1740 · Goldman Sachs, ICRA, CRISIL analyst reports.

*Independent case-competition project built on public disclosures — not an official Jindal Stainless product.*
