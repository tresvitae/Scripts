# Simple backup

`$ sudo ./users-home-dir.sh`
or `$ sudo ./users-home-dir.sh USER_NAME`

### Case Scenario
Creating a simple backup of user's home directory.

### Objectives
Create a bash script to perform user management tasks as outlined below:

    - Using tar command with various options -czf in order to create a compressed tar ball of entire user home directory /home/linuxconfig/
    - Eliminate stderr message
    - Two functions to report a number of directories and files
    - Add conditional statements to implement a sanity check to compare the number of files and directories within a source directory before and after the backup command
    - Select a system user for backup. By default the scrip will backup a current user's home directory


Source: https://linuxconfig.org/bash-scripting-tutorial-for-beginners