
class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrage):
        self.color = color 
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocodad = velocidad
        self.cilindrage = cilindrage

    def __str__(self):
        return "color {}, {} Km/h, {} ruedas, {} puertas, {} cc".format(self.color, self.velocodad, self.ruedas, self.puertas, self.cilindrage)
        
coche = Coche("rojo", 4, 4, 120, 1800)
print(coche)