# coding: utf-8

import moduleAco
import csvGestion


def statistic() -> None:
    """
    Lance plusieurs simulations ACO en faisant varier
    un seul paramètre choisi par le user

    Flemme de faire une docstring détaillé comme les autres zeubi
    """

    print("-------------------------")
    print("----- Statistique ACO ----")
    print("-------------------------")

    # Décla des variables par défauts
    nombreVilles = int(input("\nNombre de villes : "))

    nombreFourmis    : int = 100
    nombreIterations : int = 50

    ALPHA       : float  = 1.0
    BETA        : float  = 1.0
    EVAPORATION : float  = 0.5
    Q           : float  = 100

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
        chemin, distance, temps, villes, distances = moduleAco.ACO(nombreVilles, nbFourmis, nbIterations, alpha, beta, evaporation, q)

        print("\n----------")
        print("Valeur testée :", valeur)
        print("Distance :", distance)
        print("Temps :", temps)

        #  On ajoute dans le CSV
        csvGestion.ajoutCsv(nombreVilles, nbFourmis, nbIterations,alpha, beta,evaporation, q, distance, temps)

        valeur += pas

    print("\nToutes les simulations sont terminées.")


if __name__ == "__main__":
    # print("helloWorld")

    # python3 statistiques.py

    print("Simulation / Test\n")

    statistic()

"""
Simulation / Test

-------------------------
----- Statistique ACO ----
-------------------------

Nombre de villes : 100

Quel paramètre voulez-vous faire varier ?
1 - Nombre de fourmis
2 - Nombre d'itérations
3 - Alpha
4 - Beta
5 - Evaporation
6 - Q

Votre choix : 2
Valeur minimum : 1
Valeur maximum : 50
Pas : 1

----------
Valeur testée : 1.0
Distance : 3114.8890295648253
Temps : 0.5464139519999662

----------
Valeur testée : 2.0
Distance : 2769.642570895367
Temps : 1.0420720820002316

----------
Valeur testée : 3.0
Distance : 2712.6550274134156
Temps : 1.5311853370003519

----------
Valeur testée : 4.0
Distance : 1983.9305588769255
Temps : 2.0758173180001904

----------
Valeur testée : 5.0
Distance : 1742.732600682618
Temps : 2.5810786689999077

----------
Valeur testée : 6.0
Distance : 1307.6083814983133
Temps : 3.0592838619995746

----------
Valeur testée : 7.0
Distance : 1401.4867954781298
Temps : 3.5966743290000522

----------
Valeur testée : 8.0
Distance : 1337.9566239759208
Temps : 4.11495510199984

----------
Valeur testée : 9.0
Distance : 1239.8917734332058
Temps : 4.923595819000184

----------
Valeur testée : 10.0
Distance : 1130.271220628137
Temps : 5.478846770000018

----------
Valeur testée : 11.0
Distance : 1058.5494269521926
Temps : 5.859497170000395

----------
Valeur testée : 12.0
Distance : 1137.1533625436064
Temps : 6.1040750860001936

----------
Valeur testée : 13.0
Distance : 1115.161361499561
Temps : 6.589994592999574

----------
Valeur testée : 14.0
Distance : 1137.1201579658589
Temps : 7.066070244000002

----------
Valeur testée : 15.0
Distance : 1053.6736616700782
Temps : 7.662710734000029

----------
Valeur testée : 16.0
Distance : 1038.8300321104794
Temps : 7.999809949000337

----------
Valeur testée : 17.0
Distance : 1083.6339439490673
Temps : 8.439135953000005

----------
Valeur testée : 18.0
Distance : 1056.1050993880474
Temps : 8.965323636999528

----------
Valeur testée : 19.0
Distance : 1011.0752847684242
Temps : 9.52569767499972

----------
Valeur testée : 20.0
Distance : 1023.1200778612969
Temps : 9.922838385999967

----------
Valeur testée : 21.0
Distance : 1003.189601349367
Temps : 10.606499831000292

----------
Valeur testée : 22.0
Distance : 1057.4312656925383
Temps : 11.194184486999802

----------
Valeur testée : 23.0
Distance : 1001.029310679904
Temps : 12.18958970499989

----------
Valeur testée : 24.0
Distance : 995.5233515251238
Temps : 12.61500939600046

----------
Valeur testée : 25.0
Distance : 1047.579970063069
Temps : 13.617603521999627

----------
Valeur testée : 26.0
Distance : 1001.139512739609
Temps : 14.151809572000275

----------
Valeur testée : 27.0
Distance : 1028.1937113277315
Temps : 14.17859415699968

----------
Valeur testée : 28.0
Distance : 1015.5057449430873
Temps : 14.022082421999585

----------
Valeur testée : 29.0
Distance : 937.1074712675749
Temps : 15.058045013000083

----------
Valeur testée : 30.0
Distance : 933.8112065127199
Temps : 14.924980939999841

----------
Valeur testée : 31.0
Distance : 987.9974748208285
Temps : 15.998267986999963

----------
Valeur testée : 32.0
Distance : 1016.2356740300679
Temps : 16.696211020999726

----------
Valeur testée : 33.0
Distance : 1024.9470072467968
Temps : 16.64845802199943

----------
Valeur testée : 34.0
Distance : 1016.577109795597
Temps : 17.443725374000678

----------
Valeur testée : 35.0
Distance : 986.452933587742
Temps : 17.248421459999918

----------
Valeur testée : 36.0
Distance : 1003.968704085702
Temps : 19.26373505399988

----------
Valeur testée : 37.0
Distance : 1037.3321563134173
Temps : 19.36139857300077

----------
Valeur testée : 38.0
Distance : 946.6563231869204
Temps : 20.9935247479998

----------
Valeur testée : 39.0
Distance : 998.5386703075385
Temps : 19.574040810000042

----------
Valeur testée : 40.0
Distance : 1037.6041043228474
Temps : 20.77210617899982

----------
Valeur testée : 41.0
Distance : 911.8679699482796
Temps : 21.115272898000512

----------
Valeur testée : 42.0
Distance : 1039.6428978563208
Temps : 20.76244141999996

----------
Valeur testée : 43.0
Distance : 1022.2943954490977
Temps : 21.44333247800023

----------
Valeur testée : 44.0
Distance : 933.0987681797768
Temps : 22.66382109999995

----------
Valeur testée : 45.0
Distance : 1003.345870473885
Temps : 22.2535261539997

----------
Valeur testée : 46.0
Distance : 1033.4542003666534
Temps : 23.90855947899945

----------
Valeur testée : 47.0
Distance : 937.6858332537762
Temps : 23.79155546000038

----------
Valeur testée : 48.0
Distance : 897.1724668446093
Temps : 23.900849256000583

----------
Valeur testée : 49.0
Distance : 967.8581338832804
Temps : 24.31394840200028

----------
Valeur testée : 50.0
Distance : 1028.1216658116182
Temps : 25.33771377999983

"""