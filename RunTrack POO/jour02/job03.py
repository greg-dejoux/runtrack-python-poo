class Rectangle:
    def __init__(self):
        longueur = 15
        largeur = 10
        self.longueur = longueur
        self.largeur = largeur

    def périmètre(self):
        périmètre = 2 * (self.longueur + self.largeur)
        print("Le périmètre du rectangle est de", périmètre, "cm")

    def surface(self):
        surface = self.longueur * self.largeur
        print("L'aire du rectangle est de", surface, "cm²")


class Parallélépipède(Rectangle):
    def __init__(self, hauteur):
        Rectangle.__init__(self)
        self.hauteur = hauteur

    def volume(self):
        volume = (self.longueur * self.largeur * self.hauteur)
        print("Le volume du parrallélépipède est de", volume, "cm³")

########POUR LE RECTANGLE
result=Rectangle()
result.périmètre()
result.surface()
########POUR LE PARRALLÉLÉPIPÈDE
result = Parallélépipède(10)
result.volume()
