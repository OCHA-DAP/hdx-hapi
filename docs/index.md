# HDX HAPI

The [HDX Humanitarian API](https://hapi.humdata.org) (HDX HAPI) is a way
to access standardised indicators from multiple sources to automate workflows
and visualisations.

HDX HAPI is in beta phase, and we are seeking feedback. To share your thoughts
or join our Slack channel, send an email to [hdx@un.org](mailto:hdx@un.org).

## Latest Changes

_Note: this is only a 10-line snippet, for full details please refer
 to the complete [changelog](changelog.md)._

--8<-- "docs/changelog.md:20:30"

## Data Coverage

Thematically, HDX HAPI aims to include all the data subcategories from the
[HDX data grids](https://data.humdata.org/dashboards/overview-of-data-grids).
Geographically, HAPI focuses on all countries that have a humanitarian response
plan but also includes other countries for which the data is available.
The [Data Availability Table](https://data.humdata.org/hapi#data-availability)
details the data coverage that we have achieved at present, and to which
administrative level the data is available: national (admin 0), admin 1,
or admin 2.

## Accessing the Data

You can find out more about HDX HAPI in the
[Getting Started](getting-started.md) and
[API documentation](https://hapi.humdata.org) pages.

There are also
[HDX HAPI datasets on HDX](https://data.humdata.org/organization/hdx-hapi)
containing the data available from the API. Some datasets have warning and
error columns. Warnings typically indicate corrections have been made to
the data or show things to look out for. Rows with only warnings are considered
complete, and are available from the API. Errors usually mean that the data
is incomplete or unusable. Rows with any errors are not present in the API but
have been included for transparency.

## How HDX HAPI works

The full API ecosystem is illustrated in the diagram below. It depicts data
being added to HDX either through manual uploads or automated API submission
by partners, or from HDX-managed pipelines.
This incoming data is then processed through our pipelines,
which add and verify p-codes and standardize key
components.
The result is a set of global HAPI subcateogry datasets published on HDX.
These datasets as the foundation for the data available via API, and they are
further refined to create the country-specific HDX HAPI datasets.

<iframe src="img/hapi_flow_diagram.pdf" width="100%" height="600px">
This browser does not support PDFs. Please download the PDF to view it: <a href="assets/diagram.pdf">Download PDF</a>
</iframe>

## Terms Of Use

Use of HDX HAPI is governed by the
[HDX HAPI Terms of Use](https://data.humdata.org/hapi/terms).

## FAQS

Please [refer to the landing page](https://data.humdata.org/hapi)
for non-technical FAQs
