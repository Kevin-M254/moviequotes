-- this script prepares a MySQL server for the project
-- create project testing database with the name : mq_test_db
CREATE DATABASE IF NOT EXISTS mq_test_db;
-- creating new user
CREATE USER IF NOT EXISTS 'mq_test'@'localhost' IDENTIFIED BY 'mq_test_pwd';
-- granting privileges
GRANT SELECT ON perfomance_schema.* TO 'mq_test'@'localhost';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'mq_test'@'localhost';
FLUSH PRIVILEGES;
