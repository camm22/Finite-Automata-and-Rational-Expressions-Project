# class etat qui permet de miexu stocker les informations de chaque etats des automates
# c'est aussi très utilse pour la partie de reconnaissance de mot car sans class ça ne serait pas vraiment possible


class Etat:

    def __init__(self, nom):
        self.nom = nom
        self.etatInitial = ''
        self.etatTerminal = ''
        self.transition = {}
        self.objetTransition = {}
    # attributs de etat

    def initialisationTransition(self, nbAlphabet, alphabet):
        for i in range(nbAlphabet):
            self.transition[alphabet[i]] = ""
            self.objetTransition[alphabet[i]] = 'XXX'

    # méthode pour initialiser les deux dictionnaires qui stockent les transitions, un avce que le nom des etat et l'autre avec l'état sous forme d'objet
