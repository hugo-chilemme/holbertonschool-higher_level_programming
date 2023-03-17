-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title, tv_genres.name
    FROM tv_show_genres
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    ORDER BY tv_shows.title ASC, tv_genres.name ASC;
