import os
import subprocess

# Recherche tous les fichiers avec l'extension .pyc dans le répertoire actuel et ses sous-répertoires
pyc_files = [os.path.join(root, f) for root, dirs, files in os.walk(
    ".") for f in files if f.endswith(".pyc")]

# Ajoute les fichiers .pyc à .gitignore
with open(".gitignore", "a") as f:
    for file in pyc_files:
        f.write(file + "\n")

# Ajoute les fichiers .pyc à l'index git pour les ignorer
subprocess.run(["git", "update-index", "--assume-unchanged"] + pyc_files)
