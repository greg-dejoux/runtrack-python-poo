class Animal:
    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom
    def Vieillir(self):
        print("L\'age de l\'animal est de", self.age,"ans")
        self.age +=1
        print("(L\'animal prend un an)")
        print("L\'age de l\'animal est de", self.age,"ans")
    def Nommer(self):
        print("L'animal se nomme", self.prenom)

animal1 = Animal(3,"Daniel")
animal1.Vieillir()
animal1.Nommer()