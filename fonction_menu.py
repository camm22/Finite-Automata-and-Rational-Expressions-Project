from automate import *

# la fonction menu est la fonction qui permet de faire tourner et de structurer le programme et qui permet de choisir l'opérantion à effetuer sur les différents automates
# la fonction menu est une fonction récursive qui fera toujour la même chose :  afficher l'automate, lui donner ses informations et lui donner ses opérations possible en fonction
# la récursivité permet de faire un cycle car après une opération choisit, le cycle permet de d'afficher l'automtae mis à jour et ainsi de suite.
# la fonction prend en paramètre power qui est l'une des condtions d'arret dans certaines situations, chemin pour savoir quel
# automate doit être exécuter, le numéro de l'automate, l'adjectif pour savoir dans quel forme il est, veriminimisé pour savoir si l'automate vient
# d'être minimisé ou non et versiStandard qui fait pareil

def menu(power, chemin, choixAutomate, adjectif, veriMinimiser, onStandard):
    print(jaune + "\n[*]Voici la table de transition de l'automate n°" + choixAutomate + " " + adjectif + " :\n" + normal)

    automate = Automate()
    automate.lireAutomateSurFichier(chemin)
    automate.afficherAutomate()

    # initilisation de l'automate en fontion du chemin et et affichage de l'automate

    veriStandard = automate.estStandard(True)
    veriDerterministe = automate.estDeterministe(True)
    veriComplet = automate.estComplet(True)

    # appel des fonctions d'information

    if power == False:
        return
    # condition d'arrêt

    print(bleu + "\n[-]Que voulez-vous faire ?" + normal)

    num = 0
    choixVeri = []

    if onStandard:
        veriStandard = True

    if veriStandard == False:
        num += 1
        choixVeri.append(str(num))
        print("   [" + str(num) + "]Standardiser l'automate.")
    if veriDerterministe == False:
        num += 1
        choixVeri.append(str(num))
        print("   [" + str(num) + "]Déterminiser l'automate.")
    elif veriDerterministe == True and veriComplet == False:
        num += 1
        choixVeri.append(str(num))
        print("   [" + str(num) + "]Compléter l'automate.")
    elif veriDerterministe == True and veriComplet == True:
        if not veriMinimiser:
            num += 1
            choixVeri.append(str(num))
            print("   [" + str(num) + "]Minimiser l'automate.")

        num += 1
        choixVeri.append(str(num))
        print("   [" + str(num) + "]Lire des mots.")

    choixVeri.append('q')

    # cet ensemble de if permet de d'afficher les différentes possibilités d'information en fonction des fonctions d'information
    # cet ensemble permet aussi de créer les valeurs autorisées pour la saisie sécrusiée

    choix = input(" ---> :")
    while choix not in choixVeri:
        print(rouge + "\n[!]Choix incorrecte, veuillez réessayer." + normal)
        choix = input(" ---> :")

    # saisie sécurisée

    if choix == 'q':
        print(rouge + "\n[*]Retour arrière." + normal)

    # retour arrière

    else:

        # série de if avec condition en fonction du choix de l'opréation mais aussi du résultat des différentes fonction d'opération

        if choix == '1' and veriStandard == False:

            automate.standardiserAutomate()
            menu(False, "exe.txt", choixAutomate, "standard", False, True)
            # standardiser automate et appel de menu()

        elif (choix == '1' and veriDerterministe == False) or (choix == '2' and veriDerterministe == False):

            automate.determiniserAutoamte()
            menu(True, "exe.txt", choixAutomate, "déterministe", False, True)

            # déterminiser  automate et appel de menu()

        elif veriDerterministe == True and veriComplet == False:
            if choix == '1' or choix == '2':

                automate.completerAutomate()
                menu(True, "exe.txt", choixAutomate, "déterministe et complet", False, True)

                # compléter automate et appel de menu()

        elif veriDerterministe == True and veriComplet == True:

            # si déterministe et complet

            if (choix == '2' and veriStandard == False and veriMinimiser == False) or (choix == '1' and veriStandard == True and veriMinimiser == False):

                if changerNom(True):
                    automate.renommerAutomate()

                print(rouge + "\n----------------[MINIMISATION]---------------\n" + normal)
                pause(montemps)

                #automate.renommerAutomate()

                automate.afficherAutomate()
                mot = "déterministe, complet et minimisé"
                deja = automate.minimiserAutomate()

                if deja:
                    mot += " (même si cet automate était déjà minimisé au maximum)"

                pause(montemps)

                automate2 = Automate()
                print()
                automate2.lireAutomateSurFichier("exe.txt")
                automate2.afficherAutomate()
                veriRetirer = automate2.retirerEtatInutile()
                if veriRetirer:
                    automate2.completerAutomate()
                    automate3 = Automate()
                    automate3.lireAutomateSurFichier("exe.txt")
                    automate3.afficherAutomate()

                pause(montemps)

                menu(True, "exe.txt", choixAutomate, mot, True, True)

                # minimisation de l'automate et appel de menu()

            if (choix == '2' and veriStandard == False and veriMinimiser == True) or (choix == '1' and veriStandard == True and veriMinimiser == True) or (choix == '3' and veriStandard == False and veriMinimiser == False) or (choix == '2' and veriStandard == True and veriMinimiser == False):
                print(bleu + "\n[?]Voulez-vous lire le langage normal ou le langage complémentaire ?" + normal + "\n   [1]Normal.\n   [2]Complémentaire.")

                # choix du langage lu

                chemin = "exe.txt"

                choix2 = input(" ---> :")
                while choix2 not in ['1', '2', 'q']:
                    print(rouge + "\n[!]Choix incorrecte, veuillez réessayer." + normal)
                    choix2 = input(" ---> :")

                # saisie sécurisée

                if choix2 == 'q':
                    print(rouge + "\n[*]Retour arrière." + normal)
                     #retour arrière

                elif choix2 == '1':
                    print(jaune + "\n[*]Lecture du langage de l'automate n°" + choixAutomate + " " + adjectif + " :\n" + normal)
                    automate.afficherAutomate()
                    automate.lireMotsAutomate(choixAutomate)
                    # affichage de l'automate en langage normal et lecture puis arrete de munu imediat

                elif choix2 == '2':
                    automate.complementariserAutomate()
                    automate2 = Automate()
                    automate2.lireAutomateSurFichier(chemin)
                    print(jaune + "\n[*]Lecture du langage complémentaire de l'automate n°" + choixAutomate + " " + adjectif + " :\n" + normal)
                    automate2.afficherAutomate()
                    automate2.lireMotsAutomate(choixAutomate)
                    # création et affichage de l'automate complméentariser et lecture puis arrete de munu imediat
