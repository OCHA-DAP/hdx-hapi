# Climate

---

## Rainfall <a id=”rainfall”></a>

This sub-category contains dekadal rainfall indicators computed by the
World Food Programme from Climate Hazards Group InfraRed Precipitation 
satellite imagery with insitu Station data
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

None

### Usage notes

* Note that the indicators are calculated to match WFP boundaries which do
  not perfectly align with the COD boundaries.
