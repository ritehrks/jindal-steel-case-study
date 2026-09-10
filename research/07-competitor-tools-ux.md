---
topic: Competitor Tool UX Walkthrough — Primetals CO2 Calculator & SSAB EcoUpgraded App
date: 2026-09-10
method: agent-search (Gemini 3.8 Flash)
requested_by: user
status: complete
used_in: [case-study/draft.md]
---

# Competitor Tools UX Walkthrough & Usability Gap Analysis

This research covers **Task 5** of the deep research plan: analyzing the user interface, input parameters, output visualizations, scenario comparison capabilities, and practical limitations of existing industry tools—specifically **Primetals Technologies' CO2 Calculator** and **SSAB's EcoUpgraded App**—to pinpoint genuine usability and functional gaps that an India-specific, stainless-steel-tailored calculator can fill.

---

## 1. Primetals Technologies — CO2 Calculator & Production Route Modeling

### Overview & Positioning
- **Target Audience**: Primary steel plant operators, chief technology officers (CTOs), sustainability directors, and CAPEX planners.
- **Platform**: Web-based digital application (`co2calc.primetals.com`) integrated into Primetals' decarbonization consulting suite and plant automation platforms (e.g., EAF Ultimate, AOD/BOF Optimizers).
- **Core Scope**: Upstream and midstream plant-gate carbon accounting across alternative primary steelmaking routes:
  1. *BF-BOF* (Blast Furnace – Basic Oxygen Furnace)
  2. *DRI-EAF* (Direct Reduced Iron – Electric Arc Furnace, NG or H2 based)
  3. *Scrap-EAF* (Recycled scrap in shaft/quantum electric arc furnaces)
  4. *Smelter + DRI* (Submerged arc electric smelting of low-grade iron ores)

### User Inputs & Data Requirements
Primetals' tool requires deep metallurgical and chemical input data typically accessible only to plant metallurgists and process engineers:
- **Production Route Architecture**: Selection of operational route configuration (e.g., BF-BOF vs MIDREX DRI-EAF vs HYFOR/HyREX H2 direct reduction vs secondary scrap-EAF).
- **Charge & Raw Material Mix**:
  - Hot metal vs cold pig iron ratios
  - Direct reduced iron (DRI/HBI) pellet grade and carbon content
  - Sinter, pellet, and lump iron ore proportions
  - Scrap charge percentage (typically 15–25% in BOF, up to 100% in EAF)
  - Fluxing agents and calcined lime/dolomite additions
- **Energy, Reductants & Utilities**:
  - Coke, pulverized coal injection (PCI), natural gas (Nm³/t), heavy fuel oil
  - Hydrogen flow rate and purity (Nm³/t)
  - Electric power consumption (kWh/t crude steel) and electricity grid carbon intensity factor (kg CO2/MWh)
  - Oxygen, nitrogen, and argon consumption
- **Process Technologies & Efficiency Add-ons**:
  - Waste heat recovery turbines (TRT), Top Gas Recovery
  - Selective Waste Gas Recirculation (SWGR) for sinter plants
  - Carbon Capture, Utilization, and Storage (CCUS / amine absorption or LanzaTech gas fermentation)

### Results Display & Visualizations
- **Disaggregated Emissions Metrics**:
  - Granular Scope 1 (direct fossil combustion, process calcination) and Scope 2 (purchased electricity) in **tCO2e per tonne of crude steel (tcs)** and total annual megatonnes (Mt CO2e/yr).
  - Scope 3 upstream accounting for purchased pellets, DRI, and fossil consumables.
- **Visual Analytics**:
  - *Sankey Diagrams / Mass & Energy Balance*: Flow of carbon and energy from input fuels to off-gases, slag, and steel.
  - *Route Waterfall & Stacked Bar Charts*: Visual comparison of baseline plant emissions versus upgraded routes (e.g., BF-BOF baseline ~2.1 tCO2/tcs dropping to ~0.8 tCO2/tcs with DRI-NG-EAF, and down to <0.3 tCO2/tcs with green H2-DRI-EAF).
  - *Decarbonization Roadmap Trajectory*: Multi-phase transition curve: Phase 1 (Optimization) → Phase 2 (Transition) → Phase 3 (Carbon Direct Avoidance).
  - *Cost & OPEX Indicators*: Projected carbon pricing penalty exposure (e.g., EU ETS allowances, CBAM certificates) and specific energy costs.

