-- Write a script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
    id int DEFAULT 1,
    name varchar(256),
    PRIMARY KEY (id)
);
