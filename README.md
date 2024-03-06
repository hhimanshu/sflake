# sflake

## Prerequisites
### Install Miniconda
- Install [Miniconda](https://docs.anaconda.com/free/miniconda/index.html)
- Ensure `conda` is installed by running `conda --version`. You should see answer similar to following
```sh
conda --version
conda 24.1.2
```
- Exit the terminal and open a new terminal to ensure the conda is available in the new terminal. __You need to do this only once after installing conda__.
- Create a new conda environment
```sh
conda create -n sflake_env python=3.11
```
- Activate the environment
```sh
conda activate sflake_env
```

### Install Poetry
- Install [`pipx`](https://pipx.pypa.io/stable/installation/)
- Install [`poetry`](https://python-poetry.org/docs/#installing-with-pipx) using `pipx`
```sh
pipx install poetry
```
- Ensure `poetry` is installed by running `poetry --version`. You should see answer similar to following
```sh
poetry --version
Poetry (version 1.8.2)
```

## Other Resourcs
- To list the conda environments
```sh
conda env list
```
- To deactivate the environment
```sh
conda deactivate
```