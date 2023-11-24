-- 3-force_name.sql

-- Check if the table exists
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
