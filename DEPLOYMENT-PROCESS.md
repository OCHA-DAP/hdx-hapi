# HAPI COMPONENTS
-----------------
1) HAPI-SCHEMA release 0.8.17

2) HAPI-PIPELINES plays dev role: `main` branch is for (code) -> `db-export` branch (CSV daily depends on HAPI-SCHEMA release 0.8.17)

3) HAPI-PIPELINES-PROD plays prod role: `main` (code) <- PRs from HAPI-PIPELINES
    -> `db-export`  (CSV daily depends on HAPI-SCHEMA release 0.8.17)

4) HWA 0.0.7 depends on HAPI-SCHEMA
    -> imports `db-export`  (CSV daily depends on HAPI-SCHEMA release 0.8.17) from HAPI-PIPELINES-PROD / HAPI-PIPELINES -> postgres

5) HAPI API 0.7.0 depends on HAPI-SCHEMA release 0.8.17
    serves data from postgres
    
6) HAPI SMOKE TESTS depend on endpoint schema, which in turn, depends on HAPI SCHEMA
    

# PROCESS:
----------
1) HAPI-SCHEMA has a new release ( ex: deletes a column from an existing table, adds a new table ), 0.9.0
2) HAPI-PIPELINES use HAPI-SCHEMA 0.9.0 -> produces 0.9.0 CSVs
3) [Ticket] HAPI API to use new 0.9.0 HAPI-SCHEMA 
4) [Ticket] HWA to use new 0.9.0 HAPI-SCHEMA. Special care need to be taken when creating **alembic revisions**
   - *Enum changes* are not automatically detected by alembic
   - `nullable=False` constraints can pose problems with existing data
   - changes to primary keys can pose problems to existing data
  
    **NOTE**: 3 and 4 can be implemented in parallel
5) Deploy on dev server:
   - Deploy [dev] HWA
   - Run in parallel:
     - Run HWA ingest
     - Deploy [dev] HAPI
- Manual Testing
1) [Ticket] HAPI SMOKE TESTS update 
2) Test HAPI SMOKE TESTS run successfully on dev server
3) HWA new version 0.0.8
   - make sure to check for enum changes when creating alembic patch
4) HAPI API new version 0.8.0
5)  PR from HAPI-PIPELINES to HAPI-PIPELINES-PROD -> generate new 0.9.0 CSVs
6)  Deploy on prod server:
    - Deploy [0.0.8] HWA
    - Run in parallel:
        - Run HWA ingest
        - Deploy [0.8.0] HAPI
    - Manual Testing 
    - Run smoke tests on prod


IDEAS FOR A BRIGHTER FUTURE:
----------------------------
- HWA to create a new postgres schema for each new HAPI SCHEMA release
- Stop using postgres, use something that supports faceting out of the box (solr, elastic, mongo)