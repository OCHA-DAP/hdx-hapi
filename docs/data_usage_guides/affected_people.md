# Affected People

---

## Internally-Displaced Persons <a id=”idps”></a>

The data for this sub-category is taken from the
[International Organization for Migration](https://www.iom.int/) (IOM)'s
[displacement tracking matrix](https://dtm.iom.int/) (DTM),
which collects and analyzes data on population movements,
displacements, and mobility patterns to provide timely information
for humanitarian response efforts.
THe DTM data used in HAPI is taken from their
[publicly accessible API](https://dtm.iom.int/data-and-analysis/dtm-api),
however we note that there are many country-specific DTM datasets
[available on HDX](https://data.humdata.org/dataset/?dataseries_name=IOM%20-%20DTM%20Baseline%20Assessment&dataseries_name=IOM%20-%20DTM%20Event%20and%20Flow%20Tracking&dataseries_name=IOM%20-%20DTM%20Site%20and%20Location%20Assessment&organization=international-organization-for-migration&q=&sort=last_modified%20desc&ext_page_size=25),
which contain more detail and disaggregation.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/idps_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Affected%20people/get_idps_api_v1_affected_people_idps_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/idps_parameters.yaml') }}

### Transformations applied

None

### Usage notes

* To obtain the number of IDPs per year in a given location,
  only the most recent reporting round per operation should be aggregated

## Refugees & Persons of Concern <a id=”refugees”></a>

This sub-category is populated using data
compiled by [UNHCR](https://www.unhcr.org/), which offers annual
age- and gender-disaggregated global statistics on forcibly displaced and
stateless persons, categorised by their country of origin and country
of asylum. The data are sourced primarily from governments hosting
these populations, UNHCR's own registration data, and occasionally
data published by non-governmental organizations.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/refugees_and_returnees_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Affected%20people/get_refugees_api_v1_affected_people_refugees_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/refugees_and_returnees_parameters.yaml') }}

### Transformations applied

* As this endpoint only concerns refugees and people of concern, and not
  IDPs or refugees, we only include statistics from the
  [population groups](enums.md#population-group)  "REF", "ROC",
  "ASY", "OIP", "IOC", "STA", "OOC", "HST", "RST", and "NAT"

* The table has been reshaped from wide to long: demographic-specific columns
  have been cast to `gender`, `age_range`, and `population`
* It is not possible to p-code based on the location information in the
  original data, therefore population numbers are aggregated to the national
  level
* The reference period is constructed using the full range of the year
  presented in the “Year” column of the original data

### Usage notes

* Not all of the possible population groups are
  necessarily found in the UNHCR data
* An “all” value in the `gender` and `age_range` columns indicates no
  disaggregation
* `age_range` is expressed as "[`min_age`]-[`max_age`]", where `max_age` is
  inclusive, or "[`min_age`]+" for an age range starting at `min_age` or above

## Returnees <a id=”returnees”></a>

This sub-category is populated using data
compiled by [UNHCR](https://www.unhcr.org/), which offers annual
age- and gender-disaggregated global statistics on forcibly displaced and
stateless persons, categorised by their country of origin and country
of asylum. The data are sourced primarily from governments hosting
these populations, UNHCR's own registration data, and occasionally
data published by non-governmental organizations.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/refugees_and_returnees_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Affected%20people/get_returnees_api_v1_affected_people_returnees_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/refugees_and_returnees_parameters.yaml') }}

### Transformations applied

* As this endpoint only concerns refugees and people of concern, and not
  IDPs or refugees, we only include statistics from the
  [population groups](enums.md#population-group)  "RET" and "RDP"
* The table has been reshaped from wide to long: demographic-specific columns
  have been cast to `gender`, `age_range`, and `population`
* It is not possible to p-code based on the location information in the
  original data, therefore population numbers are aggregated to the national
  level
* The reference period is constructed using the full range of the year
  presented in the “Year” column of the original data

### Usage notes

* UNHCR is the only source for returnees in some countries and is therefore
  included in HDX HAPI, but if data is available from IOM, that
  data is preferable
* An “all” value in the `gender` and `age_range` columns indicates no
  disaggregation
* `age_range` is expressed as "[`min_age`]-[`max_age`]", where `max_age` is
  inclusive, or "[`min_age`]+" for an age range starting at `min_age` or above

## Humanitarian Needs <a id=”humanitarian-needs”></a>

This Humanitarian Needs Overview (HNO) represents the shared understanding of
OCHA Humanitarian Country Teams of people's widespread emergency needs during
crises. It includes an estimate of the number of people by sector who require
assistance, often referred to as People in Need (PIN), which is derived using
the [Joint Intersectoral Analysis Framework (JIAF)](https://www.jiaf.info/).

While the HNO data is
[directly available on HDX](https://data.humdata.org/dataset/?dataseries_name=Humanitarian+Needs+Overview),
it comes from different OCHA offices and is currently not standardised. Thus,
HDX HAPI obtains the PIN numbers from the
[HPC Tools API](https://api.hpc.tools/docs/v1/)-based datasets on HDX.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/humanitarian_needs_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Affected%20people/get_humanitarian_needs_api_v1_affected_people_humanitarian_needs_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/humanitarian_needs_parameters.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: the columns in the original
  data of "population", "in-need", "targeted", "affected", "reached",
  and "population" have been cast to a single
  `population_status` field, and renamed to
  "all", "INN", "TGT", "AFF", and "REA", respectively
* Sector values of “ALL” have been converted to “intersectoral”, as these
  represent the intersectoral PIN and **not** the disaggregated population
* Gender and disabled values of “a” have been converted to “all”
* The methodology in Yemen leads to negative population values in some admin 2
  level areas. Where negative values appear they have been omitted from the API.
* The reference period is obtained from the HDX dataset

### Usage notes

* The PIN should **not** be summed across sectors or population statuses,
  as the same people can be present across multiple groups
* For the number of people affected across all
  sectors, please use the PIN value where sector=intersectoral.
* An “all” value in the `gender`, `age_range`, `disable_marker`, and
 `population_group` columns indicates no disaggregation
