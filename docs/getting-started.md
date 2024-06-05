# Getting Started with the API

---

Here you will find simple instructions to help you get started with using HAPI. In addition to this getting started section we suggest exploring the [query interface](https://stage.hapi-humdata-org.ahconu.org/docs) which details all available filtering options for each endpoint, providing a hands-on way to familiarise yourself with the API's structure.


Below, you will find example URLs to help you learn how to construct your API queries. These URLs can be entered directly into your web browser for immediate results.

## Generating a key

To access HAPI you need to generate an app identifier. This can be done via the the [sandbox interface encode_identifier endpoint](https://stage.hapi-humdata-org.ahconu.org/docs#/Utility/get_encoded_identifier_api_v1_encode_identifier_get). Enter your application name and email address and it will return the app identifier. The key must be included as a query string parameter e.g.


```
https://stage.hapi-humdata-org.ahconu.org/api/v1/coordination-context/operational-presence?app_identifier={your app identifier}
```




## Accessing Operational Presence Dta(3W) Data


Retrieve the latest Operational Presence (Who's doing What, Where) data for a specific country using the `location_code` filter and the country’s ISO3 code. The following example demonstrates how to get data for Mali:


Copy this link into your browser to see the results


```plaintext
https://stage.hapi-humdata-org.ahconu.org/api/v1/coordination-context/operational-presence?location_code=mli&output_format=json&offset=0&limit=1000&app_identifier={your app identifier}


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
https://stage.hapi-humdata-org.ahconu.org/api/v1/coordination-context/operational-presence?location_code=MLI&output_format=json&offset=1000&limit=1000&app_identifier={your app identifier}
```


Check the code example section to see code for querying multiple pages and loading into a single result.


With the operational presence theme endpoint there are a variety of filters to target your results include ```sector_name```, ```admin2_code``` and ```org_name```


This query gets all of the WASH activities happening in Yobe, Nigeria using the ```sector_name``` and ```admin1_name``` filter


```plaintext
https://stage.hapi-humdata-org.ahconu.org/api/v1/coordination-context/operational-presence?sector_name=Water%20Sanitation%20Hygiene&location_name=Nigeria&admin1_name=Yobe&output_format=json&offset=0&limit=1000&app_identifier={your app identifier}
```


Remember to check the [sandbox](https://placeholder.url/docs) for the full list of filters available


## Exploring Population Data


The Population endpoint delivers detailed demographic breakdowns by age range and gender.  The example query below uses ```location_code``` rather than ```location_name``` to use the iso3 code for Afghanistan ```AFG```. In addition it also uses the ```admin_level=1``` filter to get only admin level 1 results.


```
https://stage.hapi-humdata-org.ahconu.org/api/v1/population-social/population?location_code=AFG&output_format=json&offset=0&limit=1000&admin_level=1&app_identifier={your app identifier}
```


To refine this query to retrieve population statistics specifically for males under the age of 5, append the age_range_code and gender_code filters to your request:


```
https://stage.hapi-humdata-org.ahconu.org/api/v1/population-social/population?location_code=AFG&output_format=json&offset=0&limit=10000&admin_level=1&age_range_code=0-4&gender_code=m&app_identifier={your app identifier}
```


By tailoring these filters, you can obtain a variety of demographic insights from the API


## Understanding Supporting Tables


Each theme within our API is bolstered by associated supporting tables. These tables are essential for understanding the range of possible values you can work with in the theme-specific tables. For example, if you're filtering by sector, such as, `sector=Nutrition`—you'll want to know what sectors are available.


You can retrieve a list of possible age ranges by querying the `sector` support table like so:


```plaintext
https://stage.hapi-humdata-org.ahconu.org/api/v1/metadata/sector?output_format=json&offset=0&limit=1000&app_identifier=Z2V0dGluZ3Mtc3RhcnRlZDpzaW1vbi5qb2huc29uQHVuLm9yZw==
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
https://stage.hapi-humdata-org.ahconu.org/api/v1/metadata/resource?hdx_id=b28928be-1847-408f-b3cd-9b87b596c710&update_date_min=2020-01-01&update_date_max=2024-12-31&output_format=jsonlimit=100&offset=00&app_identifier={your app identifier}
```


Executing this query provides a response like the following:


```JSON
{
  "data": [
    {
      "hdx_id": "b28928be-1847-408f-b3cd-9b87b596c710",
      "dataset_hdx_id": "d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3",
      "name": "MALI_3W_December_2023",
      "format": "XLSX",
      "update_date": "2024-03-01T12:33:46",
      "is_hxl": true,
      "download_url": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/b28928be-1847-408f-b3cd-9b87b596c710/download/mali-3w-presence-operationnelle-december-2023.xlsx",
      "hapi_updated_date": "2024-05-30T19:30:19.932113",
      "dataset_hdx_stub": "mali-operational-presence",
      "dataset_title": "Mali: Operational Presence",
      "dataset_hdx_provider_stub": "ocha-mali",
      "dataset_hdx_provider_name": "OCHA Mali",
      "hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3/resource/b28928be-1847-408f-b3cd-9b87b596c710",
      "hdx_api_link": "https://data.humdata.org/api/action/resource_show?id=b28928be-1847-408f-b3cd-9b87b596c710",
      "dataset_hdx_link": "https://data.humdata.org/dataset/d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3",
      "dataset_hdx_api_link": "https://data.humdata.org/api/action/package_show?id=d7ab89e4-bcb2-4127-be3c-5e8cf804ffd3",
      "provider_hdx_link": "https://data.humdata.org/organization/ocha-mali",
      "provider_hdx_api_link": "https://data.humdata.org/api/action/organization_show?id=ocha-mali"
    }
  ]
}
```


This output gives you a comprehensive view of the dataset's metadata, including the update date, the contributing organisation, and direct links to more information via the CKAN API and the original data file download.


As a starting point to effectively use our API, we encourage you to experiment with different queries using the [sandbox's](https://stage.hapi-humdata-org.ahconu.org/docs) query interface and review the provided code examples for guidance.

