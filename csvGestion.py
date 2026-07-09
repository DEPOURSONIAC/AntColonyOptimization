# coding: utf-8

from datetime import datetime
import os
import csv
import shutil

"""
Gestion des fichiers CSV pour l'import et l'export des données.
"""

nomFichier: str = "acoData.csv"

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

    global nomFichier

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

    global nomFichier

    with open(nomFichier, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([villes, fourmis, iterations, alpha, beta, evaporation, q, meilleureDistance, tempsExecution])

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
    
    global nomFichier
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
                - choisit l'entete et en fonction de celui-ci récupère le paramètre
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

def sauvegarderCSV(nomFichier: str)-> None:
    """     
    sauvegarderCSV(nomFichier):

            Para :
                - nomFichier (string) :  le fichier qu'on sauvegarde

            Explication :
                - on sauvegarde le fichier dans le repertoire sauvegarde avec comme nonmle datetime (l'heure de la sauvegarde)
        Return :
            - None
    
    """
    
    # On vérifie si le dossier existe sinon on le crée
    os.makedirs("sauvegardes", exist_ok=True)
    
    temps = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    nomSauvegarde = os.path.join("sauvegardes", f"{temps}.csv")

    shutil.copy(nomFichier, nomSauvegarde)
    
def viderCSV(nomFichier: str)-> None:
    """
    viderCSV(nomFichier):

            Para :
                - nomFichier (string) :  le fichier a vider 

            Explication :
                - on vide le fichier sauf l'entete
        Return :
            - None
    
    """
    with open(nomFichier, mode="w", newline="") as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow(["villes","fourmis","iterations","alpha","beta", 'Q', "evaporation","meilleureDistance","tempsExecution"])

if __name__ == "__main__":
    # python3 csvGestion.py


    creeCsv()

    ajoutCsv(100, 100, 50, 1, 1, 1,1, 934, 6)

    donnees = lireCsv()

    for ligne in donnees:
        print(ligne)

    print(lireColonne('meilleureDistance'))


    sauvegarderCSV(nomFichier)
    viderCSV(nomFichier)