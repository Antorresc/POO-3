import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def find_solutions(self):
        discriminant = self.calculate_discriminant()

        if discriminant < 0:
            return "No hay soluciones reales"
        elif discriminant == 0:
            x = -self.b / (2 * self.a)
            return x,
        else:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return x1, x2       