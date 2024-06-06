# Metadata

## HDX Metadata

All of the data in HDX HAPI comes from publicly-available datasets on HDX, and
the HDX metadata can be used refer back to the original data to see what
has been simplified or omitted in the API.
The two primary HDX metadata tables are
[`dataset`](metadata.md#dataset) and [`resource`](metadata.md#resource), and they
contain a small subset of the metadata available through the CKAN API or
HDX library.

The HAPI data records contain enough information to access the full records
from CKAN (see the parameters tables for more details).
All subcategory tables link back to a resource record, and all resources link
back to a dataset record.

### Dataset <a id="dataset"></a>

**Used in:** [`Resource`](metadata.md#resource), all sub-category tables

This table contains the HDX-specific metadata associated with all datasets
used to populate the HAPI sub-category tables. Every dataset has at least
one child [resource](metadata.md#resource).

{{ read_yaml('data_usage_guides/endpoint_parameters/dataset_parameters.yaml') }}

### Resource <a id="resource"></a>

**Used in:** All sub-category tables

This table contains the HDX-specific metadata associated with all resources
used to populate the HAPI sub-category tables. Every resource has one
parent [dataset](metadata.md#dataset).

{{ read_yaml('data_usage_guides/endpoint_parameters/resource_parameters.yaml') }}

## Geographical Metadata

HAPI supports three hierarchical levels of geographical metadata:
location (a country or country-like entity), admin 1, and admin 2.  An entry in
the location table does not necessarily imply UN recognition of statehood.
The subcategory data tables link to the lowest administrative level used by
that data type; it will usually be admin 2, but in some cases may be admin 1 or
location.

The names and p-codes are read in from a [global p-code list](https://data.humdata.org/dataset/global-pcodes)
taken from the common operational dataset (COD) gazetteers and administrative
boundaries.
In the geographical tables, the `code` (p-code) field is unique only in
combination with `reference_period_start`,
since p-codes may be reused in different versions of geographical metadata.

 When bringing in data from sub-categories, p-codes are used if
present. Sometimes, these p-codes may not strictly follow the standard with
variations such as shorter or longer country or admin unit codes.
HDX HAPI utilises p-code handling provided by the
[`hdx-python-country`](https://hdx-python-country.readthedocs.io/en/latest/)
library, which has a p-code length matching algorithm to
ensure correct admin units are determined.

This algorithm works as follows: First, a p-code is verified against the
expected p-code format. Then, a length-matching check is performed,
ensuring that for each segment (country code or admin unit code),
the length matches the predefined format for the country. For example,
a 3-letter country code could be converted to a 2-letter one or vice-versa.
Digits can be prefixed by 0's to increase the length, or have 0's dropped
from the prefix.

### Location <a id="location"></a>

Country or country-like entities in HDX HAPI, from the CODs
[global p-code list](https://data.humdata.org/dataset/global-pcodes).

{{ read_yaml('data_usage_guides/endpoint_parameters/location_parameters.yaml') }}

### Admin 1  <a id="admin1"></a>

Admin 1 level names and p-codes in HDX HAPI, from the CODs
[global p-code list](https://data.humdata.org/dataset/global-pcodes).

{{ read_yaml('data_usage_guides/endpoint_parameters/admin1_parameters.yaml') }}

### Admin 2 <a id="admin2"></a>

Admin 2 level names and p-codes in HDX HAPI, from the CODs
[global p-code list](https://data.humdata.org/dataset/global-pcodes).

{{ read_yaml('data_usage_guides/endpoint_parameters/admin2_parameters.yaml') }}

## Sub-category Metadata

### Org <a id="org"></a>

**Used in:**
[`Who is Doing What Where - Operational Presence`](coordination_and_context.md#operational-presence)

The organisation table is populated from the 3W data, using the following
methodology:

* Organisation name and acronym strings are normalised. If an acronym isn’t
  available, the first 32 characters of the name are used.
* This [organisation mapping](https://docs.google.com/spreadsheets/d/e/2PACX-1vSfBWvSu3fKA743VvHtgf-pIGkYH7zhy-NP7DZgEV9_a6YU7vtCeWhbLM56aUL1iIfrfv5UBvvjVt7B/pub?gid=1040329566&single=true&output=csv)
  is used for common alternative names
* Organisations must have an associated organisation type. If available, the
  organisation type code is taken directly from the 3W data, otherwise the name
  string is normalised and matched to the org type names. In the absence of a
  direct match, phonetic matching is used for strings > 5 characters. If no
  match is found, the organisation is skipped.

{{ read_yaml('data_usage_guides/endpoint_parameters/org_parameters.yaml') }}

### Org Type <a id="org-type"></a>

**Used in:**
[`Org`](metadata.md#org),
[`Who is Doing What Where - Operational Presence`](coordination_and_context.md#operational-presence)

The table is initially populated using the
[OCHA Digital Services organisation types list](https://data.humdata.org/dataset/organization-types-beta).
The following rows are then added:

| Code | Description            |
|------|------------------------|
| 501  | Civil Society          |
| 502  | Observer               |
| 503  | Development Programme  |
| 504  | Local NGO              |

Organisation types all have an associated description and code.

{{ read_yaml('data_usage_guides/endpoint_parameters/org_type_parameters.yaml') }}

### Sector <a id=sector></a>

**Used in:**
[`Who is Doing What Where - Operational Presence`](coordination_and_context.md#operational-presence),
[`Humanitarian Needs`](affected_people.md#humanitarian-needs)

This table is initially populated using the
[Global Coordination Groups](https://data.humdata.org/dataset/global-coordination-groups-beta?)
dataset. The following rows are then added:

| Code        | Name                                |
|-------------|-------------------------------------|
| Cash        | Cash programming                    |
| Hum         | Humanitarian assistance (unspecified)|
| Multi       | Multi-sector (unspecified)          |
| Intersectoral| Intersectoral                      |

Sectors all have an associated name and code.

{{ read_yaml('data_usage_guides/endpoint_parameters/sector_parameters.yaml') }}

### Currency <a id="currency"></a>

**Used in:**
[`Food Prices`](food_security_and_nutrition.md#food-price)

The currency table is populated using the WFP VAM Data Bridges API.

{{ read_yaml('data_usage_guides/endpoint_parameters/currency_parameters.yaml') }}

### WFP Market <a id="wfp-market"></a>

**Used in:**
[`Food Prices`](food_security_and_nutrition.md#food-price)

Markets are defined as the physical locations where buyers and sellers
come together to trade goods and services.
This table is populated from the food prices data, which contains location
names down to admin 2 as well as
a latitude and longitude, but is not p-coded. Consequently, admin 1 and 2
names must be matched to p-codes using the algorithm provided by the
[`hdx-python-country`](https://hdx-python-country.readthedocs.io/en/latest/)
library which uses phonetic name matching and
manual overrides.

{{ read_yaml('data_usage_guides/endpoint_parameters/wfp_market_parameters.yaml') }}

### WFP Commodity <a id="wfp-commodity"></a>

**Used in:**
[`Food Prices`](food_security_and_nutrition.md#food-price)

The commodity table tracks all food items, and their associated
commodity category, present in the food prices data.

{{ read_yaml('data_usage_guides/endpoint_parameters/wfp_commodity_parameters.yaml') }}
