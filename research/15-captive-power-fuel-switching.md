# Strategic Valuation of Captive Power Fuel Switching in India: Default Greenhouse Gas Emission Factors and Regulatory Alignment

## Introduction to Industrial Decarbonization and Captive Power in India
Captive Power Plants constitute a critical infrastructural pillar for India’s energy-intensive industries (aluminum, cement, iron and steel). Historically, the imperative for grid independence and reliable baseload power drove heavy reliance on coal, high-speed diesel, and heavy liquid fuels such as furnace oil. In many operations, captive power generation frequently accounts for a dominant share of total facility emissions (e.g., ~80% in primary aluminum smelting).

Driven by India’s NDCs, the Carbon Credit Trading Scheme (CCTS), and the EU CBAM, industries face unprecedented pressure to reduce Scope 1 and 2 emissions. Fuel switching in captive power generation—transitioning from high-carbon fossil fuels to lower-carbon alternatives like propane, or entirely zero-carbon renewable systems—represents one of the most immediate decarbonization levers.

To accurately model the carbon reduction potential, precise alignment with recognized GHG accounting standards is mandatory. Using generic global default multipliers instead of localized Indian fuel characteristics routinely leads to severe over/under-reporting, triggering penalties during MoEFCC verification audits.

## Thermodynamic Foundations of Carbon Accounting
The precise physical and chemical characteristics of the fuel combusted dictate the volume of CO2 released per unit of thermal energy generated.
- **Gross Calorific Value (GCV) / Higher Heating Value (HHV):** Assumes water vapor from combustion is fully condensed, recovering latent heat.
- **Net Calorific Value (NCV) / Lower Heating Value (LHV):** Assumes water vapor leaves with exhaust without condensing.

GHG Protocol and IPCC 2006 universally mandate using NCV. However, commercial fuel procurement in India is strictly billed on GCV. Applying international default NCV multipliers directly to Indian GCV purchasing data artificially inflates the emissions inventory.
The Central Electricity Authority (CEA) CO2 Baseline Database provides precise regulatory assumptions for the GCV-to-NCV differential:
- Domestic Indian coal: 3.6%
- Imported coal: 5.0%
- Liquid petroleum (furnace oil, diesel): 5.0%

Furthermore, the **Oxidation Factor** accounts for unburnt carbon (bottom ash/fly ash). Indian domestic coal is assigned an oxidation factor of 0.98 (2% remains unburnt due to extreme ash content). Imported coal and liquid/gaseous fuels are assigned 1.00. Omitting the 0.98 factor for domestic coal results in an immediate, erroneous 2% inflation of Scope 1 emissions.

## India-Specific Default Emission Factors for Captive Power Fuels

### Solid Fuels: Indian and Imported Coal
Indian domestic coal is primarily non-coking, characterized by profound ash content (30-40%) and substantial moisture, suppressing effective heating value. Therefore, its emission factors deviate significantly from standard international defaults.

| Parameter | Indian / Domestic Coal | Imported Coal |
| --- | --- | --- |
| Emission Factor (NCV Basis) | 95.8 gCO2/MJ | 89.5 gCO2/MJ |
| Emission Factor (GCV Basis) | 92.5 gCO2/MJ | 85.2 gCO2/MJ |
| GCV to NCV Delta | 3.6% | 5.0% |
| Oxidation Factor | 0.98 | 1.00 |
| **Effective Fuel Emission Factor** | **90.6 gCO2/MJ** | **85.2 gCO2/MJ** |
| Default Gross Calorific Value | 3,755 kcal/kg | Facility Specific |

*Note: The BEE PAT scheme defines one Tonne of Oil Equivalent (TOE) as 10,000,000 kcal or 41,870 MJ.*

### Heavy Liquid Fuels: Furnace Oil and Low Sulphur Heavy Stock (LSHS)
Used in thermic fluid heaters and industrial boilers. LSHS contains <0.5% sulfur; standard furnace oil contains 2.0-4.0% sulfur.
- **Emission Factor (NCV Basis):** 75.5 gCO2/MJ
- **Emission Factor (GCV Basis):** 71.9 gCO2/MJ
- **Volumetric Emission Factor:** 3.12 kg CO2 / Litre

Transitioning from domestic coal (90.6 gCO2/MJ effective) to furnace oil (71.9 gCO2/MJ) reduces carbon intensity, but is economically constrained by global petroleum market volatility.

