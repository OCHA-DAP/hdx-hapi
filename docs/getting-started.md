# Getting Started with the API

---

In addition to this getting started section we suggest exploring the [query interface](https://stage.hapi-humdata-org.ahconu.org/docs) which details all available filtering options for each endpoint, providing a hands-on way to familiarise yourself with the API's structure.


Below, you will find example URLs to help you learn how to construct your API queries. These URLs can be entered directly into your web browser for immediate results.

## Generating a key

To access HAPI you need to generate an API key. This can be done via the the [sandbox interface encode_identifier endpoint](https://stage.hapi-humdata-org.ahconu.org/docs#/Utility/get_encoded_identifier_api_v1_encode_identifier_get). Enter your application name and email address and it will return the api key. The key must be included as a query string parameter e.g.


```
https://stage.hapi-humdata-org.ahconu.org/api/v1/themes/3w?app_identifier={your api key}
```




## Accessing 3W Data


Retrieve the latest 3W (Who's doing What, Where) data for a specific country using the `location_name` filter. The following example demonstrates how to get data for Mali:


Copy this link into your browser to see the results


```plaintext
https://placeholder.url/api/v1/themes/3w?location_name=Mali&output_format=json&offset=0&limit=10000&app_identifier={your api key}


```


A single row of the result looks like this:


```JSON
[
 {
   "sector_code":"NUT",
   "dataset_hdx_stub":"mali-operational-presence",
   "resource_hdx_id":"a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
   "org_acronym":"ACF-E",
   "org_name":"Action Contre la Faim-Espagne",
   "sector_name":"Nutrition",
   "location_code":"MLI",
   "location_name":"Mali",
   "admin1_code":"ML07",
   "admin1_name":"Gao",
   "admin2_code":"ML0702",
   "admin2_name":"Bourem"
 }
]
```


The above result was in JSON. It is also possible to get a CSV by changing the output format as follows ```output_format=csv```.


The maximum number of rows returned in a single response is 10,000. To access more data beyond this limit, you can paginate through results by increasing the ```offset``` parameter as shown here:


```plaintext
https://placeholder.url/api/v1/themes/3w?location_name=Mali&output_format=json&offset=10000&limit=10000&app_identifier={your api key}
```


Check the code example section to see code for querying multiple pages and loading into a single result.


With the 3w theme endpoint there are a variety of filters to target your results include ```sector_name```, ```admin2_code``` and ```org_name```


This query gets all of the WASH activities happening in Yobe, Nigeria using the ```sector_name``` and ```admin1_name``` filter


```plaintext
https://placeholder.url/api/v1/themes/3w?sector_name=Water%20Sanitation%20Hygiene&location_name=Nigeria&admin1_name=Yobe&output_format=json&offset=0&limit=1000&app_identifier={your api key}
```


Remember to check the [technical documentation](https://placeholder.url/docs) for the full list of filters available


## Exploring Population Data


The Population endpoint delivers detailed demographic breakdowns by age range and gender.  The example query below uses ```location_code``` rather than ```location_name``` to use the iso3 code for Afghanistan ```AFG```. In addition it also uses the ```admin_level=1``` filter to get only admin level 1 results.


```
https://placeholder.url/api/v1/themes/population?location_code=AFG&output_format=json&offset=0&limit=10000&admin_level=1&app_identifier={your api key}
```


To refine this query to retrieve population statistics specifically for males under the age of 5, append the age_range_code and gender_code filters to your request:


```
https://placeholder.url/api/v1/themes/population?location_code=AFG&output_format=json&offset=0&limit=10000&admin_level=1&age_range_code=0-4&gender_code=m&app_identifier={your api key}
```


By tailoring these filters, you can obtain a variety of demographic insights from the API


## Understanding Supporting Tables


Each theme within our API is bolstered by associated supporting tables. These tables are essential for understanding the range of possible values you can work with in the theme-specific tables. For example, if you're filtering by age range—as we did with `age_range_code=0-4`—you'll want to know what age range codes are available.


You can retrieve a list of possible age ranges by querying the `age_range` support table like so:


```plaintext
https://placeholder.url/api/v1/age_range?output_format=json&offset=0&limit=1000
```


This functionality is not limited to age ranges. There are similar support tables for a variety of filters such as organisations, genders, sectors, and more. Querying these support tables provides you with the necessary information to apply precise filters and extract the data that's most relevant to your needs.


## Getting Metadata through API Queries


When you inspect the JSON output from an initial API query, you'll encounter a variety of detailed fields. Take a look at this sample output:


```json
[
 {
   "sector_code": "NUT",
   "dataset_hdx_stub": "mali-operational-presence",
   "resource_hdx_id": "a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
   "org_acronym": "ACF-E",
   "org_name": "Action Contre la Faim-Espagne",
   "sector_name": "Nutrition",
   "location_code": "MLI",
   "location_name": "Mali",
   "admin1_code": "ML07",
   "admin1_name": "Gao",
   "admin2_code": "ML0702",
   "admin2_name": "Bourem"
 }
]
```


Among these fields, ```dataset_hdx_stub``` and ```resource_hdx_id``` are keys to unlocking metadata about the dataset. This metadata includes the last update date, the organisation responsible for the data, and links to download the original dataset.


To dive deeper into the data's origin, use the resource_hdx_id in the resource endpoint URL:


```
https://placeholder.url/api/v1/resource?hdx_id=a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1&update_date_min=2020-01-01&update_date_max=2024-12-31&output_format=json&offset=0&limit=1000&app_identifier={your api key}
```


Executing this query provides a response like the following:


```JSON
[
 {
   "hdx_id": "a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
   "name": "MALI_3W_June_2023",
   "format": "XLSX",
   "update_date": "2023-09-28T10:45:27",
   "is_hxl": false,
   "download_url": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1/download/mali-3w_maj-2.xlsx",
   "dataset_hdx_id": "d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3",
   "dataset_hdx_stub": "mali-operational-presence",
   "dataset_title": "Mali: Operational Presence",
   "dataset_hdx_provider_stub": "ocha-mali",
   "dataset_hdx_provider_name": "OCHA Mali",
   "hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1/",
   "hdx_api_link": "https://data.humdata.org/api/action/resource_show?id=a92fd2e8-4cbc-4366-92a8-1ffbbd6659d1",
   "dataset_hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/",
   "dataset_hdx_api_link": "https://data.humdata.org/api/action/package_show?id=d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3"
 }
]
```


This output gives you a comprehensive view of the dataset's metadata, including the update date, the contributing organisation, and direct links to more information via the CKAN API and the original data file download.


As a starting point to effectively use our API, we encourage you to experiment with different queries using the technical documentation's query interface and review the provided code examples for guidance.
