-- Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
use hbtn_0c_0;
DESC first_table;
SELECT column_name, column_type, is_nullable, column_key, column_default, extra 
    FROM information_schema.columns 
    WHERE table_schema='$db_name' AND table_name='first_table';
