---
topic: EU Digital Product Passport (DPP) Technical Specifications for Iron and Steel under ESPR
date: 2026-09-11
method: user-provided (Gemini Deep Research)
requested_by: user
status: complete
used_in: []
---

# Digital Product Passport (DPP) for Iron and Steel — Technical Specifications

The DPP under ESPR (Regulation (EU) 2024/1781) functions as a decentralized digital twin carrying life-cycle, metallurgical, and environmental data for every batch of steel placed on the EU market.

## 1. Mandatory Data Fields for Iron and Steel

The JRC preparatory studies and CIRPASS consortium outputs anchor the DPP to the industry-standard heat number and digitized EN 10204 Mill Test Certificates.

| Category | Mandatory Data Fields | Source / Reference Standard |
|---|---|---|
| **Identification** | Heat number, batch/lot ID, steel grade, dimensions | UPI (Unique Product Identifier) via ERP |
| **Environmental** | Global Warming Potential (kg CO₂e/kg), water usage | Life Cycle Assessment (LCA) |
| **Circularity** | Recycled scrap content (%), dismantlability metrics | ESPR Circularity requirements |
| **Quality & Safety** | Chemical composition, mechanical properties, REACH SVHCs | Mill Test Certificates (EN 10204 3.1/3.2) |

## 2. Technical Architecture and EU Standards

Governed by CEN/CENELEC JTC 24 standard series (EN 18216 through EN 18223), published May 2026. Hybrid architecture: EU Commission operates central registry for unique identifiers; passport data hosted decentrally by third-party providers or manufacturers.

| Standard | Purpose |
|---|---|
| **EN 18219** | Unique Product Identifier (UPI), Unique Operator Identifier (UOI), Unique Facility Identifier (UFI) |
| **EN 18220** | Data Carriers — 2D data-matrix or QR codes physically attached to steel coil/plate/batch packaging |
| **EN 18216** | Data Exchange — open, content-negotiated HTTP serving W3C JSON-LD or Asset Administration Shell (AAS) formats |
| **EN 18222 & EN 18223** | Interoperability APIs — standardized REST APIs for lifecycle management, direct ERP/PLM integration |

## 3. Implementation Timeline

Iron and steel classified as **priority intermediate products** in the first wave.

| Date | Milestone |
|---|---|
| April 2025 | ESPR Working Plan 2025-2030 adopted, confirming iron/steel in first wave |
| Q4 2026 | Indicative adoption of product-specific Delegated Act for iron and steel |
| **2028 (estimated)** | **Mandatory compliance enforcement** (18-month transition after Delegated Act publication) |

## 4. Industry Pilots

| Company | DPP Implementation |
|---|---|
| **Outokumpu** | Piloting product-specific carbon footprint tracing: 90% recycled content, 1.52 kg CO₂e/kg (75% below global avg) |
| **thyssenkrupp & ArcelorMittal** | Transitioning ERP, lab, and quality data into digital formats tied to heat numbers. Automating green steel certificates and lab data into EU supply chain |

## 5. Intersection with CPR and EPDs

For construction-bound steel, the ESPR DPP must interoperate with revised CPR (2024/3110):

- **DoPC Integration**: Declaration of Performance and Conformity merges into single DoPC. DPP acts as immutable digital carrier over the product's 50+ year lifespan.
- **EN 15804+A2 Alignment**: EPDs supply mandatory GWP metrics for CE marking. DPP digitizes EN 15804+A2 modules (A1-A3, A4-A5, B, C, D) into machine-readable ILCD+EPD formats.

## Sources
- CIRPASS and CIRPASS-2 consortium publications
- CEN/CENELEC JTC 24 standards (EN 18216-18223, published May 2026)
- European Commission JRC preparatory studies for ESPR steel delegated act
- Battery Regulation DPP (precedent)
- Outokumpu, thyssenkrupp, ArcelorMittal pilot disclosures
