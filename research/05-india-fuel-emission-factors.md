---
topic: India-applicable GHG emission factors for fuels used in captive power & rolling mills (coal, LSHS, propane, diesel, natural gas)
date: 2026-09-10
method: agent-search (Gemini 3.8 Flash)
requested_by: user
status: complete
used_in: []
---

# India-Applicable Fuel Emission Factors for Captive Power & Rolling Mills

## Executive Summary

To model emissions accurately for industrial steel producers like **Jindal Stainless Limited (JSL)**, electricity grid emission factors alone are insufficient. JSL operates **captive thermal power plants (CPPs)** (e.g., 264 MW coal-fired CPP at Jajpur, Odisha) and direct combustion units in **hot and cold rolling mills, annealing & pickling lines (APL), and submerged arc furnaces (SAF)** that consume large quantities of fossil fuels directly (Scope 1 combustion emissions).

This research establishes official, India-applicable greenhouse gas (GHG) emission factors and heating values for:
1. **Coal** (domestic Indian non-coking coal across GCV grades G10–G13, and imported thermal coal)
2. **LSHS (Low Sulphur Heavy Stock)** and **Furnace Oil (FO)**
3. **Propane** and **LPG**
4. **High Speed Diesel (HSD / Diesel)**
5. **Natural Gas (Piped Natural Gas / RLNG)**

