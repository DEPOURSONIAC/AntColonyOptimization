# coding: utf-8

import time

import moduleAco
import statistiques
import visualisation
import csvGestion

from tools import creationDesVilles
from statistiques import ConfigurationACO


"""
Main du projet ACO.

Ce fichier permet à l'utilisateur de :

    - lancer une simulation ACO 
    - réaliser une étude statistique 
    - visualiser les résultats 
    - gérer le fichier CSV 
    - quitter le programme

Les autres modules contiennent la logique du programme.
Le main.py sert principalement à gérer l'interface de l'utilisateur.
"""


def greek(n: int) -> str:
    """
    Affiche une décoration ASCII basée sur n éléments.
    """

    s = ""

    for _ in range(n):
        s += "┌───┐ "

    s += "\n"

    for _ in range(n):
        s += "│ ┌─┘ "

    s += "\n"

    for _ in range(n):
        s += "┘ └───"

    s += "\n"

    return s


def afficherFourmi1() -> None:
    """
    Affiche une grande fourmi ASCII.
    """

    print(r"""
                      ,
      _,-'\   /|   .    .    /`.
  _,-'     \_/_|_  |\   |`. /   `._,--===--.__
 ^       _/"/  " \ : \__|_ /.   ,'    :.  :. .`-._
        // ^   /7 t'""    "`-._/ ,'\   :   :  :  .`.
        Y      L/ )\         ]],'   \  :   :  :   : `.
        |        /  `.n_n_n,','\_    \ ;   ;  ;   ;  _>
        |__    ,'     |  \`-'    `-.__\_______.==---'
       //  `""\\      |   \            \
       \|     |/      /    \            \
                     /     |             `.
                    /      |               ^
                   ^       |
                           ^
    """)


def afficherFourmi2() -> None:
    """
    Affiche une petite fourmi ASCII.
    """

    print(r"""

 \       /
  \     /  
   \.-./ 
  (o\^/o)  _   _   _     __
   ./ \.\ ( )-( )-( ) .-'  '-.
    {-} \(//  ||   \\/ (   )) '-.
         //-__||__.-\\.       .-'
        (/    ()     \)'-._.-'
        ||    ||      \\
       ('    ('       ')

    """)


def animationDemarrage() -> None:
    """
    Affiche l'écran de démarrage avec une petite animation.
    """

    afficherFourmi1()

    print(greek(9))

    print("Initialisation de la colonie de fourmis", end="", flush=True) # end = évite le retour à la ligne et flush = éviter le buffer (le tampon/ que le texte reste en attente)

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print("\n")

    time.sleep(0.5)

    print("_" * 32)
    print("ANT COLONY OPTIMISATION".center(32))
    print("_" * 32)

    time.sleep(0.5)


def afficherMenuPrincipal() -> None:
    """
    Affiche le menu principal.
    """

    print("\n")
    print(greek(5))

    print("┌────────────────────────────────────────────┐")
    print("│             MENU PRINCIPAL                 │")
    print("├────────────────────────────────────────────┤")
    print("│                                            │")
    print("│  [1]  Lancer une simulation ACO            │")
    print("│  [2]  Faire une étude statistique          │")
    print("│  [3]  Visualiser les résultats             │")
    print("│  [4]  Gestion du fichier CSV               │")
    print("│  [0]  Quitter                              │")
    print("│                                            │")
    print("└────────────────────────────────────────────┘")


def afficherHelp() -> None:
    """
        test
    """
    pass


