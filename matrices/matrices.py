import numpy as np
from fractions import Fraction
# Primera matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
print("Ingrese los elementos de la matriz fila por fila (puede usar enteros, decimales o fracciones tipo a/b):")

for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = Fraction(input(f"Elemento [{i+1},{j+1}]: "))
        fila.append(elemento)
    matriz.append(fila)

print("La matriz ingresada es:")
for fila in matriz:
    print([float(x) for x in fila])   # Mostrar en decimal

print("\nOperaciones disponibles:")
print("1. Suma")
print("2. Resta")      
print("3. Multiplicación")
opcion = int(input("Ingrese la opción deseada (1/2/3): "))

# SUMA
if opcion == 1:
    filas2 = int(input("Ingrese el número de filas: "))
    columnas2 = int(input("Ingrese el número de columnas: "))
    if filas2 != len(matriz) or columnas2 != len(matriz[0]):
        print("Error: Las dimensiones de la segunda matriz deben coincidir con las de la primera matriz.")
        exit()

    print("Ingrese los elementos de la segunda matriz fila por fila:")
    matriz2 = []
    for i in range(filas2):
        fila = []
        for j in range(columnas2):
            elemento = Fraction(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(elemento)
        matriz2.append(fila)

    print("La segunda matriz ingresada es:")
    for fila in matriz2:
        print([float(x) for x in fila])

    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            suma = matriz[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    print("El resultado de la suma de las matrices es:")
    for fila in resultado:
        print([float(x) for x in fila])

# RESTA
elif opcion == 2:
    filas2 = int(input("Ingrese el número de filas: "))
    columnas2 = int(input("Ingrese el número de columnas: "))
    if filas2 != len(matriz) or columnas2 != len(matriz[0]):
        print("Error: Las dimensiones de la segunda matriz deben coincidir con las de la primera matriz.")
        exit()

    print("Ingrese los elementos de la segunda matriz fila por fila:")
    matriz2 = []
    for i in range(filas2):
        fila = []
        for j in range(columnas2):
            elemento = Fraction(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(elemento)
        matriz2.append(fila)

    print("La segunda matriz ingresada es:")
    for fila in matriz2:
        print([float(x) for x in fila])

    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            resta = matriz[i][j] - matriz2[i][j]
            fila_resultado.append(resta)
        resultado.append(fila_resultado)

    print("El resultado de la resta de las matrices es:")
    for fila in resultado:
        print([float(x) for x in fila])

# MULTIPLICACIÓN
elif opcion == 3:
    filas2 = int(input("Ingrese el número de filas: "))
    columnas2 = int(input("Ingrese el número de columnas: "))
    if columnas2 != len(matriz):
        print("Error: El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
        exit()

    print("Ingrese los elementos de la segunda matriz fila por fila:")
    matriz2 = []
    for i in range(filas2):
        fila = []
        for j in range(columnas2):
            elemento = Fraction(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(elemento)
        matriz2.append(fila)

    print("La segunda matriz ingresada es:")
    for fila in matriz2:
        print([float(x) for x in fila])

    resultado = []
    for i in range(len(matriz)):
        fila_resultado = []
        for j in range(columnas2):
            suma = Fraction(0, 1)
            for k in range(len(matriz[0])):
                suma += matriz[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    print("El resultado de la multiplicación de las matrices es:")
    for fila in resultado:
        print([float(x) for x in fila])

else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")