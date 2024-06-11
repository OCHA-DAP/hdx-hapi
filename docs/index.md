# Overview

---

The [HDX Humanitarian API](https://dev.data-humdata-org.ahconu.org/hapi)(HDX HAPI) is a way to access standardised indicators from multiple sources to automate workflows and visualisations

HDX HAPI is in beta phase, and we are seeking feedback. To share your thoughts or join our slack channel, send an email to [hdx@un.org](hdx@un.org).

The initial scope of HDX HAPI will be the data included in the [HDX Data Grids](https://data.humdata.org/dashboards/overview-of-data-grids). Work is ongoing to add more data.

# App Identifier

To access HDX HAPI you need to generate an API identifier. This can be done via the the [sandbox interface encode_identifier endpoint](https://hapi.humdata.org/docs#/Utility/get_encoded_identifier_api_v1_encode_identifier_get). Enter your application name and email address and it will return the app identifier. The key must be included as a query string parameter e.g.

```
https://hapi.humdata.org/api/v1/themes/3w?app_identifier={your app identifier}
```

# The Structure of HDX HAPI

## Data Subcategory Endpoints
HDX HAPI is organised around a set of key humanitarian data subcategories like **Baseline Population** and **Conflict Events**. Each of these subcategories can be queried via its endpoint.

### Current list of data subcategory endpoints in HAPI

#### Affected People

- [Humanitarian Needs](https://hapi.humdata.org/docs#/Affected%20people/get_humanitarian_needs_api_v1_affected_people_humanitarian_needs_get)
- [Refugees & Persons of Concern](https://hapi.humdata.org/docs#/Affected%20people/get_refugees_api_v1_affected_people_refugees_get)

#### Coordination & Context

- [Who is Doing What Where - Operational Presence](https://hapi.humdata.org/docs#/3W%20Operational%20Presence/get_operational_presences_api_v1_coordination_context_operational_presence_get)
- [Funding](https://hapi.humdata.org/docs#/Funding/get_fundings_api_v1_coordination_context_funding_get)
- [Conflict Events](https://hapi.humdata.org/docs#/Conflict%20Events/get_conflict_events_api_v1_coordination_context_conflict_event_get)
- [National Risk](https://hapi.humdata.org/docs#/National%20Risk/get_national_risks_api_v1_coordination_context_national_risk_get)

#### Food Security & Nutrition

- [Food Security](https://hapi.humdata.org/docs#/Food%20Security%20%26%20Nutrition/get_food_security_api_v1_food_food_security_get)
- [Food Prices](https://hapi.humdata.org/docs#/Food%20Security%20%26%20Nutrition/get_food_prices_api_v1_food_food_price_get)

#### Population & Socio-economy

- [Baseline Population](https://hapi.humdata.org/docs#/Baseline%20Population/get_populations_api_v1_population_social_population_get)
- [Poverty Rate](https://hapi.humdata.org/docs#/Baseline%20Population/get_poverty_rates_api_v1_population_social_poverty_rate_get)

# Terms Of Use

Use of HDX HAPI is governed by the [HDX HAPI Terms of Use](https://data.humdata.org/hapi/terms).

## FAQS

Please [refer to the landing page](https://data.humdata.org/hapi) for non-technical FAQs
