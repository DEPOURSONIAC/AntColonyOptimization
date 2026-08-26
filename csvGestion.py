# coding: utf-8

from datetime import datetime
import os
import csv
import shutil

"""
Gestion des fichiers CSV pour l'import et l'export des données.
"""

nomFichier: str = "acoData.csv"

entetesCSV: list = ["villes", "fourmis", "iterations", "alpha", "beta", "Q", "evaporation", "meilleureDistance", "tempsExecution"]


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

    if not os.path.isfile(nomFichier):

        # os.path.isfile dit si le fichier xxxx existe ou non (alors on répond TRUE / FALSE)
        with open(nomFichier, mode="w", newline="") as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow(entetesCSV)


def ajoutCsv(villes: int, fourmis: int, iterations: int, alpha: float, beta: float, evaporation: float, q: float, meilleureDistance: float, tempsExecution: float) -> None:
    """
    ajoutCsv(villes, fourmis, iterations, alpha, beta, evaporation, q, meilleureDistance, tempsExecution):

        Para :
            - villes (int) : nombre de villes
            - fourmis (int) : nombre de fourmis
            - iterations (int) : nombre d'itérations
            - alpha (float) : constante
            - beta (float) : constante
            - evaporation (float) : constante
            - q (float) : constante
            - meilleureDistance (float) : meilleure distance entre le point A et B
            - tempsExecution (float) : temps pour trouver la meilleure distance (en sec)

        Création :
            - ajoute une simulation dans le fichier CSV

    Return :
        - None
    """

    # On vérifie que le fichier existe avec son en-tête
    creeCsv()

    with open(nomFichier, mode="a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([villes, fourmis, iterations, alpha, beta, q, evaporation, meilleureDistance, tempsExecution])


def lireCsv() -> list:
    """
    lireCsv():

            Para :
                - aucun

            Création :
                - lit toutes les données du CSV

        Return :
            - liste des données
    """

    # On vérifie que le fichier existe
    creeCsv()

    donnees: list = list()

    with open(nomFichier, mode="r", newline="") as csvfile:

        reader = csv.reader(csvfile)

        for ligne in reader:
            donnees.append(ligne)

    return donnees


def lireColonne(nomColonne: str) -> list:
    """
    lireColonne(nomColonne):

            Para :
                - nomColonne (string) : un nom de colonne parmi :
                  villes, fourmis, iterations, alpha, beta,
                  Q, evaporation, meilleureDistance, tempsExecution

            Explication :
                - choisit l'entête et en fonction de celui-ci récupère le paramètre

        Return :
            - liste des données en fct de la colonne

    """

    donnees = lireCsv()

    entetes = donnees[0]

    if nomColonne not in entetes:
        raise ValueError(f"La colonne '{nomColonne}' n'existe pas dans le CSV.")

    indice = entetes.index(nomColonne)

    colonne = []

    for ligne in donnees[1:]:
        colonne.append(float(ligne[indice]))

    return colonne


def sauvegarderCSV(nomFichier: str) -> None:
    """
    sauvegarderCSV(nomFichier):

            Para :
                - nomFichier (string) : le fichier qu'on sauvegarde

            Explication :
                - on sauvegarde le fichier dans le repertoire sauvegarde
                  avec comme nom le datetime (l'heure de la sauvegarde)

        Return :
            - None

    """

    # On vérifie si le dossier existe sinon on le crée
    os.makedirs("sauvegardes", exist_ok=True)

    temps = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    nomSauvegarde = os.path.join("sauvegardes", f"{temps}.csv")

    shutil.copy(nomFichier, nomSauvegarde)


def viderCSV(nomFichier: str) -> None:
    """
    viderCSV(nomFichier):

            Para :
                - nomFichier (string) : le fichier à vider

            Explication :
                - on vide le fichier sauf l'entête

        Return :
            - None

    """

    with open(nomFichier, mode="w", newline="") as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow(entetesCSV)


if __name__ == "__main__":
    # python3 csvGestion.py

    creeCsv()

    ajoutCsv(100, 100, 50, 1, 1, 1, 1, 100, 10)

    donnees = lireCsv()

    for ligne in donnees:
        print(ligne)

    print("Meilleur distance: ", lireColonne("meilleureDistance"))

    sauvegarderCSV(nomFichier)
    viderCSV(nomFichier)