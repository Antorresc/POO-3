from Figura import Figura

class Trapecio(Figura):
    def __init__(self, B, b, a, h):
        self.B = B
        self.b = b
        self.a = a
        self.h = h

    def calcular_area(self):
        return (self.B + self.b) * self.h / 2

    def calcular_perimetro(self):
        return 2 * self.a + self.B + self.b
