FROM python:3.11 as builder

WORKDIR /app

RUN pip install poetry

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

# We need the .git repository to get authors and last-modified dates 
COPY .git .git

RUN make build

FROM nginx:1.19


COPY --from=builder /app/site /usr/share/nginx/html