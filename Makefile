include ./make_scripts/mkdocs-documentation/mkdocs-documentation-makefile.mk

update-submodules:
	git submodule init
	git submodule update --remote
	git submodule foreach 'git checkout main'
	git submodule foreach 'git pull'
#