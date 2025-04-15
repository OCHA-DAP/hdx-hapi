# Climate

---

## Rainfall <a id=”rainfall”></a>

This sub-category contains dekadal rainfall indicators computed by the
World Food Programme (WFP) from Climate Hazards Group InfraRed
Precipitation satellite imagery with insitu Station data
([CHIRPS](https://chc.ucsb.edu/data/chirps)) version 2, aggregated by
subnational administrative units. Countries with a Humanitarian Response
Plan (HRP) and counries in the Global Humanitarian Overview (GHO) are
disaggregated to admin 2 while other countries are disaggregated to
admin 1. For the time being only the current
year of rainfall data is included due to the size of the data.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/rainfall_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Climate/get_rainfall_api_v2_climate_rainfall_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/rainfall_parameters.yaml') }}

### Transformations applied

None

### Usage notes

* Note that the indicators are calculated to match WFP boundaries which do
  not perfectly align with the COD boundaries.
