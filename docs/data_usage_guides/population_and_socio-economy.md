# Population & Socio-economy

## Baseline Population <a id="baseline-population"></a>

The population statistics presented here are sourced from the
[common operational datasets](https://cod.unocha.org/) (CODs), and are
typically disaggregated by age and/or gender, and extend to administrative
levels 1 or 2. Primary data providers include the UNFPA and OCHA country
offices. These data are projections based on demographic indicators, and
therefore caution should be used when comparing to population data from other
sources.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/baseline_population_details.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: demographic-specific columns
  have been cast to gender, age, and population
* The reference period is obtained from the HDX dataset

### Usage Notes

* Age disaggregation ranges are not consistent across countries
* Any aggregation to a higher administrative level (e.g., admin 1 for a
  country where admin 2 is also available) has been taken directly from the
  data provided, and was not computed in the API pipeline

## Poverty Rate <a id="poverty-rate"></a>

The global [Oxford Multidimensional Poverty Index](https://ophi.org.uk/global-mpi)
(MPI) measures multidimensional poverty in over 100 developing countries,
using internationally comparable datasets. The MPI assesses poverty through
three main dimensions: health, education, and living standards, each of which
is represented by specific indicators. Please see the
[OPHI methodological note](https://ophi.org.uk/publications/MN-54) for more
details.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/poverty_rate_details.yaml') }}

### Transformations applied

* For rows in the original data with two timepoints, we take each timepoint as
  single entry into HDX HAPI
* The reference period is constructed using the full range of the year or year
  range presented in the “year” column, pertaining to the timepoint in
  question, of the original data

### Usage Notes

* Please be aware of the metric definitions, provided in the parameter
  summary table !!!! TODO add link and table
