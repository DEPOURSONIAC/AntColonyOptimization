# coding: utf-8

import random
import numpy as np
import tools
import time

"""
Module ACO (Ant Colony Optimization)

Ce module contient l'algo de colonie de fourmis.
Il gère le meilleur chemin entre les villes:
    - il gère les probas via les phéromones
    - la dist entre les villes
    - l'évaporation  et le dépot des phéromones

"""

def ACO(nombreVilles: int = 100, nombreFourmis: int = 100, nombreIterations: int = 50, ALPHA: float = 1.0, BETA: float = 1.0, EVAPORATION: float = 0.5, Q: float = 100) -> tuple:
    """
    ACO (Ant Colony Optimization)

    Paramètres :
        - nombreVilles      (int)    : nombre total de villes du problème
        - nombreFourmis     (int)    : nombre de fourmis utilisées à chaque itération
        - nombreIterations  (int)    : nombre de cycles d’exécution de l’algorithme

    Explication :
        - implémente l’algo du ACO
        - chaque fourmi construit un chemin complet entre les villes
        - les choix sont crées par les phéromones et les distances
        - les bonnes solutions renforcent les chemins via le dépôt de phéromones
        - les mauvaises solutions disparaissent via l'évaporation

    Retour :
        - tuple :
            - le meilleur chemin trouvé
            - la distance minimale associée
            - le temps mis pour le trouver (deltaT)
    """

    # Décla des variables
    debut: float = time.perf_counter()

    meilleurChemin   = None
    meilleurDistance = np.inf

    villes    = tools.creationDesVilles(nombreVilles)
    distances = tools.matriceDistanceEuclidienne(villes)

    # Matrice des phéromones : toutes les valeurs sont mises à 1. Elle sert à aider les fourmis dans le choix des chemins
    MatricePheromones: np.ndarray = np.ones((nombreVilles, nombreVilles))

    # Algo du ACO
    for iteration in range(nombreIterations):

        # Liste des chemins trouvés par les fourmis
        cheminTrouverParFourmis : list = list()
        # Liste des distances associées
        listeDistance           : list = list()

        for fourmis in range(nombreFourmis):

            villeDepart = random.randint(0, nombreVilles - 1)

            cheminFourmi  : list = [villeDepart]
            villesVisitees: set  = {villeDepart}

            while (len(cheminFourmi) < nombreVilles):

                villeActuelle = cheminFourmi[-1]

                proba = []
                villesAccessibles = []

                for prochaineVille in range(nombreVilles):

                    if (prochaineVille not in villesVisitees):
                        pheromone = MatricePheromones[villeActuelle][prochaineVille] ** ALPHA
                        visibilite = (1.0 / (distances[villeActuelle][prochaineVille] + 1e-9)) ** BETA

                        score = pheromone * visibilite

                        proba.append(score)
                        villesAccessibles.append(prochaineVille)

                if (len(villesAccessibles) == 0):
                    # Un cas très rare mais par sécurité on vérifie s'il  y a des villes accessibles
                    # Sinon on casse la boucle car on ne peut pas continuer le chemin
                    break

                sommeScores = sum(proba)

                if (sommeScores == 0):
                    # Si la somme est nul alors chaque ville à la même proba d'être tirée soit 1/len(proba)
                    proba = [1 / len(proba)] * len(proba)

                else:
                    # Sinon cela veut dire qu'on a récuper plusierus données (proba brut pour chaque ville )
                    
                    # On a des données brut donc le but est de les convertir en vrai proba par exemple :
                    # proba[10,20,70]-> ingérable et trop brute donc convertion :
                    # nouvelleProba[0.1,0.2,0.7]-> Traitable, soit p(e), la proba d'un évenement:
                    # p(e) ∈ [0;1]

                    proba = [p / sommeScores for p in proba]

                # On utilise choice car ça choisit une ville en fct des probas (pondéré)
                choixVille = random.choices(villesAccessibles, weights=proba, k=1)[0]

                cheminFourmi.append(choixVille)
                villesVisitees.add(choixVille)

            cheminFourmi.append(cheminFourmi[0])  # On rajoute la ville de base comme ça la boucle est bouclé

            cheminTrouverParFourmis.append(cheminFourmi)

            distanceTotale = 0

            for i in range(len(cheminFourmi) - 1):
                distanceTotale += distances[cheminFourmi[i]][cheminFourmi[i + 1]]

            listeDistance.append(distanceTotale)

            if distanceTotale < meilleurDistance:
                meilleurDistance = distanceTotale
                meilleurChemin = cheminFourmi.copy()

        # Evaporation
        MatricePheromones *= (1 - EVAPORATION)

        # Depot

        for fourmis in range(nombreFourmis):

            cheminDeLaFourmis = cheminTrouverParFourmis[fourmis]
            distancesDeLaFourmis = listeDistance[fourmis]

            depot: float = Q / distancesDeLaFourmis

            for i in range(len(cheminDeLaFourmis) - 1):
                villeActuelle = cheminDeLaFourmis[i]
                villeSuivante = cheminDeLaFourmis[i + 1]

                MatricePheromones[villeActuelle][villeSuivante] += depot
                MatricePheromones[villeSuivante][villeActuelle] += depot

    # Mesurer le temps que ça prends
    fin: float = time.perf_counter()
    deltaT: float = fin - debut

    return meilleurChemin, meilleurDistance, deltaT, villes


if __name__ == "__main__":
    # python3 moduleAco.py

    # Décla des constantes (en MAJUSCULES)

    ALPHA       : float = 1.0
    BETA        : float = 1.0
    EVAPORATION : float = 0.5
    Q           : float = 100 # Ratio du nombre de phéromone sur une route/ chemin

    chemin, meilleurDistance, tps, villes = ACO(50, 50, 10, ALPHA, BETA, EVAPORATION, Q)

    print("Distance :", meilleurDistance)
    print("Temps :", tps)