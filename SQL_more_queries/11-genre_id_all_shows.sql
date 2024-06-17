-- Lists all shows contained in the databse
SELECT tv_show.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ASC, tv_show_genres.genre_id;