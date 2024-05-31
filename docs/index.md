# Overview

---


The HDX Humanitarian API (HDX HAPI) is a way to access standardised indicators from multiple sources to automate workflows and visualisations 

HDX HAPI is in beta phase, and we are seeking feedback. To share your thoughts or join our slack channel, send an email to [hdx@un.org](hdx@un.org).

The initial scope of HDX HAPI will be the data included in the [HDX Data Grids](https://data.humdata.org/dashboards/overview-of-data-grids). Work is ongoing to continually add more data

## API Key
To access HDX HAPI you need to generate an API key. This can be done via the the [sandbox interface encode_identifier endpoint](https://stage.hapi-humdata-org.ahconu.org/docs#/Utility/get_encoded_identifier_api_v1_encode_identifier_get). Enter your application name and email address and it will return the api key. The key must be included as a query string parameter e.g.

```
https://stage.hapi-humdata-org.ahconu.org/api/v1/themes/3w?app_identifier={your api key}
```


## Terms Of Use
[The HDX Terms of Service](https://data.humdata.org/faqs/terms)


## The Structure of HDX HAPI
### Data Subcategory Endpoints
HAPI is organised around a set of key humanitarian data subcategories like **Baseline Population** and **3W - Operational Presence**. Each of these indicators can be queried via its endpoint.

### Current list of data subcategory endpoints in HDX HAPI
#### Affected People
- [Humanitarian Needs](https://stage.hapi-humdata-org.ahconu.org/docs#/Affected%20people/get_humanitarian_needs_api_v1_affected_people_humanitarian_needs_get)
- [Refugees](https://stage.hapi-humdata-org.ahconu.org/docs#/Affected%20people/get_refugees_api_v1_affected_people_refugees_get)
#### Coordination and Context
- [Conflict Events](https://stage.hapi-humdata-org.ahconu.org/docs#/Conflict%20Events/get_conflict_events_api_v1_coordination_context_conflict_event_get)
- [Funding](https://stage.hapi-humdata-org.ahconu.org/docs#/Funding/get_fundings_api_v1_coordination_context_funding_get)
- [National risk](https://stage.hapi-humdata-org.ahconu.org/docs#/National%20Risk/get_national_risks_api_v1_coordination_context_national_risk_get)
- [Operational Presence (3W)](https://stage.hapi-humdata-org.ahconu.org/docs#/3W%20Operational%20Presence/get_operational_presences_api_v1_coordination_context_operational_presence_get)
#### Food
- [Food Prices](https://stage.hapi-humdata-org.ahconu.org/docs#/Food%20Security%20%26%20Nutrition/get_food_prices_api_v1_food_food_price_get)
- [Food Security](https://stage.hapi-humdata-org.ahconu.org/docs#/Food%20Security%20%26%20Nutrition/get_food_security_api_v1_food_food_security_get)

#### Population Social
- [Population](https://stage.hapi-humdata-org.ahconu.org/docs#/Baseline%20Population/get_populations_api_v1_population_social_population_get)
- [Poverty Rate](https://stage.hapi-humdata-org.ahconu.org/docs#/Baseline%20Population/get_poverty_rates_api_v1_population_social_poverty_rate_get)

### Supporting Tables
Additional supporting endpoints provide information about locations, codelists, and metadata.
### Current list of supporting endpoints in HDX HAPI
- [Location](https://stage.hapi-humdata-org.ahconu.org/docs#/Locations%20and%20Administrative%20Divisions/get_locations_api_v1_metadata_location_get): Get the lists of locations (countries and similar), and administrative subdivisions used as location references in HAPI. These are taken from the [Common Operational Datasets](https://data.humdata.org/dashboards/cod)
- [admin1](https://stage.hapi-humdata-org.ahconu.org/docs#/Locations%20and%20Administrative%20Divisions/get_admin1_api_v1_metadata_admin1_get): Retrieve metadata about the source of any data available in HDX HAPI.
- [admin2](https://stage.hapi-humdata-org.ahconu.org/docs#/Locations%20and%20Administrative%20Divisions/get_admin2_api_v1_metadata_admin2_get): Retrieve metadata about the source of any data available in HDX HAPI.
- [hdx-metadata](https://placeholder.url/docs#/hdx-metadata): Retrieve metadata about the source of any data available in HDX HAPI.


## FAQS
### What is an API ?
An API, or Application Programming Interface, is a set of rules and tools that allows different software programs to communicate with each other. It enables developers to interact with external software components or resources efficiently, facilitating operations such as data retrieval, updates, and complex integrations.

### What is HDX HAPI?
HDX HAPI (the Humanitarian API) is an API designed to streamline access to key datasets related to humanitarian response. The API standardises data from a variety of sources and makes them consistently available. 

### Who is HDX HAPI for?
HDX HAPI is designed for developers, researchers and anyone interested in accessing a centralised source of humanitarian data for analysis and decision-making.

### How do I access HDX HAPI?
You can access HDX HAPI through the API endpoints. Head to the HDX HAPI documentation to get started.

### Do I need an account to access HDX HAPI?
You do not need an account to access HDX HAPI, but you do need an access token which can be generated via the API.

### What time period does the data in the current version of HDX HAPI cover?
The time period covered by the data in the beta version of HDX HAPI varies depending on the resource. Please see the [detailed documentation] for more details. All data contains a reference period. Our goal is to consistently integrate the most up-to-date data from HDX into HDX HAPI.

### How have key datasets been selected?
Key datasets in the beta-phase HDX HAPI have been selected based on their usage and relevance to pressing humanitarian needs. HDX HAPI aims to incorporate the data in the HDX Data Grids, covering countries with a Humanitarian Response Plan.

### What is a sub-category? 

### How up-to-date is the data in HDX HAPI?
HDX HAPI is updated from source data daily. Each dataset’s update frequency varies from daily, weekly, yearly and as needed. Please check the source dataset for further detail.

### Is the data in HDX HAPI different from the data I can download from HDX?
The data in HDX HAPI is from selected datasets from HDX. Some of the data will have been standardised, such as aligning sector names. 

In the coming months, the standardised datasets that HDX HAPI produces will be added to the source datasets on HDX as downloadable CSV files for easy use in spreadsheet applications.

### How is HDX HAPI different from the HDX CKAN API?
The HDX CKAN API provides programmatic access to metadata from HDX. HDX HAPI provides queryable access to the data values themselves.

### Why would I use HDX HAPI instead of other organisations’ APIs?
HDX HAPI brings together a core set of humanitarian data in one place, with standardised references. HDX HAPI integrates APIs of other organisations and pulls through non-API data. 

### How do I give feedback for HDX HAPI?
Please send all feedback to hdx@un.org.
