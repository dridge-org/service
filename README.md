# dridge - service

## Development

> This section describes how to run a `dridge` proxy natively. However, in most cases it is recommended to use the enviroment found in the [development](https://github.com/dridge-org/development) respository which contains a full proxy-worker setup.

### Installation

> This project uses [Poetry](https://python-poetry.org/) for dependency management.
> Make sure you have `python` (>=3.10) and `poetry` installed.

1. Clone the repository.

```sh
git clone https://github.com/dridge-org/service
cd service
```

2. Install the dependencies.

```sh
poetry install
```

3. Install pre-commit hooks.

```sh
poetry run pre-commit install
```

### Running the application

1. Enter the virtual environment.

```sh
poetry shell
```

2. Run the ASGI application with auto-reload.

```sh
litestar --app dridge.proxy.asgi:app run --reload
```
