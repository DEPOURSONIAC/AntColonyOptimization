# coding: utf-8

import random
import numpy as np

"""
Module d’outils pour l’algorithme de colonie de fourmis (ACO) :
génération des villes, distance euclidienne et matrice des distances.

"""

# Pour fixer l'aléatoire
random.seed(100)

def creationDesVilles(nombreVilles: int = 100) -> dict:
    """
    creationDesVilles(nomvreVilles):

        Para :
            - nombreVilles (int) : nombre de villes à générer (par défaut 100)

        Création :
            - boucle de 0 à nombreVilles - 1
            - génération aléatoire des coordonnées (x, y)
                - ajout dans le dictionnaire

    Return :
        - dictionnaire des villes sous la forme :
            -{id_ville: (x, y)}
    """
    
    # Déclaration des variables
    villes:  dict = {}
    dejaVus: set  = set() # Vérification des doublons avec set() -> fonction native de Python

    # Création des villes
    for ville in range(nombreVilles):

        verifDoublon: bool = True

        while (verifDoublon):

            coordonnees: tuple = (random.randint(0, 100), random.randint(0, 100))

            if (coordonnees not in dejaVus):
                dejaVus.add(coordonnees)
                villes[ville] = coordonnees
                verifDoublon = False
    
    return villes

def distanceEuclidienne (villeA: tuple, villeB: tuple)-> float:
    """
    distanceEuclidienne():

        Para :
            -villeA (tuple) : villeA (tuple) : coordonnées (x, y) de la première ville
            -villeB (tuple) : villeB (tuple) : coordonnées (x, y) de la deuxième ville
        
        Création :
            -  calcul de la différence en x (deltaX)
            -  calcul de la différence en y (deltaY)
                - on calculte la distance entre la villeA et la villeB

    Return :
        - la distance entre les 2 villes (float)

    """

    deltaX: float = (villeA[0] - villeB[0])
    deltaY: float = (villeA[1] - villeB[1])

    return float(np.sqrt(deltaX**2 + deltaY**2))

def matriceDistanceEuclidienne(villes: dict) -> np.ndarray:
    """
    matriceDistanceEuclidienne():

    Par:
        - villes        (dict) : dictionnaire et dedans il y a les villes avec coordonnées (x, y)
        - nombreVilles  (int)  : Soit le nombre de ville au total (par défaut nombreVilles = 100)

    Description :
        1- construit une matrice NxN contenant toutes les distances euclidiennes
        2- chaque case [i][j] correspond à la distance entre la ville i et la ville j
        3- la matrice est symétrique (distance(i, j) == distance(j, i))
        4- la diagonale vaut 0 (distance d’une ville avec elle-même)

    Retour :
        - matrice numpy (np.ndarray) des distances
            (de toutes les villes”)
    """

    nombreVilles: int = len(villes)

    matriceDistance: np.ndarray = np.zeros((nombreVilles, nombreVilles))

    for i in range(nombreVilles):
        for j in range(i, nombreVilles):

            villeA = villes[i]
            villeB = villes[j]

            distance = distanceEuclidienne(villeA, villeB)

            matriceDistance[i][j] = distance
            matriceDistance[j][i] = distance

    return matriceDistance

if __name__ == "__main__":
    # python3 tools.py
    
    print ("----------TEST----------")

    # Décla des variables
    villes: dict = {}
    nombreVilles:  int

    # Saisie du user du nombre de villes
    nombreVilles: int  = int(input("Saisir le nombre de villes: "))

    # Création des villes (pour le test)
    villes = creationDesVilles(nombreVilles)
    print("\nVilles générées :")
    print(villes)



    # Test des distances entre ville0 et ville1
    print("\nDistance entre ville 0 et 1 :")
    print(distanceEuclidienne(villes[0], villes[1]))

    # matriceDistance
    print("\nMatrice des distances :")
    matriceDistance = matriceDistanceEuclidienne(villes)
    print(matriceDistance)

    # Vérif diagonale
    print("\nDiagonale (doit être 0) :")
    for i in range(nombreVilles):
        print(f"ville {i} -> {matriceDistance[i][i]}")