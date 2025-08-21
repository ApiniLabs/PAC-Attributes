# [`PAC-Attributes`](README.md) FAQ

**Q: When should I use `PAC-Attributes`?**
**A:** `PAC-Attributes` is made for reading simple key value pairs quickly. For anything more than simple data types, use another type of service that can be linked/found via PAC-ID resolver (e.g. for CDS Data, PDF Datasheets, etc.). If there would be a attributes service for CDS data, it would deliver the record’s metadata.

**Q: What should I use `Attribute Group`s for?
Attribute groups aintended to help grouping the client's UI. Expect clients to display these groups 'en bloc' or discard entire groups.

**Q: I want to publish a density as attribute. IUPAC goldbook defines 'density' but, does not state the measurement conditions. What shouldI do?
**A:** LabFREED aims to digitalize labs in achievable steps, and referencing a standard key is already a major improvement over proprietary approaches. Lab personnel will usually interpret density as measured under reference conditions. Nevertheless, it is recommended to include the reference conditions in the label. If you are working under non-standard or extraordinary conditions, define your own key within your own namespace.

