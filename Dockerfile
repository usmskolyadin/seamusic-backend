FROM python:3.11.11

COPY . /backend
WORKDIR /backend

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip --root-user-action ignore
RUN pip install uv --root-user-action ignore
RUN uv venv --python 3.11.11

CMD ["make", "run-local"]
