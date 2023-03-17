-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id AS id, cities.name AS name, states.name AS name 
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    ORDER BY cities.id
