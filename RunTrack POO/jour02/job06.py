class Vehicule:
    def __init__(self):
        marque = "..."
        modèle ="..."
        année = "..."
        prix = "..."
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule (self):
        print("Marque =", self.marque,"\nModel =", self.modèle, "\nAnnée =", self.année, "\nPrix =", self.prix)

    def demarrer(self):
        print("Attention je roule")


class Voiture(Vehicule):
    def __init__(self):
        Vehicule.__init__(self)
        marque = "Mercedes"
        modèle = "Classe A"
        année = 2020
        prix = 18500
        portes = 4
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix
        self.portes = portes
    def informationsVehicule(self):
        print("Marque =", self.marque, "\nModel =", self.modèle, "\nAnnée =", self.année, "\nPrix =", self.prix, "\nNombre de porte =", self.portes)

    def demarrer(self):
        print("Vroum vroum la vago demarre")


class Moto(Vehicule):
    def __init__(self):
        Vehicule.__init__(self)
        roues = 2
        self.roues = roues

    def informationsVehicule(self):
        marque = "Yamaha"
        modèle = "1200 Vmax"
        année = "1987"
        prix = "4500"
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix
        print("Marque =", self.marque, "\nModel =", self.modèle, "\nAnnée =", self.année, "\nPrix =", self.prix, "\nNombre de roues =", self.roues)

    def demarrer(self):
        print("Bep bep roue arrière la moto démarre")


result=Vehicule()
#result=Voiture()
#result=Moto()
result.informationsVehicule()
result.demarrer()