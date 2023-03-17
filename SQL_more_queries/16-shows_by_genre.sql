-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY tv_shows.title ASC, tv_genres.name ASC;
