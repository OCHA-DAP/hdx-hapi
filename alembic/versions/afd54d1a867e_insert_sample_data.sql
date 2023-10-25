-- ---------------------------------------------------------------------
-- Dummy core data for testing.
--
-- Note: we add explicit IDs here to simply cross referencing, but in
-- production we'll let the database generate them automatically.
--
-- Started 2023-08-09
-- ---------------------------------------------------------------------

INSERT INTO dataset (id, hdx_id, hdx_stub, title, hdx_provider_stub, provider_name)
VALUES
(1, 'c3f001fa-b45b-464c-9460-1ca79fd39b40', 'dataset01', 'Dataset #1', 'provider01', 'Provider #1'),
(2, '7cf3cec8-dbbc-4c96-9762-1464cd0bff75', 'dataset02', 'Dataset #2', 'provider02', 'Provider #2');

INSERT INTO resource (id, dataset_ref, hdx_id, name, format, update_date, download_url, is_hxl)
VALUES
(1, 1, '90deb235-1bf5-4bae-b231-3393222c2d01', 'resource-01.csv', 'csv', '2023-06-01 00:00:00',
'https://data.humdata.org/dataset/c3f001fa-b45b-464c-9460-1ca79fd39b40/resource/90deb235-1bf5-4bae-b231-3393222c2d01/download/resource-01.csv',
 TRUE),
(2, 1, 'b9e438e0-b68a-49f9-b9a9-68c0f3e93604', 'resource-02.xlsx', 'xlsx', '2023-07-01 00:00:00',
'https://fdw.fews.net/api/tradeflowquantityvaluefacts/?dataset=1845&country=TZ&fields=simple&format=xlsx',
 TRUE),
(3, 2, '62ad6e55-5f5d-4494-854c-4110687e9e25', 'resource-03.csv', 'csv', '2023-08-01 00:00:00',
 'https://data.humdata.org/dataset/7cf3cec8-dbbc-4c96-9762-1464cd0bff75/resource/62ad6e55-5f5d-4494-854c-4110687e9e25/download/resource-03.csv',
 TRUE);

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
INSERT INTO org (id, acronym, name, org_type_code, reference_period_start, reference_period_end) VALUES
(1, 'ORG01', 'Organisation 1', '433', '2023-08-01 00:00:00', NULL),
(2, 'ORG02', 'Organisation 2', '437', '2023-07-01 00:00:00', NULL),
(3, 'ORG03', 'Organisation 3', '447', '2023-06-01 00:00:00', NULL);

-- these are the actual sector codes from
-- https://data.humdata.org/dataset/global-coordination-groups-beta
-- (they won't be sufficient for production; we'll have to add to them)
INSERT INTO sector (code, name, reference_period_start, reference_period_end)
VALUES
('SHL', 'Emergency Shelter and NFI', '2023-01-01 00:00:00', NULL),
('CCM', 'Camp Coordination / Management', '2023-01-01 00:00:00', NULL),
('PRO-MIN', 'Mine Action', '2023-01-01 00:00:00', NULL),
('FSC', 'Food Security', '2023-01-01 00:00:00', NULL),
('WSH', 'Water Sanitation Hygiene', '2023-01-01 00:00:00', NULL),
('LOG', 'Logistics', '2023-01-01 00:00:00', NULL),
('PRO-CPN', 'Child Protection', '2023-01-01 00:00:00', NULL),
('PRO', 'Protection', '2023-01-01 00:00:00', NULL),
('EDU', 'Education', '2023-01-01 00:00:00', NULL),
('NUT', 'Nutrition', '2023-01-01 00:00:00', NULL),
('HEA', 'Health', '2023-01-01 00:00:00', NULL),
('ERY', 'Early Recovery', '2023-01-01 00:00:00', NULL),
('TEL', 'Emergency Telecommunications', '2023-01-01 00:00:00', NULL),
('PRO-GBV', 'Gender Based Violence', '2023-01-01 00:00:00', NULL),
('PRO-HLP', 'Housing, Land and Property', '2023-01-01 00:00:00', NULL);

-- dummy data
INSERT INTO location (id, code, name, reference_period_start, reference_period_end)
VALUES
(1, 'FOO', 'Foolandia', '2023-01-01 00:00:00', NULL);

-- dummy data
INSERT INTO admin1 (id, location_ref, code, name, is_unspecified, reference_period_start, reference_period_end)
VALUES
(1, 1, 'FOO-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL),
(2, 1, 'FOO-001', 'Province 01', FALSE, '2023-01-01 00:00:00', NULL),
(3, 1, 'FOO-002', 'Province 02', FALSE, '2023-01-01 00:00:00', NULL);

-- dummy data
-- note that we need an "Unspecified" for every Admin1, including the unspecified one
INSERT INTO admin2 (id, admin1_ref, code, name, is_unspecified, reference_period_start, reference_period_end)
VALUES
(1, 1, 'FOO-XXX-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL),
(2, 2, 'FOO-001-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL),
(3, 3, 'FOO-002-XXX', 'Unspecified', TRUE, '2023-01-01 00:00:00', NULL),
(4, 2, 'FOO-001-A', 'District A', FALSE, '2023-01-01 00:00:00', NULL),
(5, 2, 'FOO-001-B', 'District B', FALSE, '2023-01-01 00:00:00', NULL),
(6, 3, 'FOO-002-C', 'District C', FALSE, '2023-01-01 00:00:00', NULL),
(7, 3, 'FOO-002-D', 'District D', FALSE, '2023-01-01 00:00:00', NULL);


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