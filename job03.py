class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3
    def addition(self):
        self.nombre3= self.nombre1 + self.nombre2
        print(self.nombre3)

nombre=Operation()
nombre.addition()
