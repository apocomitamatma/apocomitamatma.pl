# <div align="center">apocomitamatma.pl<br>[![skeleton](https://img.shields.io/badge/0.0.2rc–219–g781ce0c-skeleton?label=%F0%9F%92%80%20skeleton-ci/skeleton-python&labelColor=black&color=grey&link=https%3A//github.com/skeleton-ci/skeleton-python)](https://github.com/skeleton-ci/skeleton-python/tree/0.0.2rc-219-g781ce0c)</div>

[![Tests](https://github.com/apocomitamatma/apocomitamatma.pl/actions/workflows/test.yml/badge.svg)](https://github.com/apocomitamatma/apocomitamatma.pl/actions/workflows/test.yml)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/apocomitamatma/apocomitamatma.pl.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/apocomitamatma/apocomitamatma.pl)

> [!Warning]
> **Work in Progress**. 🚧
>
> Hit the `👁 Watch` button to know when this project is ready to be tried out!

Web services for the best math YouTuber in Poland.

# Installation for Contributors
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
<!--
This section was generated from skeleton-ci/skeleton-python@0.0.2rc-219-g781ce0c.
Instead of changing this particular file, you might want to alter the template:
https://github.com/skeleton-ci/skeleton-python/tree/0.0.2rc-219-g781ce0c/fragments/readme.md
-->
> [!Note]
> If you use Windows, it is highly recommended to complete the installation in the way presented below through [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).
1.  Fork the [apocomitamatma.pl repository](https://github.com/apocomitamatma/apocomitamatma.pl) on GitHub.

1.  [Install Poetry](https://python-poetry.org/docs/#installation).<br/>
    Poetry is an amazing tool for managing dependencies & virtual environments, building packages and publishing them.
    You might use [pipx](https://github.com/pypa/pipx#readme) to install it globally (recommended):

    ```shell
    pipx install poetry
    ```

    <sub>If you encounter any problems, refer to [the official documentation](https://python-poetry.org/docs/#installation) for the most up-to-date installation instructions.</sub>

    Be sure to have Python 3.10 installed—if you use [pyenv](https://github.com/pyenv/pyenv#readme), simply run:

    ```shell
    pyenv install 3.10
    ```

1.  Clone your fork locally and install dependencies.

    ```shell
    git clone https://github.com/your-username/apocomitamatma.pl path/to/apocomitamatma.pl
    cd path/to/apocomitamatma.pl
    poetry env use $(cat .python-version)
    poetry install
    ```

    Next up, simply activate the virtual environment and install pre-commit hooks:

    ```shell
    poetry shell
    pre-commit install
    ```

For more information on how to contribute, check out [CONTRIBUTING.md](https://github.com/apocomitamatma/apocomitamatma.pl/blob/HEAD/CONTRIBUTING.md).<br/>
Always happy to accept contributions! ❤️

# Legal Info
© Copyright by Bartosz Sławecki ([@bswck](https://github.com/bswck)).
<br />This software is licensed under the terms of [MIT License](https://github.com/apocomitamatma/apocomitamatma.pl/blob/HEAD/LICENSE).
