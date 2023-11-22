-- Write a script that lists the number of records 

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
