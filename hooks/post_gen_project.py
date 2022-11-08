repo_name = "{{ cookiecutter.project_title.lower().replace(' ', '-') }}"

help = f"""
Your project has been created!

Initialize the repo and commit:

cd {{cookiecutter.folder_name}}
git init --initial-branch main
git add .gitignore README.md data/README.md  docs/README.md environment.yml results/README.md scripts/README.md setup.py {{cookiecutter.package_name}}/__init__.py tests/README.md
git commit -m"Add files from template"

(Optional) Make repo (e.g., {repo_name}) on github and push to there:

git remote add origin <REMOTE_URL>
git push -u origin main
"""
print(help)
