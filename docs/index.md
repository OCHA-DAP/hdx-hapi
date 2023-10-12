# Summary

For full documentation visit [the reference documentation - TBD](fix/this/link). Please note, in late 2023 and early 2024, HAPI is undergoing continual development. **Both the capabilities of the API and the data within it may change frequently.**

HAPI is a service of the [Humanitarian Data Exchange (HDX)](https://data.humdata.org), part of UNOCHA's [Centre for Humanitarian Data](https://centre.humdata.org). The purpose of HAPI is to improve access to key humanitarian datasets taken from the HDX catalog data to better support automated visualisation and analysis. HAPI is primarily intended for application developers and data scientists working within the humanitarian community.

HAPI provides a consistent, standardised and machine-readable interface to query and retrieve data from a set of high-value humanitarian indicators drawn from the HDX catalogue. With HAPI, the HDX team aims to provide a single point of access to critical humanitarian data in a standardised and structured way. 

As of November 2023, HAPI is in active development and early release. The number of indcators in HAPI is limited, and work is ongoing to continually add more data. The initial scope of HAPI will be the data included in the [HDX Data Grids](https://data.humdata.org/dashboards/overview-of-data-grids).

## The Structure of HAPI
### Indicator Endpoints
HAPI is organized around a set of key humanitarian indicators like **Baseline Population** and **3W - Operational Presence**. Each of these indicators can be queried via its endpoint.

#### Current list of indicators in HAPI
- [Baseline Population](https://stage.hapi-humdata-org.ahconu.org/docs#/population): Get data about baseline populations
- [3W](https://stage.hapi-humdata-org.ahconu.org/docs#/3W): Get data about operational presence



### Supporting Tables
Additional supporting endpoints provide information about locations, codelists, and metadata.

### Dates

## How is 


* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.



## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
