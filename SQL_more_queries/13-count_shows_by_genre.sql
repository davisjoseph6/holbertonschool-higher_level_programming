-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_genres.name 'genre', COUNT(tv_show_genres.show_id) 'number_of_shows'

-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>

FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

-- Results are sorted in descending order by the number of shows linked

GROUP BY genre
ORDER BY number_of_shows DESC;
