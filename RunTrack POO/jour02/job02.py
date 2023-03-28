class Personne:
    def __init__(self):
        age = 14
        self.age = age

    def afficherAge(self):
        print("Son age est", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age
        print("L'age à été modifié à", self.age, "ans")


class Eleve(Personne):
    def __init__(self, age):
        Personne.__init__(self)
        self.age = age
        self.bonjour()
        self.allerEnCours()
        self.__afficherAge()

    def allerEnCours(self):
        print("Je vais en cours")

    def __afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignée):
        Personne.__init__(self)
        self.bonjour()
        self.age = age
        self.__matiereEnseignée = matiereEnseignée
        self.enseigner(self)

    def enseigner(self,matiereEnseignée):
        print("Le cours de", self.__matiereEnseignée, "va commencer")

#perso = Personne()             #Activer la classe Personne
#perso.afficherAge()
#perso.bonjour()
#perso.modifierAge(20)

####################### (Ne pas activer ensemble)

perso = Eleve(15)                #Activer l'héritage Eleve
perso = Professeur(40, "Maths")    #Activer l'héritage Professeur



