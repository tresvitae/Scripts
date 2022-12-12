import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('tag_name', help='The name of the tag to create.')
parser.add_argument('commit', help='The commit to tag.', default='Fast fix.')
args = parser.parse_args()

tag = args.tag_name
commit = args.commit
command = 'git tag -a {0} {1} -m "{2}"'.format(tag, commit, tag)
output = subprocess.check_output(command, shell=True).decode('utf-8')
subprocess.call(command, shell=True)
subprocess.call('git push --tags', shell=True)
