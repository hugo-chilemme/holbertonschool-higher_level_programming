-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id AS id, cities.name AS name FROM states 
    INNER JOIN cities ON cities.state_id = states.id 
    WHERE states.name = "California"
