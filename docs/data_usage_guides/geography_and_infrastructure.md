# Geography & Infrastructure

---

## Baseline Population <a id="population"></a>

The population statistics presented here are sourced from the
[common operational datasets](https://cod.unocha.org/) (CODs), and are
typically disaggregated by age and/or gender, and extend to administrative
levels 1 or 2. Primary data providers include the UNFPA and OCHA country
offices. These data are projections based on demographic indicators, and
therefore caution should be used when comparing to population data from other
sources.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/population_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Geography%20%26%20Infrastructure/get_population_api_v1_population_social_population_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/population_parameters.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: demographic-specific columns
  have been cast to `gender`, `age_range`, and `population`
* The reference period is obtained from the HDX dataset

### Usage Notes

* Age disaggregation ranges are not consistent across countries
* Any aggregation to a higher administrative level (e.g., admin 1 for a
  country where admin 2 is also available) has been taken directly from the
  data provided, and was not computed in the API pipeline
* An “all” value in the `gender` and `age_range` columns indicates no
  disaggregation
* `age_range` is expressed as "[`min_age`]-[`max_age`]", where `max_age` is
  inclusive, or "[`min_age`]+" for an age range starting at `min_age` or above

