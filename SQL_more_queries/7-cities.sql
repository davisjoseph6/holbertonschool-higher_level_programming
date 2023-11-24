-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY,
	-- Add other columns as needed
);

-- Create the table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
