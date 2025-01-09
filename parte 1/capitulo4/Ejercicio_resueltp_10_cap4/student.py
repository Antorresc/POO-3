class Student:
    def __init__(self, registration_number, name, patrimony, social_stratum):
        self.registration_number = registration_number
        self.name = name
        self.patrimony = patrimony
        self.social_stratum = social_stratum

    def calculate_tuition(self):
        base_fee = 50000
        if self.patrimony > 2000000 and self.social_stratum > 3:
            increment = self.patrimony * 0.03
        else:
            increment = 0
        return base_fee + increment

    def display_information(self):
        tuition = self.calculate_tuition()
        print(f"El estudiante con número de inscripción: {self.registration_number}")
        print(f"y nombre: {self.name}")
        print(f"Debe pagar: ${tuition:.2f}")
