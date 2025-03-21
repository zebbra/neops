.PHONY: doc-update-assets doc-create-mkdocs doc-serve doc-build

MKDOCS_ENV=./make_scripts/mkdocs-documentation

doc-update-assets:
	$(MKDOCS_ENV)/setup_documentation.sh

doc-create-mkdocs:
	poetry run --project $(MKDOCS_ENV)/ python $(MKDOCS_ENV)/setup_documentation.py

doc-serve:
	poetry install --project $(MKDOCS_ENV)/
	poetry run --project $(MKDOCS_ENV)/ python $(MKDOCS_ENV)/setup_documentation.py
	poetry run --project $(MKDOCS_ENV)/  mkdocs serve

doc-build:
	poetry run --project $(MKDOCS_ENV)/ python $(MKDOCS_ENV)/setup_documentation.py
	poetry run --project $(MKDOCS_ENV)/  mkdocs build
	poetry run --project $(MKDOCS_ENV)/ python $(MKDOCS_ENV)/clean_sites_directory.py

doc-build-docker:
	docker build --file $(MKDOCS_ENV)/Dockerfile .

doc-site-clean:
	poetry run --project $(MKDOCS_ENV)/ python $(MKDOCS_ENV)/clean_sites_directory.py
