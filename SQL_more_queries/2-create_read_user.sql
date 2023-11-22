-- Create or use the hbtn_0d_2 databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or use the user_0d_2 user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2 on hbtn_0d_2 databse
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
