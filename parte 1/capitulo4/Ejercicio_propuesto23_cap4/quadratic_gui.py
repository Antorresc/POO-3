import tkinter as tk
from tkinter import messagebox
from quadratic import QuadraticEquation

class QuadraticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecuación Cuadrática")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.c_entry = tk.Entry(root)
        self.c_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para calcular las soluciones
        self.solve_button = tk.Button(root, text="Resolver", command=self.solve_equation)
        self.solve_button.grid(row=3, column=0, columnspan=2, pady=10)

    def solve_equation(self):
        try:
            # Obtener valores de los campos de entrada
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            # Crear instancia de QuadraticEquation
            equation = QuadraticEquation(a, b, c)
            solutions = equation.find_solutions()

            # Mostrar el resultado
            if isinstance(solutions, str):
                messagebox.showinfo("Resultado", solutions)
            else:
                messagebox.showinfo("Resultado", f"Soluciones: {', '.join(map(str, solutions))}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para a, b y c.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticApp(root)
    root.mainloop()
