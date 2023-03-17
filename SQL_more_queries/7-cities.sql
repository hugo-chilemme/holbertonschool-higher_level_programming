-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id int AUTO_INCREMENT UNIQUE NOT NULL,
    state_id int NOT NULL,
    name varchar(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

