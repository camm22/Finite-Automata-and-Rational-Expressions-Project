import copy
from etat import*
from fonctions import *

# la class Automate et la structure principale du programme. Elle permet de stocker de gérer tous les automates des fichiers texte


class Automate:

    def __init__(self):
        self.nbAlphabet = 0
        self.alphabet = []
        self.nbEtat = 0
        self.etat = []
        self.nbEtatInitiaux = 0
        self.etatInitiaux = []
        self.nbEtatTerminaux = 0
        self.etatTerminaux = []
        self.nbTransition = 0
        self.transition = []

        self.listeFichierAutomate = []

        self.listeObjetEtat = []

        # constructeur qui initialise les attributs qui permettent de stocker les infomartions essentielles pour défiinir un automate

    def ecrireAutomate(self, nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition):

        with open("exe.txt", "w+", encoding="utf-8") as file:

            file.write(str(nbAlphabet))

            for lettre in alphabet:
                file.write(" " + lettre)

            file.write("\n" + str(nbEtat))

            for element in etat:
                file.write(" " + element)

            file.write("\n" + str(nbEtatInitiaux))

            for element in etatInitiaux:
                file.write(" " + element)

            file.write("\n" + str(nbEtatTerminaux))

            for element in etatTerminaux:
                file.write(" " + element)

            file.write("\n" + str(nbTransition) + "\n")

            for element in transition:
                file.write(element + "\n")

            file.close()

    def chargerEtats(self):

        for i in range(len(self.listeObjetEtat)):

            for cle, valeur in self.listeObjetEtat[i].transition.items():

                j = 0
                while valeur != self.listeObjetEtat[j].nom:
                    j += 1

                self.listeObjetEtat[i].objetTransition[cle] = self.listeObjetEtat[j]

    def lireMotsAutomate(self, choixAutomate):
        oui = vert + "OUI" + normal
        non = rouge + "NON" + normal

        quitter = False

        self.chargerEtats()

        i_ini = 0
        while self.listeObjetEtat[i_ini].etatInitial != 'E':
            i_ini += 1

        aj = rouge + "   [-]" + normal

        print("\n" + aj + "Entrer l'un après l'autre les mots à faire reconnaître par l'automate n°" + choixAutomate + ".")
        print(aj + "Pour lire le mot vide, entrer \"epsilon\".")
        print(aj + "Après avoir fini de rentrer vos différents mots, appuyer sur *entrer*.\n")
        print(bleu + "[:]Entrer vos différents mots :" + normal)

        reponse = []
        listeDeMots = []
        mot = None
        while mot != "":
            mot = input(" ---> :")
            if mot == "q":
                quitter = True
                break
            elif mot != "":
                listeDeMots.append(mot)

        if quitter or len(listeDeMots) == 0:
            print(rouge + "\n[*]Retour arrière." + normal)
            return

        for i in range(len(listeDeMots)):

            stop = False
            temp = self.listeObjetEtat[i_ini]

            if listeDeMots[i] == 'epsilon':
                stop = True
                if temp.etatInitial == 'E' and temp.etatTerminal == 'S':
                    reponse.append(oui)
                else:
                    reponse.append(non)

            j = 0
            while j < len(listeDeMots[i]) and not stop:
                if listeDeMots[i][j] not in self.alphabet:
                    stop = True
                    reponse.append(non)
                else:
                    temp = temp.objetTransition[listeDeMots[i][j]]

                j += 1

            if not stop:
                if temp.etatTerminal == 'S':
                    reponse.append(oui)
                else:
                    reponse.append(non)

        l = []
        for k in range(len(listeDeMots)):
             l.append(len(listeDeMots[k]))

        maxlong = max(l) + 1

        print(jaune + "\n[*]Lectutre :" + normal)
        for k in range(len(listeDeMots)):
            tiret = '-' * (maxlong - len(listeDeMots[k]))

            if k < 9:
                espace = ' '
            else :
                espace = ''

            print("   {" + str(k + 1) + "} " + espace + "\"" + blanc + listeDeMots[k] + normal + '\" ' + tiret + '--------> {' + reponse[k] + '}')

    def complementariserAutomate(self):
        nbAlphabet = copy.deepcopy(self.nbAlphabet)
        alphabet = copy.deepcopy(self.alphabet)
        nbEtat = copy.deepcopy(self.nbEtat)
        etat = copy.deepcopy(self.etat)
        nbEtatInitiaux = copy.deepcopy(self.nbEtatInitiaux)
        etatInitiaux = copy.deepcopy(self.etatInitiaux)

        etatTerminaux = []
        for element in etat:
            if element not in self.etatTerminaux:
                etatTerminaux.append(element)
        nbEtatTerminaux = len(etatTerminaux)

        nbTransition = copy.deepcopy(self.nbTransition)
        transition = copy.deepcopy(self.transition)

        self.ecrireAutomate(nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition)

    def fusionEtat(self, liste):

        liste2 = []
        liste3 = []
        mystr = ""
        veri1 = False
        veri2 = False

        for i in range(len(liste)):
            if 'P' in liste[i]:
                n = ""
                for j in range(len(liste[i])):
                    if liste[i][j] != 'P':
                        n += liste[i][j]
                liste[i] = n
                veri1 = True
            elif 'I' in liste[i]:
                n = ""
                for j in range(len(liste[i])):
                    if liste[i][j] != 'I':
                        n += liste[i][j]
                liste[i] = n
                veri2 = True
            elif liste[i] not in liste2 and liste[i] != '':
                liste2.append(liste[i])

        for element in liste2:
            liste3.append(int(element))

        while len(liste3) != 0:
            if str(max(liste3)) not in mystr:
                mystr += str(max(liste3))
            liste3.remove(max(liste3))

        mystr2 = ""
        for i in range(len(mystr)):
            if mystr[i] not in mystr2:
                mystr2 += mystr[i]

        if veri1 == True:
            mystr2 += 'P'
        if veri2 == True:
            mystr2 += 'I'

        return mystr2

    def veriMinimiser(self, oN):
        # est la condition d'arret de la minimisation, si il n'y a plus du tout d'ensemble dans oN, alors la
        # la minimisation est terminée
        veri = True
        for i in range(len(oN)):
            if type(oN[i]) == list:
                veri = False
        return veri

    def afficherAutomateMinimiser(self, oN, lesEtats, n):
        pause(montemps)

        print()

        liste = []

        re = 0

        for element in oN:
            if type(element) == list:
                liste.append(element)
            else:
                if len(element) > re:
                    re = len(element)

        longueurCase = max(self.longueurMaxEtat(), self.longueurMaxTransition())

        if re > longueurCase:
            longueurCase = re

        if longueurCase < 2:
            longueurCase = 2

        caseVide = " "*longueurCase

        print(blanc + gras + 2*caseVide + ' ', end=' ')

        for j in range(2):
            for i in range(self.nbAlphabet):
                print('|' + self.alphabet[i] + self.espace(longueurCase, len(self.alphabet[i])), end=' ')
            if j + 1 != 2:
                print('|', end='')

        print()

        for i in range(len(self.listeObjetEtat)):

            for j in range(len(liste)):

                for k in range(len(liste[j])):

                    if liste[j][k] == self.listeObjetEtat[i].nom:

                        temp = ''
                        temp += self.listeObjetEtat[i].etatInitial
                        temp += self.listeObjetEtat[i].etatTerminal
                        print(temp + self.espace(longueurCase, len(temp)) + '|' + self.listeObjetEtat[i].nom + self.espace(longueurCase, len(self.listeObjetEtat[i].nom)), end=' ')

                        for cle, valeur in self.listeObjetEtat[i].transition.items():
                            if valeur == '' or valeur == ' ':
                                print('|' + '-' + self.espace(longueurCase, len('-')), end=' ')
                            else:
                                print('|' + valeur + self.espace(longueurCase, len(valeur)), end=' ')

                        print('|', end='')

                        for cle, valeur in self.listeObjetEtat[i].transition.items():

                            m = 0
                            mystr = ''
                            for g in range(len(liste)):
                                m += 1
                                if valeur in liste[g]:
                                    mystr = ensemble(n, g, m)
                                else:
                                    for h in range(len(lesEtats)):
                                        if valeur in lesEtats[h]:
                                            mystr = self.fusionEtat(copy.deepcopy(lesEtats[h]))

                            print('|' + mystr + self.espace(longueurCase, len(mystr)), end=' ')

                        print()

    def minimiserAutomate(self):
        # fonction pour minimiser un automate

        nbAlphabet = copy.deepcopy(self.nbAlphabet)
        alphabet = copy.deepcopy(self.alphabet)
        etatInitiaux = []
        etatTerminaux = []
        transition = []

        lesEtats = []

        # on commence à initialiser les premières variables locales qui seront transmises à la fonction écrireAutomate
        # qui représente les attributs de l'automate
        T = []
        NT = []

        # On défit les premiers ensembles T et NT qui seront les premiers ensemble à être testé pour la minimisation

        for element in self.listeObjetEtat:

            if element.etatTerminal == 'S':
                T.append(element.nom)
            else:
                NT.append(element.nom)

        oN = [T, NT]

        # On remplit T et NT avec les états initiaux et non-initiaux et on les ajoute dans notre liste oN qui
        # stock tous nos états et ensemble durant la minimisation

        tour = 0

        infoMinimiser(str(tour), str(tour + 1), copy.deepcopy(oN))

        # On affiche On avec la fonction infoMinimiser() (O0)

        if len(T) == 1 and len(NT) == 1:
            infoMinimiser(str(tour + 1), str(tour + 2), [T[0], NT[0]])
            self.ecrireAutomate(nbAlphabet, alphabet, copy.deepcopy(self.nbEtat), copy.deepcopy(self.etat), copy.deepcopy(self.nbEtatInitiaux), copy.deepcopy(self.etatInitiaux), copy.deepcopy(self.nbEtatTerminaux), copy.deepcopy(self.etatTerminaux), copy.deepcopy(self.nbTransition), copy.deepcopy(self.transition))
            return True

        # Première condition qui vérifie s'il y a 1 état dans chaque ensemble T et NT car si c'est le cas,
        # la mininmisation est déjà fini

        while not self.veriMinimiser(oN):
            # On lance donc la minimisation avec une fonction veriMinimiser qui vérie si la minimisation est fini ou nan

            copie0nMin = copy.deepcopy(oN)
            copieLesEtats = copy.deepcopy(lesEtats)

            tour += 1

            tab = []
            for z in oN:
                if type(z) == list:
                    tab.append([])
            i_tab = -1

            # tableau stockera tous les etat ainsi que tous leurs ensembles affiliés à chacunes de leurs transitions mis dans une liste

            # boucle pour remplir tab
            for i in range(len(oN)):

                if type(oN[i]) == list:

                    i_tab += 1

                    for j in range(len(oN[i])):

                        for k in range(self.nbEtat):

                            if oN[i][j] == self.listeObjetEtat[k].nom:

                                ajout = [oN[i][j], []] # ce quoi expliqué juste avant donc un ajout dans tab pour chaque état encore présent dans oN à chaque tour

                                for cle, valeur in self.listeObjetEtat[k].transition.items():

                                    for n in range(len(oN)):

                                        if type(oN[n]) == list:

                                            if valeur in oN[n]:

                                                # si la valeur est dans un ensemble de oN et que l'une de ses transitions et dans l'un des ensembles de oN, alors on ajoute l'état dans le tableau ainsi que ses ensembles
                                                ajout[1].append(copy.deepcopy(oN[n]))

                                        else:
                                            # ici c'est la même chose mais quand ce n'est pas un ensemble donc un état simple
                                            if valeur == oN[n]:
                                                ajout[1].append(copy.deepcopy(oN[n]))

                                tab[i_tab].append(copy.deepcopy(ajout))

            copie0 = copy.deepcopy(oN)

            p = 0
            while p < len(oN):
                sup = True
                if type(oN[p]) == list:
                    del oN[p]
                    p = 0
                    sup = False

                if sup:
                    p += 1

            # On supprime les ensembles de oN car ils seront mis à jour juste apres

            for z in range(len(tab)):
                liste = []
                poubelle = []

                for i in range(len(tab[z])):

                    temp = tab[z][i][1]
                    ajout2 = []

                    if temp not in poubelle:

                        for j in range(len(tab[z])):

                            if temp == tab[z][j][1]:

                                ajout2.append(tab[z][j][0])

                        poubelle.append(temp)
                        liste.append(ajout2)

                if len(liste) == 1:
                    oN.append(self.fusionEtat(copy.deepcopy(liste[0])))
                    lesEtats.append(copy.deepcopy(liste[0]))

                else:
                    for i in range(len(liste)):

                        if liste[i] in copie0 or len(liste[i]) == 1:

                            oN.append(self.fusionEtat(copy.deepcopy(liste[i])))
                            lesEtats.append(copy.deepcopy(liste[i]))

                        else:
                            oN.append(liste[i])

            self.afficherAutomateMinimiser(copie0nMin, copieLesEtats, tour - 1)
            infoMinimiser(str(tour), str(tour + 1), copy.deepcopy(oN))
            # dans cette successions de boucle, on vient actualiser oN avec ses nouvelles valeurs. En efft,
            # on analyse chaque élément de tab et on regarde les doublons et les sigleton. Les sigletons deviendrons un
            # un état simple d'oN tandis que les doublons deviendront les prochains ensembles de oN

        for d in range(len(oN)):
            if type(oN[d]) == list:
                oN.append(copy.deepcopy(oN[d]))
                del oN[d]
        # on met les ensembles en fin de liste (pour des raisons de clarification)

        nbEtat = len(oN)
        etat = copy.deepcopy(oN)

        for i in range(len(lesEtats)):
            for j in range(len(lesEtats[i])):
                if lesEtats[i][j] in self.etatInitiaux:
                    etatInitiaux.append(copy.deepcopy(etat[i]))
                if lesEtats[i][j] in self.etatTerminaux:
                    etatTerminaux.append(copy.deepcopy(etat[i]))

        # on définit les etats, etats initiaux et terminaux de l'automate minimisé car on a oN-fin

        nbEtatInitiaux = len(etatInitiaux)
        nbEtatTerminaux = len(etatTerminaux)

        for i in range(len(lesEtats)):

            for j in range(nbAlphabet):

                arrivee = []

                for k in range(len(lesEtats[i])):

                    for n in range(len(self.listeObjetEtat)):

                        if lesEtats[i][k] == self.listeObjetEtat[n].nom:

                            for cle, valeur in self.listeObjetEtat[n].transition.items():

                                if alphabet[j] == cle:

                                    for element in lesEtats:

                                        if valeur in element:

                                            arrivee.append(valeur)

                                            for c in range(len(element)):

                                                if element[c] not in arrivee:

                                                    arrivee.append(copy.deepcopy(element[c]))

                transition.append(self.fusionEtat(copy.deepcopy(lesEtats[i])) + ';' + alphabet[j] + ';' + self.fusionEtat(copy.deepcopy(arrivee)))

        # dans cette succession de boucles, on vient créer les nouvelles transitions de l'automate minimisé
        # grace à lesEtats

        nbTransition = len(transition)

        self.ecrireAutomate(nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition)

        ver = True
        for i in range(len(self.etat)):
            if self.etat[i] not in etat:
                ver = False
        return ver

    def retirerEtatInutile(self):

        veri = False

        liste = []

        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():
                if valeur not in self.etat:
                    veri = True
                    self.listeObjetEtat[i].transition[cle] = ""
                    self.transition.remove(self.listeObjetEtat[i].nom + ';' + cle + ';' + valeur)
                    liste.append(valeur)
        if not veri:
            return veri

        printer = rouge + "\n[!]" + normal

        if len(liste) == 1:
            printer += " L'état "
            accord = "est inutile"
            accord2 = "le"
        else:
            printer += " Les états "
            accord = "sont inutiles"
            accord2 = "les"

        for i in range(len(liste)):
            printer += "|" + liste[i] + "| "

        printer += accord + ", il faut donc " + accord2 + " supprimer.\n"

        print(printer)
        pause(montemps)
        self.afficherAutomate()
        pause(montemps)
        print(rouge + "\n[*]" + normal + " Il faut maintenant le recompléter.\n")
        pause(montemps)
        return veri

    def renommerAutomate(self):
        nouveauEtat = []
        nouveauEtatInitiaux = []
        nouveauxEtatTerminaux = []
        nouveauTransitions = []

        for i in range(self.nbEtat):
            nouveauEtat.append(str(i))

        for i in range(self.nbEtat):
            if self.etat[i] in self.etatInitiaux:
                nouveauEtatInitiaux.append(nouveauEtat[self.etat.index(self.etat[i])])
            if self.etat[i] in self.etatTerminaux:
                nouveauxEtatTerminaux.append(nouveauEtat[self.etat.index(self.etat[i])])

        for i in range(self.nbTransition):
            l = self.transition[i].split(';')
            nouveauTransitions.append(nouveauEtat[self.etat.index(l[0])] + ';' + l[1] + ';' + nouveauEtat[self.etat.index(l[2])])

        self.etat = nouveauEtat
        self.etatInitiaux = nouveauEtatInitiaux
        self.etatTerminaux = nouveauxEtatTerminaux
        self.transition = nouveauTransitions

        self.creationEtat()

    def completerAutomate(self):
        nbAlphabet = copy.deepcopy(self.nbAlphabet)
        alphabet = copy.deepcopy(self.alphabet)
        nbEtat = copy.deepcopy(self.nbEtat + 1)
        etat = copy.deepcopy(self.etat)
        etat.append('P')
        nbEtatInitiaux = copy.deepcopy(self.nbEtatInitiaux)
        etatInitiaux = copy.deepcopy(self.etatInitiaux)
        nbEtatTerminaux = copy.deepcopy(self.nbEtatTerminaux)
        etatTerminaux = copy.deepcopy(self.etatTerminaux)
        transition = []

        for i in range(self.nbEtat):
            for cle, valeur in self.listeObjetEtat[i].transition.items():
                l = valeur.split(',')
                for element in l:
                    if element == '':
                        ajout = self.listeObjetEtat[i].nom + ';' + cle + ';' + 'P'
                    else:
                        ajout = self.listeObjetEtat[i].nom + ';' + cle + ';' + valeur
                    transition.append(ajout)

        for element in alphabet:
            transition.append('P' + ';' + element + ';' + 'P')

        nbTransition = len(transition)

        self.ecrireAutomate(nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition)

    def determiniserAutoamte(self):
        nbAlphabet = copy.deepcopy(self.nbAlphabet)
        alphabet = copy.deepcopy(self.alphabet)
        etat = [self.fusionEtat(self.etatInitiaux)]
        nbEtatInitiaux = 1
        etatInitiaux = [self.fusionEtat(self.etatInitiaux)]
        etatTerminaux = []
        transition = []

        file = []
        file.append(copy.deepcopy(self.etatInitiaux))

        while len(file) != 0:

            for i in range(nbAlphabet):
                lu = []

                for j in range(len(file[0])):

                    for k in range(self.nbEtat):

                        if file[0][j] == self.listeObjetEtat[k].nom:

                            for cle, valeur in self.listeObjetEtat[k].transition.items():

                                if cle == alphabet[i]:

                                    l = valeur.split(',')

                                    for element in l:

                                        if element != '':
                                            lu.append(element)

                if lu != []:
                    fus = self.fusionEtat(lu)
                    veri = False

                    for element in lu:
                        if element in self.etatTerminaux:
                            veri = True
                    if veri:
                        if fus not in etatTerminaux:
                            etatTerminaux.append(fus)

                    str = self.fusionEtat(file[0]) + ';' + alphabet[i] + ';' + fus
                    if str not in transition:
                        transition.append(str)

                    if fus not in etat:
                        etat.append(fus)
                        file.append(lu)

            del file[0]

        nbEtat = len(etat)
        nbEtatTerminaux = len(etatTerminaux)
        nbTransition = len(transition)

        self.ecrireAutomate(nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition)

    def standardiserAutomate(self):

        nbAlphabet = copy.deepcopy(self.nbAlphabet)
        alphabet = copy.deepcopy(self.alphabet)
        nbEtat = copy.deepcopy(self.nbEtat + 1)
        etat = copy.deepcopy(self.etat)
        etat.insert(0, 'I')
        nbEtatInitiaux = 1
        etatInitiaux = ['I']
        nbEtatTerminaux = copy.deepcopy(self.nbEtatTerminaux)
        etatTerminaux = copy.deepcopy(self.etatTerminaux)
        transition = copy.deepcopy(self.transition)

        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():

                l = valeur.split(',')
                for j in range(len(l)):

                    if l[j] != '':
                        ajout = "I;" + cle + ";" + l[j]

                        if ajout not in transition:
                            transition.append(ajout)

        nbTransition = len(transition)

        self.ecrireAutomate(nbAlphabet, alphabet, nbEtat, etat, nbEtatInitiaux, etatInitiaux, nbEtatTerminaux, etatTerminaux, nbTransition, transition)

    def estComplet(self, power):

        # méthode qui permert de savoir si un automate est complet ou non. Il regarde donc s'il y a au moins un état n'a pas de transition pour au moins l'une de ses lettres


        transition = []
        veri = True

        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():
                if valeur == '':
                    veri = False
                    transition.append(self.listeObjetEtat[i].nom + ',' + cle + ',-')

        if power == True:
            infoComplet(veri, transition)

        return veri

    def estDeterministe(self, power):

        # méthode qui permert de savoir si un automate est déterministe ou non. Il regarde donc s'il y a plus d'un etat initial
        # et regarde s'il y a une ',' dans chacune des transitons car s'il y en a une , ça veut dire qu'il y ambiguïté

        condition1 = True
        condition2 = True
        transition = []
        veri = True

        if self.nbEtatInitiaux != 1:
            veri = False
            condition1 = False

        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():
                if ',' in valeur:
                    veri = False
                    condition2 = False

                    l = valeur.split(',')
                    for j in range(len(l)):
                        transition.append(self.listeObjetEtat[i].nom + ',' + cle + ',' + l[j])

        if power == True:
            # permet de savoir s'il faut afficher les informations ou non
            infoDerterministe(veri, condition1, condition2, transition, str(self.nbEtatInitiaux))

        return veri

    def estStandard(self, power):

        # méthode qui permert de savoir si un automate est standard ou non. il regarde donc s'il y a plus d'un etat initial
        # et regarde s'il y a des transitions qui mènent à un etat initial

        condition1 = True
        condition2 = True
        transition = []
        veri = True

        if self.nbEtatInitiaux != 1:
            veri = False
            condition1 = False

        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():

                l = valeur.split(',')

                for j in range(len(l)):
                    if l[j] in self.etatInitiaux:
                        veri = False
                        condition2 = False
                        transition.append(self.listeObjetEtat[i].nom + ',' + cle + ',' + l[j])

        if power == True:
            # permet de savoir s'il faut afficher les informations ou non
            infoStandard(veri, condition1, condition2, transition, str(self.nbEtatInitiaux))

        return veri

    def creationEtat(self):

        self.listeObjetEtat = []

        # on initialise listeObjetEtat qui contindrat chaque état sous la fome de la class Etat() avec les attirubut déjà initialisé

        for i in range(len(self.etat)):
            self.listeObjetEtat.append(Etat(self.etat[i]))

        # initialisation de chaque état

        for i in range(len(self.listeObjetEtat)):

            if self.listeObjetEtat[i].nom in self.etatInitiaux:
                self.listeObjetEtat[i].etatInitial = 'E'
            else:
                self.listeObjetEtat[i].etatInitial = ''

            if self.listeObjetEtat[i].nom in self.etatTerminaux:
                self.listeObjetEtat[i].etatTerminal = 'S'
            else:
                self.listeObjetEtat[i].etatTerminal = ''

        # attribut etat initial ou terminal

        for i in range(len(self.listeObjetEtat)):
            self.listeObjetEtat[i].initialisationTransition(self.nbAlphabet, self.alphabet)

        # initilisation du dictionnaire dictionnaire qui contient les transitions

        for i in range(len(self.transition)):

            l = self.transition[i].split(';')

            for j in range(len(self.listeObjetEtat)):

                if l[0] == self.listeObjetEtat[j].nom:
                    self.listeObjetEtat[j].transition[l[1]] += (',' + l[2])
                    self.listeObjetEtat[j].transition[l[1]] = self.listeObjetEtat[j].transition[l[1]].lstrip(",")

            # on rentre les valeur dans chaque dictionnaire de chaque etat

    def espace(self, longueurCase, longueurCaractere ):
        return ' '*(longueurCase - longueurCaractere)
        # calcul du reste à compléter pour la case

    def longueurMaxEtat(self):
        l = []
        for i in range(self.nbEtat):
            l.append(len(self.etat[i]))
        if len(l) == 0:
            return 1

        return max(l)
        # calcul le nom de l'état le plus long

    def longueurMaxTransition(self):
        l = []
        for i in range(len(self.listeObjetEtat)):
            for cle, valeur in self.listeObjetEtat[i].transition.items():
                l.append(len(valeur))

        if len(l) == 0:
            return 1

        return max(l)
        # calcul la transition la plus longue

    def afficherAutomate(self):

        # méthodde pour afficher la table de transiton de l'automate

        longueurCase = max(self.longueurMaxEtat(), self.longueurMaxTransition())

        # on calul grâce au 3 fonctions la taille des cases pour avoir un tableu symétrique, en fonction de l'information la plus longue

        if longueurCase < 2:
            longueurCase = 2

        caseVide = " "*longueurCase

        print(blanc + gras + 2*caseVide + ' ', end=' ')

        for i in range(self.nbAlphabet):
            print('|' + self.alphabet[i] + self.espace(longueurCase, len(self.alphabet[i])), end=' ')

        print()

        # on affiche la première ligne du tableau avec la méthode espace pour compléter la longuer de la case apres l'affichage des infos

        for i in range(len(self.listeObjetEtat)):
            temp = ''
            temp += self.listeObjetEtat[i].etatInitial
            temp += self.listeObjetEtat[i].etatTerminal
            print(temp + self.espace(longueurCase, len(temp)) + '|' + self.listeObjetEtat[i].nom + self.espace(longueurCase, len(self.listeObjetEtat[i].nom)), end=' ')

            for cle, valeur in self.listeObjetEtat[i].transition.items():
                if valeur == '' or valeur == ' ':
                    print('|' + '-' + self.espace(longueurCase, len('-')), end=' ')
                else:
                    print('|' + valeur + self.espace(longueurCase, len(valeur)), end=' ')

            if i + 1 == len(self.listeObjetEtat):
                print(normal)
            else:
                print()

            # affichage des autres lignes

    def initialiserAutomate(self):

        self.nbAlphabet = int(self.listeFichierAutomate[0][0])

        liste = self.listeFichierAutomate[0].split(' ')

        for i in range(1, len(liste)):
            self.alphabet.append(liste[i])

        liste = self.listeFichierAutomate[1].split(' ')

        self.nbEtat = int(liste[0])

        for i in range(1, len(liste)):
            self.etat.append(liste[i])

        liste = self.listeFichierAutomate[2].split(' ')

        self.nbEtatInitiaux = int(liste[0])

        for i in range(1, len(liste)):
            self.etatInitiaux.append(liste[i])

        liste = self.listeFichierAutomate[3].split(' ')

        self.nbEtatTerminaux = int(liste[0])

        for i in range(1, len(liste)):
            self.etatTerminaux.append(liste[i])

        liste = self.listeFichierAutomate[4].split(' ')
        self.nbTransition = int(liste[0])

        for i in range(5, len(self.listeFichierAutomate)):
            self.transition.append(self.listeFichierAutomate[i])

        self.creationEtat()

        # cette méthode initialiser tous les attributs de l'automate grave à la liste des lignes du fichier textes
        # puis appel de la méthode self.creationEtat()

    def lireAutomateSurFichier(self, chemin):
        fichierAutomate = open(chemin, "r", encoding="utf-8")
        self.listeFichierAutomate = fichierAutomate.readlines()
        fichierAutomate.close()

        for i in range(len(self.listeFichierAutomate)):
            self.listeFichierAutomate[i] = self.listeFichierAutomate[i].strip('\n')

        self.initialiserAutomate()

        # cette méthode permet de lire un fichier texte à partir du chemin donné en paramètre et d'initialiser un self.liste fichier automate qui stoker sous forme de liste les lignes du fichier txt
        # appel de la méthode self.initialiserAutomate()
