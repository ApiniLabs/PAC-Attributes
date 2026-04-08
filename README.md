# PAC-ID Attributes

## In a Nutshell

`PAC-ID Attributes` standardizes a generic, vendor-neutral web service interface for retrieving metadata about an item identified with a PAC-ID.
With this mechanism, software-systems dealing with `PAC-ID`s can show metadata (e.g. boiling point of a substance) to the user, without implementing vendor specific protocols. Attributes might also be used programmatically (e.g. loading an instrument method based on a boiling point), , which is why JSON-LD compatibility is built in — it ensures that attributes carry machine-interpretable semantics that different systems can reliably consume and reason over.

## Introduction

`PAC-ID`s expose only minimal human-readable information (issuer, category, item ID). However, user-facing applications require additional metadata—such as a display name or physical properties. Embedding such data in the `PAC-ID` is undesirable due to size, internationalization complexity and mutability issues.

To address this, `PAC-ID Attributes` defines a neutral, standardized web service interface for retrieving item metadata. This approach decouples data consumers from provider-specific implementations, enabling consistent, interoperable access regardless of the underlying issuer. While issuers may still offer proprietary APIs, the standardized web service provides a common, vendor-neutral mechanism usable across systems.

## Terminology

Term | Description
:--|:--
`Attribute Server` | A server which published attributes according to this specification
`Attribute Client` | Any application which requests attributes from an `Attribute Server`

## Endpoint Discovery

Attribute Services are found via the `PAC-ID Resolver` configuration. Entries with `attributes-generic` in the 'service-type' field are attribute services.

## Specification


### Endpoint

There is only one endpoint for the `PAC-ID Attributes` web service.
It is RECOMMENDED to host the attribute server at the pac subdomain of the issuer’s domain, with the `/attributes` endpoint — for example: 'https://pac.mettorius.com/attributes'.


### Request

