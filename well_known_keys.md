These are well-known keys for common scenarios:

## Table of Content
- [Table of Content](#table-of-content)
- [General Metadata](#general-metadata)
- [Logistics and Product Identifiers](#logistics-and-product-identifiers)
- [Chemistry and Scientific Terms](#chemistry-and-scientific-terms)
- [Safety](#safety)



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

Preferred source for keys: [IUPAC Gold Book](https://goldbook.iupac.org/terms), especially the [quantities](https://goldbook.iupac.org/indexes/quantities)
> [!IMPORTANT]
> Make sure to use the DOI , not the view (e.g. [https://doi.org/10.1351/goldbook.A00028](https://doi.org/10.1351/goldbook.A00028), not ~~[https://goldbook.iupac.org/terms/view/A00028](https://goldbook.iupac.org/terms/view/A00028)~~)

| Attribute |  Recommended Key | Comment |
|---|---|---|
**Material Properties**
Absorbance |https://doi.org/10.1351/goldbook.A00028
Concentration | https://doi.org/10.1351/goldbook.C01222
Density | https://doi.org/10.1351/goldbook.D01590
Evaporation | https://doi.org/10.1351/goldbook.E02227
pH | https://doi.org/10.1351/goldbook.P0452
Melting Temperature | https://doi.org/10.1351/goldbook.12788
Polarity of Solvent | https://doi.org/10.1351/goldbook.P04710
Pressure | https://doi.org/10.1351/goldbook.P04819
Refractive Index | https://doi.org/10.1351/goldbook.R05240
Solubility | https://doi.org/10.1351/goldbook.S05740
Wavelength | https://doi.org/10.1351/goldbook.W06659|
|||
**Methodology**
Reference Method | https://doi.org/10.1351/goldbook.R05231
Reference Material | https://doi.org/10.1351/goldbook.R05230
Reference Material Certificate | https://doi.org/10.1351/goldbook.08117
...



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








