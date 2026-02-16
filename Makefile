include .make_scripts/mkdocs-documentation/mkdocs-documentation-makefile.mk

BRANCH := develop
update-submodules:
	echo "Updating submodules"
	git submodule init
	git submodule foreach 'git fetch'
	git submodule foreach 'git switch ${BRANCH} 2>/dev/null || (git switch -c ${BRANCH} && git push -u origin ${BRANCH})'
	git submodule foreach 'git merge origin/develop'
	git submodule foreach 'git pull'

