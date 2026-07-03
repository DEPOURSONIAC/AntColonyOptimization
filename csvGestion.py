# coding: utf-8
import os
import csv

# Procédure
def creeCsv() -> None:
    """
    Crée le fichier CSV et ajoute l'en-tête s'il n'existe pas.
    """

    nomFichier : str = "acoData.csv"

    if not os.path.isfile(nomFichier):
        # os.path.isfile dit si le fichier xxxx existe ou non (alors on répond TRUE/ FALSE)
        with open(nomFichier, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["villes","fourmis","iterations","alpha","beta","evaporation","meilleureDistance","tempsExecution"])

def ajoutCsv(villes, fourmis, iterations, alpha, beta, evaporation, meilleureDistance, tempsExecution) -> None:
    """
    Ajoute une simulation dans le fichier CSV.
    """
    nomFichier : str = "acoData.csv"

    with open(nomFichier, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([villes,fourmis,iterations,alpha,beta,evaporation,meilleureDistance,tempsExecution])

def lireCsv() -> list:
    """
    Lit toutes les données du CSV et les retourne.
    """
    nomFichier = "acoData.csv";
    donnees : list = list()

    with open(nomFichier, mode="r", newline="") as csvfile:
        reader = csv.reader(csvfile)

        for ligne in reader:
            donnees.append(ligne)

    return donnees


if __name__ == "__main__":
    # print('HelloWorld')


    creeCsv()

    ajoutCsv(100, 100, 50, 1, 1, 1,  934, 6)

    donnees = lireCsv()

    for ligne in donnees:
        print(ligne)