### Middle Distillates: High Speed Diesel (HSD)
Primarily utilized for emergency backup generator sets.
- **Emission Factor (NCV Basis):** 72.6 gCO2/MJ
- **Emission Factor (GCV Basis):** 69.1 gCO2/MJ
- **Volumetric Emission Factor:** 2.68 kg CO2 / Litre

While HSD presents lower carbon intensity than residual oils, its exorbitant landed cost prohibits baseload generation use.

### Gaseous Fuels: Propane and Liquefied Petroleum Gas (LPG)
Propane has a highly concentrated GCV (~11,940 kcal/kg).
- **IPCC Default Emission Factor (NCV Basis):** 63.1 gCO2/MJ
- **Mass-based Emission Factor (India GHG Program):** 3.00 tCO2 / tonne of LPG

At 63.1 gCO2/MJ, propane's emission factor is ~34% lower than domestic coal (95.8 gCO2/MJ NCV). Switching from coal to propane immediately eliminates over one-third of stationary combustion emissions purely through chemical substitution.

## Captive Power Plant Efficiencies and Thermodynamic Heat Rates
To translate fuel-specific emission factors (gCO2/MJ) into electricity-specific emission intensities (tCO2/MWh), the plant's thermodynamic heat rate must be assessed. The CEA prescribes default heat rates:

| Technology and Fuel Configuration | Gross Heat Rate (kcal/kWh) | Aux Power Consumption | Net Heat Rate (kcal/kWh) | Specific Emission Intensity (tCO2/MWh) |
| --- | --- | --- | --- | --- |
| Default Captive Coal Plant | 2,500 | 8.0% | 2,717 | 1.04 |
| Sub-100 MW Coal Plant | 2,750 | 12.0% | 3,125 | 1.19 |
| Heavy Fuel Oil / LSHS Plant | 2,117 | 3.5% | 2,193 | 0.66 |
| Diesel Engine (>10 MW) | 1,975 | 3.5% | 2,047 | 0.59 |

Replacing a baseload coal captive power plant with diesel or furnace oil remains economically untenable due to severe base fuel costs, forcing the trajectory of industrial decarbonization away from fossil-to-fossil switching toward renewable energy substitution.

## Regulatory Compliance and the Techno-Economics of Fuel Switching

### The Carbon Credit Trading Scheme and Grid Parity
The CCTS replaces the legacy PAT scheme, targeting absolute and intensity-based GHG reductions. The CEA’s Weighted Average Emission Factor for the Indian grid (currently ~0.710 to 0.727 tCO2e/MWh) serves as the baseline for evaluating grid power substitutions. By 2030, the grid emission factor is forecasted to decline to 0.43 kgCO2e/kWh.

### Value Stacking in the Transition to Renewable Energy
For an export-oriented smelter, transitioning from captive coal power to a captive solar-wind hybrid installation unlocks multiple "value stacking" revenue streams:
1. **Direct Electricity Cost Savings:** Captive coal LCOE is ~₹6.00/kWh. Captive solar-wind hybrids deliver an LCOE of ~₹4.00-4.50/kWh. Commercial saving: ₹1.50/kWh.
2. **CCTS Regulatory Value:** Displacing coal generates Carbon Credit Certificates. At ₹800/certificate against a 0.710 tCO2/MWh baseline, this yields ~₹0.57/kWh.
3. **CBAM Mitigation:** Assuming an EU ETS price of €65/tCO2e, avoiding 0.710 tCO2/MWh equates to a tax avoidance of €46.15/MWh (approx. ₹4.15/kWh).
4. **Renewable Consumption Obligations (RCO):** Self-generating renewable energy avoids purchasing RECs at market rates, saving ~₹0.34/kWh.

**Total aggregate financial return:** ₹6.56/kWh. The combined regulatory and commercial return exceeds the base operational cost of generating the renewable electricity itself.

## Conclusion
Techno-economic modeling of fuel switching requires localized carbon accounting. Using the highly specific Indian domestic coal emission factor (95.8 gCO2/MJ NCV, 0.98 oxidation) is mandatory for regulatory compliance. While switching to propane or LSHS lowers theoretical emissions by over 30%, their high OPEX restricts them to specialized process heating. For captive electricity, the strategic imperative is decisively weighted toward renewable energy hybrids, where value stacking (LCOE savings + CCTS + CBAM avoidance + RCO) transforms decarbonization mandates into highly lucrative corporate financial strategies.