### Scenario Comparison Capability
- **High**: Specifically built for comparing multi-stage technological migration roadmaps side-by-side (e.g., 'Current BF-BOF' vs 'Option A: Scrap optimization + CCUS' vs 'Option B: Phased DRI-EAF transition').

### Usability & Architectural Limitations
1. **Enterprise Gating & High Friction**: Not a self-serve, lightweight tool; requires client credentials, commercial engagement, or enterprise NDA.
2. **Extreme Cognitive Load & Data Burden**: Demands mass-balance metallurgical figures, off-gas volumes, and fuel compositions that non-metallurgical executives, procurement teams, or ESG analysts do not possess.
3. **Primary Carbon-Steel Bias**: Strictly engineered for *iron ore reduction and carbon steelmaking*. Completely lacks models for high-alloy stainless steel thermodynamics (e.g., AOD decarburization, chromium oxidation/reduction, slag basicity for Cr recovery).
4. **Alloy Supply Chain Blindness**: Omits upstream embedded emissions of ferrochrome (FeCr) and Nickel Pig Iron (NPI), which constitute **60–80% of a stainless steel plant's cradle-to-gate carbon footprint**.
5. **Western/European Regulatory Bias**: Defaults to European energy paradigms (low grid factors, piped natural gas, high carbon taxes), ignoring Indian grid realities (0.710 tCO2/MWh) and captive subcritical coal-fired power dependencies.

---

## 2. SSAB — EcoUpgraded App

### Overview & Positioning
- **Target Audience**: Fleet managers, OEMs, structural design engineers, mining equipment purchasers, and transport contractors.
- **Platform**: Native mobile application on **Apple App Store** (iOS/iPadOS) and **Google Play Store** (Android), supplemented by web case studies.
- **Core Scope**: Downstream product lifecycle (Scope 3 Category 11: Use Phase) carbon and fuel savings achieved by upgrading mobile machinery from standard mild steel (e.g., S355) to SSAB’s proprietary high-strength quenched & tempered steels (**Strenx®** structural steel and **Hardox®** wear plate).

### User Inputs & Data Requirements
SSAB chose an intuitive, wizard-driven mobile interface with minimal inputs:
- **Application / Vehicle Selection**:
  - Dropdown selector for equipment category: Tipper/dump body, excavator bucket, container, trailer chassis, crane boom, cement mixer, agricultural trailer, garbage truck.
- **Operational Profile Parameters**:
  - Operating duration: Lifetime years (e.g., 5–10 years), annual operating hours or annual kilometers driven.
  - Fuel economy & consumption: Baseline liters of diesel per hour or liters/100 km.
  - Fuel cost: Local diesel price ($/liter or €/liter).
- **Weight & Component Specifications**:
  - Tare weight of baseline steel body/chassis (tonnes).
  - Steel grade upgrade choice: Standard structural steel → Strenx 700/900/1100 or Hardox 450/500.
  - Estimated structural weight reduction achieved by down-gauging thickness (typically 15% to 30% lighter).
  - Payload utilization factor: Percentage of return trips driven empty vs fully loaded.

### Results Display & Visualizations
- **Core Output KPIs**:
  - **Lifetime Fuel Savings**: Total liters of diesel fuel saved over the equipment lifespan.
  - **Lifetime CO2 Savings**: Total tonnes of CO2 avoided from eliminated fuel combustion.
  - **CO2 Payback Time**: Exact time (in months or operating hours) required for the fuel savings to offset the initial carbon footprint of producing the high-strength steel. After this breakeven threshold, the equipment operates with net-negative lifecycle emissions.
  - **Financial Return / Annual Profit Increase**: Direct fuel cost savings plus additional gross revenue generated from hauling extra payload per trip.
- **Visual Analytics**:
  - Clean speedometer-style dials and horizontal payback timelines showing the exact breakeven month.
  - High-contrast summary cards (green highlight for CO2 avoided, monetary figure for fuel cost saved).
  - **Export Capability**: Direct one-tap generation of a customer-facing branded PDF report formatted for executive presentation, procurement justification, or email dispatch.

### Scenario Comparison Capability
- **Low**: Evaluates one upgrade scenario at a time (baseline vs single selected high-strength grade). Running multiple alternative grades requires re-entering inputs or manually comparing separately exported PDFs.

