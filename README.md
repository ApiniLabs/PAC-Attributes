# PAC-ID Attributes

## In a Nutshell

`PAC-ID Attributes` standardizes a generic, vendor-neutral web service interface for retrieving metadata about an item identified with a PAC-ID.
With this mechanism, software-systems dealing with `PAC-ID`s can show metadata (e.g. boiling point of a substance) to the user, without implementing vendor specific protocols. Attributes might also be used programmatically (e.g. loading an instrument method based on a boiling point)

## Introduction

`PAC-ID`s expose only minimal human-readable information (issuer, category, item ID). However, user-facing applications require additional metadata—such as a display name or physical properties. Embedding such data in the `PAC-ID` is undesirable due to size, internationalization complexity and mutability issues.

To address this, `PAC-ID Attributes` defines a neutral, standardized web service interface for retrieving item metadata. This approach decouples data consumers from provider-specific implementations, enabling consistent, interoperable access regardless of the underlying issuer. While issuers may still offer proprietary APIs, the standardized web service provides a common, vendor-neutral mechanism usable across systems.

## Terminology

Term | Description
:--|:--
`Attribute Server` | A server which published attributes according to this specification
`Attribute Client` | Any application which requests attributes from an `Attribute Server`.

# Endpoint Discovery

Attribute Services are found via the `PAC-ID Resolver` configuration. Entries with `attributes-generic` in the 'service-type' field are attribute services.

## Specification


### Endpoint

There is only one endpoint for the `PAC-ID Attributes` web service.
It is RECOMMENDED to host the attribute server at the pac subdomain of the issuer’s domain, with the `/attributes endpoint` — for example: https://pac.mettorius.com/attributes.


