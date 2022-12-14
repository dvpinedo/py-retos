#Crear clase vehiculo y clase coche que hereda de vechiculo

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    
c = Coche("rojo", 4, 150, 1200)
print(c)