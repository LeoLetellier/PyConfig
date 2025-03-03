# Setup your project using uv

## Create a new project

````shell
uv init example-app
````

The previous command will initiate a new project in its own folder, containing:

* `.python-version`
* `README.md`
* `main.py`
* `pyproject.toml`

## Create a library

````shell
uv init --lib example-lib
````

## Lock your dependencies

````shell
uv lock
````

````shell
uv lock --check
````

````shell
uv lock --upgrade
````