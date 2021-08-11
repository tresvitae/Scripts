#!/bin/bash

function backup {
    # -z to check whether positional parameter $1 contains any value. Return true if length of string is zero.
    if [ -z $1 ]; then
        user=$(whoami)
    else
    # -d to check if user's home dir exists.
        if [ ! -d "/home/$1" ]; then
            echo "Requested $1 user home directory doesn't exist."
            exit 1
        fi
        user=$1
    fi

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

    # Output message.
    echo "########## $user ##########"
    echo "Files to be included: $src_files"
    echo "Directories to be included: $src_dir"
    echo "Files archived: $arch_files"
    echo "Directories archived: $arch_dir"

    # Sanity check of number of files and dirs within user's home dir before and after the backup command.
    if [ $src_files -eq $arch_files ]; then
        echo "Backup of $input completed! Details: "
        ls -l $output
    else
        echo "Backup of $input failed!"
    fi
}

# Multiply backup for all supplied users as an argument.
for directory in $*; do
    backup $directory
    let all=$all+$arch_files+$arch_dir
done;
    echo "Total files and directories: $all"

