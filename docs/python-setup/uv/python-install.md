# Python Installation using uv

Display all possible installation on your device:

````bash
uv python list
````

Install a specific python version:

````bash
uv python install [version]
````

Python will be installed in your home/AppData. You an switch to system installation instead of uv managed python installation with:

````toml title="pyproject.toml"
[tool.uv]
python-preference = "system"
````

Create a virtual environment:

````bash
uv venv --python [version]
````
