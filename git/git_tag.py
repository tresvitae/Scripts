import argparse
import git
from git import Repo

#Parse arguments using argparse
parser = argparse.ArgumentParser()
parser.add_argument('tag_name', help='The name/number of the tag.')
parser.add_argument('commit_id', help='The commit to tag.', default='HEAD')
args = parser.parse_args()

#Init the repo
repo = Repo('PWD')

#Create the tag and push it to the remote repository
try:
    tag_obj = repo.create_tag(args.tag_name, args.commit_id)
    repo.remotes.origin.push(tag_obj)
except Exception as error:
    print(f'Error: {error}')


