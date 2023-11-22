-- Assuming the name field is unique, we can use it to identify

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
