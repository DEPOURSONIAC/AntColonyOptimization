# coding: utf-8

import matplotlib.pyplot as plt
from csvGestion import lireColonne

"""
Module contenant les fonctions de visualisation des données et des résultats.
"""

def afficherDistance()-> None:
    """
    afficherDistance():

        Para :
            - aucun

        Création :
            - génère la distance en fct du nb d'itérations

    Return :
        - None
    """

    iterations = lireColonne("iterations")
    distance = lireColonne("meilleureDistance")

    plt.plot(iterations, distance, marker="o")

    plt.xlabel("Itérations")
    plt.ylabel("Distance")
    plt.title("Évolution de la meilleure distance")

    plt.grid(True)
    plt.show()

def afficherTemps()-> None:
    """
    afficherTemps():

        Para :
            - aucun

        Création :
            - génère le temps en fct du nb d'itérations

    Return :
        - None
    """
    iterations = lireColonne("iterations")
    temps = lireColonne("tempsExecution")

    plt.figure("Temps d'exécution")
    plt.plot(iterations, temps, marker="o")

    plt.title("Temps d'exécution")
    plt.xlabel("Itérations")
    plt.ylabel("Temps (s)")

    plt.grid(True)
    plt.show()

def afficherFourmis()-> None:
    """
    afficherFourmis():

        Para :
            - aucun

        Création :
            - génère le nb de fourmis en fct de la meilleure distance

    Return :
        - None
    """
    

    fourmis = lireColonne("fourmis")
    distance = lireColonne("meilleureDistance")

    plt.figure("Influence des fourmis")
    plt.scatter(fourmis, distance)

    plt.title("Nombre de fourmis")
    plt.xlabel("Fourmis")
    plt.ylabel("Distance")

    plt.grid(True)
    plt.show()

def afficherAlpha()-> None:
    """
    afficherAlpha():

        Para :
            - aucun

        Création :
            - génère la variation de ALPHA en fct de la meilleure distance

    Return :
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

def afficherBeta()-> None:
    """
    afficherBeta():

        Para :
            - aucun

        Création :
            - génère la variation de BETA en fct de la meilleure distance

    Return :
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

def afficherEvaporation()-> None:
    """
    afficherEvaporation():

        Para :
            - aucun

        Création :
            - génère la variation de EVAPORATION en fct de la meilleure distance

    Return :
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

def afficherGraphe(villes: dict, meilleurChemin: list)->None:
    """
    afficherGraphe(villes, meilleurChemin):

        Para :
            - aucun
            - villes             (dict)    : dict des villes de la forme-> {1: (x,y)}
            - meilleurChemin     (list)    : liste du meilleur chemin-> [1,48,45,2,10,78,1]
        Création :
            - génère le graphe du meilleur rendu pour que cela soit plus visuel pour les users

    Return :
        - None
    """

    plt.figure("Meilleur chemin")

    plt.title("Simulation d'un meilleur chemin")
    plt.xlabel("x")
    plt.ylabel("y")

    for idVille, coordonner in villes.items():
        x, y = coordonner
        plt.scatter(x, y, s=15)

        # On décale un peu le texte pour que ce soit plus visible
        # Ah mon gars, si y a bcp de villes le graphe ressemblerai a rien donc on affiche le texte que si c'est pas bcp de villes
        if len(villes) <= 25:
            plt.text(x + 1, y + 1, str(idVille) )

    for ville in range(len(meilleurChemin)-1):
        x1, y1 = villes[meilleurChemin[ville]]
        x2, y2 = villes[meilleurChemin[ville + 1]]

        # On trace un segment entre les 2 coordonnées     
        plt.plot([x1, x2], [y1, y2], linewidth=1, color="red")
     

    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    # python3 visualisation.py

    import tools
    import statistiques

    try:

        resultat = statistiques.statistic()

        if resultat != None:

            meilleurChemin, _, villes = resultat

            choixUser: int = int(input("Afficher statistiques / afficher graphe [1,2] : "))

            if choixUser == 1:
                afficherDistance()
                afficherTemps()
                afficherFourmis()
                afficherAlpha()
                afficherBeta()
                afficherEvaporation()

            elif choixUser == 2:
                afficherGraphe(villes, meilleurChemin)

            else:
                print("Erreur")

    except ValueError as erreur:
        print(f"Erreur : {erreur}")