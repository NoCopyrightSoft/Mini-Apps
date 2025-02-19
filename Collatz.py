import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def collatz_sequence(n):
    """Calcula la secuencia de Collatz para un número dado."""
    if n < 1:
        raise ValueError("El número debe ser un entero positivo.")
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def calcular():
    """Calcula la secuencia y la muestra en el área de texto."""
    try:
        num = int(entry.get())
        secuencia = collatz_sequence(num)
        result_text.config(state="normal")  # Habilita edición temporalmente
        result_text.delete("1.0", tk.END)  # Borra texto anterior
        result_text.insert(tk.END, " → ".join(map(str, secuencia)))  # Muestra la secuencia
        result_text.config(state="disabled")  # Deshabilita edición
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número entero positivo.")

# Crear la ventana
root = tk.Tk()
root.title("Calculadora de Collatz")
root.geometry("500x400")  # Aumentamos el tamaño
root.resizable(False, False)  # Evita redimensionar

# Estilos modernos con ttk
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Widgets
ttk.Label(root, text="Ingresa un número entero positivo:").pack(pady=10)
entry = ttk.Entry(root, width=15)
entry.pack(pady=5)

ttk.Button(root, text="Calcular", command=calcular).pack(pady=10)

# Área de texto con barra de desplazamiento
frame = ttk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

result_text = scrolledtext.ScrolledText(frame, width=60, height=10, wrap="word", font=("Arial", 10))
result_text.pack(fill="both", expand=True)
result_text.config(state="disabled")  # Deshabilita edición

# Ejecutar la aplicación
root.mainloop()
