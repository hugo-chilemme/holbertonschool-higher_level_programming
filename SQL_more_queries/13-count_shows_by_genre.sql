-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
    FROM tv_genres 
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
    GROUP BY number_of_shows
    ORDER BY number_of_shows DESC
