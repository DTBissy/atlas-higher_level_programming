-- Creates user and database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS user_02_d@localhost IDENTIFIED BY user_0d_2_pwd;

GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;