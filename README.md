# AntColonyOptimization (ACO)

## Projet et présentation de celui-ci.
Le projet **Ant Colony Optimization (ACO)** est une simulation du comportement des fourmis.

Le but est de résoudre des problèmes d’optimisation (comme trouver le chemin le plus court entre plusieurs villes ou le meilleur chemin pour envoyer des paquets IP avec RIP/ OSPF (Réseaux)) en imitant la nature :
les fourmis déposent des phéromones pour guider les autres.

---

## Idée générale

Voici le fonctionnement :
- Chaque fourmi explore un réseau de points (villes)
- Elle choisit ses chemins en fonction :
  des phéromones (expérience d'une autre fourmi)
  de la distance
- Les bons chemins sont renforcés
- Les mauvais chemins disparaissent avec le temps (car il y a moins de phéromones)

Le système converge vers un truc correcte.

---

## Fonctionnement
a. Création du graphe (villes + distances)  
b. Initialisation des fourmis  
c. Chaque fourmi construit un chemin  
d. Calcul de la qualité du chemin  
e. MAJ des phéromones  
f. Répétition sur plusieurs itérations  
g. Récupération du meilleur chemin  

---

## Paramètres mathématiques
- **α (alpha)** -> importance des phéromones (mémoire du système)
- **β (beta)** -> importance de la distance
- **évaporation** -> disparition des phéromones avec le temps
- **nombre de fourmis** -> intensité de l’exploration
- **nombre d’itérations** -> durée de convergence / temps de calcul

---

## Organisation du projet ACO

### main.py (point d’entrée)
- Lance toute la simulation
- Appelle les différents modules
- Affiche les résultats finaux

---

### moduleAco.py (logique ACO)
- Calcul des probas sur les chemins
- Mise à jour des phéromones
- Construction des chemins

C’est le cerveau/ le coeur de l’algorithme.

---

### tools.py (outils)
- Calcul des distances entre villes
- Gestion des matrices
- Fonctions utilitaires

Sert à simplifier le code principal.

---

### csvGestion.py
- Création du fichier CSV
- Ajout des résultats d’expérimentations
- Lecture des données

Permet de stocker et réutiliser les résultats de simulation.

---

### statistiques.py 
- Lancement de plusieurs tests automatiques
- Variation des paramètres ( nombre de fourmis, itérations etc...)
- Appel de l’ACO en boucle
- Génération des données pour analyse
  
---

### visualisation.py 
- Lecture du CSV
- Génération des graphiques avec Matplotlib
- Visualisation des performances (distance / temps / paramètres)

Permet d’interpréter les résultats.

### xxxxx.py (test/ beta)
-  Utilisation de Pygame
-  Design améliorer
-  Visualisation des résultats

Simulation graphique pour rendre ça plus beau.

---

### README.md
- Présentation du projet
- Explication rapide du fonctionnement
- Architecture globale
- Instructions pour lancer le programme

Le but est d’expliquer le projet et comment il est structuré.

---

## Outils que je vais utiliser
- **Python** -> langage principal
- **NumPy** -> calculs rapides sur matrices
- **Matplotlib** -> visualisation des chemins et résultats
- **CSV** -> stockage des résultats d’expérimentations
- (optionnel) interface graphique avec Tkinter ou Pygame (si j'ai le temps)

---

## Objectifs
- Simuler un système intelligent inspiré de la nature
- Capter un algorithme d’opti
- Résoudre un problème complexe ( genre TSP/ voyageur du commerce)

---

## Cas concrets
- Optimisation de chemins (GPS, livraison)
- Réseaux télécom (routage)
  > Je me permets de mettre routage car je suis en R&T XD
- Logistique
- Intelligence artificielle (optimisation globale des LLMs)

---

## GROSSO MODO
Des fourmis explorent un chemin( plusieurs villes).

Elles laissent des traces.
Les bonnes solutions sont renforcées.
Le système finit par trouver un bon chemin sans être programmé pour ça.

