# Food Security & Nutrition

---

## Food Security <a id="food-security"></a>

The [IPC Acute Food Insecurity (IPC AFI) classification](https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/)
provides strategically relevant information to decision makers that focuses on
short-term objectives to prevent, mitigate or decrease severe food insecurity.

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/food_security_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Food%20Security%20%26%20Nutrition/get_food_security_api_v1_food_food_security_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/food_security_parameters.yaml') }}

### Transformations applied

* We have p-coded the source data by taking the admin 1 and 2 names,
  and applying the algorithm from
  [`hdx-python-country`](https://hdx-python-country.readthedocs.io/en/latest/),
  which uses phonetic name matching and manual overrides
* Any unmatched p-codes are not included in HDX HAPI. In a future version we
  plan on retaining these rows and including the provider admin names

### Usage Notes

* The total population (`ipc_phase`="all") is not necessarily equal to the sum of
  the populations in phases 1-5. The differences are usually small (due to
  rounding errors), or because there is no IPC phase data
* Due to the above, the sum of the IPC fractions from phases 1-5 may not be
  exactly equal to 1

## Food Prices <a id="food-price"></a>

The World Food Programme Price Database covers foods such as maize, rice,
beans, fish, and sugar for 98 countries and some 3000 markets. It is updated
weekly but primarily contains data with a monthly update frequency. For a
detailed methodology, see WFP's
[Market Analysis Guidelines](https://www.wfp.org/publications/market-analysis-guidelines).

### Summary

{{ read_yaml('data_usage_guides/subcategory_details/food_price_details.yaml') }}

### Parameters Returned

The table below describes the parameters returned from this endpoint.
For available query parameters, please see the
[API sandbox](https://hapi.humdata.org/docs#/Food%20Security%20%26%20Nutrition/get_food_prices_api_v1_food_food_price_get).

{{ read_yaml('data_usage_guides/endpoint_parameters/food_price_parameters.yaml') }}

### Transformations applied

* The reference period is computed by converting date from the “date” column,
  originally presented as 15th day of a particular month, into a range spanning
  the entire month
* The source data is not p-coded, however we have used the admin 1 and 2 names
  to p-code most markets. See [WFP Market](metadata.md#wfp-market)
  for more details.
