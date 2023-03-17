-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows
    FROM tv_show_genres
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    GROUP BY tv_genres.name
    ORDER BY number_of_shows DESC
