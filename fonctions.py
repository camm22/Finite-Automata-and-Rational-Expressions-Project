import time


def pause(n):
    time.sleep(n)


montemps = 2


def changerNom(veri):
    if not veri:
        return False

    print(bleu + "\n[?]Voulez-vous renommer les états de l'automate pour une meilleure lisibilité ?" + normal + "\n   [1]Oui.\n   [2]Non.")

    choix = input(" ---> :")
    while choix not in ['1', '2']:
        print(rouge + "\n[!]Choix incorrecte, veuillez réessayer." + normal)
        choix = input(" ---> :")

    if choix == '1':
        return True
    else:
        return False


def ensemble(n, i, m):

    if n == 0:
        if i == 0:
            return 'T'
        if i == 1:
            return 'NT'

    mystr = ""
    for k in range(m):
        mystr += "I"
    return mystr


def infoMinimiser(n, num, oN):
    pause(montemps)

    print(rouge +'\n[' + num + ']' + normal + ' θ' + n + " = {", end="")

    m = 0
    veri = True
    for i in range(len(oN)):
        if type(oN[i]) == list:
            m += 1
            veri = False
            print(ensemble(int(n), i, m), end="")
        else:
            print(oN[i], end="")

        if i + 1 != len(oN):
            print(', ', end="")

    if veri:
        print('} = θfin')
    else:
        print('}')

    m = 0
    for i in range(len(oN)):
        if type(oN[i]) == list:
            m += 1
            print("    -" + ensemble(int(n), i, m) + " = {", end='')

            for j in range(len(oN[i])):
                print(oN[i][j], end='')
                if j + 1 != len(oN[i]):
                    print(', ', end='')
            print('}')


def infoComplet(veri, transition):

    # affiche les information de déterminisé  avec les accords de singulier / pluriel

    nb = len(transition)

    final = jaune + "   [•]" + normal

    if veri == True:
        final += "Cet automate est complet"
    else:
        final += "Cet automate n'est pas complet car "

        if nb == 1:
            accord1 = "la transition "
            accord2 = "ne mène "
        else:
            accord1 = "les transitions "
            accord2 = "ne mènent "

        final += accord1

        for i in range(len(transition)):
            final += "|" + transition[i] + "| "

        final += accord2 + "à rien"

    final += "."
    print(final)


def infoDerterministe(veri, condition1, condition2, transition, nb):

    # affiche les information de déterminisé  avec les accords de singulier / pluriel

    accord_et = ""
    if condition1 == False:
        if condition2 == False:
            accord_et = " et "

    final = jaune + "   [•]" + normal

    if veri == True:
        final += "Cet automate est déterministe"
    else:
        final += "Cet automate n'est pas déterministe car "

        if condition1 == False:
            final += "il possède " + nb + " entrées"

        final += accord_et

        if condition2 == False:
            final += "il y a ambiguïté au niveau des transitions"

            for i in range(len(transition)):
                final += " |" + transition[i] + "|"

    final += "."

    print(final)


def infoStandard(veri, condition1, condition2, transition, nb):

    # affiche les information de standard avec les accords de singulier / pluriel

    accord_et = ""
    if condition1 == False:
        if condition2 == False:
            accord_et = " et "

    final = "\n" + jaune + "   [•]" + normal

    if veri == True :
        final += "Cet automate est standard"
    else:
        final += "Cet automate n'est pas standard car "

        if condition1 == False:
            final += "il possède " + nb + " entrées"

        final += accord_et

        if condition2 == False:

            if len(transition) == 1:
                accord1 = "la transition "
                accord2 = "mène "
            else:
                accord1 = "les transitions "
                accord2 = "mènent "

            if condition1 == False:
                accord3 = "aux états initiaux"
            else:
                accord3 = "à l'état initial"

            final += accord1

            for i in range(len(transition)):
                final += "|" + transition[i] + "| "

            final += accord2 + accord3

    final += "."

    print(final)

# définition de toutes les couleurs utilisées

normal = "\033[0m"
bleu = "\033[0;94m"
rouge = "\033[0;91m"
jaune = "\033[0;93m"
vert = "\033[0;32m"
blanc = "\033[0;97m"
gras = "\033[1m"
