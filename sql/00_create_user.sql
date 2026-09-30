-- Run ONCE as SYSTEM, connected to FREEPDB1 (Oracle SQL Developer).
-- Creates a dedicated schema so the project is isolated from the HR sample schema.
CREATE USER funnel_prj IDENTIFIED BY "Funnel_Pass1"
  DEFAULT TABLESPACE users
  QUOTA UNLIMITED ON users;

GRANT CREATE SESSION, CREATE TABLE, CREATE VIEW, CREATE SEQUENCE TO funnel_prj;
-- Then create a new SQL Developer connection as FUNNEL (same host/port, service FREEPDB1)
-- and run 01_schema_oracle.sql there.
