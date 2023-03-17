-- Write a script that creates the table force_name on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256),
);
