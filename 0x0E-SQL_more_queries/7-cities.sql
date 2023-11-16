-- SQL Script , creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABSE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
	(id int NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id int NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name varchar(256) NOT NULL
);
