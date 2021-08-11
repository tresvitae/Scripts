!#/bin/bash

# the sed tool edits the build configuration in the data.xml file to create the build configuration in the Archive Project.
sed -i 's/projectName="[a-zA-Z0-9,.!?_ -]*" projectId/projectName="Archive" projectId/' data.xml
sed -i 's/projectId="[a-zA-Z0-9,.!?_ -]*" href=/projectId="Archive" href=/' data.xml
sed -i 's/project id="[a-zA-Z0-9,.!?_ -]*" name/project id="Archive" name/' data.xml
sed -i 's/Archive" name="[a-zA-Z0-9,.!?_ -]*" parentProjectId=/Archive" name="Archive" parentProjectId=/' data.xml
sed -i 's/html?projectId=[a-zA-Z0-9,.!?_ -]*"\/>/html?projectId=Archive"\/>/' data.xml

# clean xml from VCS
#  's/<vcs-root-entries count[a-zA-Z0-9,.!?"/=_ -]*</vcs-root-entries>//' data.xml

sleep 1