.PHONY: doc-update-assets doc-create-mkdocs doc-serve doc-build

MKDOCS_ENV= .make_scripts/mkdocs-documentation
PROJECT_NAME := $(notdir $(CURDIR))


# USE_LOCALE_REPO=<path-to-mkdocs-documentation-checkout> copies the template
# assets straight from a local repo checkout instead of downloading the latest
# GitHub release. Use it while iterating on the template itself, e.g.
#   make doc-update-assets USE_LOCALE_REPO=/home/you/projects/.../mkdocs-documentation
doc-update-assets:
ifdef USE_LOCALE_REPO
	USE_LOCALE_REPO="$(USE_LOCALE_REPO)" /bin/sh "$(USE_LOCALE_REPO)/assets/setup_documentation.sh"
else
	gh release download --repo zebbra/mkdocs-documentation --pattern setup_documentation.sh --output - | /bin/sh
endif

doc-create-mkdocs:
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/setup_documentation.py
	$(MAKE) doc-create-mkdocs-build-workflow

doc-serve:
	uv sync --project $(MKDOCS_ENV)
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/setup_documentation.py
	# doc_serve_watch.py wraps `mkdocs serve --livereload` so edits to
	# mkdocs_custom.yml / mkdocs_base.yml regenerate mkdocs.yml on the fly,
	# and so --livereload is set explicitly (mkdocs 1.6 + Click 8 resolves
	# the default to False without it). See the docstring at the top of
	# doc_serve_watch.py for details.
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/doc_serve_watch.py

doc-build:
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/setup_documentation.py
	uv run --project $(MKDOCS_ENV) mkdocs build
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/clean_sites_directory.py

doc-setup:
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/setup_documentation.py

doc-build-docker:
	docker build --file $(MKDOCS_ENV)/Dockerfile --build-context git=.git -t $(PROJECT_NAME)-docs .

doc-run-docker:
	docker run --rm -p 8000:8000 $(PROJECT_NAME)-docs:latest

doc-site-clean:
	uv run --project $(MKDOCS_ENV) python $(MKDOCS_ENV)/clean_sites_directory.py

doc-create-mkdocs-build-workflow:
	touch .github
	touch .github/workflows
	cp .make_scripts/mkdocs-documentation/.github/workflows/build-documentation.yml .github/workflows

# -r: recursive (look in subfolders)
# -c: change absolute links to relative
# -v: verbose (show what is happening)
doc-fix-symlinks:
	which symlinks || { echo "symlinks command not found. Please install it to fix symlinks in the documentation."; exit 1; }
	symlinks -rcv .