# Affected People

## Refugees & Persons of Concern <a id=”refugees”></a>

This dataset, compiled by the [UNHCR](https://www.unhcr.org/), offers annual
age- and gender-disaggregated statistics on refugees and people of concern,
categorised by their country of origin and country of asylum. The data are
sourced primarily from governments hosting these populations, UNHCR's own
registration data, and occasionally data published by non-governmental
organisations.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/refugees_details.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: demographic-specific columns
  have been cast to gender, age, and population
* Population group has been filtered for refugees (REF) and others of concern
  (OOC)
* It is not possible to p-code based on the location information in the
  original data, therefore population numbers are aggregated to the national
  level
* The reference period is constructed using the full range of the year
  presented in the “Year” column of the original data

### Usage notes

* An “all” value in the `gender` and `age_range` columns indicates no
  disaggregation

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
[HPC Tools API](https://api.hpc.tools/docs/v1/).
Datasets from the HPC API will soon be available on HDX.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/humanitarian_needs_details.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: the columns of population, in
  need, targeted, affected, and reached have been cast to a single
  `population_status` column
* Sector values of “ALL” have been converted to “intersectoral”
* Gender and disabled values of “a” have been converted to “all”
* The methodology in Yemen leads to negative population values in some admin 2
  level areas. Where negative values appear they have been omitted from the API.
* The reference period is obtained from the HDX dataset

### Usage notes

* The PIN should *not* be summed across sectors, as the same people can be
  counted across multiple sectors. For the number of people affected across all
  sectors, please use the PIN value where sector=intersectoral.
* An “all” value in the `gender`, `age_range`, `disable_marker`, and
 `population_group` columns indicates no disaggregation
* A “population” value in the `population_status` column indicates no d
  isaggregation
