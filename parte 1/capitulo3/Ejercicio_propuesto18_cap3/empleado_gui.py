import tkinter as tk
from tkinter import messagebox
from empleado import Empleado

class EmpleadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Código del empleado:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres del empleado:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas trabajadas:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Valor por hora:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.valor_hora_entry = tk.Entry(root)
        self.valor_hora_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Retención en la fuente (%):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.retencion_entry = tk.Entry(root)
        self.retencion_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón para calcular salarios
        self.calculate_button = tk.Button(root, text="Calcular Salarios", command=self.calcular_salarios)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_salarios(self):
        try:
            # Obtener valores de los campos de entrada
            codigo = self.codigo_entry.get()
            nombres = self.nombres_entry.get()
            horas_trabajadas = float(self.horas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            retencion_fuente = float(self.retencion_entry.get())

            # Crear instancia de Empleado
            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente)

            # Obtener la información del empleado
            info = empleado.obtener_informacion()

            # Mostrar resultados en un messagebox
            messagebox.showinfo(
                "Información del Empleado",
                f"Código: {info['codigo']}\n"
                f"Nombres: {info['nombres']}\n"
                f"Salario Bruto: ${info['salario_bruto']:.2f}\n"
                f"Salario Neto: ${info['salario_neto']:.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")
