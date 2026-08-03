These are well-known keys for common scenarios:

## Table of Content
- [Table of Content](#table-of-content)
- [General Metadata](#general-metadata)
- [Logistics and Product Identifiers](#logistics-and-product-identifiers)
- [Identifiers](#identifiers)
- [Chemistry and Scientific Terms](#chemistry-and-scientific-terms)
- [Chemical and Appearance Properties](#chemical-and-appearance-properties)
- [Safety](#safety)
- [Storage, Handling and Shipping](#storage-handling-and-shipping)
- [Biology and Assay](#biology-and-assay)
- [Commerce and Packaging](#commerce-and-packaging)
- [Documents](#documents)
- [Event Attributes](#event-attributes)



## General Metadata

Preferred source for keys: [schema.org](https://schema.org)

| Attibute | Recommended Key | Comment
|---|---|---|
Image | https://schema.org/image
Display Name | https://schema.org/name
Alias | https://schema.org/alternateName
Description | https://schema.org/description


## Logistics and Product Identifiers

Preferred source for keys: [GS1 Application identifier](https://ref.gs1.org/ai) 

| Attribute |Recommended Key | Comment | 
|---|---|---|
Production Date | https://ref.gs1.org/ai/11 
Expiration Data | https://ref.gs1.org/ai/17
... |


## Identifiers

Preferred sources for keys: [identifiers.org](https://identifiers.org) registries and [Wikidata](https://www.wikidata.org) properties for identifiers not covered by a chemistry ontology, [w3id.org/chemrof](https://w3id.org) for structured formula/SMILES representations, and [schema.org](https://schema.org) for generic product/commerce identifiers.

| Attribute | Recommended Key | Comment |
|---|---|---|
CAS Number | https://registry.identifiers.org/registry/cas
CAS Number (alternate, e.g. TCI/VWR) | https://www.wikidata.org/wiki/Property:P231
MDL Number | https://bioregistry.io/registry/mdl
EC Number (EINECS) | https://www.wikidata.org/wiki/Property:P232
Beilstein / Reaxys Number | https://www.wikidata.org/wiki/Property:P1579
PubChem Substance ID | https://www.wikidata.org/wiki/Property:P2153
UNSPSC Code | https://www.wikidata.org/wiki/Property:P2167
InChI | https://www.wikidata.org/wiki/Property:P234
InChIKey | https://www.wikidata.org/wiki/Property:P235
Chemical Formula | https://www.wikidata.org/wiki/Property:P274 | Wikidata's generic chemical-formula property. For a structured, machine-parseable formula use Empirical Formula below instead.
Empirical Formula | https://w3id.org/chemrof/generalized_empirical_formula
SMILES | https://w3id.org/chemrof/smiles_string
UN Number | https://www.wikidata.org/wiki/Q908597
UniProtKB Accession | http://purl.obolibrary.org/obo/NCIT_C47851
Gene Identifier | http://purl.obolibrary.org/obo/NCIT_C48664
Product Code | https://schema.org/productID
Manufacturer Number / SKU | https://schema.org/sku
Lot / Batch Number | https://schema.org/lotNumber
Serial Number | https://schema.org/serialNumber
Synonym / IUPAC Name | https://schema.org/alternateName
Supplier / Manufacturer | https://schema.org/manufacturer


## Chemistry and Scientific Terms 

Preferred source for concepts: [IUPAC Gold Book](https://goldbook.iupac.org/terms), especially the [quantities](https://goldbook.iupac.org/indexes/quantities)
> [!IMPORTANT]
> Make sure to use the DOI , not the view (e.g. [https://doi.org/10.1351/goldbook.A00028](https://doi.org/10.1351/goldbook.A00028), not ~~[https://goldbook.iupac.org/terms/view/A00028](https://goldbook.iupac.org/terms/view/A00028)~~)

For measurable physicochemical quantities specifically, prefer the [QUDT quantitykind vocabulary](https://qudt.org/vocab/quantitykind/) over a Gold Book DOI.

| Attribute |  Recommended Key | Comment |
|---|---|---|
**Material Properties (QUDT quantitykind)**
Boiling Point | https://qudt.org/vocab/quantitykind/BoilingPoint
Concentration | https://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration
Density | https://qudt.org/vocab/quantitykind/Density | Previously recommended as `goldbook.D01590`; superseded by QUDT, see note above.
Flash Point | https://qudt.org/vocab/quantitykind/FlashPoint
Melting Point | https://qudt.org/vocab/quantitykind/MeltingPoint | Previously listed as "Melting Temperature" via `goldbook.12788`; superseded by QUDT, see note above.
Molar Mass | https://qudt.org/vocab/quantitykind/MolarMass
Relative Density | https://qudt.org/vocab/quantitykind/RelativeMassDensity
pH | https://qudt.org/vocab/quantitykind/PH | Previously recommended as `goldbook.P0452`; superseded by QUDT, see note above.
Viscosity | https://qudt.org/vocab/quantitykind/Viscosity
Volume | https://qudt.org/vocab/quantitykind/Volume
Mass (net) | https://qudt.org/vocab/quantitykind/Mass
Length / Diameter | https://qudt.org/vocab/quantitykind/Length
Area | https://qudt.org/vocab/quantitykind/Area
Pressure | https://qudt.org/vocab/quantitykind/Pressure | Previously recommended as `goldbook.P04819`; superseded by QUDT, see note above.
Ambient Pressure | https://qudt.org/vocab/quantitykind/AmbientPressure
Temperature | https://qudt.org/vocab/quantitykind/Temperature
Volume Flow Rate | https://qudt.org/vocab/quantitykind/VolumeFlowRate
Refractive Index | https://qudt.org/vocab/quantitykind/RefractiveIndex | Previously recommended as `goldbook.R05240`; superseded by QUDT, see note above.
Solubility in Water | https://qudt.org/vocab/quantitykind/WaterSolubility | Previously listed as "Solubility" via `goldbook.S05740`; superseded by QUDT, see note above.
Partition Coefficient (log Kow) | https://qudt.org/vocab/quantitykind/LogOctanolWaterPartitionCoefficient
Vapour Pressure | https://qudt.org/vocab/quantitykind/VapourPressure
Surface Tension | https://qudt.org/vocab/quantitykind/SurfaceTension
Specific Heat Capacity | https://qudt.org/vocab/quantitykind/SpecificHeatCapacity
Conductivity | https://qudt.org/vocab/quantitykind/ElectricConductivity
Mass Fraction | https://qudt.org/vocab/quantitykind/MassFraction
Water Content | https://qudt.org/vocab/quantitykind/MassFractionOfWater | Previously recommended as `identifiers.org/CHEBI:15377` (reusing water's own substance identifier); superseded by this QUDT mass-fraction quantity kind.
Thickness | https://qudt.org/vocab/quantitykind/Thickness
Shipping / Gross Weight | https://schema.org/weight
|||
**Conceps (IUPAC Gold Book)**
Absorbance |https://doi.org/10.1351/goldbook.A00028
Assay | https://doi.org/10.1351/goldbook.08014
Concentration | https://doi.org/10.1351/goldbook.C01222
Evaporation | https://doi.org/10.1351/goldbook.E02227
Polarity of Solvent | https://doi.org/10.1351/goldbook.P04710


Wavelength | https://doi.org/10.1351/goldbook.W06659|
|||
**Methodology**
Reference Method | https://doi.org/10.1351/goldbook.R05231
Reference Material | https://doi.org/10.1351/goldbook.R05230
Reference Material Certificate | https://doi.org/10.1351/goldbook.08117
...


## Chemical and Appearance Properties

Preferred source for keys: [Wikidata](https://www.wikidata.org), with a few `schema.org` / NCIT terms for common properties not covered there.

| Attribute | Recommended Key | Comment |
|---|---|---|
Autoignition Temperature | https://www.wikidata.org/wiki/Q558378
Decomposition Temperature | https://www.wikidata.org/wiki/Q113847680
Odour | https://www.wikidata.org/wiki/Q1971477
Vapour Density | https://www.wikidata.org/wiki/Q3023279
Particle Size | https://www.wikidata.org/wiki/Q7140503
Surface Area | https://www.wikidata.org/wiki/Q1379273
pKa | https://www.wikidata.org/wiki/Q325519
Specific Optical Rotation | https://www.wikidata.org/wiki/Q2191631
Appearance (qualitative) | https://www.wikidata.org/wiki/Q3620816
Colour | https://schema.org/color
Physical State / Form | http://purl.obolibrary.org/obo/NCIT_C73487
Material | https://schema.org/material


## Safety

Preferred source for keys: [Wikidata](https://www.wikidata.org).

| Attribute |  Recommended Key | Comment |
|---|---|---|
GHS Hazard Statement | https://www.wikidata.org/wiki/Q28360
GHS Precautionary Statement | https://www.wikidata.org/wiki/Q2467204
GHS Signal Word | https://www.wikidata.org/wiki/Q15350855
GHS Pictogram | https://www.wikidata.org/wiki/Q19360817 | For the pictogram image assets themselves (not just the concept), [PubChem's GHS page](https://pubchem.ncbi.nlm.nih.gov/ghs) hosts ready-to-use images, e.g. `https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS08.gif` and the `.svg` equivalent.
UN Hazard Class | https://www.wikidata.org/wiki/Property:P874
UN Packing Group | https://www.wikidata.org/wiki/Property:P876
CLP Annex VI Index No. | https://www.wikidata.org/wiki/Q12021577
Water Hazard Class (WGK) | https://www.wikidata.org/wiki/Q1389895
HS / TARIC Customs Code | https://www.wikidata.org/wiki/Q55237506
Heavy Metals | https://www.wikidata.org/wiki/Q105789
Assay / Purity | https://doi.org/10.1351/goldbook.08014 | Not covered by Wikidata; IUPAC Gold Book remains the preferred source here.
Sterility | http://purl.obolibrary.org/obo/NCIT_C134278
Endotoxin | http://purl.obolibrary.org/obo/NCIT_C50918
CE Marking | https://www.wikidata.org/wiki/Q467405
ISO Standard | https://www.wikidata.org/wiki/Q15087423
Medical Device Class | https://www.wikidata.org/wiki/Q6554101
Animal Origin | https://www.wikidata.org/wiki/Q629103
BSE / TSE | https://www.wikidata.org/wiki/Q154666
GMO Status | https://www.wikidata.org/wiki/Q182726
Halal | https://www.wikidata.org/wiki/Q177823
Kosher | https://www.wikidata.org/wiki/Q1076110
Vegan | https://www.wikidata.org/wiki/Q899696
Acceptance Quality Limit | https://www.wikidata.org/wiki/Q4672371


## Storage, Handling and Shipping

Preferred source for keys: [NCIT](http://purl.obolibrary.org/obo/) / [Wikidata](https://www.wikidata.org) / `schema.org`.

| Attribute | Recommended Key | Comment |
|---|---|---|
Storage Condition | http://purl.obolibrary.org/obo/NCIT_C96145
Shipping Condition | http://purl.obolibrary.org/obo/NCIT_C40353
Shelf Life | http://purl.obolibrary.org/obo/NCIT_C70855
Transport | https://www.wikidata.org/wiki/Q7590
Proper Shipping Name | https://www.wikidata.org/wiki/Q1436174
Expiry Date | https://schema.org/expires


## Biology and Assay

Preferred source for keys: domain ontologies ([EFO](http://www.ebi.ac.uk/efo/), [NCIT](http://purl.obolibrary.org/obo/), [CHMO](http://purl.obolibrary.org/obo/)) and [Wikidata](https://www.wikidata.org) where no ontology term fits.

| Attribute | Recommended Key | Comment |
|---|---|---|
Cell Type | http://www.ebi.ac.uk/efo/EFO_0000324
Sample Type | http://purl.obolibrary.org/obo/NCIT_C210102
Application (Technique) | http://purl.obolibrary.org/obo/NCIT_C60755
DNA Polymerase | http://purl.obolibrary.org/obo/NCIT_C19172
Polymerase Chain Reaction | http://purl.obolibrary.org/obo/NCIT_C17003
Transfection | http://purl.obolibrary.org/obo/NCIT_C17209
Detection Method | http://purl.obolibrary.org/obo/CHMO_0001709
Molecular Target | http://purl.obolibrary.org/obo/NCIT_C16128
Species Reactivity | https://schema.org/appliesToTaxon
Buffer / Solution | https://www.wikidata.org/wiki/Q208465
Stabiliser | https://www.wikidata.org/wiki/Q910592
Preservative | https://www.wikidata.org/wiki/Q274579
Food Additive | https://www.wikidata.org/wiki/Q350176
Protein | https://www.wikidata.org/wiki/Q8054
Fatty Acid | https://www.wikidata.org/wiki/Q61476
Enzyme Activity | https://www.wikidata.org/wiki/Q22035510
Bacteria | https://www.wikidata.org/wiki/Q10876
Mycoplasma | https://www.wikidata.org/wiki/Q210975
Fungi | https://www.wikidata.org/wiki/Q764
Virus | https://www.wikidata.org/wiki/Q808
Microbial Contamination | https://www.wikidata.org/wiki/Q118218165


## Commerce and Packaging

Preferred source for keys: `schema.org`, with NCIT terms for packaging-specific concepts.

| Attribute | Recommended Key | Comment |
|---|---|---|
Brand / Product Line | https://schema.org/brand
Grade | http://purl.obolibrary.org/obo/NCIT_C48309
Format (Kit / Packaging) | http://purl.obolibrary.org/obo/NCIT_C42761
Container / Closure Packaging | http://purl.obolibrary.org/obo/NCIT_C113033
Pack Size (Count) | https://schema.org/numberOfItems
Size / Pack Descriptor | https://schema.org/size
Quantity | https://schema.org/quantity
Price | https://schema.org/price
Category (Storefront) | https://schema.org/category
Intended Use | https://schema.org/potentialUse
Country of Origin | https://schema.org/countryOfOrigin
Disambiguating Description | https://schema.org/disambiguatingDescription
Usage Info | https://schema.org/usageInfo
Protein Content | https://schema.org/proteinContent
Carbohydrate Content | https://schema.org/carbohydrateContent
Fat Content | https://schema.org/fatContent
Unmapped Field (fallback) | https://schema.org/additionalProperty/\<snake_case_name\> | Use only when nothing above fits.


## Documents

Preferred source for keys: [Wikidata](https://www.wikidata.org)

| Attribute | Recommended Key | Comment |
|---|---|---|
Safety Data Sheet | https://www.wikidata.org/wiki/Q222067
Certificate of Analysis | https://www.wikidata.org/wiki/Q1056230
Datasheet | https://www.wikidata.org/wiki/Q20819677
User Manual | https://www.wikidata.org/wiki/Q1057179


## Event Attributes

For `PAC-ID`s identifying event tickets rather than products. Preferred source for keys: `schema.org`.

| Attribute | Recommended Key | Comment |
|---|---|---|
Attendee Name | https://schema.org/name
Given Name | https://schema.org/givenName
Family Name | https://schema.org/familyName
Company | https://schema.org/affiliation
Booking Number | https://schema.org/reservationNumber
