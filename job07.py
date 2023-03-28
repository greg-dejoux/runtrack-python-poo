class Livre:
    def __init__(self,titre, auteur, nbdepages ):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbdepages = nbdepages
    def titre(self):
        print("Le titre du livre est",self.__titre)
    def auteur(self):
        print("L'auteur du livre est",self.__auteur)
    def nbdepages(self):
        if self.__nbdepages <1:
            print("Désolé mais le livre doit au moins contenir une page. Veuillez reesayer s'il vous plait")
            quit()
        else:
            print("Le nombre de pages du livre est",self.__nbdepages)
bouquin = Livre("Le Petit Prince", "Antoine de Saint Exupery", 7)
bouquin.nbdepages()
bouquin.titre()
bouquin.auteur()


