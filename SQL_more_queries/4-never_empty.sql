-- 4-never_empty.sql

USE hbtn_0d_2;

-- Create the id_not_null table if it does not exist
CREATE TABLE IF NOT EXISTS `id_not_null` (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256)
);

-- Insert sample data
INSERT INTO `id_not_null` (`id`, `name`) VALUES (89, 'Best School');

-- Display the contents of the id_not_null table
SELECT * FROM `id_not_null`;

