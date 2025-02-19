import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        
        self.expresion = ""
        
        # Pantalla de entrada/salida
        self.entrada_texto = tk.StringVar()
        self.entrada = tk.Entry(root, textvariable=self.entrada_texto, font=("Arial", 20), bd=10, relief="ridge", justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)
        
        # Botones
        botones = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sin', 'cos', 'tan', '√'),
            ('log', 'ln', '^', '!')
        ]

        for i, fila in enumerate(botones):
            for j, simbolo in enumerate(fila):
                tk.Button(root, text=simbolo, font=("Arial", 16), width=6, height=2, command=lambda s=simbolo: self.boton_presionado(s)).grid(row=i + 1, column=j, padx=5, pady=5)

        # Botón de limpiar
        tk.Button(root, text="C", font=("Arial", 16), width=28, height=2, bg="red", fg="white", command=self.limpiar).grid(row=7, column=0, columnspan=4, padx=5, pady=5)
    
    def boton_presionado(self, simbolo):
        if simbolo == "=":
            try:
                self.expresion = self.expresion.replace("^", "**")
                self.expresion = self.expresion.replace("√", "math.sqrt")
                resultado = eval(self.expresion, {"math": math, "__builtins__": {}})
                self.entrada_texto.set(str(resultado))
                self.expresion = str(resultado)
            except Exception as e:
                messagebox.showerror("Error", "Expresión no válida")
                self.entrada_texto.set("")
                self.expresion = ""
        elif simbolo == "C":
            self.limpiar()
        elif simbolo == "sin":
            self.expresion = f"math.sin(math.radians({self.expresion}))"
            self.boton_presionado("=")
        elif simbolo == "cos":
            self.expresion = f"math.cos(math.radians({self.expresion}))"
            self.boton_presionado("=")
        elif simbolo == "tan":
            self.expresion = f"math.tan(math.radians({self.expresion}))"
            self.boton_presionado("=")
        elif simbolo == "log":
            self.expresion = f"math.log10({self.expresion})"
            self.boton_presionado("=")
        elif simbolo == "ln":
            self.expresion = f"math.log({self.expresion})"
            self.boton_presionado("=")
        elif simbolo == "!":
            try:
                num = int(self.expresion)
                self.expresion = str(math.factorial(num))
                self.entrada_texto.set(self.expresion)
            except:
                messagebox.showerror("Error", "Número inválido para factorial")
                self.expresion = ""
        else:
            self.expresion += str(simbolo)
            self.entrada_texto.set(self.expresion)
    
    def limpiar(self):
        self.expresion = ""
        self.entrada_texto.set("")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
