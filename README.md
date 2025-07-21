# PAC-Attributes


## In a Nutshell
PAC-ID Attributes standardizes a generic, neutral interface for retrieving metadata about an item identified with a PAC-ID.


## Introduction
PAC-IDs expose only minimal human-readable information (issuer, category, item ID). However, user-facing applications require additional metadata—such as a display name or physical properties. Embedding such data in the PAC is undesirable due to size, internationalization complexity and  mutability issues.

While issuers may offer proprietary APIs to fetch this data, these are not usable generically. PAC-ID Attributes defines a neutral, standardized interface for retrieving item metadata, decoupling data consumers from provider-specific implementations.


## Terminology
Term | Description
:--|:--
`Attribute Server` | A server which published attributes according to this specification
`Attribute Client` | Any application which requests attributes from an `Attribute Server`. 





## Specification

### Endpoint
It is RECOMMENDED to use the term 'attributes' in the url of the attribute server, e.g. `https://attributes.mettorius.com.` or `https://www.mettorius.com/attributes` but any valid url is fine. 

Attribute Services are found via the `PAC-ID Resolver`’s mapping table. Entries with `attributes-generic` in the 'service-type' column are attribute services.

### Request
Attributes are retrieved from the `Attribute Server` by a HTTP GET request with this json body: 
```json
{
  "pacs": [
     "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/1234",
     "HTTPS://PAC.METTORIUS.COM/-MD/BAL501/5897*59K77LWDX8W" 
   ],  
  "include_translations": true
}
```
Field | Description 
:--- | :---
`pacs` | A list of PAC-ID, serialized as urls. <br>`PAC-ID`s MUST be valid and MAY contain extensions. <br>`pacs` MUST NOT exceeding 100 items. 
`include_translations` | Instructs the server to include translations in the response. <br> MUST be boolean. <br>If omitted the server MUST  treat it as true



### Response
The `Attribute Server` MUST send a response of this form
<!-- BEGIN RESPONSE JSON -->
```json
{
  "schema_version": "1.0",
  "responses": [
    {
      "pac_url": "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/12346/EXAMPLE",
      "response_from": "2025-07-21T10:05:58.493467",
      "attribute_groups": [
        {
          "key": "ProductionData",
          "attributes": [
            {
              "key": "MfgDate",
              "value": "2015-10-05T10:12:00",
              "valid_until": "forever",
              "type": "datetime"
            },
            {
              "key": "MaxWeight",
              "value": "100.00",
              "type": "numeric",
              "unit": "GRM"
            }
          ]
        },
        {
          "key": "Maintenance",
          "attributes": [
            {
              "key": "CalWeight",
              "value": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002",
              "type": "reference"
            },
            {
              "key": "CalDate",
              "value": "2025-07-20T00:00:00",
              "valid_until": "2025-08-20T00:00:00",
              "type": "datetime"
            },
            {
              "key": "DailyCheckResult",
              "value": "OK",
              "valid_until": "2025-07-20T00:00:00",
              "observed_at": "2025-07-20T00:00:00",
              "type": "text"
            }
          ]
        },
        {
          "key": "Random",
          "attributes": [
            {
              "key": "Foo",
              "value": "aNaE4aZvav",
              "type": "text"
            },
            {
              "key": "Foo",
              "value": "lxx8ieK3go",
              "type": "text"
            },
            {
              "key": "Bar",
              "value": "6yf1Ti0L0Z",
              "type": "text"
            }
          ]
        },
        {
          "key": "PACAnalyzer",
          "attributes": [
            {
              "key": "IsPAC-CAT",
              "value": "This PAC-ID follows the PAC-CAT spezifications.",
              "type": "text"
            },
            {
              "key": "Category",
              "value": "Material_Device",
              "type": "text"
            }
          ]
        }
      ]
    },
    {
      "pac_url": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002",
      "response_from": "2025-07-21T10:05:58.493467",
      "attribute_groups": [
        {
          "key": "MetaData",
          "attributes": [
            {
              "key": "DisplayName",
              "value": "Calibration Weight PRN003",
              "type": "text"
            }
          ]
        },
        {
          "key": "ProductionData",
          "attributes": [
            {
              "key": "NominalWeight",
              "value": "50.0",
              "valid_until": "forever",
              "type": "numeric",
              "unit": "GRM"
            }
          ]
        },
        {
          "key": "Random",
          "attributes": [
            {
              "key": "Deadmeat",
              "value": "lWD8Eoz6tc",
              "type": "text"
            },
            {
              "key": "Deadmeat",
              "value": "MJUIP2Z6c1",
              "type": "text"
            },
            {
              "key": "Deadmeat",
              "value": "FMzHcflGsY",
              "type": "text"
            }
          ]
        },
        {
          "key": "PACAnalyzer",
          "attributes": [
            {
              "key": "IsPAC-CAT",
              "value": "This PAC-ID follows the PAC-CAT spezifications.",
              "type": "text"
            },
            {
              "key": "Category",
              "value": "Material_Device",
              "type": "text"
            }
          ]
        }
      ]
    }
  ],
  "translations": [
    {
      "key": "MfgDate",
      "translations": {
        "en": "Manufactoring date",
        "en-US": "Manufactoring date",
        "fr": "Date de fabrication"
      }
    },
    {
      "key": "CalWeight",
      "translations": {
        "en": "Calibration weight",
        "fr": "Poids calibration"
      }
    },
    {
      "key": "MaxWeight",
      "translations": {
        "en": "Maximum weight",
        "fr": "Poids maximal"
      }
    }
  ]
}
```
<!-- END RESPONSE JSON -->

