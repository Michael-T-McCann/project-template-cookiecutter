help = """
Your project has been created!

Initialize the repo and commit

cd {{cookiecutter.repo_name}}
git init --initial-branch main
git add .gitignore README.md data/README.md  docs/README.md environment.yml results/README.md scripts/README.md setup.py {{package_name}}/__init__.py tests/README.md
git commit -m"Add files from template"

(Optional) Make repo on github and push to there.

"""
print(help)
