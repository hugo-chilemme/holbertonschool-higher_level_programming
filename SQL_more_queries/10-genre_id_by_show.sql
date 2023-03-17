-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
    FROM tv_shows
    INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_shows.id
    ORDER BY tv_shows.title, tv_show_genres.genre_id

