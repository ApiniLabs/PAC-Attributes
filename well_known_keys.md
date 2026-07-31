These are well-known keys for common scenarios:

## Table of Content
- [Table of Content](#table-of-content)
- [General Metadata](#general-metadata)
- [Logistics and Product Identifiers](#logistics-and-product-identifiers)
- [Chemistry and Scientific Terms](#chemistry-and-scientific-terms)
- [Safety](#safety)
- [Documents](#documents)



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
Pressure | https://qudt.org/vocab/quantitykind/Pressure
Ambient Pressure | https://qudt.org/vocab/quantitykind/AmbientPressure
Refractive Index | https://qudt.org/vocab/quantitykind/RefractiveIndex
Solubility in Water | https://qudt.org/vocab/quantitykind/WaterSolubility


|||
**Concepts (IUPAC Gold Book)**
Absorbance |https://doi.org/10.1351/goldbook.A00028
Assay | https://doi.org/10.1351/goldbook.08014
Concentration | https://doi.org/10.1351/goldbook.C01222
Evaporation | https://doi.org/10.1351/goldbook.E02227
pH | https://doi.org/10.1351/goldbook.P0452
Polarity of Solvent | https://doi.org/10.1351/goldbook.P04710

Wavelength | https://doi.org/10.1351/goldbook.W06659|
|||
**Methodology**
Reference Method | https://doi.org/10.1351/goldbook.R05231
Reference Material | https://doi.org/10.1351/goldbook.R05230
Reference Material Certificate | https://doi.org/10.1351/goldbook.08117
...
|||
**Chemical Identifiers**

Preferred source: [identifiers.org](https://identifiers.org) registries and [Wikidata](https://www.wikidata.org) properties, since neither CAS nor EC numbers are covered by IUPAC Gold Book.

CAS Number | https://registry.identifiers.org/registry/cas
EC Number | https://www.wikidata.org/wiki/Property:P232
Empirical Formula | https://w3id.org/chemrof/generalized_empirical_formula
Water Content | https://identifiers.org/CHEBI:15377 | Reuses ChEBI's identifier for the substance "water" itself as the key for its content/purity fraction - there's no dedicated "water content" term to key off instead.



## Safety

Preferred source for keys: https://pubchem.ncbi.nlm.nih.gov/ghs 
> [!Note] Pubchem maintains a list of the definitions in [Globally Harmonized System of Classification and Labelling of Chemicals](https://unece.org/transport/publications/globally-harmonized-system-classification-and-labelling-chemicals-ghs-rev-10), which is ideally suited for our needs.
> [!Important]
> All identifiers are defined on the same page, but there are anchors, we can use (e.g. https://pubchem.ncbi.nlm.nih.gov/ghs/#P101)


| Attribute |  Recommended Key | Comment |
|---|---|---|
Hazard Statements | https://pubchem.ncbi.nlm.nih.gov/ghs/#_haz |
H204 | https://pubchem.ncbi.nlm.nih.gov/ghs/#H204
Precautionary Statements | https://pubchem.ncbi.nlm.nih.gov/ghs/#_prec | 
P101 |https://pubchem.ncbi.nlm.nih.gov/ghs/#P101
Pictograms | https://pubchem.ncbi.nlm.nih.gov/ghs/#_pict 
...

Attribute Values for Pictograms are accessible as well: 
https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS08.gif
https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS08.svg



## Documents

Preferred source for keys: [Wikidata](https://www.wikidata.org)

| Attribute | Recommended Key | Comment |
|---|---|---|
Safety Data Sheet | https://www.wikidata.org/wiki/Q222067
Certificate of Analysis | https://www.wikidata.org/wiki/Q1056230
Datasheet | https://www.wikidata.org/wiki/Q20819677
User Manual | https://www.wikidata.org/wiki/Q1057179








