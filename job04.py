class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print("Je suis " + self.prenom + " " + self.nom)



p1=Personne("Dejoux","Greg")
p2=Personne("Johnson","Dwayne")
p1.SePresenter()
p2.SePresenter()




