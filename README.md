- [Résumé](#résumé)
- [Développement local](#développement-local)
  - [Prérequis](#prérequis)
  - [macOS / Linux](#macos--linux)
    - [Cloner le repository](#cloner-le-repository)
    - [Créer l'environnement virtuel](#créer-lenvironnement-virtuel)
    - [Exécuter le site](#exécuter-le-site)
    - [Linting](#linting)
    - [Tests unitaires](#tests-unitaires)
    - [Base de données](#base-de-données)
    - [Panel d'administration](#panel-dadministration)
  - [Windows](#windows)
- [Tests et déploiement via CircleCI](#tests-et-déploiement-via-circleci)
  - [Prérequis](#prérequis-1)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
- [Exécution du docker en local](#exécution-du-docker-en-local)
  - [Prérequis](#prérequis-2)
  - [Utilisation](#utilisation-1)
- [Sentry](#sentry)
  - [Prérequis](#prérequis-3)
  - [Utilisation](#utilisation-2)
- [Variables d'environnement](#variables-denvironnement)
  
## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Tests et déploiement via CircleCI

Après une mise à jour du code sur la branche master, CircleCI lance un pipeline dans lequel le code est linté puis exécute les tests unitaires.

Si cette étape se termine correctement, il exécute une dockerisation de l'application et envoie une image taguée sur DockerHub.

Ensuite si l'action précédente a abouti, l'application est déployée sur Heroku.


### Prérequis

Il est nécessaire de créer les comptes suivants :

- Compte [CircleCI](https://circleci.com/signup/)
- Compte [DockerHub](https://hub.docker.com/)
- Compte [Heroku](https://signup.heroku.com/)

Pour intéragire avec Heroku, il est néessaire d'intaller Heroku CLI, voici la documentation:

- Installer [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

### Installation

- Créer un projet CircleCI et le lier à votre repository GitHub.
- Créer un projet DockerHub.
- Créer un projet Heroku.
- Obtenir un token d'authentification Heroku. [Documentation](https://devcenter.heroku.com/articles/authentication). (ce token sera à renseigner comme variable dans CircleCi)
  

### Utilisation

- Si toute l'installation est respectée, l'exécution du pipeline devrait se lancer à chaque mise à jour du code sur GitHub.
- Les tests unitaires et le lint du code se fera à chaque mise à jour de code dans n'importe quelle branche contenant la configuration CircleCI.
- La dockerization sur DockerHub et le déploiement sur Heroku s'exécuteront à chaque mise à jour du code dans la branche master.
 
Après le déploiement le site est accéssible à l'adresse: [oc-lettings-78.herokuapp.com](https://oc-lettings-78.herokuapp.com/)

## Exécution du docker en local

### Prérequis

- Compte [DockerHub](https://hub.docker.com/)
- Installer Docker
  - Linux Ubuntu : [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
  - Windows : [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- Avoir exécuté le Pipeline précédent (sur CircleCi).
- Renseigner les variables d'environnement dans le fichier ".env" (voir le tableau plus bas pour les variables)

Vous devez renseigner le fichier ".env" dans ".gitignore" pour l'exclure de la gestion git.
Il doit absolument rester uniquement sur votre machine.

exemple de fichier ".env":

```txt

DJANGO_SECRET_KEY='votre_secret_key'
DEBUG=1
SENTRY_DSN=https://xxxxxxxxxxxxxxxxxxxxxxxx.ingest.sentry.io/111111111

```
Remarque la valeur de la variable "SENTRY_DSN" ne doit pas avoir de quote.

### Utilisation

En considérant:
- user = Nom d'utilisateur du compte DockerHub.
- repo = Application créée dans DockerHub.
- tag = Nom donné automatiquement à une image.
- .env = chemin d'accès du fichier ".env".
- port = port bind pour gunicorn

Etapes:
- Ouvrir un terminal avec les privilèges "root".
  - Télécharger l'image docker `docker pull user/repo:tag`.
  - Exécuter l'image docker `docker run -d -e "PORT=port" -p 8000:8000 --env-file .env user/repo:tag`. (si vous lancez uniquement cette commande, l'image Docker sera aussi télégargée)

Exemple : docker run -d -e "PORT=8000" -p 8000:8000 --env-file .env lahou/oc-lettings:cb634a753c32902e593130bbef45b8e25bf6fd40
  
Pour accéder au site rendez-vous à l'adresse: [localhost:8000](http://localhost:8000)


## Sentry

Sentry est une application de suivi d'exceptions non gérées.

### Prérequis

- Compte [Sentry](https://sentry.io/signup/)

### Utilisation

- Créer un projet Sentry
- Une valeur "dsn" vous sera fournie. (Ce "dsn"" sera à renseigner comme variable dans CircleCi et dans le fichier ".env")

## Variables d'environnement

Les variables d'environnement sont des données sensibles à ne pas publier.

Pour se faire ces variables seront rajoutées dans :
- la configuration du projet dans CircleCI
- le fichier ".env" pour l'éxécution en locale (ce fichier reste en locale et n'est pas poussé sur Github)

| Clé  | Valeur          | Lieu |
| :--------------: |:---------------:|:---------:|
| DJANGO_SECRET_KEY  |   Clé secrète DJANGO  | ".env" et CircleCI |
| DEBUG  | Mode DEBUG : 0 ou 1  | ".env" et CircleCI |
| DOCKER_USER  | Utilisateur DockerHub  | CircleCI |
| DOCKER_PASS  | Mot de passe DockerHub  | CircleCI |
| HEROKU_TOKEN  | Tocken de connexion Heroku  | CircleCI |
| SENTRY_DSN  | DSN Sentry  | ".env" et CircleCI |
