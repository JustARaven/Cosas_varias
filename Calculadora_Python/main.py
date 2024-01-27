# main_calculadora.py
from calculadora import sumar, restar, multiplicar, dividir

# Tomar la entrada del usuario
print("Selecciona la operación que deseas realizar:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Validar entrada del usuario
try:
    input_teclado = int(input("Elige una opción escribiendo su número:"))
except ValueError:
    print("Por favor, ingresa un número válido.")
    exit()

# Realizar la operación
if 1 <= input_teclado <= 4:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    operadores = {1: '+', 2: '-', 3: '*', 4: '/'}
    resultado = None

    if input_teclado == 1:
        resultado = sumar(num1, num2)
    elif input_teclado == 2:
        resultado = restar(num1, num2)
    elif input_teclado == 3:
        resultado = multiplicar(num1, num2)
    elif input_teclado == 4:
        resultado = dividir(num1, num2)

    print(f"El resultado de tu operación es: {num1} {operadores[input_teclado]} {num2} = {resultado}")

else:  # Mensaje de error - Elección inválida
    print(f"Has seleccionado {input_teclado}, lo cual no es una elección válida.")
