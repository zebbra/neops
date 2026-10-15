#!/usr/bin/env bash

set -euo pipefail

client_directory="docs/neops-web-client"
card_lab_assets_source="${client_directory}/docs/assets"
card_lab_assets_target="site/neops-web-client/docs/assets"

# MkDocs must run before npm creates node_modules inside docs/, and the Card Lab
# must be copied after MkDocs removes unsupported files from site/.
if [ -e "${client_directory}/node_modules" ]; then
  echo "${client_directory}/node_modules already exists before the MkDocs build and would be crawled into the site" >&2
  exit 1
fi

make doc-build

mkdir -p "${card_lab_assets_target}"
for asset in card-lab.css card-lab.js dashboard-card-reference.css dashboard-card-reference.js; do
  if [ ! -f "${card_lab_assets_source}/${asset}" ]; then
    echo "Card Lab documentation asset missing at ${card_lab_assets_source}/${asset}" >&2
    exit 1
  fi
  cp "${card_lab_assets_source}/${asset}" "${card_lab_assets_target}/${asset}"
done

if ! npm ci --prefix "${client_directory}"; then
  echo "npm ci failed. If the error above is a 401 or 403 from npm.pkg.github.com, grant zebbra/neops Actions read access to every required private @zebbra package under Package settings > Manage Actions access." >&2
  exit 1
fi

npm run --prefix "${client_directory}" build:card-lab

# web-client ships exactly one Card Lab, built from the same commit as its pages, which link
# card-lab/index.html; there is no version segment to agree on.
card_lab_target="site/neops-web-client/docs/card-lab"
card_docs_target="site/neops-web-client/docs/dashboard-cards"

mkdir -p "${card_lab_target}"
cp -R "${client_directory}/dist/card-lab/." "${card_lab_target}/"

if [ ! -f "${card_lab_target}/index.html" ]; then
  echo "card lab entry point missing at ${card_lab_target}/index.html" >&2
  exit 1
fi

if ! card_lab_symlinks="$(find "${card_lab_target}" -type l -print)"; then
  echo "failed to scan ${card_lab_target} for symlinks" >&2
  exit 1
fi
if [ -n "${card_lab_symlinks}" ]; then
  echo "card lab contains symlinks:" >&2
  echo "${card_lab_symlinks}" >&2
  exit 1
fi

if ! site_node_modules="$(find site -type d -name node_modules -print -quit)"; then
  echo "failed to scan site for node_modules" >&2
  exit 1
fi
if [ -n "${site_node_modules}" ]; then
  echo "node_modules leaked into the published site at ${site_node_modules}" >&2
  exit 1
fi

if [ ! -d "${card_docs_target}" ]; then
  echo "dashboard-card documentation missing at ${card_docs_target}" >&2
  exit 1
fi

if versioned_links="$(grep -RhoE 'card-lab/[^"?]+' "${card_docs_target}" | grep -v '^card-lab/index\.html$' | sort -u)" && [ -n "${versioned_links}" ]; then
  echo "dashboard-card links must reference card-lab/index.html; found '${versioned_links}'" >&2
  exit 1
fi
