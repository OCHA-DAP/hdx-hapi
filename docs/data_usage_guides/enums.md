# Enums

## Commodity Category <a id="commodity-category"></a>

**Used in:**
[`Food Prices`](food_security_and_nutrition.md#food-prices),
[`WFP Commodity`](metadata.md#wfp-commodity)

The commodity categories are used in the WFP food prices data to
group together similar types of food items.

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/commodity_category_parameters.yaml') }}

## Disabled Marker <a id="disabled-marker"></a>

**Used in:** [`Humanitarian Needs`](affected_people.md#humanitarian-needs)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/disabled_marker_parameters.yaml') }}

## Event Type <a id="event-type"></a>

**Used in:** [`Conflict Events`](coordination_and_context.md#conflict-events)

ACLED compiles information on political violence, demonstrations, and other
non-violent but politically important events. For their public dataset,
these events are aggregated into three, non-mutually exclusive categories,
outlined in the table below.
Please see the [ACLED Codebook](https://acleddata.com/knowledge-base/codebook/#acled-events)
for their methodology and more detailed descriptions of the sub-event types.

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/event_type_parameters.yaml') }}

## Gender <a id="gender"></a>

**Used in:**
[`Baseline Population`](population_and_socio-economy.md#baseline-population),
[`Humanitarian Needs`](affected_people.md#humanitarian-needs),
[`Refugees & Persons of Concern`](refugees)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/gender_parameters.yaml') }}

## IPC Code <a id="ipc-code"></a>

**Used in:** [`Food Security`](food_security_and_nutrition.md#food-security)

The IPC classification includes 5 different phases of increasing severity,
described in detail on page 53 of
[the IPC technical manual version 3.1](https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/manual/IPC_Technical_Manual_3_Final.pdf),
and summarised in the table below.
This enum also includes Phase 3+, to highlight the population in need of action,
and total population, used to compute fractions.

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/ipc_phase_parameters.yaml') }}

## IPC Type <a id="ipc_type"></a>

**Used in:** [`Food Security`](food_security_and_nutrition.md#food-security)

The IPC provides different projections to aid in planning and response efforts.

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/ipc_type_parameters.yaml') }}

## Population Group <a id="population-group"></a>

**Used in:**
[`Humanitarian Needs`](affected_people.md#humanitarian-needs),
[`Refugees & Persons of Concern`](refugees)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/population_group_parameters.yaml') }}

## Population Status <a id="population-status"></a>

**Used in:**
[`Humanitarian Needs`](affected_people.md#humanitarian-needs),

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/population_status_parameters.yaml') }}

## Price Flag <a id="price-flag"></a>

**Used in:** [`Food Prices`](food_security_and_nutrition.md#food-prices)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/price_flag_parameters.yaml') }}

## Price Type <a id="price-type"></a>

**Used in:** [`Food Prices`](food_security_and_nutrition.md#food-prices)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/price_type_parameters.yaml') }}

## Risk Class <a id="risk-class"></a>

**Used in:** [`National Risk`](coordination_and_context.md#national-risk)

### Allowed values

{{ read_yaml('data_usage_guides/enum_parameters/risk_class_parameters.yaml') }}
