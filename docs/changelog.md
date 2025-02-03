# HDX HAPI Changelog

HDX HAPI is built on several interconnected codebases:

- [hdx-hapi](https://github.com/OCHA-DAP/hdx-hapi): provides the API endpoints,
  API documentation, and ReadTheDocs
- [hapi-sqlalchemy-schema](https://github.com/OCHA-DAP/hapi-sqlalchemy-schema):
  defines the schema for the underlying database
- [hapi-pipelines](https://github.com/OCHA-DAP/hapi-pipelines)
  handles data collection and transformation from HDX, populating the
  database with structured datasets
- [hapi-pipelines-prod](https://github.com/OCHA-DAP/hapi-pipelines-prod),
  a clone of `hapi-pipelines` used for deployment

Below we outline the major changes and updates to the production version of
the API.

## Latest changes

### Unreleased
- Aligned category and sub-category endpoint names in the docs with
  [HDX data grids](https://data.humdata.org/dashboards/overview-of-data-grids?)

### 2025-01-06
- Added functionality to filter by time period

### 2024-12-19

- Increased temporal coverage for humanitarian needs
  subcategory
- Increased geographical coverage to all available for
  operational presence subcategory

### 2024-11-21

- Increased geographical coverage to global for
  baseline population and poverty rate subcategories

### 2024-11-11

- Gender, age, and disability disaggregation in
  humanitarian needs reduced to a single freeform category column
- Switch from using Cadre Harmonisé to IPC for food security data.
  This change entails that geographical coverage is expanded to global,
  and involves p-coding the administrative names.
- Added `provider_admin1_name` and `provider_admin2_name` columns
