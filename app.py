from flask import Flask, render_template, jsonify
import numpy as np
import json

app = Flask(__name__)

# Données réelles des communes d'Abidjan (estimations basées sur les données disponibles)
COMMUNES_ABIDJAN = {
    'Cocody': {
        'population': 450000,
        'densite': 8500,  # hab/km²
        'superficie': 53,  # km²
        'categories': {
            'jeunes': 0.35,  # 35% de moins de 25 ans
            'adultes': 0.55,  # 55% de 25-64 ans
            'seniors': 0.10   # 10% de 65+ ans
        }
    },
    'Yopougon': {
        'population': 1050000,
        'densite': 12000,
        'superficie': 87,
        'categories': {
            'jeunes': 0.40,
            'adultes': 0.52,
            'seniors': 0.08
        }
    },
    'Abobo': {
        'population': 1200000,
        'densite': 15000,
        'superficie': 80,
        'categories': {
            'jeunes': 0.45,
            'adultes': 0.48,
            'seniors': 0.07
        }
    },
    'Adjamé': {
        'population': 250000,
        'densite': 25000,
        'superficie': 10,
        'categories': {
            'jeunes': 0.30,
            'adultes': 0.60,
            'seniors': 0.10
        }
    },
    'Plateau': {
        'population': 150000,
        'densite': 18000,
        'superficie': 8.5,
        'categories': {
            'jeunes': 0.25,
            'adultes': 0.65,
            'seniors': 0.10
        }
    },
    'Treichville': {
        'population': 200000,
        'densite': 22000,
        'superficie': 9,
        'categories': {
            'jeunes': 0.35,
            'adultes': 0.55,
            'seniors': 0.10
        }
    },
    'Marcory': {
        'population': 180000,
        'densite': 9000,
        'superficie': 20,
        'categories': {
            'jeunes': 0.30,
            'adultes': 0.60,
            'seniors': 0.10
        }
    },
    'Koumassi': {
        'population': 350000,
        'densite': 14000,
        'superficie': 25,
        'categories': {
            'jeunes': 0.40,
            'adultes': 0.53,
            'seniors': 0.07
        }
    },
    'Port-Bouët': {
        'population': 200000,
        'densite': 8000,
        'superficie': 25,
        'categories': {
            'jeunes': 0.35,
            'adultes': 0.58,
            'seniors': 0.07
        }
    },
    'Bingerville': {
        'population': 80000,
        'densite': 4000,
        'superficie': 20,
        'categories': {
            'jeunes': 0.45,
            'adultes': 0.48,
            'seniors': 0.07
        }
    }
}

def generer_donnees_demographiques():
    """Génère des données démographiques réalistes basées sur les communes d'Abidjan"""
    donnees = {}
    
    for commune, info in COMMUNES_ABIDJAN.items():
        # Générer des données avec une variation réaliste (±10%)
        variation = np.random.normal(1, 0.1)
        population_reelle = int(info['population'] * variation)
        
        # Répartition par âge avec variation
        jeunes = int(population_reelle * info['categories']['jeunes'] * np.random.normal(1, 0.05))
        adultes = int(population_reelle * info['categories']['adultes'] * np.random.normal(1, 0.05))
        seniors = population_reelle - jeunes - adultes
        
        donnees[commune] = {
            'population': population_reelle,
            'densite': round(info['densite'] * np.random.normal(1, 0.08), 0),
            'superficie': info['superficie'],
            'repartition_age': {
                'jeunes': jeunes,
                'adultes': adultes,
                'seniors': seniors
            }
        }
    
    return donnees

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/donnees-abidjan')
def get_donnees_abidjan():
    """Retourne les données démographiques des communes d'Abidjan"""
    donnees = generer_donnees_demographiques()
    
    # Calculer les statistiques globales
    populations = [d['population'] for d in donnees.values()]
    densites = [d['densite'] for d in donnees.values()]
    
    stats_globales = {
        'population_totale': sum(populations),
        'moyenne_population': round(np.mean(populations), 0),
        'mediane_population': round(np.median(populations), 0),
        'ecart_type_population': round(np.std(populations), 0),
        'densite_moyenne': round(np.mean(densites), 0),
        'nombre_communes': len(donnees)
    }
    
    return jsonify({
        'communes': donnees,
        'statistiques_globales': stats_globales
    })

@app.route('/api/analyse-demographique')
def analyse_demographique():
    """Analyse démographique détaillée"""
    donnees = generer_donnees_demographiques()
    
    # Analyser la répartition par âge
    total_jeunes = sum(d['repartition_age']['jeunes'] for d in donnees.values())
    total_adultes = sum(d['repartition_age']['adultes'] for d in donnees.values())
    total_seniors = sum(d['repartition_age']['seniors'] for d in donnees.values())
    population_totale = total_jeunes + total_adultes + total_seniors
    
    # Analyser la densité de population
    densites = [d['densite'] for d in donnees.values()]
    
    return jsonify({
        'repartition_age': {
            'jeunes': {
                'nombre': total_jeunes,
                'pourcentage': round((total_jeunes / population_totale) * 100, 1)
            },
            'adultes': {
                'nombre': total_adultes,
                'pourcentage': round((total_adultes / population_totale) * 100, 1)
            },
            'seniors': {
                'nombre': total_seniors,
                'pourcentage': round((total_seniors / population_totale) * 100, 1)
            }
        },
        'densite_population': {
            'moyenne': round(np.mean(densites), 0),
            'mediane': round(np.median(densites), 0),
            'minimum': round(np.min(densites), 0),
            'maximum': round(np.max(densites), 0),
            'ecart_type': round(np.std(densites), 0)
        },
        'population_totale': population_totale
    })

@app.route('/api/comparaison-communes')
def comparaison_communes():
    """Compare les communes selon différents critères"""
    donnees = generer_donnees_demographiques()
    
    # Trier les communes par différents critères
    communes_par_population = sorted(donnees.items(), key=lambda x: x[1]['population'], reverse=True)
    communes_par_densite = sorted(donnees.items(), key=lambda x: x[1]['densite'], reverse=True)
    
    # Calculer des indices de développement (fictifs mais réalistes)
    indices_developpement = {}
    for commune, info in donnees.items():
        # Indice basé sur la densité et la répartition d'âge
        densite_norm = info['densite'] / 25000  # Normalisation
        ratio_jeunes = info['repartition_age']['jeunes'] / info['population']
        indice = (densite_norm * 0.6) + (ratio_jeunes * 0.4)
        indices_developpement[commune] = round(indice * 100, 1)
    
    return jsonify({
        'classement_population': [
            {'commune': commune, 'population': info['population']} 
            for commune, info in communes_par_population
        ],
        'classement_densite': [
            {'commune': commune, 'densite': info['densite']} 
            for commune, info in communes_par_densite
        ],
        'indices_developpement': indices_developpement
    })

if __name__ == '__main__':
    app.run(debug=True) 