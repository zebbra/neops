include .make_scripts/mkdocs-documentation/mkdocs-documentation-makefile.mk

# To call with another branch, use make update-submodules BRANCH=feature/documentation
BRANCH := develop
update-submodules:
	echo "Updating submodules"
	git submodule init
	git submodule foreach 'git fetch'
	git submodule foreach 'git switch develop'
	git submodule foreach 'git switch ${BRANCH} 2>/dev/null || (git switch -c ${BRANCH} && git push -u origin ${BRANCH})'
	git submodule foreach 'git merge origin/develop'
	git submodule foreach 'git pull || (git branch --set-upstream-to=origin/${BRANCH} ${BRANCH} && git pull)'

set-upstream:
	echo "Setting upstream branches for submodules"
	git submodule foreach 'git branch --set-upstream-to=origin/${BRANCH} ${BRANCH}'

create-prs:
	echo "Creating pull requests for submodules"
	git submodule foreach 'git push -u'
	git submodule foreach 'gh pr create --title "Update ${name} submodule" --body "This PR updates the ${name} submodule to the latest changes from the ${BRANCH} branch." --base develop --head ${BRANCH}'

