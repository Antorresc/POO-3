class NumberComparator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self):
        if self.a > self.b:
            return "A es mayor que B"
        elif self.a < self.b:
            return "A es menor que B"
        else:
            return "A es igual a B"

