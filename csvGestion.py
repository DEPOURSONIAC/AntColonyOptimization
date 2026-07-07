# coding: utf-8

import os
import csv

"""
Gestion des fichiers CSV pour l'import et l'export des données.
"""

def creeCsv() -> None:
    """
    creeCsv()

    Paramètres :
        - aucun

    Explication :
        - crée le fichier CSV
        - ajoute l'en-tête s'il n'existe pas

    Retour :
        - None
    """

    nomFichier : str = "acoData.csv"

    if not os.path.isfile(nomFichier):

        # os.path.isfile dit si le fichier xxxx existe ou non (alors on répond TRUE/ FALSE)
        with open(nomFichier, mode="w", newline="") as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow(["villes","fourmis","iterations","alpha","beta", 'Q', "evaporation","meilleureDistance","tempsExecution"])

def ajoutCsv(villes: float, fourmis: float, iterations: float, alpha: int, beta: float, evaporation: float, q: float, meilleureDistance: float, tempsExecution: float) -> None:
    """
    ajoutCsv(villes, fourmis, iterations, alpha, beta, evaporation, q, meilleureDistance, tempsExecution):

        Para :
            - villes (float) : nombre de villes 
            - fourmis (float) : nombre de fourmis
            - iterations (float) : nombre d'itérations
            - alpha (float) : constante
            - beta (float) : constante
            - evaporation (float) : constante
            - q (float) : constante
            - meilleureDistance (float) : meilleur distance entre le point A et B (en m)
            - tempsExecution (float) : temps pour trouver la meilleure distance (en sec)

        Création :
            - ajoute une simulation dans le fichier CSV

    Return :
        - None
    """

    nomFichier: str = "acoData.csv"

    with open(nomFichier, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([villes, fourmis, iterations, alpha, beta, evaporation, q, meilleureDistance, tempsExecution])

def lireCsv() -> list:
    """
    lireCsv():

            Para :
                - aucun

            Création :
                - Lit toutes les données du CSV
        Return :
            - liste des données
    """
    
    nomFichier: str = "acoData.csv"
    donnees : list = list()

    with open(nomFichier, mode="r", newline="") as csvfile:
        reader = csv.reader(csvfile)

        for ligne in reader:
            donnees.append(ligne)

    return donnees

def lireColonne(nomColonne: str)->list:
    """
    lireColonne(nomColonne):

            Para :
                - nomColonne (string) :  un nom de colonne parmit : villes, fourmis, iterations, alpha, beta,  Q,evaporation, meilleureDistance, tempsExecution

            Explication :
                - Choisit l'entete et en fonction de celui-ci récupère le paramètre
        Return :
            - liste des données en fct de la colonne
    
    """
    donnees = lireCsv()

    entetes = donnees[0]
    indice = entetes.index(nomColonne)

    colonne = []

    for ligne in donnees[1:]:
        colonne.append(float(ligne[indice]))

    return colonne

if __name__ == "__main__":
    # python3 csvGestion.py


    creeCsv()

    ajoutCsv(100, 100, 50, 1, 1, 1,1, 934, 6)

    donnees = lireCsv()

    for ligne in donnees:
        print(ligne)

    print(lireColonne('meilleureDistance'))