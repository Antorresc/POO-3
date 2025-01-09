from Figura import Figura

class Rombo(Figura):
    def __init__(self, D, d, l):
        self.D = D
        self.d = d
        self.l = l

    def calcular_area(self):
        return self.D * self.d / 2

    def calcular_perimetro(self):
        return 4 * self.l
    
    #esto calcula el area y perimetro del rombo 