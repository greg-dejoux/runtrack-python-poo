class Rectangle:
    def __init__(self,largeur,longueur):
        self.__largeur = largeur
        self.__longueur = longueur
        print("Longueur =", self.__longueur, "\nLargeur =", self.__largeur)

animal1 = Rectangle(10,5)