Data is harmonized following the regulatory hierarchy prioritized by Indian industrial accounting standards:
1. **Bureau of Energy Efficiency (BEE)**: PAT Scheme Normalization Guidelines & Energy Auditor Handbooks
2. **Ministry of Environment, Forest and Climate Change (MoEFCC) & Central Electricity Authority (CEA)**: *CO2 Baseline Database for the Indian Power Sector* (Version 21.0, December 2025; India's Initial/Second/Third Biennial Update Reports — BUR-3 to UNFCCC)
3. **IPCC Guidelines for National Greenhouse Gas Inventories** (2006 Guidelines & 2019 Refinements, Vol. 2 Energy)
4. **GHG Protocol Cross-Sector Tools & India GHG Program** (WRI India / CII / TERI)

---

## 1. Master Summary Table: Fuel Emission Factors & Calorific Values

The table below presents official emission factors on both an **Energy Basis** (g CO2/MJ or t CO2/TJ) and a **Physical Unit Basis** (t CO2/tonne, kg CO2/litre, or kg CO2/SCM), explicitly distinguishing between **Gross Calorific Value (GCV)** and **Net Calorific Value (NCV)**.

| Fuel Type | Typical Sub-Category / Grade | Typical GCV (kcal/unit) | Typical GCV (MJ/unit) | NCV / GCV Ratio (Delta) | Emission Factor (NCV basis) | Emission Factor (GCV basis) | Oxidation Factor | Effective Factor (Physical Unit) | Primary Regulatory Source |
|---|---|---|---|---|---|---|---|---|---|
| **Indian Coal** | CPP Average Blend (G11–G13) | **3,755 kcal/kg** | 15.72 MJ/kg | 0.965 (+3.6% GCV) | 95.8 g CO2/MJ | 92.5 g CO2/MJ | 0.98 | **1.424 t CO2 / tonne** | CEA V21.0 App. B / MoEFCC NatCom |
| **Indian Coal** | Grade G11 (ROM CPP coal) | **4,150 kcal/kg** | 17.38 MJ/kg | 0.965 (+3.6% GCV) | 95.8 g CO2/MJ | 92.5 g CO2/MJ | 0.98 | **1.574 t CO2 / tonne** | BEE PAT Scheme / Ministry of Coal |
| **Indian Coal** | Grade G12 (Mid-grade CPP coal) | **3,850 kcal/kg** | 16.12 MJ/kg | 0.965 (+3.6% GCV) | 95.8 g CO2/MJ | 92.5 g CO2/MJ | 0.98 | **1.460 t CO2 / tonne** | BEE PAT Scheme / Ministry of Coal |
| **Indian Coal** | Grade G13 (High-ash Talcher coal) | **3,550 kcal/kg** | 14.86 MJ/kg | 0.965 (+3.6% GCV) | 95.8 g CO2/MJ | 92.5 g CO2/MJ | 0.98 | **1.347 t CO2 / tonne** | BEE PAT Scheme / Ministry of Coal |
| **Imported Coal** | Bituminous Thermal Coal | **6,000 kcal/kg** | 25.12 MJ/kg | 0.952 (+5.0% GCV) | 89.5 g CO2/MJ | 85.2 g CO2/MJ | 1.00 | **2.140 t CO2 / tonne** | CEA V21.0 App. B / IPCC 2006 |
| **LSHS** | Low Sulphur Heavy Stock | **10,500 kcal/kg** | 43.96 MJ/kg | 0.952 (+5.0% GCV) | 75.5 g CO2/MJ | 71.9 g CO2/MJ | 1.00 | **3.161 t CO2 / tonne**<br>*(3.003 kg CO2 / L @ 0.95 kg/L)* | BEE PAT / CEA V21.0 / IPCC 2006 |
| **Furnace Oil (FO)** | Heavy Residual Fuel Oil | **10,100 kcal/kg** | 42.29 MJ/kg | 0.952 (+5.0% GCV) | 75.5 g CO2/MJ | 71.9 g CO2/MJ | 1.00 | **3.040 t CO2 / tonne**<br>*(2.888 kg CO2 / L @ 0.95 kg/L)* | BEE PAT / CEA V21.0 / IPCC 2006 |
| **Diesel (HSD)** | High Speed Diesel (0.83 kg/L) | **10,500 kcal/kg** | 43.96 MJ/kg | 0.952 (+5.0% GCV) | 72.6 g CO2/MJ | 69.1 g CO2/MJ | 1.00 | **3.038 t CO2 / tonne**<br>*(2.521 kg CO2 / L @ 0.83 kg/L)* | CEA V21.0 App. B / BEE Book 1 |
| **Diesel (HSD - IPCC)**| Standard IPCC default | **10,270 kcal/kg** | 43.00 MJ/kg (NCV) | NCV standard | 74.1 g CO2/MJ | 70.5 g CO2/MJ | 1.00 | **3.186 t CO2 / tonne**<br>*(2.680 kg CO2 / L @ 0.84 kg/L)* | IPCC 2006 Table 2.2 / GHG Protocol |
| **Propane** | Commercial pure propane (C3H8)| **11,950 kcal/kg** | 50.03 MJ/kg | 0.922 (+8.5% GCV) | 64.2 g CO2/MJ | 59.17 g CO2/MJ | 1.00 | **2.960 t CO2 / tonne**<br>*(1.510 kg CO2 / L @ 0.51 kg/L)* | IPCC 2006 Vol 2 Ch 1 / BEE Book 1 |
| **LPG** | Commercial 60:40 propane/butane | **11,800 kcal/kg** | 49.40 MJ/kg | 0.922 (+8.5% GCV) | 63.1 g CO2/MJ | 58.15 g CO2/MJ | 1.00 | **2.873 t CO2 / tonne**<br>*(1.551 kg CO2 / L @ 0.54 kg/L)* | IPCC 2006 Table 2.2 / India GHG Prog. |
| **Natural Gas** | Domestic / RLNG (per SCM) | **8,800 kcal/SCM** | 36.84 MJ/SCM | 0.909 (+10.0% GCV) | 54.3 g CO2/MJ | 49.4 g CO2/MJ | 1.00 | **1.820 kg CO2 / SCM**<br>*(~2.366 t CO2 / tonne @ 0.77 kg/SCM)* | CEA V21.0 App. B / BEE PAT |
| **Natural Gas (IPCC)**| Pipeline Natural Gas | **9,080 kcal/SCM** | 38.00 MJ/SCM (NCV) | NCV standard | 56.1 g CO2/MJ | 50.5 g CO2/MJ | 1.00 | **2.132 kg CO2 / SCM**<br>*(~2.750 t CO2 / tonne)* | IPCC 2006 Table 2.2 / GHG Protocol |

*Notes on conversion units:*
- 1 calorie = 4.1868 Joules; 1 kcal = 4.1868 kJ; 1 Gcal = 4.1868 GJ.
- 1 g CO2/MJ = 1 kg CO2/GJ = 1 t CO2/TJ.
- **SCM**: Standard Cubic Metre (at 15 °C, 1.01325 bar absolute).
- **TOE (Tonne of Oil Equivalent)** per BEE standard = 10,000,000 kcal = 41.868 GJ = 11,630 kWh.

---

## 2. Fuel-Specific Analysis & Engineering Nuances

### A. Coal (Indian Non-Coking Coal vs. Imported Coal)
- **Indian Coal Quality in Captive Power**: Indian domestic non-coking coal, notably sourced from Odisha coalfields (Mahanadi Coalfields Ltd - Talcher and Ib Valley fields supplying JSL Jajpur), has high mineral matter (ash content typically 35%–45%) and high moisture (10%–14%), resulting in low Gross Calorific Value.
- **Grading Structure (Ministry of Coal & BEE PAT Scheme)**:
  - **Grade G10**: GCV 4,301–4,600 kcal/kg (Avg: 4,450 kcal/kg -> **1.688 t CO2/tonne**)
  - **Grade G11**: GCV 4,001–4,300 kcal/kg (Avg: 4,150 kcal/kg -> **1.574 t CO2/tonne**)
  - **Grade G12**: GCV 3,701–4,000 kcal/kg (Avg: 3,850 kcal/kg -> **1.460 t CO2/tonne**)
  - **Grade G13**: GCV 3,401–3,700 kcal/kg (Avg: 3,550 kcal/kg -> **1.347 t CO2/tonne**)
  - **CEA Baseline Database Standard**: CEA uses a representative national weighted GCV of **3,755 kcal/kg** for non-coking utility and captive power coal, yielding **1.424 t CO2/t coal**.
- **Carbon Intensity vs. Ash Paradox**:
  - While low-grade Indian coal emits *fewer* tonnes of CO2 per bulk tonne delivered (because ~40% of the rock is inert ash), its **specific emission per megajoule of useful heat** is significantly higher (**95.8 g CO2/MJ NCV**) than imported bituminous coal (**89.5 g CO2/MJ NCV**).
  - Furthermore, burning high-ash coal degrades boiler thermal efficiency (increased auxiliary power consumption for pulverizers, draft fans, and electrostatic precipitators), leading to higher net CPP emissions of **1.04–1.12 t CO2/MWh generated**.
- **Oxidation Factor**: India's MoEFCC and CEA specify an oxidation factor of **0.98 (98%)** for Indian coal to reflect unburnt carbon remaining in bottom ash and fly ash (consistent with IPCC 1996/2006 guidelines for domestic pulverized fuel boilers). Imported coal uses **1.00 (100%)**.

### B. LSHS (Low Sulphur Heavy Stock) and Furnace Oil (FO)
- **Industrial Function**:
  - In captive power plants: Secondary fuel used for initial boiler light-up, warm-up, low-load flame stabilization, and shutdown.
  - In rolling mills: Direct fuel for reheating furnaces (billets, blooms, and slabs prior to hot rolling) and intermediate annealing furnaces.
- **Difference Between LSHS and FO**:
  - **LSHS**: Derived from paraffinic indigenous crude (e.g., Assam or Mumbai High). Characterized by very low sulfur content (<0.5% vs. 2.0%–4.0% in normal furnace oil), higher pour point (>45 °C requiring heated transfer lines and storage tanks), and a higher calorific value (**~10,500 kcal/kg GCV**).
  - **Furnace Oil (FO)**: Standard residual fuel oil with higher sulfur and slightly lower calorific value (**~10,100 kcal/kg GCV**).
- **Emissions Factors**:
  - CEA and BEE specify an emission factor of **75.5 g CO2/MJ (NCV)** and **71.9 g CO2/MJ (GCV)**.
  - **LSHS**: **3.161 t CO2 / tonne** (or **3.003 kg CO2 / litre** at 0.95 kg/L density).
  - **Furnace Oil**: **3.040 t CO2 / tonne** (or **2.888 kg CO2 / litre** at 0.95 kg/L density).
  - Under international IPCC 2006 default (Table 2.2: 77,400 kg CO2/TJ NCV), the factor equates to **3.127 t CO2 / tonne** (or **2.971 kg CO2 / litre**).

### C. Propane and Liquefied Petroleum Gas (LPG)
- **Industrial Function**:
  - Extensively used in stainless steel cold rolling mills, Bright Annealing (BA) lines, and Annealing & Pickling Lines (APL) where sulphur-free, clean combustion is essential to prevent surface contamination, scaling, or discolouration of high-value stainless sheets (e.g., 300-series and 400-series grades).
  - Ladle pre-heating and tundish heating prior to casting.
- **Emissions Factors**:
  - Pure Commercial Propane (C3H8): **64.2 g CO2/MJ (NCV)**; at GCV 11,950 kcal/kg -> **2.960 t CO2 / tonne**; at liquid density 0.51 kg/L -> **1.510 kg CO2 / litre**.
  - Commercial LPG (60% Propane / 40% Butane): **63.1 g CO2/MJ (NCV)**; at GCV 11,800 kcal/kg -> **2.873 t CO2 / tonne**; at liquid density 0.54 kg/L -> **1.551 kg CO2 / litre**.

### D. High Speed Diesel (HSD)
- **Industrial Function**:
  - Captive emergency Diesel Generator (DG) sets for black-start, critical backup power to EAF/AOD cooling water pumps, crane hydraulics, and furnace tilt systems.
  - Heavy material-handling equipment: slag pot carriers, scrap yard front loaders, ladle haulers, and internal diesel shunting locomotives.
- **Emissions Factors**:
  - CEA Baseline Database Appendix B: **72.6 g CO2/MJ (NCV)**; GCV basis: **69.1 g CO2/MJ**; at GCV 10,500 kcal/kg -> **3.038 t CO2 / tonne**; at density 0.83 kg/L -> **2.521 kg CO2 / litre**.
  - Standard IPCC 2006 / GHG Protocol Default: **74.1 g CO2/MJ (NCV)** -> **3.186 t CO2 / tonne** -> **2.680 kg CO2 / litre** (assuming density 0.84 kg/L).

### E. Natural Gas (Piped Natural Gas / Re-gasified LNG - RLNG)
- **Industrial Function**:
  - Replaces heavy fuel oils (LSHS/FO) in rolling mill reheating furnaces, continuous annealing lines, and tundish pre-heaters to drastically cut carbon and eliminate SOx emissions.
  - Potential fuel for gas turbine captive cogeneration (combined cycle heat and power).
- **Emissions Factors**:
  - CEA Baseline Database Appendix B (conservative lower 95% CI bound): **54.3 g CO2/MJ (NCV)**; GCV basis: **49.4 g CO2/MJ**; at standard GCV of 8,800 kcal/SCM -> **1.820 kg CO2 / SCM** (or **~2.366 t CO2 / tonne gas**).
  - Standard IPCC 2006 Table 2.2 Default: **56.1 g CO2/MJ (NCV)**; GCV basis: **50.5 g CO2/MJ**; at typical imported LNG GCV of 9,080 kcal/SCM -> **2.132 kg CO2 / SCM** (or **~2.750 t CO2 / tonne gas**).

---

## 3. Application to Jindal Stainless Decarbonization Model

In Jindal Stainless's disclosed GHG inventory (FY24 Scope 1 intensity = **1.70 t CO2e/tcs**, representing **79%** of combined Scope 1+2 emissions):
- Captive coal combustion in the 264 MW Jajpur power plant accounts for the overwhelming majority of direct stationary combustion emissions.
- Liquid/gaseous fossil fuels in rolling and finishing (reheating furnaces, annealing lines) represent the remainder of Scope 1.

### Modeling "Fuel Mix for Captive Power & Reheating" as an Optimization Lever

To evaluate fuel substitution scenarios in the Carbon & Energy Calculator:

1. **Captive Power Baseline Formula**:
   $$\text{Emissions}_{\text{CPP Coal}} (\text{t CO2}) = \text{Coal Consumed (t)} \times \text{GCV}_{\text{coal}} (\text{kcal/kg}) \times 4.1868 \times 10^{-6} \times \text{EF}_{\text{GCV}} (\text{g/MJ}) \times 0.98$$
   - *Baseline:* For 1 tonne of Grade G12 non-coking coal (3,850 kcal/kg), emissions = **1.460 t CO2**.
   - *Power Generation Intensity:* At a heat rate of 2,500 kcal/kWh gross (typical 135 MW subcritical CPP units) and 9% auxiliary consumption, coal CPP electricity intensity = **1.045 t CO2/MWh** (substantially dirtier than the national grid average of 0.710 t CO2/MWh).

2. **Rolling Mill Fuel Switching Lever (FO/LSHS -> Natural Gas / Bio-LDO / Green H2)**:
   - **Baseline (Furnace Oil / LSHS)**: Emits **~71.9 g CO2/MJ** heat input (**3.04–3.16 t CO2/t fuel**).
   - **Natural Gas Substitution**: Emits **~49.4–50.5 g CO2/MJ** heat input.
     $$\text{Emission Reduction} = \frac{71.9 - 49.4}{71.9} \approx \mathbf{31.3\%\text{ reduction in direct reheating furnace emissions}}$$
   - **Bio-LDO Substitution (Jindal Hisar Track Record)**: Jindal replaced 30% of liquid fossil fuel with Bio-LDO (Bio-Light Diesel Oil, derived from plant oils/tallow) in Hisar hot rolling mills, abating ~17,400 t CO2e/year. Bio-LDO has biogenic carbon accounting treated as near-zero fossil Scope 1.
   - **Green Hydrogen Substitution (Jindal Hisar Track Record)**: Commissioned 90 Nm³/hr green H2 plant (abating ~2,700 t CO2e/yr) displacing cracked ammonia/propane in bright annealing. Feasibility study underway for 700 Nm³/hr at Jajpur.

---

## 4. Prioritized Source Hierarchy & Citations

1. **Central Electricity Authority (CEA), Ministry of Power, Government of India**:
   - *CO2 Baseline Database for the Indian Power Sector, User Guide Version 21.0* (Published December 2025).
   - Specific Reference: Section 4.3 (Calculation Approach - Station Level), Table 5, and Appendix B (Assumptions for CO2 Emission Calculations: Fuel Emission Factors, GCV, and Oxidation Factors).
   - [CEA Official Database](https://cea.nic.in/cdm-co2-baseline-database/?lang=en)

2. **Bureau of Energy Efficiency (BEE), Ministry of Power, Government of India**:
   - *Normalization Document and Monitoring & Verification (M&V) Guidelines for Thermal Power Plants and Iron & Steel Sector* under the Perform, Achieve and Trade (PAT) Scheme (BEE PAT Cycle II–VI).
   - *National Examination for Certification of Energy Managers and Energy Auditors: Guide Book 1 — General Aspects of Energy Management & Energy Audit* (Bureau of Energy Efficiency, New Delhi).
   - [BEE India Official Portal](https://beeindia.gov.in)

3. **Ministry of Environment, Forest and Climate Change (MoEFCC), Government of India**:
   - *India: Third Biennial Update Report (BUR-3) to the UNFCCC* (2021), Chapter 2: National Greenhouse Gas Inventory, Energy Sector Methodologies and Country-Specific Emission Factors.
   - *India's Initial National Communication (NatCom 1) and Second National Communication (NatCom 2) to the UNFCCC* (derived from experimental analysis of 120 Indian coal seam samples).
   - [UNFCCC India BUR-3 Filing](https://unfccc.int/sites/default/files/resource/INDIA_%20BUR3_20.02.2021_High.pdf)

4. **Intergovernmental Panel on Climate Change (IPCC)**:
   - *2006 IPCC Guidelines for National Greenhouse Gas Inventories*, Prepared by the National Greenhouse Gas Inventories Programme, Eggleston H.S., Buendia L., Miwa K., Ngara T. and Tanabe K. (eds). Published: IGES, Japan.
   - Volume 2: Energy, Chapter 1 (Table 1.4: Default Net Calorific Values and Lower/Upper Bounds) and Chapter 2 (Table 2.2: Default Emission Factors for Stationary Combustion in the Energy Industries and Manufacturing).
   - [IPCC NGGIP Guidelines](https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol2.html)

5. **GHG Protocol & India GHG Program**:
   - *GHG Protocol Emission Factor Database (EFDB) & Cross-Sector Stationary Combustion Tool* (Version 4.8 / GHG Protocol, WRI / WBCSD).
   - *India GHG Program*: Voluntary GHG accounting standard anchored by WRI India, Confederation of Indian Industry (CII), and TERI.
   - [India GHG Program](https://indiaghgp.org) / [GHG Protocol Tools](https://ghgprotocol.org/calculation-tools)
