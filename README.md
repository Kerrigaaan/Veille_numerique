# Veille IA Médecine

Ce projet est une application de veille numérique sur l'intelligence artificielle (IA) dans le domaine de la médecine. L'application permet de scraper des données à partir de sites web, de les analyser et de les visualiser pour en extraire des informations pertinentes.

## Fonctionnalités

1. **Collecte et Filtrage des Données**
    - **Scraping Web** : Extraction automatisée des données à partir de sites web.
    - **API** : Utilisation d'API pour récupérer des données structurées.
    - **Filtres de Recherches** : Application de critères pour filtrer les données non pertinentes.

2. **Nettoyage des Données**
    - **Suppression des Doublons** : Élimination des entrées en double.
    - **Correction des Erreurs** : Correction des fautes de frappe et des incohérences.
    - **Normalisation** : Uniformisation des formats de date, unités de mesure, etc.
    - **Complétion** : Ajout des données manquantes.

3. **Transformation des Données**
    - **Agrégation** : Regroupement de données similaires pour obtenir des totaux, moyennes, etc.
    - **Conversion** : Transformation des données en différents formats ou unités.
    - **Enrichissement** : Ajout de données supplémentaires provenant d'autres sources.

4. **Analyse des Données**
    - **Statistiques Descriptives** : Calcul de mesures telles que la moyenne, la médiane, l'écart-type.
    - **Analyse de Tendance** : Identification des tendances et des motifs dans les données.
    - **Segmentation** : Division des données en sous-groupes significatifs.
    - **Analyse de Sentiment** : Détection des opinions positives, négatives ou neutres dans les textes.

5. **Visualisation des Données**
    - **Graphiques** : Création de diagrammes, graphiques en barres, graphiques en lignes, etc.
    - **Tableaux de Bord** : Conception de tableaux de bord interactifs pour une vue d'ensemble.
    - **Cartographie** : Visualisation des données géographiques sur des cartes.

6. **Modélisation et Prédiction**
    - **Apprentissage Machine** : Utilisation de modèles prédictifs pour anticiper les tendances futures.
    - **Analyse de Régression** : Établissement de relations entre différentes variables.
    - **Clustering** : Regroupement des données en clusters basés sur des similarités.

7. **Rapport et Communication**
    - **Synthèses et Résumés** : Création de résumés exécutifs et de rapports détaillés.
    - **Alertes et Notifications** : Mise en place de systèmes d'alertes pour les événements importants.
    - **Présentations** : Préparation de présentations visuelles pour partager les résultats.

8. **Surveillance Continue**
    - **Mise à Jour Automatique** : Configuration de scripts pour mettre à jour les données en temps réel.
    - **Moniteurs de Veille** : Utilisation d'outils pour surveiller les sources de données en continu.

9. **Évaluation et Amélioration**
    - **Feedback** : Recueil des commentaires des utilisateurs pour améliorer le système de veille.
    - **Audit des Données** : Réalisation d'audits pour vérifier l'exactitude et la fiabilité des données.

## Prérequis

- Python 3.7 ou supérieur
- MySQL

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/veille-ia-medecine.git
    cd veille-ia-medecine
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Configurez la base de données MySQL :
    - Assurez-vous que MySQL est installé et en cours d'exécution.
    - Exécutez le script SQL pour créer la base de données et la table :
      ```bash
      mysql -u root -p < data/db_setup.sql
      ```

5. Lancez l'application :
    ```bash
    uvicorn app.main:app --reload
    ```

## Utilisation

- **Accueil** : Accédez à `http://127.0.0.1:8000` pour voir la page d'accueil.
- **Informations** : Accédez à `http://127.0.0.1:8000/informations` pour voir les informations scrappées.
- **Scraping** : Accédez à `http://127.0.0.1:8000/scrape` pour scraper les informations et les stocker dans la base de données.
- **Analyse** : Accédez à `http://127.0.0.1:8000/analyze` pour analyser les données.
- **Visualisation** : Accédez à `http://127.0.0.1:8000/visualize` pour visualiser les données.