### Request
HTTP **POST** request to the endpoint with the following JSON as payload.

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
`pac_ids` | A list of PAC-ID, serialized as urls. <br>Each `PAC-ID` MUST be valid and MAY contain extensions. <br> MUST NOT exceeding 100 items.
`restrict_to_attribute_groups` <br> (optional) | A list of `attribute group` keys. Instructs the server to only return these attribute groups. <br> If omitted, the server MUST return all available attribute groups. <br> If none of these attribute groups are found for a requested PAC-ID the server MUST return a response where the responses field does not include an entry for this PAC-ID.
`language_preferences` <br> (optional) | A list of languages with decreasing preference. <br> Entries MUST be ISO 639-1 language codes (e.g. "en" or "de"). The server MUST return the first language it can. If the server does not support any of languages in `language_preferences` it MUST return its default language.<br> If omitted the server MUST return its default language. (see [internationalization](#internationalization))
`suppress_forward_lookup` <br> (optional)| Instructs the server to not include attributes of `PAC-ID` which are attributes of type 'reference' of the requested `PAC-ID` (see [avoid round trips](#avoid-round-trips)). <br>If omitted the server MUST treat it as false and include attributes of references `PAC-ID`s.

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
                    ]
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
                                "numerical_value": "14.88",
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
                    ]
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
                    ]
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

Field | Description |
:-- |:-- |
`pac_id` |The `PAC-ID` for which attributes are returned. Extensions from the request MUST be preserved.
`attribute_groups` |Array of [`attribute group`](#attribute-group).

##### Attribute Groups

Attributes are grouped. See [best practices for grouping attributes](#best-practices-for-grouping-attributes)

| Field         |  required| Description|
| :-| :-| :-|
| `key`         | Yes | Unique URL identifying the attribute group. (see [on the choice of keys](#choice-of-keys))|
| `label`       | Yes | Human-readable label in the [language of the response](#top-level-fields).|
| `attributes`  | Yes | Array of attribute objects (see [Attributes](#attributes)).|


##### Attributes

| field | required| |
|:-|-|:-|
`key` | Yes | Unique URL identifying the attribute. (see [on the choice of keys](#choice-of-keys)) <br> MUST be unique within an `attribute group`. <br> It is RECOMMENDED to choose keys which are unique within the entire Attribute Service. 
`label` |Yes| Human-readable label in the [language of the response](#top-level-fields).|
| `type`| Yes | One of "bool", "datetime", "numeric", "text", "reference", "resource", "object" |
| `value` | Yes | Either a value matching the type-specific format (see below), or a homogeneous list of such value. 


##### Type-Specific `value`formats

| Type| Value Format|
| :-- | :-- |
| bool | `true` or `false` |
| datetime | ISO 8601 UTC date-time. MUST be in (`YYYY-MM-DDTHH:MM:SSZ`) format. MUST be in UTC.|
| numeric   | json object with fields:<br>- `numerical_value` MUST be a string in decimal or scientific notation (`"14.88"`, `"-51.89E-2"`).<br>- `unit` MUST be a valid UCUM unit [^1]. Use `"1"` for unitless values.<br> |
| text     | Any Unicode string. SHOULD NOT exceed 5000 characters.|
| reference | String referring to another entity. It is RECOMMENDED to use `PAC-ID`s serialized as url. |
| resource | A url to an asset, such as an image. It is RECOMMENDED to end with the file extension (e.g. "https://mettorius.com/images/BAL500.png")
| object    | Any json object. **Only use as a last resort** |


> [!NOTE]
> The numeric data type was chosen with scientific use cases in mind: We have chosen to representation of numbers as strings to allow for capturing the precision of the measurement (not the datatype). "10.000" means that there are 3 significant digits. <br> Numbers must always be accompanied by units or it must be explicitly stated when a number is unitless.



#### Authentication

`Attribute Servers` MAY require authentication via standard HTTP authentication mechanisms, such as those defined in RFC 7235, OAuth 2.0 (RFC 6749), or OpenID Connect.

#### Response Status

The Attribute Server MUST follow standard HTTP status codes, except that 404 (Not Found) is generally not used.

The `Attribute Server` MUST return `HTTP 400 Bad Request` if the request is invalid, with a plain text description of the error.

If no attributes are found for a requested `PAC-ID` the server MUST return a response where the `responses` field does not include an entry for this `PAC-ID`.
> [!NOTE]
> Why not send 404? Consider the case, when multiple pac-ids are included in the request, and for parts there are attributes, while for the others there are none: 404 would not be appropriate.

If invalid credentials were provided the server MUST return `HTTP 401 Unauthorized` with a WWW-Authenticate header according to RFC7235.

### Internationalization

Although `PAC-Attributes` are primarily about data transfer, it is a common use case to display attributes together with a label. Our approach balances simplicity with localization needs:

#### Numbers and Dates

- `Attribute Server` format: Always non-localized.
  - Dates: All datetimes MUST be in UTC. The timezone SHOULD be explicitly stated; if omitted, clients MUST assume UTC. Examples: 2025-07-21T15:30:00+00:00 or 2025-07-21T15:30:00Z.
  - Numbers: Always use a "." as the decimal separator.
- `Attribute Client` localize formatting (e.g., decimal separators, units) as needed.

#### Labels and Text Attributes

Labels and attributes of type `text` require translation. Since `Attribute Client`s cannot reliably infer appropriate translations, the `Attribute Server`s response MUST already contain translations.

- `Attribute Server` response language:
- MUST be consistent across the entire response.
  - Labels of `attribute groups` and `attributes` MUST be in this language.
  - Text attribute values MUST be in this language.

Language negotiation:

- The `Attribute Client` sends an ordered list of preferred languages.
- The `Attribute Server` MUST use the first supported language.
- If none are supported, respond in the default language.

### Forward Lookup

If a attribute of type `reference`is itself a `PAC-ID`, which the `Attribute Server` has attributes for, the attributes for this 'PAC-ID' SHOULD be included, i.e. append the attributes of this PAC-ID to the `responses` list. This avoids repeated requests.
> [!NOTE]
> It is not the intention to request attributes from other `Attribute Servers`



## Best Practices

### `Attribute Server`

#### Scope of `Attribute Server`

It is RECOMMENDED to scope attribute servers by category (or similar logical grouping) so that the attribute groups available from a given server are usually applicable to all `PAC-ID`s it handles.

#### Choice of Keys

Keys of `attribute groups` and `attributes` SHOULD be chosen with respect to the area of concern to which an attribute belongs (e.g. generic metadata, chemistry, safety, logistics).

Keys CAN also refer to your own domain (e.g. https://mettorius.com/terms/maximum-weight). Use this option as a last resort. It is RECOMMENDED the key is an active endpoint, where a definition and translations are displayed.

To ensure interoperability, implementers SHOULD prefer identifiers from well-known authoritative sources before defining their own. 
> [!NOTE]
>The use of such standardized keys enables clients to discover and process information in a predictable manner. For example a client that understands the https://schema.org/image key can reliably fetch and display product images. Or a lab instrument looking for melting point keys can find them, retrieve values, and even suggest a method for substance verification.

Here is a list of [recommended keys](well_known_keys.md) for common scenarios.





### Grouping of Attributes

Attributes SHOULD be grouped with these guidelines in mind:

- if an 'Attribute Client' shows `attribute groups` and their attributes the ordering should make sense to a user
- 'Attribute Client' should be able to selectively show only a subset of `attribute groups`
- Facilitate caching by grouping attributes with similar validity (e.g. valid forever and fast paced).

### Inclusion of Common Attributes
To support human-friendly presentation, the following attributes SHOULD be included in _exactly one_ attribute group:
| Key                        | Value                                                  | Purpose                     |
|:--- | :--- | :---  |
| `https://schema.org/name`  | A Unicode string; MUST be human-readable and concise. <br> SHOULD be in the 'language' of the response, unless set by user | Human-readable display name |
| `https://schema.org/image` | MUST be a URL which resolves to a valid image resource retrievable via HTTP <br> SHOULD have (~1:1 aspect ratio) and size o at least 256×256 px                | Representative image        |




### `Attribute Client`


### Presentation of Attributes to the End User

There may be multiple services returning attributes for one particular `PAC-ID`. Services might be of different importance to a user and their (perceived) reliability might vary. Also there is a potential for conflicting attributes.
It is RECOMMENDED the client presents attribute groups with a title “{AttributeGroupDisplayName} ( from {issuer})” e.g. “Physical Properties (from METTORIUS.COM ).
The order of attributes SHOULD be preserved.

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


