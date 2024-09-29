# Installation

## Getting Started

The following instructions will help you to setup a clone of the project and run it on your local machine for development. Skip ahead to the [deployment section](#deployment) to get a dockerized version up & running.

### Prerequisites

- `Python 3.7.0` or greater - _for running neops.io_
- `git` - _to checkout the source code repository_
- `docker` and `docker-compose` - _to run the application containers using docker_
- `pipenv` - _for running the backend services_
- `yarn` and `node` - _for running the frontend_
- `overmind` - _optional: as mapper to run all services together_ -> get the latest version [here](https://github.com/DarthSim/overmind/releases/latest) (requires `tmux`)

### Development Installation

A step by step examples that tells you how to get a development env running

Clone the repository

```shell
git clone https://github.com/zebbra/neops-core.git
```

Start the development containers

```shell
cd neops-core/docker
docker-compose up -d
```

#### Backend

Configure the backend environment (edit the content of `.env` if necessary)

```shell
cd neops-core/backend
cp .env.dist .env
```

Create the python virtual enviroment and install the required python libraries

```shell
cd neops-core/backend
mkdir .venv
pipenv install
```

Apply the database migrations

```shell
cd neops-core/backend
pipenv run ./manage.py migrate
```

Deploy the elastic indexes

```shell
cd neops-core/backend
pipenv run ./manage.py elastic_index --rebuild
```

Create a superuser for the backend

```shell
cd neops-core/backend
pipenv run ./manage.py createsuperuser
```

#### Frontend

Install node modules

```shell
cd neops-core/frontend
yarn install
```

If you run into any problems during the installation, please refer to the [Common Problems and Solutions](#common-problems-and-solutions).

### Run Application

#### Start with overmind

```shell
cd neops-core/
overmind start
```

#### Start dedicated

Frontend

```shell
cd neops-core/frontend
yarn dev
```

Backend

```shell
cd neops-core/backend
pipenv run ./manage.py runserver 0.0.0.0:8000
```

Workers

```shell
cd neops-core/backend
pipenv run celery -A neopsapp worker -n w1 -l INFO --concurrency=1
```

Beat (task scheduling)

```shell
cd neops-core/backend
pipenv run celery -A neopsapp beat -l info --scheduler neops.enterprise.celery.cron.scheduler:NeopsCeleryScheduler
```

## Configuration

Configuration is handled by the backend with the enviroment variables in `backend/.venv`

### Modules

neops modules are listed in `NEOPS_PLUGINS`

add all modules to load at startup, django settings for those modules are located at `neopsapp/settings/neops_plugins`

### Authentication

For authentication an appropriate neops module is required.

#### Django Backend (neops_auth_django, default in .env)

Users are authenticated against the django default user model.

Please use django admin to manage users

#### Static API Key (neops_auth_static_api_key, default in .env)

Used to set static API keys per user

Static API keys are set by django manage commands

```shell
cd neops-core/backend
pipenv run ./manage.py generate_api_key 1 graphiql
```

The last 2 parameters are the user id and the name of the app

#### Keycloak (neops_auth_keycloak)

!> **Coming with version 1.0**

## Web Frontends

- [neops Frontend](http://localhost:3000) - _the magic_
- [django Admin](http://localhost:8000/admin/) - _access to the database/models_
- [graphiql](http://localhost:8000/graphiql/) - _GraphQL API_

### neops Application

Use the discovery process on the dashboard to add new devices

### GraphiQL

[set an API Key first](#static-api-key-neops_auth_static_api_key-default-in-env) to gain permission to the API

## Deployment

### Kubernetes

!> **Coming with version 1.0** Neops can be deployed on a kubernetes cluster using helm. We are standardizing last things under the hood to fulfill our **backwards compatibility commitment** according to [SemVer](semver.org). Stay tuned!

### Docker - Compose

Download [docker-compose files](neops-docker-compose.tar.gz)

```shell
tar -zxvf neops-docker-compose.tar.gz
```

#### Traefik

Install Traefik reverse proxy when needed

```shell
cd traefik
cp .env.dist .env
```

Fill variables in `.env` with your specific values

Create network for Traefik if needed

```shell
docker network create \
	--driver=bridge \
	--attachable \
	--internal=false \
	traefik
```

Create self-signed certs

```shell
echo "Generating self-signed certificate for localhost"
mkdir data
mkdir data/traefik
mkdir data/traefik/certs
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout data/traefik/certs/traefik.key -out data/traefik/certs/traefik.crt  -subj "/CN=localhost"
chmod 700 data/traefik/certs/traefik.key
```

Generate .htpasswd for Trafik Dashboard

```shell
echo "pw" | htpasswd -b -i data/traefik/.htpasswd admin
```

#### neops

Create env file and adjust settings

```shell
cd neops
cp .env.dist .env
```

Fill variables in `.env` with your specific values

Create quay.io login

```shell
docker login -u="zebbra+neops" -p="$PW" quay.io
```

Start containers

```shell
docker-compose up -d --scale frontend=2 --scale worker=2
```

Run db migrations

```shell
echo "Running database migrations for neops"
docker-compose exec frontend ./manage.py migrate
```

Setup admin

```shell
Create Django admin user
docker-compose exec frontend ./manage.py createsuperuser
```

#### Keycloak

```shell
cd keycloak
cp .evn.dist .env
```

Fill variables in `.env` with your specific values

```shell
docker-compose up -d
```

Add neops-realm-export.json as realm in keycloak

Setup Realm in Django Admin

## Common Problems and Solutions

### General

#### Problem: `ERROR: Version in "./docker-compose.yml" is unsupported`

```shell-session
$ docker-compose up -d
ERROR: Version in "./docker-compose.yml" is unsupported. You might be seeing this error because you're using the wrong Compose file version. Either specify a supported version (e.g "2.2" or "3.3") and place your service definitions under the `services` key, or omit the `version` key and place your service definitions at the root of the file to use version 1.
For more on the Compose file format versions, see https://docs.docker.com/compose/compose-file/
```

##### Solution:

If you get this error messagen when running `docker-compose`, you have to change the version setting **from "3.7" to "3.3"** in the file `neops-core/docker/docker-compose.yml` on line 2:

```yaml
# docker-compose file for development with django and vue.js running directly on the host
version: "3.3"

services:
  redis:
    image: redis:5-alpine
			(content skipped)

```

#### Problem: `ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?`

```shell-session
$ docker-compose up -d
ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
```

##### Solution:

Make sure that the `docker` is running (example for `ubuntu-linux`-OS):

```shell-session
$ systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; disabled; vendor preset:
   Active: inactive (dead)
     Docs: https://docs.docker.com
```

Start the service if required and afterwards re-run `docker-compose`:

```shell
systemctl start docker

cd neops-core/backend
docker-compose up -d
```

### Backend

#### Problem: `Warning: Python 3.7 was not found on your system…`

```shell-session
$ cd neops-core/backend
$ pipenv install
Warning: Python 3.7 was not found on your system…
You can specify specific versions of Python with:
  $ pipenv --python path/to/python
```

##### Solution:

Install and specify the correct `python` version for `pipenv` (example for `ubuntu-linux`-OS):

```shell
sudo apt install python3.7

cd neops-core/backend
pipenv --python /usr/bin/python3.7
```

### Frontend

#### Problem: `ERROR: [Errno 2] No such file or directory: 'install'`

```shell-session
$ yarn install
00h00m00s 0/0: : ERROR: [Errno 2] No such file or directory: 'install'
```

##### Solution:

By default the commands `yarn` and `cmdtest` are the black box testing tools for Unix command line tools [cmdtest](https://liw.fi/cmdtest/).

Simply remove the existing `yarn` and `cmdtest` tools and install the required `yarn` tool from an external source (example for `ubuntu-/debian-linux`-OS):

```shell
sudo apt remove cmdtest
sudo apt remove yarn
sudo apt install curl
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn
```

#### Problem: `error yn@4.0.0: The engine "node" is incompatible with this module. Expected version ">=10"`

```shell-session
$ yarn install
yarn install v1.22.4
[1/4] Resolving packages...
[2/4] Fetching packages...
error yn@4.0.0: The engine "node" is incompatible with this module. Expected version ">=10". Got "8.10.0"
error Found incompatible module.
info Visit https://yarnpkg.com/en/docs/cli/install for documentation about this command.
```

##### Solution:

The existing version of `node` is not recent enough. Update `node` from an external repository (example for `ubuntu-linux`-OS):

```shell
sudo apt update
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt -y install nodejs
```

## Documentation

We are using [docsify.js](https://docsify.js.org/) to generate the documentation available here.

The source is located in the [`/docs`](https://github.com/zebbra/neops-core/tree/master/docs) folder of the project and served using Github Pages.

The site consists of several `.md` files and a single `index.html`, which loads the markdown files and renders them in the browser.

?> **NOTE:** The projects `README.md` and `CONTRIBUTING.md` files are also located in the `docs/` (and symlinked into the project root directory) to make it available in Github Pages.

### Previewing the documentation

You may want to preview the documentation locally using the docsify CLI:

```shell-session
$ # install the docsify cli
$ npm i docsify-cli -g

$ # start the docsify server
$ docsify serve docs

Serving /Users/hw/Projects/neops-core/docs now.
Listening at http://localhost:3000
```

Open http://localhost:3000 in your browser to preview the documentation.

### Theming

The site is using the [docsify-themeable](https://jhildenbiddle.github.io/docsify-themeable/) theme.
