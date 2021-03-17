# Linux Essentials Skills of creating various bash shell scripts.

**Table of Contents**

###Creating users and groups [Users&Groups](https://github.com/tresvitae/basic-shell-scripts/tree/main/users-and-groups "Users&Groups")



Working reopository:
```sh
$ docker image build -t lab:v1 .
$ docker run -it lab:v1
```

Clearing images from last 24h:
```sh
$ docker container stop $(docker ps -aq)
$ docker image prune -a --force --filter "until=24h"
```