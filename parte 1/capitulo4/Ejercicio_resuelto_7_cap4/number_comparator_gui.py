import tkinter as tk
from tkinter import messagebox
from number_comparator import NumberComparator

class ComparatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Números")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Ingrese el valor de A:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Ingrese el valor de B:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para comparar
        self.compare_button = tk.Button(root, text="Comparar", command=self.compare_numbers)
        self.compare_button.grid(row=2, column=0, columnspan=2, pady=10)

    def compare_numbers(self):
        try:
            # Obtener valores de los campos de entrada
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())

            # Crear instancia de NumberComparator
            comparator = NumberComparator(a, b)
            result = comparator.compare()

            # Mostrar el resultado
            messagebox.showinfo("Resultado", result)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para A y B.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComparatorApp(root)
    root.mainloop()
