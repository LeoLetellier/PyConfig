# UV (Astral)

uv is a package and project manager for python, written in Rust by [Astral](https://docs.astral.sh/).

> View complete details on [Astral Website](https://docs.astral.sh/uv/) | [Github](https://github.com/astral-sh/uv)

It aims to replace former package manager like ``pip``, and handle virtual environments like ``virtualenv``.

## Installation

You are one command line from getting started:

=== "Linux/Mac"

    ```Bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```Shell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

The following commands are available: ``run``, ``init``, ``add``, ``remove``, ``sync``, ``lock``, ``export``, ``tree``, ``tool``, ``python``, ``pip``, ``venv``, ``build``, ``publish``, ``cache``, ``self``, ``version``

## Update

````bash
uv self upgrade
````