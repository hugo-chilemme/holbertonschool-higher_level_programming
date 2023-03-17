-- Write a script that creates the table force_name on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id int AUTO_INCREMENT UNIQUE,
    name varchar(256) NOT NULL,
    PRIMARY KEY(id)
);
