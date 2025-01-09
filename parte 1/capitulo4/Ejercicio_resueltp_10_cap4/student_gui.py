import tkinter as tk
from tkinter import messagebox
from student import Student

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")

        # Labels y campos de entrada
        tk.Label(root, text="Número de inscripción:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.registration_number_entry = tk.Entry(root)
        self.registration_number_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.patrimony_entry = tk.Entry(root)
        self.patrimony_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Estrato social:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.social_stratum_entry = tk.Entry(root)
        self.social_stratum_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botón para calcular matrícula
        self.calculate_button = tk.Button(root, text="Calcular Matrícula", command=self.calculate_tuition)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_tuition(self):
        try:
            # Obtener datos de los campos de entrada
            registration_number = self.registration_number_entry.get()
            name = self.name_entry.get()
            patrimony = float(self.patrimony_entry.get())
            social_stratum = int(self.social_stratum_entry.get())

            # Crear instancia de Student
            student_instance = Student(registration_number, name, patrimony, social_stratum)

            # Calcular matrícula y mostrar resultado
            tuition = student_instance.calculate_tuition()
            messagebox.showinfo("Resultado", f"El estudiante con número de inscripción: {registration_number}\n"
                                        f"y nombre: {name}\n"
                                        f"Debe pagar: ${tuition:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para el patrimonio y el estrato social.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
