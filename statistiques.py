# coding: utf-8

import numpy as np
import moduleAco
from tools import creationDesVilles
import csvGestion

def statistic() -> tuple | None:
    """
    statistic():

        Para :
            - Y a rien

        Création :
            - le user choisit nombreVilles
            - par défaut on a:
                - nombreFourmis = 100
                - nombreIterations = 50
                - ALPHA = 1.0
                - BETA = 1.0
                - EVAPORATION = 0.5
                - Q = 100.0
            - lance plusieurs simulations ACO en faisant varier
                un seul paramètre choisi par le user

    Return :
        - None si la simulation n'a pas pu être faite
        - (cheminFinal, distanceFinal, villes)
    """

    cheminFinal   = None
    distanceFinal = None
    villes        = None

    try:

        print("-------------------------")
        print("----- Statistique ACO ----")
        print("-------------------------")

        # Décla des variables par défauts
        nombreVilles = int(input("\nNombre de villes : "))

        if nombreVilles < 2:
            # On lève une exception
            raise ValueError("Il faut au moins 2 villes.")

        villes : dict= creationDesVilles(nombreVilles)

        cheminFinal: dict = dict()
        distanceFinal = np.inf

        # Para par défaut
        nombreFourmis: int = 100
        nombreIterations: int = 50

        ALPHA: float = 1.0
        BETA: float = 1.0
        EVAPORATION: float = 0.5
        Q: float = 100.0

        print("\nParamètres :")
        print("1 - Utiliser les paramètres par défaut")
        print("2 - Personnaliser les paramètres")

        choix = input("\nVotre choix : ")

        if choix == "2":

            # Le user modifie tous les paramètres
            nombreFourmis = int(input("\nNombre de fourmis ]0, +inf[ : "))
            nombreIterations = int(input("\nNombre d'itérations ]0, +inf[ : "))

            ALPHA = float(input("\nALPHA ]0, +inf[ : "))
            BETA = float(input("\nBETA ]0, +inf[ : "))
            EVAPORATION = float(input("\nEVAPORATION ]0, 1] : "))
            Q = float(input("\nQ ]0, +inf[ : "))

        if nombreFourmis <= 0:
            raise ValueError("Le nombre de fourmis > 0")

        if nombreIterations <= 0:
            raise ValueError("Le nombre d'itérations > 0")

        if ALPHA < 0:
            raise ValueError("ALPHA > 0")

        if BETA < 0:
            raise ValueError("BETA > 0")

        if EVAPORATION <= 0 or EVAPORATION > 1:
            raise ValueError("EVAPORATION comprit entre 0 et 1 (0 exclus)")

        if Q <= 0:
            raise ValueError("Q > 0")

        print("\n----------------------------")
        print("Paramètres de la simulation")
        print("----------------------------")
        print(f"Nb de villes          : {nombreVilles}")
        print(f"Nb de fourmis         : {nombreFourmis}")
        print(f"Nombre d'itérations   : {nombreIterations}")
        print(f"ALPHA                 : {ALPHA}")
        print(f"BETA                  : {BETA}")
        print(f"EVAPORATION           : {EVAPORATION}")
        print(f"Q                     : {Q}")

        print("\nQuel paramètre voulez-vous faire varier ?")
        print("1 - Nombre de fourmis")
        print("2 - Nombre d'itérations")
        print("3 - Alpha")
        print("4 - Beta")
        print("5 - Evaporation")
        print("6 - Q")

        choixUser = int(input("\nVotre choix : "))

        if choixUser not in range(1, 7):
            raise ValueError("Choix invalide.")

        minimum = float(input("Valeur minimum : "))
        maximum = float(input("Valeur maximum : "))
        pas = float(input("Pas : "))

        if minimum > maximum:
            raise ValueError("Le minimum doit être inférieur au maximum.")

        if pas <= 0:
            # C'est comme en PHP: throw new Exception("Message d'erreur personnalisé", 0);   
            raise ValueError("Le pas doit être positif")

        valeur = minimum

        while valeur <= maximum:

            nbFourmis = nombreFourmis
            nbIterations = nombreIterations

            alpha = ALPHA
            beta = BETA
            evaporation = EVAPORATION
            q = Q

            # On modifie uniquement le paramètre du user
            match choixUser:

                case 1:
                    nbFourmis = int(valeur)

                case 2:
                    nbIterations = int(valeur)

                case 3:
                    alpha = valeur

                case 4:
                    beta = valeur

                case 5:
                    evaporation = valeur

                case 6:
                    q = valeur

            # Lancement de la simulation
            chemin, distance, temps = moduleAco.ACO(villes, nbFourmis, nbIterations, alpha, beta, evaporation, q)

            if distance < distanceFinal:
                cheminFinal = chemin
                distanceFinal = distance

            print("\n----------")
            print(f"Valeur testée : {valeur}")
            print(f"Distance      : {distance}")
            print(f"Temps         : {temps}")

            # On ajoute dans le CSV
            csvGestion.ajoutCsv(nombreVilles, nbFourmis, nbIterations, alpha, beta, evaporation, q, distance,temps)

            # Flemme d'arrondir pour les incertitudes
            valeur += pas

        print("\nToutes les simulations sont terminées.")
        print("\n____________________________")
        print("Meilleur résultat obtenu")
        print("____________________________")

        print(f"Distance : {distanceFinal}")
        print(f"Chemin   : {cheminFinal}")
    # C'est comme en PHP avec le try/ catch
    except ValueError as erreur:
        print(f"Erreur : {erreur}")

        cheminFinal = None
        distanceFinal = None
        villes = None

    if (cheminFinal is not None) and (distanceFinal is not None) and (villes is not None):
        resultat = (cheminFinal, distanceFinal, villes)
    else:
        resultat = None

    return resultat

if __name__ == "__main__":
    # python3 statistiques.py

    print("Simulation / Test\n")

    statistic()