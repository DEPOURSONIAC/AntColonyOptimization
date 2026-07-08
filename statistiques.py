# coding: utf-8

import numpy as np
import moduleAco
import csvGestion


def statistic()-> tuple | None:
    """
    statistic():

        Para :
            - aucun

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
        - None s'il y a rien
        - meilleurDistance et meilleurChemin
    """


    print("-------------------------")
    print("----- Statistique ACO ----")
    print("-------------------------")

    # Décla des variables par défauts
    nombreVilles = int(input("\nNombre de villes : "))

    cheminFinal : dict = dict()
    distanceFinal      = np.inf

    nombreFourmis    : int = 100
    nombreIterations : int = 50

    ALPHA       : float  = 1.0
    BETA        : float  = 1.0
    EVAPORATION : float  = 0.5
    Q           : float  = 100.0

    print("\nQuel paramètre voulez-vous faire varier ?")
    print("1 - Nombre de fourmis")
    print("2 - Nombre d'itérations")
    print("3 - Alpha")
    print("4 - Beta")
    print("5 - Evaporation")
    print("6 - Q")

    choixUser = int(input("\nVotre choix : "))

    minimum = float(input("Valeur minimum : "))
    maximum = float(input("Valeur maximum : "))
    pas = float(input("Pas : "))

    valeur = minimum

    while valeur <= maximum:

        # On repart des valeurs par défaut
        nbFourmis = nombreFourmis
        nbIterations = nombreIterations

        alpha = ALPHA
        beta = BETA
        evaporation = EVAPORATION
        q = Q

        # On modifie uniquement le paramètre du user
        match choixUser: # Comme le switch/ case en C/C++/JAVA/PHP -> Comme les if/elif/else mais en mieux

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

            case _:
                print("Choix invalide.")
                return

        # Lancement de la simulation
        chemin, distance, temps= moduleAco.ACO(nombreVilles, nbFourmis, nbIterations, alpha, beta, evaporation, q)

        if distance < distanceFinal:
            cheminFinal   = chemin
            distanceFinal = distance


        print("\n----------")
        print("Valeur testée :", valeur)
        print("Distance :", distance)
        print("Temps :", temps)

        #  On ajoute dans le CSV
        csvGestion.ajoutCsv(nombreVilles, nbFourmis, nbIterations,alpha, beta,evaporation, q, distance, temps)

        valeur += pas


    print("\nToutes les simulations sont terminées.")

    print("\n____________________________")
    print("Meilleur résultat obtenu")
    print("____________________________")
    print(f"Distance : {distanceFinal}")
    print(f"Chemin   : {cheminFinal}")

    return cheminFinal, distanceFinal

if __name__ == "__main__":
    # python3 statistiques.py

    print("Simulation / Test\n")

    statistic()
    