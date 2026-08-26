# coding: utf-8

import matplotlib.pyplot as plt

from .csvGestion import lireColonne
from . import statistiques


"""
Module contenant les fonctions de visualisation des données et des results.
"""


def afficherHistorique(historiqueDistance: list[float]) -> None:
    """
    afficherHistorique(historiqueDistance):

        Paramètre :
            - historiqueDistance (list[float]) :
                meilleure distance obtenue à chaque itération.

        Création :
            - génère la courbe de convergence de l'ACO.

        Retour :
            - None
    """

    iterations = range(1, len(historiqueDistance) + 1)

    plt.figure("Convergence ACO")

    plt.plot(iterations, historiqueDistance, marker="o")

    plt.title("Convergence de l'algorithme ACO")
    plt.xlabel("Itérations")
    plt.ylabel("Meilleure distance")

    plt.grid(True)
    plt.show()


def afficherDistance() -> None:
    """
    afficherDistance():

        Paramètre :
            - aucun

        Création :
            - affiche la distance finale obtenue pour chaque expérience
              en fonction du nombre d'itérations configuré.

        Retour :
            - None
    """

    iterations = lireColonne("iterations")
    distance = lireColonne("meilleureDistance")

    plt.figure("Distance / Itérations")

    plt.plot(iterations, distance, marker="o")

    plt.xlabel("Nombre d'itérations")
    plt.ylabel("Distance")
    plt.title("Distance finale en fonction des itérations")

    plt.grid(True)
    plt.show()


def afficherTemps() -> None:
    """
    afficherTemps():

        Paramètre :
            - aucun

        Création :
            - affiche le temps d'exécution en fonction
              du nombre d'itérations configuré.

        Retour :
            - None
    """

    iterations = lireColonne("iterations")
    temps = lireColonne("tempsExecution")

    plt.figure("Temps d'exécution")

    plt.plot(iterations, temps, marker="o")

    plt.title("Temps d'exécution")
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("Temps (s)")

    plt.grid(True)
    plt.show()


def afficherFourmis() -> None:
    """
    afficherFourmis():

        Paramètre :
            - aucun

        Création :
            - affiche la distance finale en fonction
              du nombre de fourmis.

        Retour :
            - None
    """

    fourmis = lireColonne("fourmis")
    distance = lireColonne("meilleureDistance")

    plt.figure("Influence des fourmis")

    plt.scatter(fourmis, distance)

    plt.title("Influence du nombre de fourmis")
    plt.xlabel("Nombre de fourmis")
    plt.ylabel("Distance")

    plt.grid(True)
    plt.show()


def afficherAlpha() -> None:
    """
    afficherAlpha():

        Paramètre :
            - aucun

        Création :
            - affiche la distance finale en fonction d'Alpha.

        Retour :
            - None
    """

    alpha = lireColonne("alpha")
    distance = lireColonne("meilleureDistance")

    plt.figure("Influence Alpha")

    plt.scatter(alpha, distance)

    plt.title("Influence de Alpha")
    plt.xlabel("Alpha")
    plt.ylabel("Distance")

    plt.grid(True)
    plt.show()


def afficherBeta() -> None:
    """
    afficherBeta():

        Paramètre :
            - aucun

        Création :
            - affiche la distance finale en fonction de Beta.

        Retour :
            - None
    """

    beta = lireColonne("beta")
    distance = lireColonne("meilleureDistance")

    plt.figure("Influence Beta")

    plt.scatter(beta, distance)

    plt.title("Influence de Beta")
    plt.xlabel("Beta")
    plt.ylabel("Distance")

    plt.grid(True)
    plt.show()


def afficherEvaporation() -> None:
    """
    afficherEvaporation():

        Paramètre :
            - aucun

        Création :
            - affiche la distance finale en fonction
              du taux d'évaporation.

        Retour :
            - None
    """

    evaporation = lireColonne("evaporation")
    distance = lireColonne("meilleureDistance")

    plt.figure("Influence Evaporation")

    plt.scatter(evaporation, distance)

    plt.title("Influence de l'évaporation")
    plt.xlabel("Evaporation")
    plt.ylabel("Distance")

    plt.grid(True)
    plt.show()


def afficherGraphe(villes: dict[int, tuple[int, int]], meilleurChemin: list[int]) -> None:
    """
    afficherGraphe(villes, meilleurChemin):

        Paramètres :
            - villes (dict) :
                dictionnaire des villes sous la forme :
                {id_ville: (x, y)}

            - meilleurChemin (list) :
                meilleur chemin trouvé par l'ACO.

        Création :
            - affiche les villes.
            - affiche le meilleur chemin trouvé.

        Retour :
            - None
    """

    plt.figure("Meilleur chemin")

    plt.title("Meilleur chemin trouvé par l'ACO")
    plt.xlabel("x")
    plt.ylabel("y")

    # Affichage des villes
    for idVille, coordonnees in villes.items():

        x, y = coordonnees

        plt.scatter(x, y, s=15)

        # On affiche les identifiants uniquement
        # lorsqu'il n'y a pas trop de villes.
        if len(villes) <= 25:
            plt.text(x + 1,y + 1, str(idVille))

    # Affichage du chemin
    for i in range(len(meilleurChemin) - 1):

        villeActuelle = meilleurChemin[i]
        villeSuivante = meilleurChemin[i + 1]

        x1, y1 = villes[villeActuelle]
        x2, y2 = villes[villeSuivante]

        plt.plot([x1, x2], [y1, y2], linewidth=1, color="red")

    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    # python3 visualisation.py

    print("------------------------------")
    print("       VISUALISATION ACO")
    print("------------------------------")

    configuration = statistiques.ConfigurationACO()

    try:

        # Vérification de la configuration par défaut
        statistiques.verifierConfiguration(configuration)

        # Affichage de la configuration
        statistiques.afficherConfiguration(configuration)

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

        # Lancement des expérimentations
        resultat = statistiques.statistic(configuration, choixUser, minimum, maximum, pas)

        if resultat is not None:

            meilleurChemin, distanceFinal, villes, historiqueFinal = resultat

            print("\n------------------------------")
            print("     SIMULATIONS OVER")
            print("------------------------------")

            print(f"Distance : {distanceFinal}")
            print(f"Chemin   : {meilleurChemin}")

            print("\nQue voulez-vous afficher ?")
            print("1 - Historique final")
            print("2 - Statistiques")
            print("3 - Meilleur chemin")
            print("4 - Tout")

            choixAffichage = int(input("\nVotre choix : "))

            if choixAffichage == 1:

                afficherHistorique(historiqueFinal)

            elif choixAffichage == 2:

                afficherDistance()
                afficherTemps()
                afficherFourmis()
                afficherAlpha()
                afficherBeta()
                afficherEvaporation()

            elif choixAffichage == 3:

                afficherGraphe(villes, meilleurChemin)

            elif choixAffichage == 4:

                afficherHistorique(historiqueFinal)

                afficherDistance()
                afficherTemps()
                afficherFourmis()
                afficherAlpha()
                afficherBeta()
                afficherEvaporation()

                afficherGraphe(villes, meilleurChemin) 

            else:
                print("Erreur : choix invalide.")

    except ValueError as erreur:

        print(f"Erreur : {erreur}")