### Usability & Architectural Limitations
1. **Downstream-Only Scope (Use Phase Focus)**: Completely ignores the steelmaker's plant operations, energy sources, and melting metallurgy. It calculates fuel burn in trucks, not emissions in smelters.
2. **Proprietary Vendor Lock-in**: Designed as a specialized B2B sales enablement tool to market SSAB Strenx® and Hardox® trademarked steel products against generic mild steel.
3. **Zero Metallurgical / Process Levers**: Offers no levers for scrap ratio, ferroalloy sourcing, captive power generation, green hydrogen, or renewable electricity.
4. **Irrelevant to Stainless Steel**: Stainless steel applications are selected for corrosion resistance, chemical passivity, hygienic standards, and high-temperature durability—not purely payload lightweighting via ultra-high yield strength.

---

## 3. Side-by-Side Comparison Matrix

| Attribute / Feature | Primetals CO2 Calculator | SSAB EcoUpgraded App | Proposed Stainless Steel Carbon & Energy Calculator |
|---|---|---|---|
| **Primary Focus** | Upstream plant route engineering & CAPEX planning | Downstream product use-phase lightweighting & fuel savings | Midstream stainless steel production, alloy mix, & energy optimization |
| **Target Sector** | Primary carbon steelmakers (BF-BOF, DRI) | Heavy vehicle OEMs, fleet operators, mining equipment | Stainless steelmakers (Jindal), industrial consumers, ESG analysts |
| **Platform / Access** | Web portal (`co2calc.primetals.com`), enterprise gated | Free public mobile app (iOS / Android) | Fast interactive web application / dashboard |
| **Material Coverage** | Carbon steel (hot metal, DRI, crude carbon steel) | High-strength carbon plate (Strenx®, Hardox®) | Stainless steel grades (**AISI 304, 316, 430, 200-series**) |
| **Alloying Elements Modeled** | None (negligible in carbon steel) | None | **High-carbon Ferrochrome (FeCr), Nickel / NPI, Ferromanganese** |
| **Process Route Modeled** | BF-BOF, DRI-EAF, Scrap-EAF, Smelter | None (downstream vehicle operation) | **EAF + AOD Converter + Submerged Arc Furnace (SAF)** |
| **User Inputs Required** | 30+ complex chemical/energy mass-balance parameters | 5–7 fleet operating parameters | **4 intuitive operational levers (Scrap %, NPI vs Virgin Ni, RE %, Clean Fuel %)** |
| **Time to First Result** | Hours/days (requires detailed engineering inputs) | < 2 minutes | **Instant (real-time reactive sliders, < 1 second)** |
| **Scenario Comparison** | Multi-route comparison tables & roadmaps | Single scenario vs baseline (manual PDF compare) | **Live side-by-side comparison cards (Baseline vs User vs Net-Zero Target)** |
| **Grid / Local Context** | Generic global or European grid defaults | Unspecified / irrelevant (diesel fuel burn) | **India-specific CEA Grid (0.710 tCO2/MWh) + Captive Coal (1.08 tCO2/MWh)** |
| **Target Benchmark Alignment** | Generic theoretical Net-Zero | Machine lifetime breakeven | **Jindal Disclosed Milestones (FY22: 1.98 → FY26: 1.76 → FY35: 0.99 t/tcs)** |

---

## 4. Genuine Usability & Functional Gaps Identified

Studying these two industry extremes—the **over-complex enterprise engineering tool (Primetals)** and the **over-simplified single-purpose sales app (SSAB)**—reveals five distinct gaps that our proposed calculator directly addresses:

### Gap 1: The 'Alloy Blindspot' in Mainstream Steel Calculators
- *The Problem*: Almost every available steel emissions calculator is built for ordinary carbon steel, where iron ore reduction constitutes >90% of the footprint. However, in austenitic stainless steel (e.g., AISI 304 with 18% Cr and 8% Ni), **upstream extraction and smelting of ferrochrome and nickel pig iron (NPI) account for 60% to 80% of total Scope 1–3 emissions**.
- *Our Solution*: Explicitly decouple and expose the **Alloy Sourcing lever** (e.g., captive Odisha ferrochrome @ 5.4–6.2 tCO2e/t, Indonesian rotary-kiln electric furnace NPI @ 60–85 tCO2/t contained Ni, and secondary recycled stainless scrap @ 0.07–0.39 tCO2/t).

