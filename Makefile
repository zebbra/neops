include ./make_scripts/mkdocs-documentation/mkdocs-documentation-makefile.mk

update-submodules:
	echo "Updating submodules"
	git submodule init
	git submodule foreach 'git fetch'
	git submodule foreach 'git checkout develop'
	git submodule foreach 'git pull'

