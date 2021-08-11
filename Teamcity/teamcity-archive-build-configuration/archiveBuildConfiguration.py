#! /usr/bin/python3

import subprocess
import requests
from requests.api import delete, head, request
import urllib3
import xml.dom.minidom as minidom

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TC_SERVER_URL = 'https://dev-teamcity.saas.amherst.com'
TC_TOKEN = '' # Your Token

headers = {
    'Authorization' : 'Bearer {}'.format(TC_TOKEN)
    }

def append_new_line(file_name, text_to_append):
    # Append given text as a new line at the end of file
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n' and append text at the end of file
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

def createBackup():
    with open('archive.txt', 'r') as read:
        Lines = read.readlines()
        for build_id in Lines:
            get_bc = requests.get(TC_SERVER_URL + "/app/rest/buildTypes/{}".format(build_id.strip()), verify=False, headers=headers)
            # Saving backup of BC
            append_new_line('backup.txt', get_bc.text)
    print ("All Build Configurations data has been saved in backup.txt file.")

def saveIt(text):
    with open("data.xml", "w") as save:
        save.write(text)

def main():
    print(TC_SERVER_URL)

    createBackup()
    
    # get Build Configuration
    with open('archive.txt', 'r') as read:
        Lines = read.readlines()
        for build_id in Lines:
            get_bc = requests.get(TC_SERVER_URL + "/app/rest/buildTypes/{}".format(build_id.strip()), verify=False, headers=headers)
            saveIt(get_bc.text)

            # Get id of attached VCS from Build Conf
            doc = minidom.parse('data.xml')
            try:
                memory = doc.getElementsByTagName('vcs-root-entry')[0]
            except IndexError:
                continue
            
            # deleteVcsRoot from Build Configuration
            vcs_locator = memory.getAttribute('id')
            print("{} is VCS id which going to be detached from {} BC.".format(vcs_locator, build_id.strip()))
            delete_vcs = requests.delete(TC_SERVER_URL + "/app/rest/buildTypes/{}/vcs-root-entries/{}".format(build_id.strip(), vcs_locator), verify=False, headers=headers)
            print("{}. VCS {} has been deleted from BC: {}. Now, it going to get cleaned BC parameters to recreate it in Archive Project.".format(delete_vcs, vcs_locator, build_id.strip()))
            
            # get Build Configuration without VCS
            get_clean_bc = requests.get(TC_SERVER_URL + "/app/rest/buildTypes/{}".format(build_id.strip()), verify=False, headers=headers)
            saveIt(get_clean_bc.text)

            # Change parameters of project id&name to "Archive"
            subprocess.call("sed.sh", shell=True)

            # delete Build Configuration
            delete_build_type = requests.delete(TC_SERVER_URL + "/app/rest/buildTypes/{}".format(build_id.strip()), verify=False, headers=headers)
            print("{}. Build Configuration: {} has beed deleted.".format(delete_build_type, build_id.strip()))
            # Read XML
            with open('data.xml', 'r') as r:
                data = r.read()
            # create Build Configuration
            headers['Content-Type'] = 'application/xml'
            response2 = requests.post(TC_SERVER_URL + "/app/rest/buildTypes", data=data, headers=headers, verify=False)
            print("{}. Build Configuration: {} has been recreated in Archive Project.".format(response2, build_id.strip()))
            print('\n')

if __name__ == "__main__":
    main()