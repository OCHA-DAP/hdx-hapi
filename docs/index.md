# Summary

For full documentation visit [the reference documentation](https://placeholder.url). Please note, in late 2023 and early 2024, HAPI is undergoing continual development. **Both the capabilities of the API and the data within it may change frequently.**

HAPI is a service of the [Humanitarian Data Exchange (HDX)](https://data.humdata.org), part of UNOCHA's [Centre for Humanitarian Data](https://centre.humdata.org). The purpose of HAPI is to improve access to key humanitarian datasets taken from the HDX catalog data to better support automated visualisation and analysis. HAPI is primarily intended for application developers and data scientists working within the humanitarian community.

HAPI provides a consistent, standardised and machine-readable interface to query and retrieve data from a set of high-value humanitarian indicators drawn from the HDX catalogue. With HAPI, the HDX team aims to provide a single point of access to critical humanitarian data in a standardised and structured way. 

As of November 2023, HAPI is in active development and early release. The number of indcators in HAPI is limited, and work is ongoing to continually add more data. The initial scope of HAPI will be the data included in the [HDX Data Grids](https://data.humdata.org/dashboards/overview-of-data-grids).

# Data Coverage

|                                    |     3w     | food_security | humanitarian_needs | national_risk | population |
|:----------------------------------:|:----------:|:-------------:|:------------------:|:-------------:|:----------:|
|            Afghanistan             | Yes (adm2) |       No      |     Yes (adm2)     |   Yes (adm0)  | Yes (adm1) |
|            Burkina Faso            |     No     |   Yes (adm2)  |         No         |   Yes (adm0)  | Yes (adm2) |
|              Cameroon              |     No     |   Yes (adm2)  |         No         |   Yes (adm0)  | Yes (adm1) |
|      Central African Republic      |     No     |   Yes (adm2)  |         No         |   Yes (adm0)  |     No     |
|                Chad                |     No     |   Yes (adm2)  |     Yes (adm2)     |   Yes (adm0)  | Yes (adm2) |
|              Colombia              |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|  Democratic Republic of the Congo  |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|            El Salvador             |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|              Ethiopia              |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|             Guatemala              |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|               Haiti                |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|              Honduras              |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|                Mali                | Yes (adm2) |   Yes (adm2)  |         No         |   Yes (adm0)  | Yes (adm2) |
|             Mozambique             |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|              Myanmar               |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|               Niger                |     No     |   Yes (adm2)  |         No         |   Yes (adm0)  | Yes (adm2) |
|              Nigeria               | Yes (adm2) |   Yes (adm2)  |         No         |   Yes (adm0)  | Yes (adm2) |
|              Somalia               |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|            South Sudan             |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|         State of Palestine         |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm1) |
|               Sudan                |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm1) |
|        Syrian Arab Republic        |     No     |       No      |         No         |   Yes (adm0)  |     No     |
|              Ukraine               |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm1) |
| Venezuela (Bolivarian Republic of) |     No     |       No      |         No         |   Yes (adm0)  | Yes (adm2) |
|               Yemen                |     No     |       No      |     Yes (adm2)     |   Yes (adm0)  |     No     |

# Terms Of Use

[The HDX Terms of Service](https://data.humdata.org/faqs/terms)

# The Structure of HAPI
## Indicator Endpoints
HAPI is organized around a set of key humanitarian indicators like **Baseline Population** and **3W - Operational Presence**. Each of these indicators can be queried via its endpoint.

### Current list of indicator endpoints in HAPI
- [population](https://placeholder.url/docs#/population): Get data about baseline populations of a location
- [3w](https://placeholder.url/docs#/3W): Get data about operational presence. You can learn more about 3w data [here](https://3w.unocha.org/)

## Supporting Tables
Additional supporting endpoints provide information about locations, codelists, and metadata.
### Current list of supporting endpoints in HAPI
- [admin-level](https://placeholder.url/docs#/admin-level): Get the lists of locations (countries and similar), and administrative subdivisions used as location references in HAPI. These are taken from the [Common Operational Datasets](https://data.humdata.org/dashboards/cod)
- [humanitarian-response](https://placeholder.url/docs#/humanitarian-response): Get the lists of organizations, organization types, and humanitarian sectors used in the data available in HAPI.
- [demographic](https://placeholder.url/docs#/demographic): Get the lists of gender categories and age groupings used in the data available in HAPI.
- [hdx-metadata](https://placeholder.url/docs#/hdx-metadata): Retrieve metadata about the source of any data available in HAPI.
## Dates
As of version 1 (released in late 2023), the data in HAPI is static and intended only for testing purposes. However you can filter your HAPI queries based on the date the source data was updated in HDX. Future versions will offer more robust date-related features.