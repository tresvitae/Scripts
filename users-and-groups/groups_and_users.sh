#!/bin/sh

echo -n "Enter new group name: \n"
read GROUP_NAME
while grep -q $GROUP_NAME /etc/group
  do
    echo "This group already exists. Please type again:"
    read GROUP_NAME
  done
groupadd $GROUP_NAME
echo "Group created successfully!"

# Setting new user account
echo -n "Enter a username name for the new user: \n"
read USER_NAME

getent passwd $USER_NAME >> /dev/null

while [ $? -eq 0 ]
  do
    echo -n "User aleady exists!\nPlease type another one: "
    read USER_NAME
    getent passwd $USER_NAME >> /dev/null
  done

useradd -m -s /bin/bash -g $GROUP_NAME $USER_NAME
passwd $USER_NAME

echo "New user created successfully!\n"

# Creating directory for new user with sticky bit privilege
mkdir /$USER_NAME
chown $USER_NAME.$GROUP_NAME /$USER_NAME
chmod 1770 /$USER_NAME