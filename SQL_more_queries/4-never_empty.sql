-- 4-never_empty.sql

-- Create the id_not_null table if it does not exist
CREATE TABLE IF NOT EXISTS `id_not_null` (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256)
);
