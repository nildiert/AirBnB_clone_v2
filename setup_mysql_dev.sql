-- Create a database if not exist
-- A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbtn_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
DROP USER 'hbnb_dev'@'localhost';
