# sflake

## Prerequisites
### Install Miniconda
- You must have `python` installed on your machine.
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

### Install `pip`
- Install [`pip`](https://pypi.org/project/pip/)
```sh
conda install pip
```
- Ensure `pip` is installed by running `pip --version`. You should see answer similar to following
```sh
pip --version
pip 23.3.1 from /opt/homebrew/Caskroom/miniconda/base/envs/sflake_env/lib/python3.11/site-packages/pip (python 3.11)
```
### Install project dependencies
- Install the project dependencies
```sh
pip install -r requirements.txt
```

## Run the project
- Copy environment variables from `.env.sample` to `.env` and update the values
```sh
cp .env.sample .env
```

Update the values in `.env` file according to your environment.

- Run the project
```sh
python src/main.py
```

## Other Resources
- To list the conda environments
```sh
conda env list
```
- To deactivate the environment
```sh
conda deactivate
```
- To remove the environment
```sh
conda env remove --name sflake_env
```