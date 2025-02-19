import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz(n, indice=2):
    if n < 0 and indice % 2 == 0:
        return "Error: Raíz de un número negativo"
    return n ** (1 / indice)

def logaritmo(n, base=10):
    if n <= 0:
        return "Error: Logaritmo de un número no positivo"
    return math.log(n, base)

def factorial(n):
    if n < 0:
        return "Error: Factorial de un número negativo"
    return math.factorial(n)

def trigonometria(funcion, angulo):
    radianes = math.radians(angulo)
    funciones = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan
    }
    return funciones.get(funcion, lambda _: "Función inválida")(radianes)

def calculadora():
    print("📌 Calculadora Científica 📌")
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Logaritmo")
    print("8. Factorial")
    print("9. Funciones trigonométricas (sin, cos, tan)")
    print("0. Salir")

    while True:
        opcion = input("\nSeleccione una opción: ")

        if opcion == "0":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ["1", "2", "3", "4", "5"]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            operaciones = {
                "1": suma,
                "2": resta,
                "3": multiplicacion,
                "4": division,
                "5": potencia
            }
            print("Resultado:", operaciones[opcion](a, b))
        elif opcion == "6":
            n = float(input("Ingrese el número: "))
            indice = int(input("Ingrese el índice de la raíz (ej. 2 para raíz cuadrada): "))
            print("Resultado:", raiz(n, indice))
        elif opcion == "7":
            n = float(input("Ingrese el número: "))
            base = int(input("Ingrese la base del logaritmo (ej. 10 para logaritmo decimal): "))
            print("Resultado:", logaritmo(n, base))
        elif opcion == "8":
            n = int(input("Ingrese el número entero: "))
            print("Resultado:", factorial(n))
        elif opcion == "9":
            funcion = input("Ingrese la función trigonométrica (sin, cos, tan): ").lower()
            angulo = float(input("Ingrese el ángulo en grados: "))
            print("Resultado:", trigonometria(funcion, angulo))
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    calculadora()