### Gap 2: The 'All-or-Nothing' Usability Dilemma
- *The Problem*: Primetals requires an entire plant engineering team with hundreds of data points, making it inaccessible for rapid executive or procurement decisions. SSAB is lightweight and clean, but restricted to equipment tare weight and diesel fuel consumption.
- *Our Solution*: Deliver the **'SSAB simplicity with Primetals depth'**—distill complex metallurgical mass-balances into **4 high-impact, independent sliders**:
  1. *Recycled Scrap Input Share* (% scrap in charge mix: 40% to 80%)
  2. *Nickel & Alloy Procurement Strategy* (% low-carbon scrap/matte vs virgin NPI)
  3. *Electricity Sourcing & Captive Power* (% renewable solar/wind vs captive subcritical coal/grid)
  4. *Combustion Fuel Substitution* (% Green H2 / Bio-LDO replacing fossil coal/LSHS)

### Gap 3: Ignorance of India-Specific Grid & Captive Power Realities
- *The Problem*: Western tools assume low-carbon grid electricity (0.2–0.4 tCO2/MWh) or natural gas availability. In India:
  - The national grid factor is **0.710 tCO2/MWh** (CEA FY25).
  - Primary industrial steel clusters (e.g., Jajpur, Odisha) run **captive subcritical coal power plants** with 35–45% ash domestic coal, emitting **1.05–1.15 tCO2/MWh**.
  - Open and semi-closed submerged arc furnaces (SAFs) flare CO off-gas.
- *Our Solution*: Model the unique split between **captive coal power, open-access renewable solar/wind PPAs, and the state grid**, allowing users to see the dramatic carbon penalty of captive coal and the exact leverage of on-site renewables.

### Gap 4: Theoretical Perfection vs. Practical Operational Constraints
- *The Problem*: Generic calculators allow users to drag scrap to 100% or hydrogen to 100%, producing unrealistic zero-carbon outputs that cannot be implemented in a real plant due to scrap-tramp element accumulation (copper/lead contamination) and scrap availability deficits.
- *Our Solution*: Built-in **Practicality Guardrails**:
  - Enforce a visible **scrap ceiling cap (~75–80%)**, grounded in India's domestic collection realities and tramp element metallurgical tolerance for critical grades.
  - Display actionable warnings when users attempt combinations that violate physical or supply-chain feasibility.

### Gap 5: Disconnect from Corporate Targets & Disclosed Realities
- *The Problem*: Existing tools output abstract numbers in a vacuum. Users cannot tell whether 1.8 tCO2/t is commendable or failing.
- *Our Solution*: Anchor every live calculation directly against **Jindal Stainless Limited's actual disclosed ESG milestones**:
  - *FY22 Baseline*: 1.98 tCO2e/tcs (Scope 1+2)
  - *FY24 Peak*: 2.15 tCO2e/tcs
  - *FY26 Actual*: 1.76 tCO2e/tcs (achieved via 70.12% scrap & 47% renewable power)
  - *FY35 Science-Based Target*: **0.99 tCO2e/tcs** (-50% reduction)
  - *2050 Goal*: Net Zero emissions

---

## 5. Summary Takeaways for Case Study & Prototype Design

1. **UX Layout Recommendation**:
   - *Left Column (Controls)*: 4 interactive sliders with preset buttons ('Current JSL Baseline', 'FY35 Compliance Route', 'Maximum Feasible Green Route').
   - *Center/Right Column (Live Feedback)*:
     - Real-time gauge / hero metric: **Scope 1+2 and Scope 3 Intensity (tCO2e/tcs)**.
     - Side-by-side comparison cards: Baseline (FY22/FY26) vs User Simulation vs Target (FY35 0.99 t/tcs).
     - Waterfall breakdown attributing savings to specific levers (e.g., '-0.32 t from scrap', '-0.28 t from captive solar', '-0.15 t from Green H2').
   - *Bottom / Modal*: One-click exportable ESG Compliance & Cost Report (inspired by SSAB's clean PDF export).
2. **Key Differentiation Narrative**:
   *'Unlike Primetals' heavy carbon-steel plant simulator or SSAB's downstream mobile wear-plate tool, our calculator is the first interactive, real-time tool specifically calibrated for stainless steel metallurgy, Indian captive coal-to-renewable transition dynamics, and verified corporate ESG disclosure targets.'*
