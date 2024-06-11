# Enums

Enums, or enumerations, are a data type used to define a set of named values
that represent fixed options for a field in the API.

## Commodity Category <a id="commodity-category"></a>

**Used in:**
[`Food Prices`](food_security_and_nutrition.md#food-price),
[`WFP Commodity`](metadata.md#wfp-commodity)

The commodity categories are used in the WFP food prices data to organize
foods into food groups.

{{ read_yaml('data_usage_guides/enum_parameters/commodity_category_parameters.yaml') }}

## Disabled Marker <a id="disabled-marker"></a>

**Used in:** [`Humanitarian Needs`](affected_people.md#humanitarian-needs)

This marker is used to indicate any HNO PIN calculations that are disaggregated
by disability. For more information on disability classification, see the
[WHO International Classification of Functioning, Disability and Health (ICF)](https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health).

{{ read_yaml('data_usage_guides/enum_parameters/disabled_marker_parameters.yaml') }}

## Event Type <a id="event-type"></a>

**Used in:** [`Conflict Events`](coordination_and_context.md#conflict-event)

ACLED compiles information on political violence, demonstrations, and other
non-violent but politically important events. For their public dataset,
these events are aggregated into three, non-mutually exclusive categories,
outlined in the table below.
Please see the [ACLED Codebook](https://acleddata.com/knowledge-base/codebook/#acled-events)
for their methodology and more detailed descriptions of the sub-event types.

{{ read_yaml('data_usage_guides/enum_parameters/event_type_parameters.yaml') }}

## Gender <a id="gender"></a>

**Used in:**
[`Baseline Population`](population_and_socio-economy.md#population),
[`Humanitarian Needs`](affected_people.md#humanitarian-needs),
[`Refugees & Persons of Concern`](affected_people.md#refugees)

Several sub-categories in HDX-HAPI are disaggregated by gender.

{{ read_yaml('data_usage_guides/enum_parameters/gender_parameters.yaml') }}

## IPC Code <a id="ipc-code"></a>

**Used in:** [`Food Security`](food_security_and_nutrition.md#food-security)

The IPC/CH classification includes 5 different phases of increasing severity,
described in detail on page 53 of
[the IPC technical manual version 3.1](https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/manual/IPC_Technical_Manual_3_Final.pdf),
and summarised in the table below.
This enum also includes Phase 3+, to highlight the population in need of action,
and total population, used to compute fractions.

{{ read_yaml('data_usage_guides/enum_parameters/ipc_phase_parameters.yaml') }}

## IPC Type <a id="ipc_type"></a>

**Used in:** [`Food Security`](food_security_and_nutrition.md#food-security)

The IPC and Cadre Harmonisé provide different projections to aid in planning
and response efforts.

{{ read_yaml('data_usage_guides/enum_parameters/ipc_type_parameters.yaml') }}

## Population Group <a id="population-group"></a>

**Used in:**
[`Humanitarian Needs`](affected_people.md#humanitarian-needs),
[`Refugees & Persons of Concern`](affected_people.md#refugees)

Almost all population group terms come from
[UNHCR's glossary](https://www.unhcr.org/refugee-statistics/methodology/data-content/),
except for "RRI", and "all". "all" represents no-disaggregation", while
RRI" was added as an umbrella term
for returnees because the humanitarian
needs data does not distinguish between returned refugees and returned
IDPs.

{{ read_yaml('data_usage_guides/enum_parameters/population_group_parameters.yaml') }}

## Population Status <a id="population-status"></a>

**Used in:**
[`Humanitarian Needs`](affected_people.md#humanitarian-needs)

The population status disaggregation provides a framework for the HNO to
determine how effectively people in need are being reached.
Note that "all" does **not** represent a sum over the different status types,
but rather a disaggregation, as the same people may be present in
multiple groups.

{{ read_yaml('data_usage_guides/enum_parameters/population_status_parameters.yaml') }}

## Price Flag <a id="price-flag"></a>

**Used in:** [`Food Prices`](food_security_and_nutrition.md#food-price)

Pre-processing characteristics of food prices.

{{ read_yaml('data_usage_guides/enum_parameters/price_flag_parameters.yaml') }}

## Price Type <a id="price-type"></a>

**Used in:** [`Food Prices`](food_security_and_nutrition.md#food-price)

The point in the supply chain at which the price is determined.
See FAO's
[concepts on price data](https://www.fao.org/economic/the-statistics-division-ess/methodology/methodology-systems/price-statistics-and-index-numbers-of-agricultural-production-and-prices/4-concepts-on-price-data/en/)
for more information.

{{ read_yaml('data_usage_guides/enum_parameters/price_type_parameters.yaml') }}

## Risk Class <a id="risk-class"></a>

**Used in:** [`National Risk`](coordination_and_context.md#national-risk)

In national risk, the final INFORM risk score is grouped into one of five
risk classes, with the objective of systemically identifying risk in a
consistent manner. Note that other categories and dimensions are also
grouped into classes but with different thresholds, and these are not included
in HDX HAPI. Please see the
[methodology](https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/Methodology)
for more details.

{{ read_yaml('data_usage_guides/enum_parameters/risk_class_parameters.yaml') }}
