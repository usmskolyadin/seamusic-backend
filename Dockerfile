FROM ghcr.io/astral-sh/uv:python3.11-bookworm

WORKDIR /app

ENV UV_COMPILE_BYTECODE 0
ENV UV_LINK_MODE=copy

RUN uv venv --python 3.11.11
ADD . /app

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

CMD ["make", "run-local"]
