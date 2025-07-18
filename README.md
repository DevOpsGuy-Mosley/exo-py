# 🏙️ Démographie Abidjan - Analyse NumPy

Un projet d'analyse démographique utilisant NumPy pour analyser les données réelles des communes d'Abidjan avec une interface web moderne.

## 🚀 Fonctionnalités

- **Données démographiques réelles** : Population, densité et répartition par âge des communes d'Abidjan
- **Analyse statistique** : Calculs de moyennes, médianes, écarts-types avec NumPy
- **Visualisations interactives** : Graphiques en donut pour la répartition par âge
- **Comparaisons** : Classements par population et densité
- **Interface moderne** : Design responsive avec Tailwind CSS

## 📊 Communes d'Abidjan incluses

- **Cocody** : 450 000 habitants (densité : 8 500 hab/km²)
- **Yopougon** : 1 050 000 habitants (densité : 12 000 hab/km²)
- **Abobo** : 1 200 000 habitants (densité : 15 000 hab/km²)
- **Adjamé** : 250 000 habitants (densité : 25 000 hab/km²)
- **Plateau** : 150 000 habitants (densité : 18 000 hab/km²)
- **Treichville** : 200 000 habitants (densité : 22 000 hab/km²)
- **Marcory** : 180 000 habitants (densité : 9 000 hab/km²)
- **Koumassi** : 350 000 habitants (densité : 14 000 hab/km²)
- **Port-Bouët** : 200 000 habitants (densité : 8 000 hab/km²)
- **Bingerville** : 80 000 habitants (densité : 4 000 hab/km²)

## 📋 Prérequis

- Python 3.7+
- pip (gestionnaire de paquets Python)

## 🛠️ Installation

1. **Cloner ou télécharger le projet**
   ```bash
   # Si vous avez git
   git clone <url-du-repo>
   cd exo-py
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Utilisation

1. **Lancer l'application**
   ```bash
   python app.py
   ```

2. **Ouvrir votre navigateur**
   - Allez sur `http://localhost:5000`
   - L'interface s'affichera automatiquement

3. **Explorer les données**
   - **📊 Données Communes** : Voir le tableau complet avec toutes les communes
   - **👥 Analyse Démographique** : Répartition par âge et statistiques de densité
   - **📈 Comparaison Communes** : Classements et indices de développement

## 📁 Structure du projet

```
exo-py/
├── app.py                 # Application Flask avec données Abidjan
├── requirements.txt       # Dépendances Python (Flask + NumPy)
├── templates/
│   └── index.html        # Interface utilisateur moderne
└── README.md            # Ce fichier
```

## 🔧 Technologies utilisées

- **Backend** : Flask (framework web Python)
- **Calculs** : NumPy (analyses statistiques démographiques)
- **Frontend** : HTML5 + Tailwind CSS (interface moderne)
- **Graphiques** : Chart.js (visualisations interactives)

## 📊 Fonctionnalités NumPy

Le projet utilise NumPy pour :

- **Génération de variations réalistes** :
  - `np.random.normal()` : Variations démographiques (±10%)
  - Simulation de fluctuations naturelles des données

- **Calculs statistiques démographiques** :
  - `np.mean()` : Densité moyenne, population moyenne
  - `np.median()` : Médiane des populations
  - `np.std()` : Écart-type des densités
  - `np.min()` / `np.max()` : Valeurs extrêmes

- **Analyses démographiques** :
  - Calcul de répartition par âge
  - Indices de développement
  - Classements comparatifs

## 🎨 Interface utilisateur

L'interface propose :

- **📊 Données Communes** :
  - Tableau complet avec population, densité, superficie
  - Répartition détaillée par âge (jeunes, adultes, seniors)
  - Statistiques globales d'Abidjan

- **👥 Analyse Démographique** :
  - Graphique en donut de la répartition par âge
  - Statistiques de densité de population
  - Pourcentages détaillés par tranche d'âge

- **📈 Comparaison Communes** :
  - Classement par population
  - Classement par densité
  - Indices de développement calculés

## 🔄 API Endpoints

- `GET /` : Page d'accueil
- `GET /api/donnees-abidjan` : Données démographiques des communes
- `GET /api/analyse-demographique` : Analyse détaillée par âge et densité
- `GET /api/comparaison-communes` : Classements et indices

## 📝 Exemples d'utilisation NumPy

### Génération de variations démographiques
```python
import numpy as np
# Variation réaliste de ±10%
variation = np.random.normal(1, 0.1)
population_reelle = int(population_base * variation)
```

### Calculs statistiques démographiques
```python
# Densité moyenne des communes
densite_moyenne = np.mean(densites)
# Écart-type des populations
ecart_type_pop = np.std(populations)
```

### Analyse de répartition par âge
```python
# Calcul des pourcentages par tranche d'âge
pourcentage_jeunes = (total_jeunes / population_totale) * 100
```

## 🏙️ Données démographiques

Les données sont basées sur :
- **Estimations démographiques réelles** d'Abidjan
- **Densités de population** observées
- **Répartitions par âge** typiques des villes africaines
- **Superficies** officielles des communes

## 🤝 Contribution

Ce projet démontre l'utilisation de NumPy pour :
1. Analyser des données démographiques réelles
2. Générer des variations statistiques réalistes
3. Créer des visualisations interactives
4. Comparer des indicateurs urbains

## 📄 Licence

Ce projet est fourni à des fins éducatives et de démonstration de l'utilisation de NumPy pour l'analyse démographique. 