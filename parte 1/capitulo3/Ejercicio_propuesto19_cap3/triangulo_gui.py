import tkinter as tk
from tkinter import messagebox
from triangulo_equilatero import Trianguloequilatero

class TrianguloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos de Triángulo Equilátero")

        # Etiqueta y campo de entrada para el lado
        tk.Label(root, text="Valor del lado:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.lado_entry = tk.Entry(root)
        self.lado_entry.grid(row=0, column=1, padx=10, pady=5)

        # Botón para calcular
        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            # Obtener el valor del lado desde el campo de entrada
            lado = float(self.lado_entry.get())

            # Crear instancia de TrianguloEquilatero
            triangulo = Trianguloequilatero(lado)

            # Calcular los valores
            perimetro = triangulo.obtener_perimetro()
            altura = triangulo.obtener_altura()
            area = triangulo.obtener_area()

            # Mostrar resultados en un messagebox
            messagebox.showinfo(
                "Resultados",
                f"Perímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}"
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")