#### Attribute Data Type
```json
{
    "key": ... ,
    "type": ... // "bool", "datetime", "numeric", "text", "reference"
    "value": ...,
    "unit": ... //optional. Used for numeric attributes only.

    "valid_until": ... // "forever" or a datetime in ISO 8601
    "observed_at": ...
}
```

The `key` MUST be unique within an `attribute group`, but it is RECOMMENDED to choose keys which are unique within the entire Attribute Service.
It is RECOMMENDED to choose `key`s in English language, so they are intelligible to humans (expect them to be displayed to end users as fallback) 



| type| value | unit |
| --- | --- | --- |
bool | ```true``` or ```false``` | -
datetime | MUST be a date-time serialized in ISO 8601 format. <br> MUST be in UTC ('2025-07-21T15:30:00+02:00' or '2025-07-21T15:30:00Z') | -
numeric | String representing a number in decimal or scientific notation: '-0.518' or '-51.89E-2' (same as TREX) | MUST be a `Unit of Measure Common Code` [^1]. Plain numbers MUST NOT be used; Use 'C62' for unitless values. Attributes of type NumericValueWithUnit SHOULD be using SI units. .
text | Text consisting of any Unicode characters. Text SHOULD NOT span multiple lines. | -
reference | A string with the semantic meaning that it refers to item. It is RECOMMENDED to use `PAC-ID`s serialized as url. | -

