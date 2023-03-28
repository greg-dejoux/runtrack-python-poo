class Livre:

    def __init__(self, titre, auteur, nbdepages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbdepages = nbdepages
        self.__disponible = True  # changer en True ou False pour déterminer si le livre est disponible ou pas

    def titre(self):
        print("Le titre du livre est", self.__titre)

    def auteur(self):
        print("L'auteur du livre est", self.__auteur)

    def nbdepages(self):
        if self.__nbdepages < 1:
            print("Désolé mais le livre doit au moins contenir une page. Veuillez réessayer s'il vous plait")
            quit()
        else:
            print("Le nombre de pages du livre est", self.__nbdepages)

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        self.vérification()
        if self.__disponible == True: #vérifier si le livre est dispo
            reponse = input("Ce livre est actuellement disponible. Voulez-vous l'emprunter ? [o/N] ")
            reponse = reponse.strip().lower()
            if reponse.startswith('o'):
                self.__disponible = False
                print("Vous avez bien emprunté ce livre")
            else:
                print("Vous avez choisi de ne pas emprunter ce livre")
        else:
            print("Le livre n'est pas disponible car il a déja été emprunté")

    def rendre(self):
        self.vérification()
        if self.__disponible == True:
            print("Vous n'avez pas le livre en votre possession")

        else:
            choix = input("Voulez-vous rendre ce livre ? [o/N] ")
            choix = choix.strip().lower()
            if choix.startswith('o'):
                self.__disponible = True
                print("Vous avez bien rendu ce livre")
            else:
                print("Vous avez choisi de garder ce livre")


bouquin = Livre("Le Petit Prince", "Antoine de Saint Exupery", 7)
bouquin.nbdepages()
bouquin.titre()
bouquin.auteur()
bouquin.vérification()
bouquin.emprunter()  #choisir pour emprunter
#bouquin.rendre()  #choisir pour rendre
