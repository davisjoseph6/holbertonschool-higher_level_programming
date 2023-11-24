-- 8-cities_of_california_subquery.sql

SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;
