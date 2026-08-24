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
    - l'évaporation et le dépot des phéromones

"""


def ACO(villes: dict, nombreFourmis: int = 100, nombreIterations: int = 50, ALPHA: float = 1.0, BETA: float = 1.0, EVAPORATION: float = 0.5,Q: float = 100) -> tuple:
    """
    ACO (Ant Colony Optimization)

    Paramètres :
        - villes            (dict)   : dictionnaire des villes de la forme-> {1: (x, y), 2: (x', y')}
        - nombreFourmis     (int)    : nombre de fourmis utilisées à chaque itération
        - nombreIterations  (int)    : nombre de cycles d’exécution de l’algorithme
        - ALPHA             (float)  : importance des phéromones
        - BETA              (float)  : importance de la visibilité
        - EVAPORATION       (float)  : taux d'évaporation des phéromones
        - Q                 (float)  : quantité de phéromones déposée

    Explication :
        - implémente l'algo du ACO
        - chaque fourmi construit un chemin complet entre les villes
        - les choix sont crées par les phéromones et les distances
        - les bonnes solutions renforcent les chemins via le dépôt de phéromones
        - les mauvaises solutions disparaissent via l'évaporation

    Retour :
        - tuple :
            - le meilleur chemin trouvé
            - la distance minimale associée
            - le temps mis pour le trouver (deltaT)
            - historique de la meilleure distance à chaque itération
    """

    # Vérification des paramètres
    if len(villes) < 2:
        raise ValueError("Il faut au moins 2 villes.")

    if nombreFourmis < 1:
        raise ValueError("Le nombre de fourmis doit être supérieur à 0.")

    if nombreIterations < 1:
        raise ValueError("Le nombre d'itérations doit être supérieur à 0.")

    if ALPHA < 0:
        raise ValueError("ALPHA doit être supérieur ou égal à 0.")

    if BETA < 0:
        raise ValueError("BETA doit être supérieur ou égal à 0.")

    if not 0 <= EVAPORATION <= 1:
        raise ValueError("L'évaporation doit être comprise entre 0 et 1.")

    if Q <= 0:
        raise ValueError("Q doit être supérieur à 0.")

    # Décla des variables
    debut: float = time.perf_counter()

    meilleurChemin: list[int] | None = None
    meilleurDistance: float = np.inf

    # Historique de la meilleure distance à chaque itération
    historiqueDistance: list[float] = []

    nombreVilles = len(villes)

    distances = tools.matriceDistanceEuclidienne(villes)

    # Matrice des phéromones : toutes les valeurs sont mises à 1. Elle sert à aider les fourmis dans le choix des chemins
    MatricePheromones: np.ndarray = np.ones((nombreVilles, nombreVilles))

    # Algo du ACO
    for iteration in range(nombreIterations):

        # Liste des chemins trouvés par les fourmis
        cheminTrouverParFourmis: list = list()

        # Liste des distances associées
        listeDistance: list = list()

        for fourmis in range(nombreFourmis):

            villeDepart = random.randint(0, nombreVilles - 1)

            cheminFourmi: list = [villeDepart]
            villesVisitees: set = {villeDepart}

            while (len(cheminFourmi) < nombreVilles):

                villeActuelle = cheminFourmi[-1]

                proba = []
                villesAccessibles = []

                for prochaineVille in range(nombreVilles):

                    if prochaineVille not in villesVisitees:
                        pheromone = MatricePheromones[villeActuelle][prochaineVille] ** ALPHA
                        visibilite = (1.0 / (distances[villeActuelle][prochaineVille] + 1e-9)) ** BETA

                        score = pheromone * visibilite

                        proba.append(score)
                        villesAccessibles.append(prochaineVille)

                if len(villesAccessibles) == 0:
                    # Un cas très rare mais par sécurité on vérifie s'il y a des villes accessibles
                    # Sinon on casse la boucle car on ne peut pas continuer le chemin
                    break

                sommeScores = sum(proba)

                if sommeScores == 0:
                    # Si la somme est nul alors chaque ville à la même proba d'être tirée soit 1/len(proba)
                    proba = [1 / len(proba)] * len(proba)

                else:
                    # Sinon cela veut dire qu'on a récuper plusieurs données (proba brut pour chaque ville)

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

        # On garde la meilleure distance trouvée à cette étape de l'algo
        historiqueDistance.append(float(meilleurDistance))

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

    return meilleurChemin, float(meilleurDistance), deltaT, historiqueDistance


if __name__ == "__main__":
    # python3 moduleAco.py

    # Décla des constantes (en MAJUSCULES)

    ALPHA: float = 1.0
    BETA: float = 1.0
    EVAPORATION: float = 0.5
    Q: float = 100  # Ratio du nombre de phéromone sur une route/ chemin

    villes = tools.creationDesVilles(100)

    chemin, meilleureDistance, tps, historiqueDistance = ACO(villes, 10, 50, ALPHA, BETA, EVAPORATION, Q)

    print("Distance :", meilleureDistance)
    print("Temps :", tps)
    print("Historique :", historiqueDistance)