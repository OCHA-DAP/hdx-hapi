# Data subcateogry details and usage notes

---

This page contains detailed information about the data in HAPI, including usage notes on each subcategory of data.

## Category: Affected People

### Sub-category: Humanitarian Needs

This data represents the shared understanding of OCHA Humanitarian Country Teams of people's widespread emergency needs during crises. It includes the estimated number of people who need assistance, often referred to as People in Need (PIN). This PIN data is derived from the [Joint Intersectoral Analysis Framework (JIAF)](https://www.jiaf.info/), which consolidates and analyses evidence to inform and direct strategic response planning.

The JIAF data is available for all Humanitarian Response Plan (HRP) countries on HDX. However as the raw data comes from multiple providers (OCHA offices), and is not standardised at this time, HDX HAPI obtains the numbers from the [HPC Tools API](https://api.hpc.tools/docs/v1/). Datasets from the HPC API will soon be available on HDX. 

#### Details


|||
|:----|:----|
|Time series|Past datasets are available in the HPC API, but are sparse prior to 2023.|
|Update frequency|Annually|
|Data provider|OCHA HPC|
|Datasets||
|Related endpoints and schemas|Sector, Disabled Marker, Gender, Population Group, Population Status|

#### Usage Notes

- The PIN should *not* be summed across sectors, as the same people can be counted across multiple sectors. For the number of people affected across all sectors, please use the PIN value where sector=intersectoral.
- Methodology in Yemen leads to negative population values in some admin 2 level areas. Where negative values appear they have been omitted from the API.https://www.jiaf.info/

### Sub-category: Refugees & Persons of Concern

This dataset, compiled by the UNHCR, provides annual age- and gender-disaggregated statistics on refugees and others of concern, categorised by their country of origin and country of asylum. The data are sourced primarily from governments hosting these populations, UNHCR's own registration data, and occasionally data published by non-governmental organisations.

#### Details
|||
|:----|:----|
|Time series|Yes, annual dating back to 2001|
|Update frequency|Annually|
|Data provider|UNHCR|
|Dataset|[Data on forcibly displaced populations and stateless persons (Global)](https://data.humdata.org/dataset/unhcr-population-data-for-world)|
|Related endpoints and schemas|Gender, Population Group|

#### Usage Notes

- The source data is not p-coded and only includes vague location descriptions. Since these are not consistently mappable to admin subdivisions, we aggregate to the national tables and enumslevel. 
- The original data source contains several population groups such as IDPs and asylum seekers, but we only consider refugees (REF) and others of concern (OOC)
- Note that an “all” value in the` `gender` (age_range) column indicates a sum over all genders (age ranges) 

## Category: Coordination & Context

### Sub-category: Operation Presence (3W - Who is Doing What Where)

The [Who does What Where (3W)](https://3w.unocha.org/) is a core humanitarian coordination dataset that contains the geographic and sectoral spread of humanitarian activities and partners. It is critical to know where humanitarian organisations are working and what they are doing in order to ensure collaboration and efficient resource allocation, avoid duplication of efforts, identify gaps, and plan for future humanitarian response.

#### Details

|||
|:----|:----|
|Time series|Not available for this subcategory. While older resources are available on HDX, HDX HAPI currently only supports the latest resource.|
|Update frequency|Irregular, depending on the country. Common update frequencies include quarterly and annually. Please check individual resources for more information|
|Data provider|OCHA country and regional offices|
|Datasets|See the [data grids](https://data.humdata.org/dashboards/overview-of-data-grids?)|
|Related endpoints and schemas|Org, Org Type, Sector|

#### Usage Notes

- This data comes from multiple providers (OCHA offices), in many different formats and levels of detail
- For consistency and interoperability, we aggregate to an [operational presence](https://humanitarian.atlassian.net/wiki/spaces/imtoolbox/pages/214499412/Who+does+What+Where+3W) level (3W:OP, per org, sector, and admin2), even if the original 3W data is more detailed (e.g. the source lists individual activities)

### Sub-category: Funding

FTS publishes data on humanitarian funding flows as reported by donors and recipient organisations. It presents all humanitarian funding to a country and funding that is reported or that can be specifically mapped against funding requirements stated in Humanitarian Response Plans. 

#### Details

|||
|:----|:----|
|Time series|Data contains funding for several years, but the timepoints are not regular|
|Update frequency|Annually|
|Data provider|OCHA FTS|
|Dataset|[OCHA FTS - Requirements and Funding Data series](https://data.humdata.org/dataset/?dataseries_name=OCHA+FTS+-+Requirements+and+Funding+Data)|
|Related endpoints and schemas|None|

#### Usage Notes

- The present version of the API currently captures only funding associated with an appeal. Funding data without associated appeals will be added in a future version. 

### Sub-category: Conflict Events

[ACLED](https://acleddata.com/) collects real-time data on the locations, dates, actors, fatalities, and types of all reported political violence and protest events around the world.

#### Details

|||
|:----|:----|
|Time series|Yes, monthly|
|Update frequency|Weekly|
|Data provider|ACLED|
|Dataset|[ACLED Conflict Events Data series](https://data.humdata.org/dataset/?dataseries_name=ACLED+-+Conflict+Events)|
|Related endpoints and schemas|Event Type|

#### Usage Notes

- The API uses ACLED’s public aggregated data
- The data for political violence events, civilian targeting events, and demonstrations are in separate resource on HDX, but are combined into a single endpoint in the API

### Sub-category: National Risk

The [INFORM Risk Index](https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk) is a global, open-source risk assessment for humanitarian crises and disasters. It can support decisions about prevention, preparedness and response. For more information on the methodology, see [here](https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/Methodology). 

#### Details

|||
|:----|:----|
|Time series|Not available for this subcategory|
|Update frequency|Annually|
|Data provider|INFORM|
|Dataset|[INFORM Risk Index](https://data.humdata.org/dataset/inform-risk-index-2021)|
|Related endpoints and schemas|RiskClass|

## Category: Food Security & Nutrition

### Sub-category: Food Security

The [IPC Acute Food Insecurity (IPC AFI) classification](https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/) provides strategically relevant information to decision makers that focuses on short-term objectives to prevent, mitigate or decrease severe food insecurity.

#### Details

|||
|:----|:----|
|Time series|Yes, with projections|
|Update frequency|Annually|
|Data provider|Food Security and Nutrition Working Group, West and Central Africa|
|Dataset|[West & Central Africa Food Security Data - Cadre Harmonise (CH) and Integrated Food Security Phase Classification (IPC) data](https://data.humdata.org/dataset/cadre-harmonise)|
|Related endpoints and schemas|IPCPhase, IPCType|

#### Usage Notes

- The Beta release only contains data from the [Cadre Harmonisé](https://www.cadreharmonise.org/en_GB), as it is p-coded. In a future release we will p-code and expand coverage to other IPC datasets. 
- The reference period refers to the time frame that the projection covers, not when the projection was made
= The IPC fraction is computed in the HDX HAPI API pipeline, buy dividing the population by the the total population (ipc_phase=all). 
- The total population (ipc_phase=all) is not necessarily equal to the sum of the populations in phases 1-5.

### Sub-category: Food Prices

The World Food Programme Price Database covers foods such as maize, rice, beans, fish, and sugar for 98 countries and some 3000 markets. It is updated weekly but primarily contains data with a monthly update frequency. 

#### Details

|||
|:----|:----|
|Time series|Yes, primarily monthly|
|Update frequency|Weekly|
|Data provider|The World Food Programme|
|Dataset|[WFP Food Prices data series](https://data.humdata.org/dataset/?dataseries_name=WFP+-+Food+Prices)|
|Related endpoints and schemas|Commodity, Currency, Market|

#### Usage Notes

- The source data is not p-coded, however we have used the admin 1 and 2 names to p-code most markets. See the Markets section for more details. 

## Category: Population & Socio-economy

### Sub-category: Baseline Population

This data comprises population statistics sourced from the [common operational datasets](https://cod.unocha.org/) (CODs), typical disaggregated by age and/or gender, and reaching administrative levels 1 or 2. The primary sources include the UNFPA and OCHA country offices, utilised for coordination purposes, although disparities may arise when compared to alternative sources.  

#### Details

|||
|:----|:----|
|Time series|No|
|Update frequency|Annually|
|Data provider|UNFPA, OCHA country offices|
|Dataset|[COD - subnational population statistics data series](https://data.humdata.org/dataset/?dataseries_name=COD+-+Subnational+Population+Statistics)|
|Related endpoints and schemas|Gender|

### Sub-category: Poverty Rate

The global [Oxford Multidimensional Poverty Index](https://ophi.org.uk/global-mpi) (MPI) measures multidimensional poverty in over 100 developing countries, using internationally comparable datasets. 
The MPI assesses poverty through three main dimensions: health, education, and living standards, each of which is represented by specific indicators.Please see the [OPHI methodological note](https://ophi.org.uk/publications/MN-54) for more details. 

#### Details

|||
|:----|:----|
|Time series|Annual, with some combined years|
|Update frequency|Annually|
|Data provider|Oxford Poverty and Human Development Initiative (OPHI)|
|Dataset|[Oxford Poverty and Human Development Initiative - Global Multidimensional Poverty Index data series](https://data.humdata.org/dataset/?dataseries_name=Oxford+Poverty+and+Human+Development+Initiative+-+Global+Multidimensional+Poverty+Index)|
|Related endpoints and schemas|None|


#### Usage Notes 

The source data is very detailed. We’ve chosen the following subset of indicators, detailed below:

|Indicator|format|Description|
|:----|:----|:----|
|mpi|fraction|The multidimensional poverty index. Derived as a product of the headcount ratio and intensity of deprivation.|
|headcount_ratio|%|The percentage of people deprived in 33% or more indicators|
|intensity_of_deprivation|%|The average proportion of indicators in which people are deprived|
|vulnerable_to_poverty|%|The percentage of people deprived in 20-33% of indicators|
|in_severe_poverty|%|The percentage of people deprived in 50% or more indicators|

## Metadata

### Sectors

- The list of sectors is available through the sector endpoint
-  This table is populated using the Global Coordination Groups, with the following additional entries:
    - cash
    - humanitarian assistance
    - multi-sector
    - intersectoral
The sector name strings in the 3W data are normalised and then aligned to the sector table, using the “sector_map” section of this configuration file if needed: https://github.com/OCHA-DAP/hapi-pipelines/blob/main/src/hapi/pipelines/configs/core.yaml. In the absence of a direct match, phonetic matching is used for strings > 5 characters. 

### Org

- The organisation table is populated from the 3W data
- Organisation name and acronym strings are normalised. If an acronym isn’t available, the first 32 characters of the name are used. 
- This [organisation mapping](https://docs.google.com/spreadsheets/d/e/2PACX-1vSfBWvSu3fKA743VvHtgf-pIGkYH7zhy-NP7DZgEV9_a6YU7vtCeWhbLM56aUL1iIfrfv5UBvvjVt7B/pub?gid=1040329566&single=true&output=csv) is used for common alternative names
- Organisations without a sector are not included
- Organisations can have an associated organisation type. If available, the organisation type code is taken directly from the 3W data, otherwise the name string is normalised and matched to the org type names. In the absence of a direct match, phonetic matching is used for strings > 5 characters. If no match is found, the organisation is skipped. 

### OrgType

- The table is populated using [OCHA Digital Services organization types list](https://data.humdata.org/dataset/organization-types-beta), with the addition of: 
    - Civil Society
    - Observer
    - Development Programme
    - Local NGO
Organisation types all have an associated name and code

### IPC Code

The IPC classification includes 5 different phases of increasing severity, described in detail on page 53 of [the IPC technical manual version 3.1](https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/manual/IPC_Technical_Manual_3_Final.pdf), and summarised below:

|Phase|Name|Description|
|:----|:----|:----|
|1|None/Minimal|Households are able to meet essential food and non-food needs without engaging in atypical and unsustainable strategies to access food and income.|
|2|Stressed|Households have minimally adequate food consumption but are unable to afford some essential non-food expenditures without engaging in stress-coping strategies.|
|3|Crisis|Households either have food consumption gaps that are reflected by high or above-usual acute malnutrition, or are marginally able to meet minimum food needs but only by depleting essential livelihood assets or through crisis-coping strategies.|
|4|Emergency|Households either have large food consumption gaps which are reflected in very high acute malnutrition and excess mortality, or are able to mitigate large food consumption gaps but only by employing emergency livelihood strategies and asset liquidation.|
|5|Catastrophe/Famine|Households have an extreme lack of food and/or other basic needs even after full employment of coping strategies. Starvation, death, destitution and extremely critical acute malnutrition levels are evident. (For Famine Classification, an area needs to have extreme critical levels of acute malnutrition and mortality.)|
|3|In Need of Action|Sum of population in phases 3, 4, and 5. The population in Phase 3+ does not necessarily reflect the full population in need of urgent action. This is because some households may be in Phase 2 or even 1 but only because of receipt of assistance, and thus, they may be in need of continued action.|
|all|Total population|Total population|

The above table also includes Phase 3+, to highlight the population in need of action, and total population, used to compute fractions. 

### IPC Type

The IPC provides different projections to aid in planning and response efforts, outlined in the following table:

|IPC type|Definition|
|:----|:----|
|current|Food insecurity that is occurring in the current analysis period.|
|first projection|Projected food insecurity occurring in the period immediately following the current analysis period.|
|second projection|Projected food insecurity occurring in the period immediately following the first projection period.|