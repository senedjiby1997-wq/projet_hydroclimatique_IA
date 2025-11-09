# 🌦️ Projet Hydroclimatique IA

Ce projet vise à prédire la pluviométrie à partir de données météorologiques historiques en utilisant des techniques d’intelligence artificielle (IA) et d’apprentissage automatique.
L’objectif principal est de fournir un outil d’aide à la planification agricole et à la gestion des ressources en eau, particulièrement dans les zones à forte variabilité climatique.

## 🎯 Objectif

Développer un modèle prédictif basé sur des algorithmes d’IA (ex. LSTM, Random Forest, ou Régression linéaire).

Identifier les facteurs météorologiques clés influençant les précipitations (température, humidité, pression, etc.).

Fournir des prévisions fiables de la pluviométrie pour anticiper les risques de sécheresse ou d’inondation.

Soutenir les décisions agricoles intelligentes grâce à une approche basée sur les données.

Favoriser la durabilité agricole dans le contexte du changement climatique.

### 🧩 Aperçu du projet

Collecte et préparation des données

Données météorologiques historiques (température, humidité, vent, pression, précipitations, etc.).

Nettoyage, normalisation et structuration dans le dossier data/.

Exploration et visualisation

Analyse des tendances climatiques.

Corrélation entre variables (température ↔ pluie).

Graphiques d’évolution temporelle.

Modélisation IA

Entraînement d’un modèle prédictif (par ex. LSTM pour séries temporelles).

Évaluation des performances (RMSE, MAE, R²).

Déploiement et utilisation

Sauvegarde du modèle dans le dossier model/.

Interface ou script pour faire des prédictions à partir de nouvelles données météo.

### 📂 Structure du projet
Projet_Hydroclimatique_IA/
│
├── src/                # Scripts Python pour traitement et modélisation
├── data/               # Données météorologiques historiques
├── model/              # Modèles entraînés et sauvegardés
├── notebooks/          # Analyses exploratoires et tests
├── requirements.txt    # Librairies Python nécessaires
└── README.md           # Description du projet

### 🧠 Technologies utilisées

Python 3.10+

TensorFlow / Keras

Scikit-learn

Pandas, NumPy, Matplotlib, Seaborn

Jupyter Notebook
