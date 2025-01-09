import math

class Trianguloequilatero:
    def __init__(self, lado):
        self.lado = lado
    
    def obtener_perimetro(self):
        return 3 * self.lado

    def obtener_altura(self):
        return (self.lado * math.sqrt(3)) / 2

    def obtener_area(self):
        return (math.pow(self.lado, 2) * math.sqrt(3)) / 4