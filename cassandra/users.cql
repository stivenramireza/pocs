CREATE KEYSPACE k1 WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE k1;
CREATE TABLE users (user_name varchar, password varchar, gender varchar, PRIMARY KEY (user_name));
INSERT INTO users (user_name, password, gender) VALUES ('John', 'test123', 'male');
SELECT * from users;