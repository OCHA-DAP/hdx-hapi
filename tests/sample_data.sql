-- ---------------------------------------------------------------------
-- Dummy core data for testing.
--
-- Note: we add explicit IDs here to simply cross referencing, but in
-- production we'll let the database generate them automatically.
--
-- Started 2023-08-09
-- ---------------------------------------------------------------------

INSERT INTO dataset (id, hdx_id, hdx_stub, title, hdx_provider_stub, hdx_provider_name)
VALUES
(1, 'c3f001fa-b45b-464c-9460-1ca79fd39b40', 'dataset01', 'Dataset #1', 'provider01', 'Provider #1'),
(2, '7cf3cec8-dbbc-4c96-9762-1464cd0bff75', 'dataset02', 'Dataset #2', 'provider02', 'Provider #2');

INSERT INTO resource (id, dataset_ref, hdx_id, name, format, update_date, download_url, is_hxl, hapi_updated_date)
VALUES
(1, 1, '90deb235-1bf5-4bae-b231-3393222c2d01', 'resource-01.csv', 'csv', '2023-06-01 00:00:00',
'https://data.humdata.org/dataset/c3f001fa-b45b-464c-9460-1ca79fd39b40/resource/90deb235-1bf5-4bae-b231-3393222c2d01/download/resource-01.csv',
 TRUE, '2023-01-01 00:00:00'),
(2, 1, 'b9e438e0-b68a-49f9-b9a9-68c0f3e93604', 'resource-02.xlsx', 'xlsx', '2023-07-01 00:00:00',
'https://fdw.fews.net/api/tradeflowquantityvaluefacts/?dataset=1845&country=TZ&fields=simple&format=xlsx',
 TRUE, '2023-01-01 00:00:00'),
(3, 2, '62ad6e55-5f5d-4494-854c-4110687e9e25', 'resource-03.csv', 'csv', '2023-08-01 00:00:00',
 'https://data.humdata.org/dataset/7cf3cec8-dbbc-4c96-9762-1464cd0bff75/resource/62ad6e55-5f5d-4494-854c-4110687e9e25/download/resource-03.csv',
 TRUE, '2023-01-01 00:00:00');

-- these are the actual datatypes from
-- https://data.humdata.org/dataset/organization-types-beta
INSERT INTO org_type (code, description) VALUES
('431', 'Academic / Research'),
('433', 'Donor'),
('434', 'Embassy'),
('435', 'Government'),
('437', 'International NGO'),
('438', 'International Organization'),
('439', 'Media'),
('440', 'Military'),
('441', 'National NGO'),
('443', 'Other'),
('444', 'Private sector'),
('445', 'Red Cross / Red Crescent'),
('446', 'Religious'),
('447', 'United Nations');

