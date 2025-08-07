# Climate

---

## Rainfall <a id=”rainfall”></a>

This sub-category contains dekadal rainfall indicators computed by the
World Food Programme (WFP) from Climate Hazards Group InfraRed
Precipitation satellite imagery with insitu Station data
([CHIRPS](https://chc.ucsb.edu/data/chirps)) version 2, aggregated by
subnational administrative units.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/rainfall_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Climate/get_rainfall_api_v2_climate_rainfall_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/rainfall_parameters.yaml') }}

### Transformations applied

* At the admin 2 level, the data is only made available in HAPI for countries
  with a Humanitarian Response Plan (HRP) and countries in the
  [Global Humanitarian Overview (GHO)](https://humanitarianaction.info/), 
  and only for the past year.
* At the admin 1 level, the data is made available in HAPI for all countries
  for the past five years.

### Usage notes

* Note that the indicators are calculated to match WFP boundaries which do
  not perfectly align with the COD boundaries.
