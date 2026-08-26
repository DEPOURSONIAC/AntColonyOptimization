# coding: utf-8

from dataclasses import dataclass
import numpy as np

from . import moduleAco
from .tools import creationDesVilles
from . import csvGestion

"""
Module contenant les statistiques et les expérimentations ACO.
"""

# On fait du POO en mode compresser t'as capté
@dataclass
class ConfigurationACO:
    """
    Configuration d'une simulation ACO.

    Permet d'éviter de faire circuler tous les paramètres
    indépendamment dans les différentes fonctions. Genre évite de retaper le init, self et tout...
    """

    nombreVilles: int = 100
    nombreFourmis: int = 100
    nombreIterations: int = 50

    ALPHA: float = 1.0
    BETA: float = 1.0
    EVAPORATION: float = 0.5
    Q: float = 100.0


def verifierConfiguration(configuration: ConfigurationACO) -> None:
    """
    verifierConfiguration(configuration):

        Vérifie que les paramètres de la configuration sont valides.

    Return :
        - None
    """

    if configuration.nombreVilles < 2:
        raise ValueError("Il faut au moins 2 villes.")

    if configuration.nombreFourmis <= 0:
        raise ValueError("Le nombre de fourmis doit être supérieur à 0.")

    if configuration.nombreIterations <= 0:
        raise ValueError("Le nombre d'itérations doit être supérieur à 0.")

    if configuration.ALPHA < 0:
        raise ValueError("ALPHA doit être supérieur ou égal à 0.")

    if configuration.BETA < 0:
        raise ValueError("BETA doit être supérieur ou égal à 0.")

    if configuration.EVAPORATION < 0 or configuration.EVAPORATION > 1:
        raise ValueError("EVAPORATION doit être comprise entre 0 et 1.")

    if configuration.Q <= 0:
        raise ValueError("Q doit être supérieur à 0.")


def afficherConfiguration(configuration: ConfigurationACO) -> None:
    """
    afficherConfiguration(configuration):

        Affiche les paramètres utilisés pour la simulation.

    Return :
        - None
    """

    print("\n----------------------------")
    print("Para de la simulation")
    print("----------------------------")

    print(f"Nb de villes          : {configuration.nombreVilles}")
    print(f"Nb de fourmis         : {configuration.nombreFourmis}")
    print(f"Nombre d'itérations   : {configuration.nombreIterations}")
    print(f"ALPHA                 : {configuration.ALPHA}")
    print(f"BETA                  : {configuration.BETA}")
    print(f"EVAPORATION           : {configuration.EVAPORATION}")
    print(f"Q                     : {configuration.Q}")


def statistic(configuration: ConfigurationACO, choixUser: int, minimum: float, maximum: float,pas: float) -> tuple | None:
    """
    statistic(configuration, choixUser, minimum, maximum, pas):

        Para :
            - configuration : paramètres de base de l'ACO
            - choixUser     : paramètre que l'on veut faire varier
            - minimum       : valeur minimale à tester
            - maximum       : valeur maximale à tester
            - pas           : pas entre chaque valeur

        Création :
            - génère les villes
            - fait varier un seul paramètre
            - lance plusieurs simulations ACO
            - sauvegarde les résultats dans le CSV

    Return :
        - None si la simulation n'a pas pu être faite
        - (cheminFinal, distanceFinal, villes, historiqueFinal)
    """

    # Vérification de la configuration
    verifierConfiguration(configuration)

    if choixUser not in range(1, 7):
        raise ValueError("Choix invalide.")

    if minimum > maximum:
        raise ValueError("Le minimum doit être inférieur au maximum.")

    if pas <= 0:
        # C'est comme en PHP: throw new Exception("Message d'erreur ", 0);
        raise ValueError("Le pas doit être positif.")

    # Décla des variables
    cheminFinal: list[int] | None = None
    distanceFinal: float = np.inf
    historiqueFinal: list[float] | None = None

    villes = creationDesVilles(configuration.nombreVilles)

    valeur = minimum

    while valeur <= maximum:

        nbFourmis = configuration.nombreFourmis
        nbIterations = configuration.nombreIterations

        alpha = configuration.ALPHA
        beta = configuration.BETA
        evaporation = configuration.EVAPORATION
        q = configuration.Q

        # On modifie uniquement le paramètre du user
        match choixUser:

            case 1:
                if valeur != int(valeur):
                    raise ValueError("Le nombre de fourmis doit être un entier.")

                nbFourmis = int(valeur)

            case 2:
                if valeur != int(valeur):
                    raise ValueError("Le nombre d'itérations doit être un entier.")

                nbIterations = int(valeur)

            case 3:
                alpha = valeur

            case 4:
                beta = valeur

            case 5:
                evaporation = valeur

            case 6:
                q = valeur

        # Vérification des paramètres modifiés
        configurationTest = ConfigurationACO(configuration.nombreVilles, nbFourmis, nbIterations, alpha, beta, evaporation, q)

        verifierConfiguration(configurationTest)

        # Lancement de la simulation
        chemin, distance, temps, historiqueDistance = moduleAco.ACO(villes, nbFourmis, nbIterations, alpha, beta, evaporation, q)

        if distance < distanceFinal:
            cheminFinal = chemin
            distanceFinal = distance
            historiqueFinal = historiqueDistance

        print("\n----------")
        print(f"Valeur testée : {valeur}")
        print(f"Distance      : {distance}")
        print(f"Temps         : {temps}")

        # On ajoute dans le CSV
        csvGestion.ajoutCsv(configuration.nombreVilles, nbFourmis, nbIterations, alpha, beta, evaporation, q, distance, temps)

        # Flemme d'arrondir pour les incertitudes
        valeur += pas

    return cheminFinal, float(distanceFinal), villes, historiqueFinal

if __name__ == "__main__":
    # python3 statistiques.py

    print("Simulation / Test\n")

    configuration = ConfigurationACO()

    try:

        verifierConfiguration(configuration)

        afficherConfiguration(configuration)

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

        resultat = statistic(configuration, choixUser, minimum, maximum, pas)

        if resultat is not None:

            cheminFinal, distanceFinal, villes, historiqueFinal = resultat

            print("\nToutes les simulations sont terminées.")
            print("\n____________________________")
            print("Meilleur résultat obtenu")
            print("____________________________")

            print(f"Distance : {distanceFinal}")
            print(f"Chemin   : {cheminFinal}")
            print(f"\nHistoriqueFinal   : {historiqueFinal}")

    except ValueError as erreur:
        print(f"Erreur : {erreur}")