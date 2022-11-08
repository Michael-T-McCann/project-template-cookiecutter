# {{cookiecutter.project_title}}

{{cookiecutter.description}}

## One-time setup
Create a conda environment for your new project:

conda env create --file environment.yml

## Getting the latest version
git pull
conda env update --file ./environment.yml

## Running code
conda activate {{cookiecutter.folder_name}}


