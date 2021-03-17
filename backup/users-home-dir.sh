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

function total_arch_files {
    tar -tzf $1 | grep -v /$ | wc -l
}

function total_arch_dir {
    tar -tzf $1 | grep /$ | wc -l
}

tar -czf $output $input 2> /dev/null

src_files=$( total_files $input )
arch_files=$( total_arch_files $output )

src_dir=$( total_dir $input )
arch_dir=$( total_arch_dir $output )

echo "Files to be included: $src_files"
echo "Directories to be included: $src_dir"
echo "Files archived: $arch_files"
echo "Directories archived: $arch_dir"

# Output message.
echo -n "Files to be included: "
total_files

echo -n "Directories to be included: "
total_dir


# Sanity check of number of files and dirs within user's home dir before and after the backup command.
if [ $src_files -eq $arch_files ]; then
    echo "Backup of $input completed! Details: "
    ls -l $output
else
    echo "Backup of $input failed!"
fi
