# Projet de Veille Numérique sur l'IA en Médecine

Ce projet est une application web de veille numérique sur l'IA en médecine. Elle utilise Python, FastAPI, Jinja2 pour les templates, et MySQL pour la base de données. L'application permet de récupérer des articles via le scraping web et des API externes, de les stocker dans une base de données et de les afficher sur une interface web.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.8+
- MySQL
- Les dépendances Python listées dans `requirements.txt`

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/veille_ia_medecine.git
    cd veille_ia_medecine
    ```

2. Créez et activez un environnement virtuel Python :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez votre base de données MySQL :

    ```sql
    CREATE DATABASE veille_ia_medecine;
    ```

5. Mettez à jour `DATABASE_URL` dans `app/database.py` avec vos informations de connexion MySQL :

    ```python
    DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/veille_ia_medecine"
    ```

## Utilisation

1. Lancez l'application avec Uvicorn :

    ```bash
    uvicorn app.main:app --reload
    ```

2. Accédez à l'application dans votre navigateur à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. Pour récupérer des articles via le scraping web, accédez à l'endpoint `/scrape-articles/`.

4. Pour visualiser les articles, accédez à l'endpoint `/articles/`.