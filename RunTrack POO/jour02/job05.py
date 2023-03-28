from math import pi

class Forme:
    def aire(self):
        aire = 0
        return aire
        print("L'aire de la forme est de", aire, "cm²")

class Rectangle(Forme):
    def __init__(self):
        Forme.__init__(self)
        largeur = 10
        hauteur = 15
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self):
        aire = self.hauteur * self.largeur
        print("L'aire du rectangle est de", aire, "cm²")

class Cercle(Forme):
    def __init__(self):
        Forme.__init__(self)
        radius = 20
        self.radius = radius

    def aire(self):
        aire = self.radius * 2 * pi
        print("L'aire du cercle est de", aire, "cm²")





#result = Forme()
#result = Rectangle()
result = Cercle()
result.aire()
