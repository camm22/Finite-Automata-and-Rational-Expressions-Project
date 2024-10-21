from fonction_menu import *

print(blanc + "\n###################################################################\n##############{-Projet : Traitement d'automate fini-}##############\n###################################################################")
print(rouge + "\n*Vous pouvez quitter le programme ou revenir en arrière à tout moment en entrant \"q\" lors des inputs*")

#Début du programme

choixVeri = []

for i in range(1, 44+1):
    choixVeri.append(str(i))

choixVeri.append('q')

# valeur possible pour la saisie sécurisée

while 1:

    # boucle while infini qui fait tourner le programme jusqu'à son arrêt (boucle principale)

    print(bleu + "\n[-]Le programme possède actuellement", len(choixVeri) - 1, "automates. Lequel voulez-vous exécuter ?" + normal)

    # choix de l'automate testé

    choix = input(" ---> :")
    while choix not in choixVeri or choix in ['31', '32', '33', '34', '35']:
        if choix in ['31', '32', '33', '34', '35']:
            print(rouge + "\n[!]Oups, il semblerait que cet automate ne soit plus au programme..." + normal)
        else :
            print(rouge + "\n[!]Cet automate n'existe pas. Veuillez réessayer." + normal)
        choix = input(" ---> :")

    # saisie sécurisé

    if choix == 'q':
        print(blanc + "\n###################################################################\n###########################{-Au revoir-}###########################\n###################################################################" + normal)
        break

    # "q" pour quitter le programme

    chemin = "automates_de_test\\C1-" + choix + ".txt"

    # création du chemin le l'automate à exécuter


    menu(True, chemin, choix, '', False, False)

    # appel de la focntion menu
