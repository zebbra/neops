FROM python:3.11 AS builder

WORKDIR /app

RUN pip install uv && apt-get update && apt-get install -y --no-install-recommends make git

COPY . .
COPY --from=git . .git

# `safe.directory` covers /app *and every git submodule path* under it. The
# submodule_authors hook runs `git log` with cwd inside each submodule's
# working tree (e.g. /app/docs/<sub>); marking only /app would fail with
# "fatal: detected dubious ownership" on every submodule. We trust the build
# context inside this single-shot container, so '*' is the simplest fix.
RUN git config --global --add safe.directory '*'

RUN make doc-build

FROM nginxinc/nginx-unprivileged:1.19

COPY --from=builder /app/site /usr/share/nginx/html