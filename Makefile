include ./make_scripts/mkdocs-documentation/mkdocs-documentation-makefile.mk

BRANCH := develop
update-submodules:
	echo "Updating submodules"
	git submodule init
	git submodule foreach 'git fetch'
	git submodule foreach 'git checkout ${BRANCH}'
	git submodule foreach 'git pull'

