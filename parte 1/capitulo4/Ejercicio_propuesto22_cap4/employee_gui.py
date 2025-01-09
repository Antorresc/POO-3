import tkinter as tk
from tkinter import messagebox
from employee import Employee

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Nombre del empleado:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Salario por hora:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.hourly_wage_entry = tk.Entry(root)
        self.hourly_wage_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas trabajadas:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.hours_worked_entry = tk.Entry(root)
        self.hours_worked_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para calcular el salario
        self.calculate_button = tk.Button(root, text="Calcular Salario", command=self.calculate_salary)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_salary(self):
        try:
            # Obtener datos de los campos de entrada
            name = self.name_entry.get()
            hourly_wage = float(self.hourly_wage_entry.get())
            hours_worked = int(self.hours_worked_entry.get())

            # Crear instancia de Employee
            employee = Employee(name, hourly_wage, hours_worked)
            monthly_salary = employee.calculate_monthly_salary()

            # Mostrar el resultado en el messagebox
            if monthly_salary > 450000:
                result = f"Nombre empleado: {employee.name}\nSalario mensual: ${monthly_salary:.2f}"
            else:
                result = f"Nombre empleado: {employee.name}\nSalario mensual por debajo del límite."
            
            messagebox.showinfo("Resultado", result)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para los campos.")
