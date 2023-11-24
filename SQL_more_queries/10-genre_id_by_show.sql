-- 10-genre_id_by_show.sql

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tv_shows.tv_shows
JOIN hbtn_0d_tv_show.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
