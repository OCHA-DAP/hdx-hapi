-- ----------------------------------------------------------------------
-- Views for core data types
--
-- Started 2023-08-09
--
-- On the API end, we will always reference the views rather than the
-- tables, to insulate us from changes in the underlying structure.
-- That's why there are views even for tables that have no joins.
-- ---------------------------------------------------------------------

DROP VIEW IF EXISTS dataset_view;

CREATE VIEW dataset_view AS
SELECT D.*
FROM dataset D;


DROP VIEW IF EXISTS resource_view;

CREATE VIEW resource_view AS
SELECT R.*,
       D.hdx_id AS dataset_hdx_id,
       D.hdx_stub AS dataset_hdx_stub, 
       D.title AS dataset_title,
       D.provider_code AS dataset_provider_code,
       D.provider_name AS dataset_provider_name
FROM resource R
LEFT JOIN dataset D ON R.dataset_ref=D.id;


DROP VIEW IF EXISTS sector_view;

CREATE VIEW sector_view AS
SELECT S.*
FROM sector S;


DROP VIEW IF EXISTS org_type_view;

CREATE VIEW org_type_view AS
SELECT OT.*
FROM org_type OT;


DROP VIEW IF EXISTS org_view;

CREATE VIEW org_view AS
SELECT O.*, OT.description AS org_type_description
FROM org O
LEFT JOIN org_type OT ON O.org_type_code=OT.code;


DROP VIEW IF EXISTS admin2_view;

CREATE VIEW admin2_view AS
SELECT ADM2.*,
       ADM1.code AS admin1_code,
       ADM1.name AS admin1_name,
       ADM1.is_unspecified AS admin1_is_unspecified,
       ADM1.reference_period_start AS admin1_reference_period_start,
       ADM1.reference_period_end AS admin1_reference_period_end,
       LOC.code AS location_code,
       LOC.name AS location_name,
       LOC.reference_period_start AS location_reference_period_start,
       LOC.reference_period_end AS location_reference_period_end
FROM admin2 ADM2
LEFT JOIN admin1 ADM1 ON ADM2.admin1_ref=ADM1.id
LEFT JOIN location LOC ON ADM1.location_ref=LOC.id;


DROP VIEW IF EXISTS admin1_view;

CREATE VIEW admin1_view AS
SELECT ADM1.*,
       LOC.code AS location_code,
       LOC.name AS location_name,
       LOC.reference_period_start AS location_reference_period_start,
       LOC.reference_period_end AS location_reference_period_end
FROM admin1 ADM1
LEFT JOIN location LOC ON ADM1.location_ref=LOC.id;


DROP VIEW IF EXISTS location_view;

CREATE VIEW location_view AS
SELECT LOC.*
FROM location LOC;


DROP VIEW IF EXISTS gender_view;

CREATE VIEW gender_view AS
SELECT G.*
FROM gender G;


DROP VIEW IF EXISTS age_range_view;

CREATE VIEW age_range_view AS
SELECT AR.*
FROM age_range AR;

-- end

-- ---------------------------------------------------------------------
-- Denormalised operation presence (3W) view for HAPI
--
-- Started 2023-08-09
--
-- Depends on hapi-core-tables.sql and hapi-op-tables.sql
-- ---------------------------------------------------------------------

DROP VIEW IF EXISTS operational_presence_view;

CREATE VIEW operational_presence_view AS
SELECT OP.*,
       D.hdx_id AS dataset_hdx_id,
       D.hdx_stub as dataset_hdx_stub,
       D.title AS dataset_title,
       D.provider_code AS dataset_provider_code,
       D.provider_name AS dataset_provider_name,
       R.hdx_id AS resource_hdx_id,
       R.filename AS resource_filename,
       R.update_date AS resource_update_date,
       O.acronym AS org_acronym,
       O.name AS org_name,
       O.org_type_code AS org_type_code,
       OT.description AS org_type_description,
       S.name AS sector_name,
       LOC.code AS location_code,
       LOC.name AS location_name,
       ADM1.code AS admin1_code,
       ADM1.name AS admin1_name,
       ADM1.is_unspecified AS admin1_is_unspecified,
       ADM2.code AS admin2_code,
       ADM2.name AS admin2_name,
       ADM2.is_unspecified AS admin2_is_unspecified
FROM operational_presence OP
LEFT JOIN resource R ON OP.resource_ref=R.id
LEFT JOIN dataset D ON R.dataset_ref=D.id
LEFT JOIN org O ON OP.org_ref=O.id
LEFT JOIN org_type OT ON O.org_type_code=OT.code
LEFT JOIN sector S ON OP.sector_code=S.code
LEFT JOIN admin2 ADM2 ON OP.admin2_ref=ADM2.id
LEFT JOIN admin1 ADM1 ON ADM2.admin1_ref=ADM1.id
LEFT JOIN location LOC ON ADM1.location_ref=LOC.id;

-- ---------------------------------------------------------------------
-- Denormalised baseline-population view for HAPI
--
-- Started 2023-08-09
--
-- Depends on hapi-core-tables.sql and hapi-pop-tables.sql
-- ---------------------------------------------------------------------

DROP VIEW IF EXISTS population_view;

CREATE VIEW population_view AS
SELECT POP.*,
       D.hdx_id AS dataset_hdx_id,
       D.hdx_stub as dataset_hdx_stub,
       D.title AS dataset_title,
       D.provider_code AS dataset_provider_code,
       D.provider_name AS dataset_provider_name,
       R.hdx_id AS resource_hdx_id,
       R.filename AS resource_filename,
       R.update_date AS resource_update_date,
       G.description AS gender_description,
       LOC.code AS location_code,
       LOC.name AS location_name,
       ADM1.code AS admin1_code,
       ADM1.name AS admin1_name,
       ADM1.is_unspecified AS admin1_is_unspecified,
       ADM2.code AS admin2_code,
       ADM2.name AS admin2_name,
       ADM2.is_unspecified AS admin2_is_unspecified
FROM population POP
LEFT JOIN resource R ON POP.resource_ref=R.id
LEFT JOIN dataset D ON R.dataset_ref=D.id
LEFT JOIN gender G ON POP.gender_code=G.code
LEFT JOIN age_range AR ON POP.age_range_code=AR.code
LEFT JOIN admin2 ADM2 ON POP.admin2_ref=ADM2.id
LEFT JOIN admin1 ADM1 ON ADM2.admin1_ref=ADM1.id
LEFT JOIN location LOC ON ADM1.location_ref=LOC.id;

-- end