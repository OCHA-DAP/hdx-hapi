# Metadata

## Dataset <a id="dataset"></a>

## Resource <a id="resource"></a>

## Location <a id="location"></a>

## Admin1  <a id="admin1"></a>

## Admin2 <a id="admin2"></a>

## Org <a id="org></a>

* The organisation table is populated from the 3W data
* Organisation name and acronym strings are normalised. If an acronym isn’t
  available, the first 32 characters of the name are used.
* This [organisation mapping](https://docs.google.com/spreadsheets/d/e/2PACX-1vSfBWvSu3fKA743VvHtgf-pIGkYH7zhy-NP7DZgEV9_a6YU7vtCeWhbLM56aUL1iIfrfv5UBvvjVt7B/pub?gid=1040329566&single=true&output=csv)
  is used for common alternative names
* Organisations without a sector are excluded
* Organisations can have an associated organisation type. If available, the
  organisation type code is taken directly from the 3W data, otherwise the name
  string is normalised and matched to the org type names. In the absence of a
  direct match, phonetic matching is used for strings > 5 characters. If no
  match is found, the organisation is skipped.

## Org Type <a id="org-type"></a>

* The table is populated using
  [OCHA Digital Services organization types list](https://data.humdata.org/dataset/organization-types-beta),
  with the addition of:
  * Civil Society
  * Observer
  * Development Programme
  * Local NGO
* Organisation types all have an associated name and code

## Sector  <a id=sector></a>

* This table is populated using the Global Coordination Groups, with the
  following additional entries:
  * cash
  * humanitarian assistance
  * multi-sector
  * intersectoral
* The sector name strings in the 3W data are normalised and then aligned to the
  sector table, using the “sector_map” section of
  [this configuration file](https://github.com/OCHA-DAP/hapi-pipelines/blob/main/src/hapi/pipelines/configs/core.yaml)
  if needed.
  In the absence of a direct match, phonetic matching is used for
  strings > 5 characters.

## Currency <a id="currency"></a>

## WFP Market <a id="wfp-market"></a>

The Markets data comes from the WFP Food Prices datasets. We p-code it by …

## WFP Commodity <a id="wfp-commodity"></a>
