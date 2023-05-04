# Cariol

## Start

Avant de commencer à la racine de backend éxecuter la commande suivante:

    py ou python -m venv .venv

Dans le fichier .venv/ pyvenv.cfg remplacer le contenu par, cependant les " premières lignes, du code ci-dessous doivent êtres remplacées per le code déjà présent dans le fichier pyvenv.cfg":

    [venv]
    home = /usr/bin
    include-system-site-packages = false
    version = 3.10.10
    user=postgres
    password=your_password
    database=cariol

Ensuite éxécuter la commande:

    pip install -r requirements.txt

### Lancer le serveur

Avant de lancer le serveur démarer l'environement virtuel, puis:

    hug -f server.py
