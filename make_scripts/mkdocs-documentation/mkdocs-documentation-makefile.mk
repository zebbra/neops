.PHONY: doc-update-assets doc-create-mkdocs doc-serve doc-build

doc-update-assets:
	./make_scripts/mkdocs-documentation/setup_documentation.sh

doc-create-mkdocs:
	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/setup_documentation.py

doc-serve:
	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/setup_documentation.py
	poetry run --directory make_scripts/mkdocs-documentation/  mkdocs serve

doc-build:
	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/setup_documentation.py
	poetry run --directory make_scripts/mkdocs-documentation/  mkdocs build
	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/clean_sites_directory.py

doc-build-docker:
	docker build --file make_scripts/mkdocs-documentation/Dockerfile .

doc-site-clean:
	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/clean_sites_directory.py

#doc-build-strict:
#	poetry run --directory make_scripts/mkdocs-documentation/ python make_scripts/mkdocs-documentation/setup_documentation.py
#	poetry run --directory make_scripts/mkdocs-documentation/  mkdocs build --strict
