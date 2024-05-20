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