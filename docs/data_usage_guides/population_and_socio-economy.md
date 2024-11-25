# Population & Socio-economy

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
[API sandbox](https://hapi.humdata.org/docs#/Population%20%26%20Socio-Economy/get_population_api_v1_population_social_population_get).

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

## Poverty Rate <a id="poverty-rate"></a>

The global [Oxford Multidimensional Poverty Index](https://ophi.org.uk/global-mpi)
(MPI) measures multidimensional poverty in over 100 developing countries,
using internationally comparable datasets. The MPI assesses poverty through
three main dimensions: health, education, and living standards, each of which
is represented by specific indicators. For each country, MPI trends over time 
are supplied if available. Relevant OPHI methodological notes are 
[58](https://ophi.org.uk/publications/MN-58), 
[59](https://ophi.org.uk/publications/MN-59) and 
[60](https://ophi.org.uk/publications/MN-60).

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/poverty_rate_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Population%20%26%20Socio-Economy/get_poverty_rate_api_v1_population_social_poverty_rate_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/poverty_rate_parameters.yaml') }}

### Transformations applied

* For rows in the original data with two timepoints, we take each timepoint as
  single entry into HDX HAPI
* The reference period is constructed using the full range of the year or year
  range presented in the “year” column, pertaining to the timepoint in
  question, of the original data

### Usage Notes

* The data is available at admin 0 and admin 1
* We use p-codes from the source data which was p-coded by taking the admin 1 
  names, and applying the algorithm from [`hdx-python-country`](https://hdx-python-country.readthedocs.io/en/latest/)
* Any rows whose p-codes are unmatched are p-coded at the national level with
  admin names supplied in the returned data
* Trends are estimated using indicators in the global MPI that are harmonised 
  across the time periods and are used where data is available for a country
* For any country where trends are unavailable in the source, the latest data
  (which is not harmonised across time) is used instead

