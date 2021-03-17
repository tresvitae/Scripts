#!/bin/bash

user=$(whoami)
input=/home/$user
output=/tmp/${user}_home_$(date +%Y-%m-%d_%H%M%S).tar.gz

# Reports a total number of files for a given directory.
function total_files {
    find $1 -type f | wc -l
}

function total_dir {
    find $1 -type d | wc -l
}

tar -czf $output $input 2> /dev/null

# Output message.
echo -n "Files to be included: "
total_files

echo -n "Directories to be included: "
total_dir

echo "Backup of $input completed! Details: "
ls -l $output