-- dummy data
INSERT INTO org (id, acronym, name, org_type_code, reference_period_start, reference_period_end, hapi_updated_date) VALUES
(1, 'ORG01', 'Organisation 1', '433', '2023-08-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(2, 'ORG02', 'Organisation 2', '437', '2023-07-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(3, 'ORG03', 'Organisation 3', '447', '2023-06-01 00:00:00', NULL, '2023-01-01 00:00:00');

-- these are the actual sector codes from
-- https://data.humdata.org/dataset/global-coordination-groups-beta
-- (they won't be sufficient for production; we'll have to add to them)
INSERT INTO sector (code, name)
VALUES
('SHL', 'Emergency Shelter and NFI'),
('CCM', 'Camp Coordination / Management'),
('PRO-MIN', 'Mine Action'),
('FSC', 'Food Security'),
('WSH', 'Water Sanitation Hygiene'),
('LOG', 'Logistics'),
('PRO-CPN', 'Child Protection'),
('PRO', 'Protection'),
('EDU', 'Education'),
('NUT', 'Nutrition'),
('HEA', 'Health'),
('ERY', 'Early Recovery'),
('TEL', 'Emergency Telecommunications'),
('PRO-GBV', 'Gender Based Violence'),
('PRO-HLP', 'Housing, Land and Property');

-- dummy data
INSERT INTO location (id, code, name, has_hrp, in_gho, reference_period_start, reference_period_end, hapi_updated_date)
VALUES
(1, 'FOO', 'Foolandia', TRUE, TRUE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00');

-- dummy data
INSERT INTO admin1 (id, location_ref, code, name, is_unspecified, reference_period_start, reference_period_end, hapi_updated_date)
VALUES
(1, 1, 'FOO-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(2, 1, 'FOO-001', 'Province 01', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(3, 1, 'FOO-002', 'Province 02', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00');

-- dummy data
-- note that we need an "Unspecified" for every Admin1, including the unspecified one
INSERT INTO admin2 (id, admin1_ref, code, name, is_unspecified, reference_period_start, reference_period_end, hapi_updated_date)
VALUES
(1, 1, 'FOO-XXX-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(2, 2, 'FOO-001-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(3, 3, 'FOO-002-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(4, 2, 'FOO-001-A', 'District A', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(5, 2, 'FOO-001-B', 'District B', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(6, 3, 'FOO-002-C', 'District C', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00'),
(7, 3, 'FOO-002-D', 'District D', FALSE, '2023-01-01 00:00:00', NULL, '2023-01-01 00:00:00');


-- may be OK for production
INSERT INTO gender (code, description) VALUES
('f', 'female'),
('m', 'male'),
('x', 'non-binary');

-- will likely include more buckets for production
INSERT INTO age_range (code, age_min, age_max) VALUES
('0-4', 0, 4),
('5-9', 5, 9),
('10-14', 10, 14),
('15-19', 15, 19),
('20-24', 20, 24),
('25-29', 25, 29),
('30-34', 30, 34),
('35-39', 35, 39),
('40-44', 40, 44),
('45-49', 45, 49),
('50-54', 50, 54),
('55-59', 55, 59),
('60-64', 60, 64),
('65-69', 65, 69),
('70-74', 70, 74),
('75-79', 75, 79),
('80+', 80, NULL);

-- end

-- ---------------------------------------------------------------------
-- Sample data for the operational presence table.
--
-- Started 2023-08-09
--
-- Note: we add explicit IDs here to simply cross referencing, but in
-- production we'll let the database generate them automatically.
--
-- Depends on core-data.sql
-- ------------------------------------------------------------------------

INSERT INTO operational_presence (id, resource_ref, org_ref, sector_code, admin2_ref, reference_period_start, reference_period_end, source_data)
VALUES
(1, 1, 1, 'SHL', 2, '2023-01-01 00:00:00', NULL, 'DATA,DATA,DATA'),
(2, 1, 2, 'FSC', 4, '2023-01-01 00:00:00', NULL, 'DATA,DATA,DATA'),
(3, 1, 3, 'WSH', 4, '2023-01-01 00:00:00', NULL, 'DATA,DATA,DATA'),
(4, 1, 3, 'HEA', 6, '2023-01-01 00:00:00', NULL, 'DATA,DATA,DATA'),
(5, 1, 2, 'WSH', 1, '2023-01-01 00:00:00', NULL, 'DATA,DATA,DATA');

-- end


-- ---------------------------------------------------------------------
-- Sample data for the baseline population table.
--
-- Started 2023-08-09
--
-- Note: we add explicit IDs here to simply cross referencing, but in
-- production we'll let the database generate them automatically.
--
-- Depends on core-data.sql
-- ------------------------------------------------------------------------

INSERT INTO population (id, resource_ref, admin2_ref, gender_code, age_range_code, population, reference_period_start, reference_period_end, source_data)
VALUES
(1, 1, 1, 'x', '10-14', 1000000, '2023-01-01 00:00:00', '2023-06-30 00:00:00', 'DATA,DATA,DATA'),       -- total national
(2, 1, 1, 'f', '25-29', 500001, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),         -- national (f), all ages
(3, 1, 1, 'm', '10-14', 489999, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),         -- national (f), all ages
(4, 1, 1, 'x', '25-29', 9999, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),           -- national (x), all ages
(5, 1, 1, 'f', '0-4', 300000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),   -- national (f) children
(6, 1, 2, 'x', '5-9', 2000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),  -- admin1 (x) adolescents
(7, 1, 4, 'm', '10-14', 100000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA');    -- admin2 (m) elderly
-- end


-- ---------------------------------------------------------------------
-- Sample data for the national_risk table.
--
-- Started 2024-02-20
--
-- ------------------------------------------------------------------------

INSERT INTO public.national_risk (id, resource_ref, admin2_ref, risk_class, global_rank, overall_risk, hazard_exposure_risk, vulnerability_risk, coping_capacity_risk, meta_missing_indicators_pct, meta_avg_recentness_years, reference_period_start, reference_period_end, source_data) VALUES (1, 1, 1, 5, 4, 8.1, 8.7, 8.5, 7.1, 0.0784313725490196, 0.2571428571428571, '2024-01-01 00:00:00', '2024-12-31 23:59:59.999999', 'not yet implemented');
INSERT INTO public.national_risk (id, resource_ref, admin2_ref, risk_class, global_rank, overall_risk, hazard_exposure_risk, vulnerability_risk, coping_capacity_risk, meta_missing_indicators_pct, meta_avg_recentness_years, reference_period_start, reference_period_end, source_data) VALUES (2, 2, 2, 5, 12, 7, 6.9, 7.9, 6.4, 0, 0.3013698630136986, '2024-01-01 00:00:00', '2024-12-31 23:59:59.999999', 'not yet implemented');
INSERT INTO public.national_risk (id, resource_ref, admin2_ref, risk_class, global_rank, overall_risk, hazard_exposure_risk, vulnerability_risk, coping_capacity_risk, meta_missing_indicators_pct, meta_avg_recentness_years, reference_period_start, reference_period_end, source_data) VALUES (3, 3, 3, 4, 19, 6.6, 7.2, 6.8, 5.9, 0, 0.3918918918918919, '2024-01-01 00:00:00', '2024-12-31 23:59:59.999999', 'not yet implemented');

-- end


-- ---------------------------------------------------------------------
-- Sample data for the ipc_phase, ipc_type and food_security tables.
--
-- Started 2024-02-19
--
-- ------------------------------------------------------------------------

INSERT INTO public.ipc_phase (code, name, description) VALUES ('1', 'Phase 1: None/Minimal', 'Households are able to meet essential food and non-food needs without engaging in atypical and unsustainable strategies to access food and income.');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('2', 'Phase 2: Stressed', 'Households have minimally adequate food consumption but are unable to afford some essential non-food expenditures without engaging in stress-coping strategies.');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('3', 'Phase 3: Crisis', 'Households either have food consumption gaps that are reflected by high or above-usual acute malnutrition, or are marginally able to meet minimum food needs but only by depleting essential livelihood assets or through crisis-coping strategies.');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('4', 'Phase 4: Emergency', 'Households either have large food consumption gaps which are reflected in very high acute malnutrition and excess mortality, or are able to mitigate large food consumption gaps but only by employing emergency livelihood strategies and asset liquidation.');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('5', 'Phase 5: Catastrophe/Famine', 'Households have an extreme lack of food and/or other basic needs even after full employment of coping strategies. Starvation, death, destitution and extremely critical acute malnutrition levels are evident. (For Famine Classification, an area needs to have extreme critical levels of acute malnutrition and mortality.)');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('3+', 'Phase 3+: In Need of Action', 'Sum of population in phases 3, 4, and 5. The population in Phase 3+ does not necessarily reflect the full population in need of urgent action. This is because some households may be in Phase 2 or even 1 but only because of receipt of assistance, and thus, they may be in need of continued action.');
INSERT INTO public.ipc_phase (code, name, description) VALUES ('all', 'Phases 1, 2, 3, 4, and 5', 'Sum of population in phases 1, 2, 3, 4, and 5. Used as the denominator to determine the fraction of population per phase.');

INSERT INTO public.ipc_type (code, description) VALUES ('current', 'Food insecurity that is occurring in the current analysis period.');
INSERT INTO public.ipc_type (code, description) VALUES ('first projection', 'Projected food insecurity occurring in the period immediately following the current analysis period.');
INSERT INTO public.ipc_type (code, description) VALUES ('second projection', 'Projected food insecurity occurring in the period immediately following the first projection period.');

INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (1, 1, 1, '1', 'current', 49348, 0.8399945530060597, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (2, 1, 1, '2', 'current', 8225, 0.1400047661196977, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (3, 1, 1, '3', 'current', 1175, 0.02000068087424253, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (4, 1, 1, '4', 'current', 0, 0, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (5, 1, 1, '5', 'current', 0, 0, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (6, 1, 1, '3+', 'current', 1175, 0.02000068087424253, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (7, 1, 1, 'all', 'current', 58748, 1, '2021-01-01 00:00:00', '2021-05-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (8, 1, 2, '1', 'first projection', 47586, 0.8100020426227276, '2021-06-01 00:00:00', '2021-08-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (9, 1, 2, '2', 'first projection', 9400, 0.16000544699394023, '2021-06-01 00:00:00', '2021-08-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (10, 1, 4, '3', 'first projection', 1762, 0.0299925103833322, '2021-06-01 00:00:00', '2021-08-31 00:00:00', 'not yet implemented');
INSERT INTO public.food_security (id, resource_ref, admin2_ref, ipc_phase_code, ipc_type_code, population_in_phase, population_fraction_in_phase, reference_period_start, reference_period_end, source_data) VALUES (11, 1, 4, '4', 'first projection', 0, 0, '2021-06-01 00:00:00', '2021-08-31 00:00:00', 'not yet implemented');

-- end


-- ---------------------------------------------------------------------
-- Sample data for the population_group table.
--
-- Started 2024-02-23
--
-- ------------------------------------------------------------------------

INSERT INTO public.population_group(code, description) VALUES ('refugees', 'refugees');

-- end


-- ---------------------------------------------------------------------
-- Sample data for the population_status table.
--
-- Started 2024-02-23
--
-- ------------------------------------------------------------------------

INSERT INTO public.population_status(code, description) VALUES ('inneed', 'number of people in need');

-- end


-- ---------------------------------------------------------------------
-- Sample data for the humanitarian_needs table.
--
-- Started 2024-02-23
--
-- ------------------------------------------------------------------------

INSERT INTO public.humanitarian_needs (id, resource_ref, admin2_ref, population_status_code, population_group_code, sector_code, gender_code, age_range_code, disabled_marker, population, reference_period_start, reference_period_end, source_data) VALUES (1, 1, 1, 'inneed', 'refugees', 'EDU', 'm', '0-4', FALSE, 100, '2017-01-01 00:00:00', '2024-12-31 23:59:59', 'not yet implemented');
INSERT INTO public.humanitarian_needs (id, resource_ref, admin2_ref, population_status_code, population_group_code, sector_code, gender_code, age_range_code, disabled_marker, population, reference_period_start, reference_period_end, source_data) VALUES (2, 2, 2, 'inneed', 'refugees', 'EDU', 'f', '0-4', TRUE, 200, '2017-01-01 00:00:00', '2024-12-31 23:59:59', 'not yet implemented');
INSERT INTO public.humanitarian_needs (id, resource_ref, admin2_ref, population_status_code, population_group_code, sector_code, gender_code, age_range_code, disabled_marker, population, reference_period_start, reference_period_end, source_data) VALUES (3, 3, 4, 'inneed', 'refugees', NULL, NULL, '80+', NULL, 300, '2017-01-01 00:00:00', '2024-12-31 23:59:59', 'not yet implemented');

-- end