def lancerSimulation() -> tuple | None:
    """
    Demande les paramètres à l'utilisateur
    puis lance une simulation ACO.

    Retour :
        - résultat de ACO
        - None en cas d'erreur
    """

    print("\n" + "*" * 64)
    print("SIMULATION ACO".center(64))
    print("*" * 64)

    nombreVilles = int(input("\nNombre de villes : "))
    nombreFourmis = int(input("Nombre de fourmis : "))
    nombreIterations = int(input("Nombre d'itérations : "))

    ALPHA = float(input("ALPHA : "))
    BETA = float(input("BETA : "))
    EVAPORATION = float(input("EVAPORATION : "))
    Q = float(input("Q : "))

    configuration = ConfigurationACO(nombreVilles=nombreVilles, nombreFourmis=nombreFourmis, nombreIterations=nombreIterations, ALPHA=ALPHA, BETA=BETA, EVAPORATION=EVAPORATION, Q=Q)

    statistiques.verifierConfiguration(configuration)

    print("\nParamètres sélectionnés :")
    statistiques.afficherConfiguration(configuration)

    print("\nGénération des citys...")

    villes = creationDesVilles(nombreVilles)

    print("Villes générées.")

    print("\n Lancement de la colonie", end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print("\n\t")

    chemin, distance, tempsExecution, historiqueDistance = moduleAco.ACO(villes, nombreFourmis, nombreIterations, ALPHA, BETA, EVAPORATION, Q)

    print("\n" + "+" * 64)
    print("RÉSULTAT".center(64))
    print("+" * 64)

    print(f"Distance : {distance}")
    print(f"Temps    : {tempsExecution} s")
    print(f"Chemin   : {chemin}")

    return chemin, distance, tempsExecution, historiqueDistance, villes


def menuVisualisation(resultat: tuple | None) -> None:
    """
    Menu permettant de choisir une visualisation.

    Paramètre :
        resultat :
            résultat d'une simulation ACO.
    """

    state: bool = True
    while state:

        print("\n")
        print("┌──────────────────────────────────────────────┐")
        print("│              VISUALISATION                   │")
        print("├──────────────────────────────────────────────┤")
        print("│ [1] Courbe de distance                       │")
        print("│ [2] Temps d'exécution                        │")
        print("│ [3] Influence des fourmis                    │")
        print("│ [4] Influence de ALPHA                       │")
        print("│ [5] Influence de BETA                        │")
        print("│ [6] Influence de l'évaporation               │")
        print("│ [7] Meilleur chemin                           │")
        print("│ [8] Historique ACO                            │")
        print("│ [0] Retour                                    │")
        print("└──────────────────────────────────────────────┘")

        choix = int(input("\nVotre choix : "))

        if choix == 1:
            visualisation.afficherDistance()

        elif choix == 2:
            visualisation.afficherTemps()

        elif choix == 3:
            visualisation.afficherFourmis()

        elif choix == 4:
            visualisation.afficherAlpha()

        elif choix == 5:
            visualisation.afficherBeta()

        elif choix == 6:
            visualisation.afficherEvaporation()

        elif choix == 7:

            if resultat is None:
                print("\n Aucune simulation disponible.")

            else:
                chemin, _, _, _, villes = resultat

                visualisation.afficherGraphe(villes, chemin)

        elif choix == 8:

            if resultat is None:
                print("\n Aucune simulation disponible.")

            else:
                _, _, _, historiqueDistance, _ = resultat

                visualisation.afficherHistorique(historiqueDistance)

        elif choix == 0:
            state = False

        else:
            print("\n Choix invalide. Erreur.")


def menuCSV() -> None:
    """
    Menu de gestion du fichier CSV.
    """

    state: bool = True
    while state:

        print("\n")
        print("┌─────────────────────────────────────────────┐")
        print("│                GESTION CSV                  │")
        print("├─────────────────────────────────────────────┤")
        print("│ [1] Lire les données                        │")
        print("│ [2] Sauvegarder le CSV                      │")
        print("│ [3] Vider le CSV                            │")
        print("│ [0] Retour                                  │")
        print("└─────────────────────────────────────────────┘")

        choix = int(input("\nVotre choix : "))

        if choix == 1:

            donnees = csvGestion.lireCsv()

            print("\nDonnées du CSV :")

            for ligne in donnees:
                print(ligne)

        elif choix == 2:

            csvGestion.sauvegarderCSV(csvGestion.nomFichier)

            print("\n Sauvegarde effectuée.")

        elif choix == 3:

            confirmation = input("\n Vider le CSV ? [o/n] : ")

            if confirmation.lower() == "o":

                csvGestion.viderCSV(csvGestion.nomFichier)

                print("\n CSV vidé.")

            else:

                print("\nOpération annulée.")

        elif choix == 0:
            state = False

        else:
            print("\n Choix invalide. Erreur.")


def main() -> None:
    """
    Fonction principale du programme.

    Le programme reste dans une boucle jusqu'à ce
    que l'utilisateur choisisse de quitter.
    """

    resultat = None

    animationDemarrage()

    csvGestion.creeCsv()

    state: bool = True
    while state:

        afficherMenuPrincipal()

        try:

            choix = int(input("\nVotre choix : "))

            if choix == 1:

                resultat = lancerSimulation()

            elif choix == 2:

                configuration = ConfigurationACO(nombreVilles = int(input("\nNombre de villes : ")))

                print("""\nParamètre à faire varier :\n\t[1] Nombre de fourmis\n\t[2] Nombre d'itérations\n\t[3] ALPHA\n\t[4] BETA\n\t[5] EVAPORATION\n\t[6] Q""")

                choixUser = int(input("\nParamètre à faire varier : "))

                minimum = float(input("Valeur minimum : "))

                maximum = float(input("Valeur maximum : "))

                pas = float(input("Pas : "))

                resultatStatistique = statistiques.statistic(configuration, choixUser, minimum, maximum, pas)

                if resultatStatistique is not None:

                    cheminFinal, distanceFinal, villes, historiqueFinal = resultatStatistique

                    resultat = (cheminFinal, distanceFinal,None, historiqueFinal, villes)

                    print("\n\tMeilleur résultat de l'étude :")
                    print(f"Distance : {distanceFinal}")
                    print(f"Chemin   : {cheminFinal}")

            elif choix == 3:

                menuVisualisation(resultat)

            elif choix == 4:

                menuCSV()

            elif choix == 0:

                print("\n")
                afficherFourmi2()

                print("Simulation OVER...")

                time.sleep(1)

                print("\nMerci d'avoir utilisé ACO, à bientôt...")
                print(greek(5))

                state = False

            else:

                print("\n Choix invalide.")

        except ValueError as erreur:

            print(f"\nErreur : {erreur}")

        except KeyboardInterrupt:

            print("\n\n Programme interrompu.")
            state = False


if __name__ == "__main__":
    # python3 main.py

    main()
