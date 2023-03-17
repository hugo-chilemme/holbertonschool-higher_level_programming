-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id AS id, states.name AS name, cities.name AS name 
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
