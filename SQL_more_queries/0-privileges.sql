# Create user_0d_1
echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# Grant privileges to user_0d_1
echo "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# Create user_0d_2
echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

# Grant privileges to user_0d_2
echo "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER ON *.* TO 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

# List privileges for both users
cat <<EOF | mysql -hlocalhost -uroot -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
EOF
