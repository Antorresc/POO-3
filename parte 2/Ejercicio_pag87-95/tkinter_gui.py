import tkinter as tk
from tkinter import messagebox
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Triangulo_rectangulo import TrianguloRectangulo
from Rombo import Rombo
from Trapecio import Trapecio


def calcular():
    try:
        # Obtener la figura seleccionada
        figura_seleccionada = figura_var.get()

        # Leer los valores ingresados
        if figura_seleccionada == "Círculo":
            radio = float(entry_valor.get())
            figura = Circulo(radio)
        elif figura_seleccionada == "Cuadrado":
            lado = float(entry_valor.get())
            figura = Cuadrado(lado)
        elif figura_seleccionada == "Rectángulo":
            base = float(entry_valor.get())
            altura = float(entry_valor_altura.get())
            figura = Rectangulo(base, altura)
        elif figura_seleccionada == "Triángulo Rectángulo":
            base = float(entry_valor.get())
            altura = float(entry_valor_altura.get())
            figura = TrianguloRectangulo(base, altura)
        elif figura_seleccionada == "Rombo":
            D = float(entry_valor.get())
            d = float(entry_valor_altura.get())
            l = float(entry_valor_lado.get())
            figura = Rombo(D, d, l)
        elif figura_seleccionada == "Trapecio":
            B = float(entry_valor.get())
            b = float(entry_valor_altura.get())
            a = float(entry_valor_lado.get())
            h = float(entry_valor_lado_altura.get())
            figura = Trapecio(B, b, a, h)
        else:
            messagebox.showerror("Error", "Seleccione una figura")
            return

        # Calcular área y perímetro
        area = figura.calcular_area()
        perimetro = figura.calcular_perimetro()

        # Mostrar los resultados
        label_resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")

        # Para Triángulo Rectángulo, mostramos también el tipo
        if figura_seleccionada == "Triángulo Rectángulo":
            tipo = figura.determinar_tipo_triangulo()
            label_resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nTipo: {tipo}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un valor válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Geométrica")

# Variable para almacenar la figura seleccionada
figura_var = tk.StringVar()

# Etiqueta de título
tk.Label(ventana, text="Seleccione una figura geométrica:", font=("Arial", 12)).pack(pady=10)

# Botones para seleccionar la figura
tk.Radiobutton(ventana, text="Círculo", variable=figura_var, value="Círculo").pack()
tk.Radiobutton(ventana, text="Cuadrado", variable=figura_var, value="Cuadrado").pack()
tk.Radiobutton(ventana, text="Rectángulo", variable=figura_var, value="Rectángulo").pack()
tk.Radiobutton(ventana, text="Triángulo Rectángulo", variable=figura_var, value="Triángulo Rectángulo").pack()
tk.Radiobutton(ventana, text="Rombo", variable=figura_var, value="Rombo").pack()
tk.Radiobutton(ventana, text="Trapecio", variable=figura_var, value="Trapecio").pack()

# Entrada para ingresar el valor (dependiendo de la figura)
tk.Label(ventana, text="Ingrese el valor (radio para Círculo, lado para Cuadrado, base para otros):", font=("Arial", 12)).pack(pady=10)
entry_valor = tk.Entry(ventana, font=("Arial", 12))
entry_valor.pack(pady=5)

# Entradas adicionales para figuras que requieren más de un valor (como Rectángulo, Triángulo Rectángulo, etc.)
tk.Label(ventana, text="Ingrese otro valor (altura, lado, etc.):", font=("Arial", 12)).pack(pady=10)
entry_valor_altura = tk.Entry(ventana, font=("Arial", 12))
entry_valor_altura.pack(pady=5)

# Entradas adicionales para figuras como Rombo y Trapecio
entry_valor_lado = tk.Entry(ventana, font=("Arial", 12))
entry_valor_lado.pack(pady=5)

entry_valor_lado_altura = tk.Entry(ventana, font=("Arial", 12))
entry_valor_lado_altura.pack(pady=5)

# Botón para calcular el área y el perímetro
tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
