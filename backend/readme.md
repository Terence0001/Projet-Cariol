# Cariol

## Start 
Avant de commencer à la racine de backend éxecuter la commande suivant:
    
    py ou python -m venv .venv

dans le fichier .venv/ pyvenv.cfg remplacer le contenue par:

    [venv]
    home = /usr/bin
    include-system-site-packages = false
    version = 3.10.10
    user=postgres
    password=yout_password
    database=cariol

Ensuite éxécuter la commande:

    pip install -r requirements.txt


### Lancer le serveur 
avant de lancer le serveur démarer l'environement virtuelle puis:

    hug -f server.py