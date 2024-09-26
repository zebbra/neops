FROM python:3.11 as builder

WORKDIR /app

RUN pip install poetry

COPY make_scripts make_scripts

RUN poetry --directory make_scripts/mkdocs-documentation/ install

COPY . .

# We need the .git repository to get authors and last-modified dates 
COPY .git .git

RUN make doc-build

FROM nginx:1.19


COPY --from=builder /app/site /usr/share/nginx/html