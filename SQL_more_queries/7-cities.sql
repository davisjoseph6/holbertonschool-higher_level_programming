-- Create the table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
