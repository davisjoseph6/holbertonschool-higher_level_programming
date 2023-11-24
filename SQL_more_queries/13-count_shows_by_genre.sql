-- 13-count_shows_by_genre.sql

SELECT genre, COUNT(*) as number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
