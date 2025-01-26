# SeaMusic API

<div>
  <img src="https://img.shields.io/github/stars/seamusic-official/seamusic-backend?style=flat-square&label=stars&color=darkgreen">
  <img src="https://img.shields.io/github/forks/seamusic-official/seamusic-backend?style=flat-square&label=forks&color=darkgreen">
  <img src="https://img.shields.io/github/actions/workflow/status/seamusic-official/seamusic-backend/check.yml?branch=dev&style=flat-square&label=linter&color=darkgreen">
  <img src="https://img.shields.io/codeclimate/maintainability/seamusic-official/seamusic-backend?style=flat-square&label=maintainability&color=darkgreen">
  <img src="https://img.shields.io/codeclimate/coverage/seamusic-official/seamusic-backend?style=flat-square&label=coverage&color=darkgreen">
</div>


### ✍️ About
This is the [SeaMusic](https://github.com/seamusic-official/)
API source code

### 🛠️ Build and run commands

*Make sure you have `docker`, `docker-compose`, `make` and `uv` installed.*

> You'll need to specify `for` argument with some commands. `for` can have 3 values: `dev`, `prod` and `test` depending on app build purpose.

Building a docker container (`for` required)
```bash
make build
```

Starting an app (`for` required)
```bash
make start
```

Starting the app in background mode (`for` required)
```bash
make up
```

Stopping the app (`for` required)
```bash
make stop
```

Deleting the docker container (`for` required)
```bash
make stop
```

Linting the project
```bash
make lint
```

Running tests
```bash
make test
```

Creating a virtual environment **locally**
```bash
make install
```

Creating an alembic revision
```bash
make revision
```

Running the revision
```bash
make upgrade revision=<revision identificator>
```

Downgrading the revision
```bash
make downgrade revision=<revision identificator>
```

### 🤝 Contributing

The project is closed for open-source contributions

### 📜 License

Check [our license](https://github.com/seamusic-official/seamusic-backend/blob/master/LICENSE.md)
