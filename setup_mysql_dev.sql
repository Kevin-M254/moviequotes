-- this script prepares a MySQL server for the project
-- create a project development database with the name : mq_dev_db
CREATE DATABASE hbnb_dev_db;
-- creating new user named : mq_dev with all privileges
-- with the password : mq_dev_pwd
CREATE USER 'mq_dev'@'localhost' IDENTIFIED BY 'mq_dev_pwd';
-- granting all privileges
GRANT ALL PRIVILEGES ON mq_dev_db.* TO 'mq_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting SELECT privilege in the db perfomance_schema
GRANT SELECT ON perfomance_schema.* TO 'mq_dev'@'localhost';
FLUSH PRIVILEGES;