[^1]: Unit of Measure Common Code as defined by UN/CEFACT in REC 20 ([https://unece.org/trade/uncefact/cl-recommendations](https://unece.org/trade/uncefact/cl-recommendations) > REC20 > Latest Revision > Column “CommonCode“ of Annexes I-III Excel File)

<span style="color:red"> TODO: indeed force timezone UTC?


`valid_until` indicatees how long this value can be cached. If it is not provided clients MUST treat the attribute as not cacheable.

`observed_at`: <span style="color:red"> TODO 



#### Avoid round trips
If a reference attribute is itself a PAC-ID which the `Attribute Server` has attributes for, a forward lookup SHOULD be included, i.e. append the attributes of this PAC-ID to the `responses` list. This avoids repeated requests.
NOTE: It is not the intention to request attributes from other `Attribute Servers`


#### Error Conditions
The attribute service MUST return `400 Bad Request` if the request is invalid, with a plain text description of the error.

If no attributes are found for a requested `PAC-ID` the server MUST return a response where the `responses` field does not include an entry for this `PAC-ID`. 
DESIGN REMARK: Why not send 404? Consider the case, when multiple pac-ids are included in the request, and for parts there are attributes, while for the others there are none: 404 would not be appropriate. 



### Caching of Attributes
Usability can be greatly improved if values are cached, making applications much faster. The general caching strategy is that the attribute service provides information about validity of attributes, but it is up to the client to implement an appropriate caching mechanism.

Attribute services provide SHOULD provide information about the validity duration (`valid_until`) of attributes. 
Clients SHOULD use this information to cache data (it is best practice but optional).


<span style="color:red"> TODO: if there is no way to request specific attribute group`, how would caching ever be useful, for clients which do not hide attribute groups? 



#### Best practices for `Attribute Servers`

`Attribute Servers` SHOULD aim to makes caching possible, by

- grouping attributes with similar validity in dedicated attribute groups (e.g.  valid forever and fast paced). 
  Reason: the request can only be sent for all attributes. If only one attribute cannot be cached, the request has to be sent each time. By grouping all “forever” attributes together the client knows that this request only needs to be sent once.
- provide `valid_until`, even when the value is small. Choose a value in the order of magnitude it takes for a value to realistically become obsolete. 
Reason: In many cases a new value needs to be propagated through multiple systems / organisational units. Setting ValidUntil to the same order of magnitude it takes to reach eventual consistency or maybe an order lower will reduce the number of meaningless requests. requests, while keeping the 

#### Best practices for `Attribute Clients`
Clients SHOULD use this information to cache data (it is best practice but optional).






### Multiple sources
There may be multiple services returning values for one particular PAC-ID. Services might be of different importance to a user and their (perceived) reliability might vary. Also there is a potential for conflicting attributes. 
It is the `Attribute Client`s responsibility to present this in a way, which is meaningful to their users. The `Attribute Service` is MUST not pre-filter. (BEST PRACTICE for library implementation on client side: The library should not filter either, as it typically lacks the context to judge the importance and reliability. ) 

## Presentation of attributes to the end user
It is RECOMMENDED the client presents attribute groups with a title “{AttributeGroupDisplayName} ( from {issuer})” e.g. “Physical Properties (from METTORIUS.COM ). 
It is RECOMMENDED the client presents the attribute groups in order of the CITs (assuming CITs are ordered by importance)

TODO: Q: How is this related to the name of the service as specified in teh CIT`?




### Internationalization
Attributes are about data transfer and not display. Attributes are therefore not localized. 

`Attribute Servers` SHOULD include include English translations for the 'key's of both `Attribute Group` and `Attributes`.
Translations to other languages CAN be included.
Languages MUST start with a ISO 639-1 language code, optionally followed by a ISO 3166-1 alpha-2 country code, separated by hyphen (e.g.  “de” or  “de-CH”) 

```json
"translations": [
        {
            "key": "MfgDate",
            "translations": {
                "en": "Manufactoring date",
                "en-US": "Manufactoring date",
                "fr": "Date de fabrication"
            }
        },
        {
            "key": "CalWeight",
            "translations": {
                "en": "Calibration weight",
                "fr": "Poids calibration"
            }
        },
        {
            "key": "MaxWeight",
            "translations": {
                "en": "Maximum weight",
                "fr": "Poids maximal"
            }
        }
    ]
```

Clients CAN display the attribute key, if no display name can be found.




## Documentation of `Attribute Server`
TODO: How would a consumer of a attribute service know how to authenticate and which attributes are provided? How to write a CIT when this is not known?



## Implementation Considerations for Libraries
<div style="color:red"> Note, that this application will usually have a functionality which goes beyond what is specified here. Conversely, a library implementing an `Attribute Client` would typically not implement the entire specification but focus on the generic parts and provide means for applications to inject databases etc.

On client side there are two levels of concern: 
1. attribute client library,  which knows about the details of attributes, typically implemented in the form of a library
2. an app, which makes use of attributes for interactions with the environment (e.g. user)

The app typically provides infrastructure such as databases etc. Thus long term caching (would need database) cannot solely be handled by the attribute client. Additionally, the app knows more about it’s context and might need to implement a custom caching strategy (there might be scenarios, where higher or lower update frequency is necessary).
Thus the attribute client (especially if a library) should:

- implement an in memory cache as default
- provide means for the app to inject a storage for caching (e.g. database or file)
- provide means for the app to inject a custom caching logic
</div>




## Terminology Used

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) "Key words for use in RFCs to Indicate Requirement Levels".

## FAQ

See [here](faq.md).

## License

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
