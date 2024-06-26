-- Counts genres and lists genres while counting shows linked
SELECT DISTINCT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_of_shows DESC;