MUST be a HTTP **GET** request to the endpoint with the ID of the item added as url segment. The ID MUST be url-encoded. The ID must be an [IRI](https://datatracker.ietf.org/doc/html/rfc3987), preferably a `PAC-ID`.

Example:
```
GET https://pac.mettorius.com/attributes/HTTPS%3A%2F%2FPAC.METTORIUS.COM%2F-MD%2FBAL500%2F000001
```

#### Parameters
The endpoint SHOULD support the following query parameters: 

Parameter | Value
:--- | :---
`attr_grps` (optional) | An comma separated list of attribute group keys. MUST be url-encoded. The client MAY repeat this parameter to specify multiple attribute groups:<br>`?attr_grps={key1},{key2}`<br>If omitted, the server MUST return all available attribute groups. If none of the specified attribute groups are found for the requested PAC-ID, the server MUST return a response where the `responses` field does not include an entry for this PAC-ID.
`attr_fwd_lkp` (optional) | Boolean flag ('true' or 'false'). Instructs the server to not include attributes of PAC-IDs which are attributes of type `reference` of the requested PAC-ID (see [avoid round trips](#avoid-round-trips)). If omitted, the server MUST treat it as 'true' and include attributes of referenced PAC-IDs.

#### Language Preferences

The client MAY express its language preferences using the standard HTTP `Accept-Language`e header (see RFC 9110, §12.5.4), for example:
`Accept-Language: en-US;q=1.0, en;q=0.9, fr;q=0.6`

Each language tag MUST use an ISO 639-1 language code as its primary subtag (e.g. "en", "de").

The server MUST perform language negotiation in accordance with RFC 9110. If none of the requested languages are supported, or if the `Accept-Language` header is omitted, the server MUST fall back to its default language (see [internationalization](#internationalization)).




### Response

#### Response Structure

The `Attribute Server` MUST send a response with a JSON payload, adhering to this [schema](attribute_response_payload.schema.json).
Here is an example of such a response:
<!-- BEGIN RESPONSE JSON -->
```json
{
  "schema_version": "1.0",
  "language": "en",
  "data": [
    {
      "id": "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/000001*59K77LWDX8W",
      "attribute_groups": [
        {
          "group_label": "Example Attribute Group",
          "group_key": "https://mettorius.com/terms/attribute_group_example",
          "attributes": {
            "https://labfreed.org/terms/example/TextAttribute": {
              "label": "Text Attribute",
              "items": [
                { "value": "Bar", "type": "text" }
              ]
            },
            "https://labfreed.org/terms/example/NumericAttribute": {
              "label": "Numeric Attribute",
              "items": [
                { "value": "14.88 mol/L", "type": "numeric" }
              ]
            },
            "https://labfreed.org/terms/example/ReferenceAttribute": {
              "label": "Reference Attribute",
              "items": [
                { "value": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002", "type": "reference" }
              ]
            },
            "https://labfreed.org/terms/example/DateTimeAttribute": {
              "label": "Date Attribute",
              "items": [
                { "value": "2025-08-11T07:00:41.523080Z", "type": "datetime" }
              ]
            },
            "https://labfreed.org/terms/example/BoolAttribute": {
              "label": "Boolean Attribute",
              "items": [
                { "value": false, "type": "bool" }
              ]
            },
            "https://labfreed.org/terms/example/ObjectAttribute": {
              "label": "Object Attribute (LAST RESORT)",
              "items": [
                {
                  "value": {
                    "k1": 1,
                    "k2": {
                      "a": "bar",
                      "b": "foo"
                    },
                    "k3": [0, 1, 2]
                  },
                  "type": "object"
                }
              ]
            }
          }
        },
        {
          "group_label": "Example Attribute Group with List",
          "group_key": "https://mettorius.com/terms/attribute_group_example_list",
          "attributes": {
            "https://labfreed.org/terms/example/MultiTextAttribute": {
              "label": "Multi Text Attribute",
              "items": [
                { "value": "list element 1", "type": "text" },
                { "value": "list element 2", "type": "text" },
                { "value": "list element 3", "type": "text" }
              ]
            }
          }
        }
      ]
    },
    {
      "id": "HTTPS://PAC.METTORIUS.COM/-MD/CALWEIGH/A00002",
      "attribute_groups": [
        {
          "group_label": "MetaData",
          "group_key": "https://labfreed.org/terms/attribute_group_metadata",
          "attributes": {
            "https://schema.org/name": {
              "label": "Display Name",
              "items": [
                { "value": "Calibration Weight PRN003", "type": "text" }
              ]
            },
            "https://schema.org/image": {
              "label": "Image",
              "items": [
                { "value": "https://picsum.photos/id/86/200", "type": "text" }
              ]
            }
          }
        }
      ]
    }
  ],
  "@context":  "https://vocab.labfreed.org/attributes/v1.jsonld"
}

```
<!-- END RESPONSE JSON -->
Learn why  `@context`  is there:  [^json-ld_support]

#### Field Descriptions

##### Top-Level Fields

| Field            | Description |
|:---|:---|
| `schema_version` |  Version of the response schema.|
| `language`       | The language of the response. See [internationalization](#internationalization) |
| `data` | Array of [`pac_attributes`](pac_attributes).|

##### `data`

Each item represents attributes for a single `PAC-ID`.

Field | Description |
:-- |:-- |
`id` |The ID of the item for which attributes are returned. Extensions from the request MUST be preserved.
`attribute_groups` |Array of [`attribute group`](#attribute-group).

##### Attribute Groups

For better usability attributes are organized into `attibute_groups`. See [best practices for grouping attributes](#best-practices-for-grouping-attributes)

| Field         |  required| Description|
| :-| :-| :-|
| `group_key`         | Yes | Unique URL identifying the attribute group. (see [on the choice of keys](#choice-of-keys))|
| `group_label`       | Yes | Human-readable label in the [language of the response](#top-level-fields).|
| `attributes`        | Yes | Object whose keys are attribute identifiers and whose values are Attribute objects (see [Attributes](#attributes)). Each key MUST be a unique URL identifying the attribute (see on the choice of keys). Keys MUST be unique within an attribute group, and it is RECOMMENDED that they remain unique across the entire Attribute Service.


##### Attributes

| field | required| |
|:-|-|:-|
`label` |Yes| Human-readable label in the [language of the response](#top-level-fields).|
`items` | Yes | Array of [AttributeValue objects](#attributevalue) `{"value": "...", "type": "..."}` The values are considered **un**ordered. <br> <small> Rationale for the design choice: [^always_list] </small>|


##### AttributeValue
| field | required| |
|:-|-|:-|
| `type`| Yes | One of "bool", "datetime", "numeric", "text", "reference", "resource", "object"
| `value` | Yes | A value matching the type-specific format (see below) 


##### Type-Specific `value`formats

| Type| Value Format|
| :-- | :-- |
| bool | `true` or `false` |
| datetime | ISO 8601 UTC date-time. MUST be in (`YYYY-MM-DDTHH:MM:SSZ`) format. MUST be in UTC.|
| numeric   | String composed of the following concatenated elements, separated by a blankspace:<br>- numerical_value MUST be a string in decimal or scientific notation (`"14.88"`, `"-51.89E-2"`).<br>- unit MUST be a valid UCUM unit [^ucum]. Use `"1"` for unitless values.<br> Example: `51.89E-2 mol.L-1` <br> <small> Rationale for the design choices: [^num_as_str] </small>|
| text     | Any Unicode string. SHOULD NOT exceed 5000 characters.|
| reference | String referring to another entity. It is RECOMMENDED to use `PAC-ID`s serialized as url. |
| resource | A url to an asset, such as an image. It is RECOMMENDED to end with the file extension (e.g. "https://mettorius.com/BAL500.png")
| object    | Any json object. **Only use as a last resort** |


#### Authentication

`Attribute Servers` MAY require authentication via standard HTTP authentication mechanisms, such as those defined in RFC 7235, OAuth 2.0 (RFC 6749), or OpenID Connect.

#### Response Status

The Attribute Server MUST follow standard HTTP status codes, specifically:

- The `Attribute Server` MUST return `HTTP 400 Bad Request` if the request is invalid, with a plain text description of the error.

- If no attributes are found for a requested `PAC-ID` the server MUST return `HTTP 404 Not Found`.

- If invalid credentials were provided the server MUST return `HTTP 401 Unauthorized` with a WWW-Authenticate header according to RFC7235.

### Internationalization

Although `PAC-Attributes` are primarily about data transfer, it is a common use case to display attributes together with a label. Our approach balances simplicity with localization needs:

#### Numbers and Dates

- `Attribute Server` format: Always non-localized.
  - Dates: All datetimes MUST be in UTC. The timezone SHOULD be explicitly stated; if omitted, clients MUST assume UTC. Examples: 2025-07-21T15:30:00+00:00 or 2025-07-21T15:30:00Z.
  - Numbers: Always use a "." as the decimal separator. [^num_as_str]
- `Attribute Client`s localize formatting (e.g., decimal separators, units) as needed.

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
Keys CAN also refer to your own domain (e.g. https://mettorius.com/terms/maximum-weight).
It is RECOMMENDED the key is an active endpoint, where a definition and translations are displayed.

To ensure interoperability, implementers SHOULD prefer identifiers from well-known authoritative sources before defining their own.
> [!NOTE]
>The use of such standardized keys enables clients to discover and process information in a predictable manner. For example a client that understands the https://schema.org/image key can reliably fetch and display product images. Or a lab instrument looking for melting point keys can find them, retrieve values, and even suggest a method for substance verification.

Here is a list of [recommended keys](well_known_keys.md) for common scenarios.





### Grouping of Attributes

Attributes SHOULD be grouped with these guidelines in mind:

- 'Attribute Client' should be able to selectively show only a subset of `attribute groups`
- Facilitate caching by grouping attributes with similar validity (e.g. valid forever and fast paced).


### Inclusion of Common Attributes

To support human-friendly presentation, the following attributes SHOULD be included in _exactly one_ attribute group:
| Key                        | Type |Value                                                  | Purpose                     |
|:--- | :--- | :---  | :---
| `https://schema.org/name`  | text | A Unicode string; MUST be human-readable and concise. <br> SHOULD be in the 'language' of the response, unless set by user | Human-readable display name |
| `https://schema.org/image` | resource | MUST be a URL which resolves to a valid image resource retrievable via HTTP <br> SHOULD have (~1:1 aspect ratio) and size o at least 256×256 px                | Representative image        |

Here is an example of a response, which includes these attributes:
```json
{
  "schema_version": "1.0",
  "language": "en",
  "data": [
    {
      "id": "HTTPS://PAC.METTORIUS.COM/-MD/BAL500/000001",
      "attribute_groups": [
        {
          "group_label": "MetaData",
          "group_key": "https://labfreed.org/terms/attribute_group_metadata",
          "attributes": {
            "https://schema.org/name": {
              "label": "Display Name",
              "items": [
                { "value": "My Balance", "type": "text" }
              ]
            },
            "https://labfreed.org/terms/example/ResourceAttribute": {
              "label": "Image",
              "items": [
                { "value": "https://mettorius.com/BAL500.png", "type": "resource" }
              ]
            }
          }
        }
      ]
    }
  ]
}
```



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

[^ucum]: [The Unified Code for Units of Measure](https://ucum.org/):
In a nutshell:
To find units it is recommended to use the [unit validator](https://lhncbc.github.io/ucum-lhc/demo.html) or refer to [common examples](https://github.com/ucum-org/ucum/blob/main/common-units/TableOfExampleUcumCodesForElectronicMessagingwithPreface.pdf)
Units can be combined by multiplication: Examples of units: "kg", "m", "s", "kg.m.s-2" or "kg.m/s2"

[^num_as_str]: The numeric data type was chosen with scientific use cases in mind: We have chosen to representation of numbers as strings to allow for capturing the precision of the measurement (not the datatype). "10.000" means that there are 3 significant digits. <br> Numbers must always be accompanied by units or it must be explicitly stated when a number is unitless. Statement of unitlessness is done by adding unit "1"

[^json-ld_support]: The `@context` block tells tools that this JSON isn’t just arbitrary data — it follows [JSON-LD](https://json-ld.org/), a W3C standard that adds semantic meaning to JSON. For people unfamiliar with RDF or JSON-LD: this allows your data to be understood in a predictable way by other systems, enabling interoperability, graph querying, and long-term stability of meaning. In practice, this makes your attributes “self-describing” and compatible with knowledge-graph tooling. The context itself is hosted and maintained by the Labfreed community; regular users don’t need to interact with it directly, and the system automatically applies it. For those who are curious, the context can be seen [here] (json-LD-context.json)


[^always_list]: We have chosen to represent both single and multiple values in `items`.  Using an array even for single values avoids special-case handling and keeps the structure uniform — consumers can always treat attributes as lists, whether they contain one item or many.
The `{"value": "...", "type": "..."}` pattern for elements of `items`was chosen for compatibility with JSON-LD. It requires explicit value objects: each value carries its own type so it can be correctly transformed into RDF.


