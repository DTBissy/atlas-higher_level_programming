-- Creates cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INT NOT NULL FOREIGN KEY(id, states),
    name VARCHAR(256) NOT NULL
);
