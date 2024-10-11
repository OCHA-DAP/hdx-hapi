-- dummy data

INSERT INTO population (resource_hdx_id,admin2_ref,provider_admin1_name,provider_admin2_name,gender,age_range,min_age,max_age,population,reference_period_start,reference_period_end) VALUES
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',1,'Provider admin1 name 1','Provider admin2 name 1','x','10-14',10,14,1000000,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',1,'Provider admin1 name 1','Provider admin2 name 1','f','25-29',25,25,500001,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',1,'Provider admin1 name 1','Provider admin2 name 1','m','10-14',10,14,489999,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',1,'Provider admin1 name 1','Provider admin2 name 1','x','25-29',25,29,9999,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',1,'Provider admin1 name 1','Provider admin2 name 1','f','0-4',0,4,300000,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',2,'Provider admin1 name 2','Provider admin2 name 2','x','5-9',5,9,2000,'2023-01-01 00:00:00','2023-06-30 00:00:00'),
	 ('17acb541-9431-409a-80a8-50eda7e8ebab',4,'Provider admin1 name 4','Provider admin2 name 4','m','10-14',10,14,100000,'2023-01-01 00:00:00','2023-06-30 00:00:00');

-- INSERT INTO population (id, resource_ref, admin2_ref, gender_code, age_range_code, population, reference_period_start, reference_period_end, source_data)
-- VALUES
-- (1, 1, 1, 'x', '10-14', 1000000, '2023-01-01 00:00:00', '2023-06-30 00:00:00', 'DATA,DATA,DATA'),       -- total national
-- (2, 1, 1, 'f', '25-29', 500001, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),         -- national (f), all ages
-- (3, 1, 1, 'm', '10-14', 489999, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),         -- national (f), all ages
-- (4, 1, 1, 'x', '25-29', 9999, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),           -- national (x), all ages
-- (5, 1, 1, 'f', '0-4', 300000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),   -- national (f) children
-- (6, 1, 2, 'x', '5-9', 2000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA'),  -- admin1 (x) adolescents
-- (7, 1, 4, 'm', '10-14', 100000, '2023-01-01 00:00:00',  '2023-06-30 00:00:00','DATA,DATA,DATA');    -- admin2 (m) elderly

-- -- end
