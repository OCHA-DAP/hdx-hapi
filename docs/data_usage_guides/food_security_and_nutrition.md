# Food Security & Nutrition

## Food Security <a id="food-security"></a>

The [IPC Acute Food Insecurity (IPC AFI) classification](https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/)
provides strategically relevant information to decision makers that focuses on
short-term objectives to prevent, mitigate or decrease severe food insecurity.

The Beta release of HDX HAPI only contains data from the
[Cadre Harmonisé](https://www.cadreharmonise.org/en_GB), as it is p-coded. In
a future release we will p-code and expand coverage to other IPC datasets.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/food_security_details.yaml') }}

### Transformations applied

* The table has been reshaped from wide to long: the population and individual
* IPC phase columns have been cast to a combination of `ipc_phase` and
  `population_in_phase`
* The IPC fraction is computed in the HDX HAPI API pipeline, by dividing the
  population in that phase by the total population (ipc_phase=all).
* The reference period is computed from the “reference_label” and
  “reference_year” columns in the original data. In the case of a projection,
  it captures date range that the projection covers, not when the projection
  was made
* In the `ipc_type` column, “projected” is converted to “first projection”

### Usage Notes

* The total population (ipc_phase=all) is not necessarily equal to the sum of
  the populations in phases 1-5. The differences are usually small (due to
  rounding errors), or because there is no IPC phase data
* Due to the above, the sum of the IPC fractions from phase 1-5 may not sum to
  exactly 1

## Food Prices <a id="food-prices"></a>

The World Food Programme Price Database covers foods such as maize, rice,
beans, fish, and sugar for 98 countries and some 3000 markets. It is updated
weekly but primarily contains data with a monthly update frequency.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/food_prices_details.yaml') }}

### Transformations applied

* The reference period is computed by converting date from the “date” column,
  originally presented as 15th day of a particular month, into a range spanning
  the entire month
* The source data is not p-coded, however we have used the admin 1 and 2 names
  to p-code most markets. See [Markets](markets) for more details.
