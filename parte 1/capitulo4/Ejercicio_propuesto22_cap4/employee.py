class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_monthly_salary(self):
        return self.hourly_wage * self.hours_worked

    def display_salary_info(self):
        monthly_salary = self.calculate_monthly_salary()
        if monthly_salary > 450000:
            print(f"Nombre empleado: {self.name}\nSalario mensual: {monthly_salary:.2f}")
        else:
            print(f"Nombre empleado: {self.name}")
