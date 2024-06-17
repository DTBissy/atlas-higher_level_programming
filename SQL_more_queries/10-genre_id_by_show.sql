-- Shows all shows with a genre link
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv.shows.title ASC, tv_shows_genres.show_id ASC;