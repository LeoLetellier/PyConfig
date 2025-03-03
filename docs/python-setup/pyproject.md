# Python Project

A Python project can be described through the `pyproject.toml` file.

The [specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/) and a [tutorial](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) regarding this file are available at the python.org website.

This file is decomposed mainly in two parts:

* `[build-system]` describe which build-backend must be used when creating a package from the project source files.
* `[project]` contains multiple variables that directly describe the project, such as: name, dependencies, requires-python, authors, maintainers, license, ...

The possible keys are: ``authors``, ``classifiers``, ``dependencies``, ``description``, ``dynamic``, ``entry-points``, ``gui-scripts``, ``keywords``, ``license``, ``license-file``, ``maintainers``, ``name``, ``optional-dependencies``, ``readme``, ``requires-python``, ``scripts``, ``urls``, ``version``

Refers to this [full example](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#a-full-example) for more, or this [repository pyproject](https://raw.githubusercontent.com/LeoLetellier/PyConfig/main/pyproject.toml).
