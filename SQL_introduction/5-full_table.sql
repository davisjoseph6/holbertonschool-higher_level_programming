-- File: 5-full_table.sql

-- Check if the database exists
USE information_schema;
SELECT SCHEMA_NAME
FROM SCHEMATA
WHERE SCHEMA_NAME = 'hbtn_0c_0';

-- Switch to the specified database
USE hbtn_0c_0;

-- Retrieve table information
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table';
