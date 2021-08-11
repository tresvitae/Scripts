#! /usr/bin/python3

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TC_SERVER_URL = 'https://localhost:8111'
TC_TOKEN = '' # Your Token
headers = {
    'Authorization' : 'Bearer {}'.format(TC_TOKEN)
    }

def archiveProject(project_id):
    requests.put(TC_SERVER_URL + "/app/rest/projects/{}/archived".format(project_id), verify=False, data="true", headers=headers)

def main():
    print(TC_SERVER_URL)
    
    # Archiving every project with build configurations and subprojects
    with open('archive.txt', 'r') as read:
        Lines = read.readlines()
        for project_id in Lines:
            archiveProject(project_id.strip())
            print("{} project has been archived.".format(project_id.strip()) + '\n')

    '''
    # Get archived projects list
    getArchivedProjects = requests.get(TC_SERVER_URL + '/app/rest/projects?locator=archived:true', verify=False, headers=headers)
    print(getArchivedProjects.text + '\n\n')

    #Create project
    project_data2 ='<newProjectDescription name=\'PatrykTestAPI\' id=\'PatrykTestAPI\'><parentProject locator=\'id:_Root\'/></newProjectDescription>'
    #headers['Content-Type'] = 'application/xml'
    createdProject = requests.post(TC_SERVER_URL + '/app/rest/projects', data=project_data2, verify=False, headers=headers)
    print(createdProject)
    '''

if __name__ == "__main__":
    main()