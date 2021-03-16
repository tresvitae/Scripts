#!/bin/sh

echo "Enter new group name:"
read GROUP_NAME
while grep -q $GROUP_NAME /etc/group
  do
      echo "This group already exists. Please type again:"
      read GROUP_NAME
  done
groupadd $GROUP_NAME
echo "Group created successfuly!"
