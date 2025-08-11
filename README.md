# PAC-Attributes

## In a Nutshell
PAC-ID Attributes standardizes a generic, neutral interface for retrieving metadata about an item identified with a PAC-ID.
With this mechanism, applications dealing with `PAC-ID`s can show metadata (e.g. boiling point of a substance) to the user, without implementing vendor specific protocols. Attributes might also be used programmatically (e.g. loading an instrument method based on a boling point)


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
Attribute Services are found via the `PAC-ID Resolver`’s mapping table. Entries with `attributes-generic` in the 'service-type' column are attribute services.

It is RECOMMENDED to use the term 'attributes' in the url of the attribute server, e.g. `https://attributes.mettorius.com.` or `https://www.mettorius.com/attributes` . 



### Request
Attributes are retrieved from the `Attribute Server` by a HTTP **POST** request with this json body: 
```json
{
  "pac_ids": [
    "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/000001/EXAMPLE*59K77LWDX8W" 
  ],  
  "restrict_to_attribute_groups": [
    "https://labfreed.org/terms/attribute_group_metadata",
    "https://mettorius.com/terms/attribute_group_example"
  ],
  "language_preferences": ["en", "fr"], 
  "suppress_forward_lookup": false  
}

```
Field | Description 
:--- | :---
`pac_ids` | A list of PAC-ID, serialized as urls. <br>`PAC-ID`s MUST be valid and MAY contain extensions. <br> MUST NOT exceeding 100 items. 
`restrict_to_attribute_groups` <br> (optional) | A list of `attribute group` keys. Instructs the server to only return these attribute groups. <br> If omitted, the server MUST return all available attribute groups. 
`language_preferences` <br> (optional) | A list of languages with decreasing preference. <br> Entries MUST be ISO 639-1 language codes (e.g. "en" or "de"). The server MUST return the first language it can. <br>If omitted the server MUST return it's default language. (see [internationalization](#internationalization))
`suppress_forward_lookup` <br> (optional)| Instructs the server to not include attributes of `PAC-ID` which are referenced in attributes of the requested `PAC-ID` (see [avoid round trips](#avoid-round-trips)). <br>If omitted the server MUST treat it as false and include attributes of references `PAC-ID`s.



### Response

#### Response Structure
The `Attribute Server` MUST send a response of this form:
<!-- BEGIN RESPONSE JSON -->
```json
{
    "schema_version": "1.0",
    "language": "en",
    "pac_attributes": [
        {
            "pac_id": "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/000001*59K77LWDX8W",
            "attribute_groups": [
                {
                    "key": "https://labfreed.org/terms/attribute_group_metadata",
                    "label": "MetaData",
                    "attributes": [
                        {
                            "key": "https://schema.org/name",
                            "value": "My Balance",
                            "label": "Display Name",
                            "type": "text"
                        },
                        {
                            "key": "https://schema.org/image",
                            "value": "https://picsum.photos/id/82/200",
                            "label": "Image",
                            "type": "text"
                        }
                    ],
                    "state_of": "2025-08-11T07:00:41.063055Z"
                },
                {
                    "key": "https://mettorius.com/terms/attribute_group_example",
                    "label": "attribute_group_example",
                    "attributes": [
                        {
                            "key": "https://labfreed.org/terms/example/TextAttribute",
                            "value": "Bar",
                            "label": "Text Attribute",
                            "type": "text"
                        },
                        {
                            "key": "https://labfreed.org/terms/example/NumericAttribute",
                            "value": {
                                "magnitude": "14.88",
                                "unit": "mol/L"
                            },
                            "label": "Numeric Attribute",
                            "type": "numeric"
                        },
                        {
                            "key": "https://labfreed.org/terms/example/ReferenceAttribute",
                            "value": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002",
                            "label": "Reference Attribute",
                            "type": "reference"
                        },
                        {
                            "key": "https://labfreed.org/terms/example/DateTimeAttribute",
                            "value": "2025-08-11T07:00:41.523080Z",
                            "label": "Date Attribute",
                            "type": "datetime"
                        },
                        {
                            "key": "https://labfreed.org/terms/example/BoolAttribute",
                            "value": false,
                            "label": "Boolean Attribute",
                            "type": "bool"
                        },
                        {
                            "key": "https://labfreed.org/terms/example/ObjectAttribute",
                            "value": {
                                "k1": 1,
                                "k2": {
                                    "a": "bar",
                                    "b": "foo"
                                },
                                "k3": [
                                    0,
                                    1,
                                    2
                                ]
                            },
                            "label": "Object Attribute (LAST RESORT)",
                            "type": "object"
                        }
                    ],
                    "state_of": "2025-08-11T07:00:41.526506Z"
                }
            ]
        },
        {
            "pac_id": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002",
            "attribute_groups": [
                {
                    "key": "https://labfreed.org/terms/attribute_group_metadata",
                    "label": "MetaData",
                    "attributes": [
                        {
                            "key": "https://schema.org/name",
                            "value": "Calibration Weight PRN003",
                            "label": "Display Name",
                            "type": "text"
                        },
                        {
                            "key": "https://schema.org/image",
                            "value": "https://picsum.photos/id/86/200",
                            "label": "Image",
                            "type": "text"
                        }
                    ],
                    "state_of": "2025-08-11T07:00:41.063055Z"
                }
            ]
        }
    ]
}
```
<!-- END RESPONSE JSON -->


#### Field Descriptions

##### Top-Level Fields

| Field            | Description |
|:---|:---|
| `schema_version` |  Version of the response schema.|
| `language`       | The language of the response. See [internaltionalization](#internationalization) |
| `pac_attributes` | Array of [`pac_attributes`](pac_attributes).|


##### `pac_attributes` 
Each item represents attributes for a single `PAC-ID`.

Field |	Description |
:-- |:-- |
`pac_id` |The `PAC-ID` for which attributes are returned. Extensions from the request MUST be preserved.
`attribute_groups` |Array of [`attribute group`](#attribute-group)..


##### Attribute Groups
Attributes are grouped. See [best practices for grouping attributes](#best-practices-for-grouping-attributes)

| Field         |  required| Description|
| :-| :-| :-|
| `key`         | Yes | Unique URL identifying the attribute group. (see [on the choice of keys](#choice-of-keys))|
| `label`       | Yes | Human-readable label in the [language of the response](#top-level-fields).|
| `attributes`  | Yes | Array of attribute objects (see [Attributes](#attributes)).|
| `state_of`    | Optional | ISO 8601 UTC timestamp when the attribute values were gathered by the server. [a guide to dates in the response](#a-guide-to-timestamps-in-the-response) |
| `valid_until` | Optional | ISO 8601 UTC timestamp until which the data may be cached. If absent, treat as **not cacheable**. |


##### Attributes
| field | required| |
|:-|-|:-|
`key` | Yes | Unique URL identifying the attribute. (see [on the choice of keys](#choice-of-keys)) <br> MUST be unique within an `attribute group`. <br> It is RECOMMENDED to choose keys which are unique within the entire Attribute Service. )
`label` |Yes| Human-readable label in the [language of the response](#top-level-fields).| 
| `type`| Yes | One of the "bool", "datetime", "numeric", "text", "reference", "object" |
`value` | Yes | Value matching the type-specific format (see below).
`observed_at` | Optional | ISO 8601 UTC timestamp when the value was observed. e.g. test date, analysis date

##### Type-Specific `value`formats
| Type| Value Format|
| :-- | :-- |
| bool | `true` or `false` |
| datetime | ISO 8601 UTC date-time. MUST be in (`YYYY-MM-DDTHH:MM:SSZ`) format. MUST be in UTC.|
| numeric   | json object with fields:<br>- `magnitude` MUST be a string in decimal or scientific notation (`"14.88"`, `"-51.89E-2"`).<br>- `unit` MUST be a valid UCUM unit [^1]. Use `"1"` for unitless values. |
| text     | Any Unicode string. SHOULD NOT span multiple lines.|
| reference | String referring to another entity. It is RECOMMENDED to use `PAC-ID`s serialized as url. |
| object    | Any json object. **Only use as a last resort** |

> **<span style="color:blue"> ℹ️️ </span>**: The numeric data type was chosen with scientific use cases in mind: We have chosen to representation of numbers as strings to allow for capturing the precision of the measurement (not the datatype). "10.000" means that there are 3 significant digits. <br> Numbers must always be accompanied by units or it must be explicitly stated when a number is unitless.


#### A guide to timestamps in the response


<div style="color:red">
TODO: Welche Timestamps soll es geben?

| Timestamp | Description | Comment |
|:--|:--|:--|
| `state_of`    | The attribute server will often not be the leading system for attribute data, but take a copy. State of indicates the time this data was copied from the leading system to the attribute server. |
| `valid_until` | ISO 8601 UTC timestamp until which the data may be cached. If absent, treat as **not cacheable**. |
`observed_at` | e.g. test date, analysis date
</div>


#### Error Conditions
The attribute service MUST return `HTTP 400 Bad Request` if the request is invalid, with a plain text description of the error.

If no attributes are found for a requested `PAC-ID` the server MUST return a response where the `responses` field does not include an entry for this `PAC-ID`. 
DESIGN REMARK: Why not send 404? Consider the case, when multiple pac-ids are included in the request, and for parts there are attributes, while for the others there are none: 404 would not be appropriate. 

If invalid credentials were provided the server MUST return `HTTP 401 Unauthorized` with a WWW-Authenticate header according to RFC7235.



### Internationalization
Although `PAC-Attributes` are primarily about data transfer, it is a common use case to display attributes together with a label. Our approach balances simplicity with localization needs:

#### Numbers and Dates
- `Attribute Server` format: Always non-localized.
  - Dates: All datetimes MUST be in UTC. The timezone SHOULD be explicitly stated; if omitted, clients MUST assume UTC. Examples: 2025-07-21T15:30:00+00:00 or 2025-07-21T15:30:00Z.
  - Numbers: Always use a . as the decimal separator.
- `Attribute Client` localize formatting (e.g., decimal separators, units) as needed.

#### Labels and Text Attributes
Labels and attributes of type `text` require translation. Since `Attribute Client`s cannot reliably infer appropriate translations, the `Attribute Server`s response MUST already contain translations. 

- `Attribute Server` response language:
-   MUST be consistent across the entire response.
    - Labels of `attribute groups` and `attributes` MUST be in this language.
    - Text attribute values MUST be in this language.

Language negotiation:
- The `Attribute Client` sends an ordered list of preferred languages.
- The `Attribute Server` MUST use the first supported language.
- If none are supported, respond in the default language.


### Avoid round trips
If a attribute of type `reference`is itself a `PAC-ID`, which the `Attribute Server` has attributes for, a forward lookup SHOULD be included, i.e. append the attributes of this PAC-ID to the `responses` list. This avoids repeated requests.
> **<span style="color:blue"> ℹ️️ </span>**: It is not the intention to request attributes from other `Attribute Servers`


### Server Capabilities

<div style="color:red">Discuss:
How would a consumer of a attribute service know how to authenticate and which attributes are provided? How to write a CIT when this is not known?
To facilitate configuration of `PAC-ID Resolver``Attribute Servers` SHOULD publish their capabilities.
```$server_end_point/capabilities``` or use the GET or OPTIONS method on the same endpoint

```json
{
  "supported_languages": [
    "en",
    "fr",
    "de",
    "es"
  ],
  "default_language": "en",

  "available_attribute_groups": [
       "https://schema.org/additionalProperty",
        "mettorius.com/keys/Example",
        "mettorius.com/keys/AnotherGroup"
  ],

    "guarantees": {
        "using_ucum_units" 
        "quality" 
    }

  "auth": {
    "auth_type": "bearer",
    "token_endpoint": "https://auth.example.com/oauth2/token",
    "docs": "https://docs.example.com/auth"
    }
}
```
Field | Description 
:--- | :---
`supported_languages` | The languages the attribute server supports. If a language is listed her, the server MUST be capable of providing a response in this language for _all_ attributes.
`default_language` | The language the server will respond in, when a language is requested which is not supported.
`available_attribute_groups` | Lists which attribute groups the server knows, and therefore the valid elements of the requests `restrict_to_attribute_groups` field
`guarantees` | Information about standards being followed. Allows clients to decide whether it's save to use the information for specific purposes (e.g. like make programmatic use of the attributes). <br>- guaranteeing that numbers are in ucum format and can therefore be used programmatically. <br> -whether the information is carefully curated or scraped from somewhere: INFORMATIVE, RELIABLE

where to get credentials from
</div>


### Caching of Attributes
Usability can be greatly improved if values are cached, making applications much faster. 
Attribute services provide SHOULD provide information about the validity duration (`valid_until`) of attributes. 
Clients SHOULD use this information to cache data (it is best practice but optional).


## Best Practices

### Choice of Keys
Keys of `attribute groups` and `attributes` SHOULD  refer to a definition in an well-known source or to your own domain:

Source | Example Key | Comment
:--|:--|:--
schema.org | https://schema.org/location |
[GS1 Application identifier](https://ref.gs1.org/ai) | https://ref.gs1.org/ai/17 |
[IUPAC gold book](https://goldbook.iupac.org/terms) | https://doi.org/10.1351/goldbook.A00028 |
labfreed.org | https://labfreed.com/terms/boiling-point
your domain | https://mettorius.com/terms/melting-point | CAN be an active endpoint. If so it is suggested to display a definition and translations.

Here is a list of [recommended keys](well_known_keys.md) for common scenarios. 


### Grouping of Attributes
Attributes SHOULD be grouped with these guidelines in mind:
- if an 'Attribute Client' shows `attribute groups` and their attributes the ordering should make sense to a user
- 'Attribute Client' should be able to selectively show only a subset of `attribute groups`
- Facilitate caching by grouping attributes with similar validity (e.g. valid forever and fast paced). 



### Presentation of Attributes to the End User
There may be multiple services returning attributes for one particular `PAC-ID`. Services might be of different importance to a user and their (perceived) reliability might vary. Also there is a potential for conflicting attributes.
It is RECOMMENDED the client presents attribute groups with a title “{AttributeGroupDisplayName} ( from {issuer})” e.g. “Physical Properties (from METTORIUS.COM ). 






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




[^1]: [The Unified Code for Units of Measure](https://ucum.org/): 
In a nutshell:
To find units it is recommended to use the [unit validator](https://lhncbc.github.io/ucum-lhc/demo.html) or refer to [common examples](https://github.com/ucum-org/ucum/blob/main/common-units/TableOfExampleUcumCodesForElectronicMessagingwithPreface.pdf) 
Units can be combined by multiplication: Examples of units: "kg", "m", "s", "kg.m.s-2" or "kg.m/s2"
