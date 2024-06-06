# Coordination & Context

## Who is Doing What Where - Operational Presence <a id=”operational-presence”></a>

The [Who is Doing What Where (3W)](https://3w.unocha.org/) is a core
humanitarian coordination dataset that contains the geographic and sectoral
spread of humanitarian activities and partners. It is critical to know where
humanitarian organisations are working and what they are doing in order to
ensure collaboration and efficient resource allocation, avoid duplication of
efforts, identify gaps, and plan for future humanitarian response.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/operational_presence_details.yaml') }}

### Parameters

{{ read_yaml('data_usage_guides/endpoint_parameters/operational_presence_parameters.yaml') }}

### Transformations applied

* For consistency and interoperability, we aggregate to an
  [operational presence](https://humanitarian.atlassian.net/wiki/spaces/imtoolbox/pages/214499412/Who+does+What+Where+3W)
  level (3W:OP, per org, sector, and admin 2), even if the original 3W data is
  more detailed (e.g. the source lists individual activities)
* Countries that are not p-coded are aggregated to the national level
* Organisation deduplication is a long-running challenge with this data, since
  there are no unique identifiers, and organisation names may be spelled
  different ways by different OCHA offices, or sometimes even within the same
  3W. See the [`org`](org) section below for more information on how we handle
  these details.
* The sector name strings in the 3W data are normalised and then aligned to the
  [sector](metadata.md#sector) table, using the “sector_map” section of
  [this configuration file](https://github.com/OCHA-DAP/hapi-pipelines/blob/main/src/hapi/pipelines/configs/core.yaml)
  if needed. In the absence of a direct match, phonetic matching is used for
  strings > 5 characters.
* Rows without an associated sector are skipped
* The reference period is derived manually per resource based on the
  resource metadata

### Usage notes

* Available at either Admin 0, 1, or 2 depending on the country. Please check
  data coverage for further information
* We cannot guarantee org consistency over time; for example, if an IMO
  changes, the 3W might change the spelling or the whole name of an org between
  releases

## Funding <a id=”funding”></a>

[OCHA Financial Tracking Service](https://fts.unocha.org/home/2024/donors/view)
(FTS) publishes data on
humanitarian funding flows as reported by donors and
recipient organisations. It presents all humanitarian funding to a country
as well as funding that is reported or that can be specifically
mapped against funding requirements stated in Humanitarian Response Plans.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/funding_details.yaml') }}

### Parameters

{{ read_yaml('data_usage_guides/endpoint_parameters/funding_parameters.yaml') }}

### Transformations applied

* The present version of the API currently captures only funding associated
  with an appeal. Funding data without associated appeals will be added in a
  future version.
* The reference period is taken from the start and end date provided in each
  row from the original data

## Conflict Events <a id="conflict-event"></a>

[ACLED](https://acleddata.com/) collects real-time data on the locations,
dates, actors, fatalities, and types of all reported political violence and
protest events around the world. HDX HAPI leverages ACLED’s publicly accessible
data, aggregated on a monthly basis and to administrative regions.
To learn more about their methodology, please consult the
[ACLED Codebook](https://acleddata.com/knowledge-base/codebook/).

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/conflict_event_details.yaml') }}

### Parameters

{{ read_yaml('data_usage_guides/endpoint_parameters/conflict_event_parameters.yaml') }}

### Transformations applied

* The data for political violence events, civilian targeting events, and
  demonstrations are in separate resource on HDX, but are combined into a
  single endpoint in the API
* Any duplicate rows in the original data are removed
* The reference period is constructed using the full range of the month
  presented in the “Month” and “Year” columns of the original data

### Usage notes

* The three event categories are not mutually exclusive, see
  [`Event Type`](enums.md#event-type) for more details
* Data is either national or disaggregated to admin 2, see individual resources
  for more details

## National Risk <a id="national-risk"></a>

The [INFORM Risk Index](https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk)
is a global, open-source risk assessment for humanitarian crises and disasters.
It can support decisions about prevention, preparedness and response. For more
information on the methodology, see
[here](https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/Methodology).

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/national_risk_details.yaml') }}

### Parameters

{{ read_yaml('data_usage_guides/endpoint_parameters/national_risk_parameters.yaml') }}

### Transformations applied

* The reference period is obtained from the HDX dataset
