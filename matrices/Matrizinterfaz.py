import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from fractions import Fraction
class CalculadoraMatrices:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Matrices")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#f0f0f0")
        
        # Variables para almacenar las matrices
        self.matriz1 = None
        self.matriz2 = None
        self.filas1 = tk.StringVar(value="3")
        self.columnas1 = tk.StringVar(value="3")
        self.filas2 = tk.StringVar(value="3")
        self.columnas2 = tk.StringVar(value="3")
        
        # Frames para organizar la interfaz
        self.frame_principal = tk.Frame(self.ventana, bg="#f0f0f0")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título principal
        titulo = tk.Label(self.frame_principal, text="Calculadora de Matrices", 
                         font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2c3e50")
        titulo.pack(pady=(0, 20))
        
        # Frame para configuración de dimensiones
        frame_config = tk.LabelFrame(self.frame_principal, text="Configuración de Matrices", 
                                   font=("Arial", 12, "bold"), bg="#f0f0f0")
        frame_config.pack(fill=tk.X, pady=(0, 10))
        
        # Matriz 1
        frame_matriz1 = tk.Frame(frame_config, bg="#f0f0f0")
        frame_matriz1.pack(side=tk.LEFT, padx=20, pady=10)
        
        tk.Label(frame_matriz1, text="Matriz 1", font=("Arial", 11, "bold"), 
                bg="#f0f0f0").pack()
        
        frame_dim1 = tk.Frame(frame_matriz1, bg="#f0f0f0")
        frame_dim1.pack(pady=5)
        
        tk.Label(frame_dim1, text="Filas:", bg="#f0f0f0").pack(side=tk.LEFT)
        spinbox_filas1 = tk.Spinbox(frame_dim1, from_=1, to=5, width=5, 
                                   textvariable=self.filas1)
        spinbox_filas1.pack(side=tk.LEFT, padx=5)
        
        tk.Label(frame_dim1, text="Columnas:", bg="#f0f0f0").pack(side=tk.LEFT)
        spinbox_cols1 = tk.Spinbox(frame_dim1, from_=1, to=5, width=5, 
                                  textvariable=self.columnas1)
        spinbox_cols1.pack(side=tk.LEFT, padx=5)
        
        btn_crear1 = tk.Button(frame_matriz1, text="Crear Matriz 1", 
                              command=self.crear_matriz1, bg="#3498db", fg="white")
        btn_crear1.pack(pady=5)
        
        # Matriz 2
        frame_matriz2 = tk.Frame(frame_config, bg="#f0f0f0")
        frame_matriz2.pack(side=tk.LEFT, padx=20, pady=10)
        
        tk.Label(frame_matriz2, text="Matriz 2", font=("Arial", 11, "bold"), 
                bg="#f0f0f0").pack()
        
        frame_dim2 = tk.Frame(frame_matriz2, bg="#f0f0f0")
        frame_dim2.pack(pady=5)
        
        tk.Label(frame_dim2, text="Filas:", bg="#f0f0f0").pack(side=tk.LEFT)
        spinbox_filas2 = tk.Spinbox(frame_dim2, from_=1, to=5, width=5, 
                                   textvariable=self.filas2)
        spinbox_filas2.pack(side=tk.LEFT, padx=5)
        
        tk.Label(frame_dim2, text="Columnas:", bg="#f0f0f0").pack(side=tk.LEFT)
        spinbox_cols2 = tk.Spinbox(frame_dim2, from_=1, to=5, width=5, 
                                  textvariable=self.columnas2)
        spinbox_cols2.pack(side=tk.LEFT, padx=5)
        
        btn_crear2 = tk.Button(frame_matriz2, text="Crear Matriz 2", 
                              command=self.crear_matriz2, bg="#3498db", fg="white")
        btn_crear2.pack(pady=5)
        
        # Frame para las matrices
        self.frame_matrices = tk.Frame(self.frame_principal, bg="#f0f0f0")
        self.frame_matrices.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Frame para operaciones
        frame_operaciones = tk.LabelFrame(self.frame_principal, text="Operaciones", 
                                        font=("Arial", 12, "bold"), bg="#f0f0f0")
        frame_operaciones.pack(fill=tk.X, pady=(0, 10))
        
        frame_botones = tk.Frame(frame_operaciones, bg="#f0f0f0")
        frame_botones.pack(pady=10)
        
        btn_suma = tk.Button(frame_botones, text="Suma (A + B)", 
                           command=self.sumar_matrices, bg="#2256a8", fg="blue", width=12)
        btn_suma.pack(side=tk.LEFT, padx=5)
        
        btn_resta = tk.Button(frame_botones, text="Resta (A - B)", 
                            command=self.restar_matrices, bg="#e74c3c", fg="white", width=12)
        btn_resta.pack(side=tk.LEFT, padx=5)
        
        btn_multiplicacion = tk.Button(frame_botones, text="Multiplicación (A × B)", 
                                     command=self.multiplicar_matrices, bg="#9b59b6", fg="white", width=15)
        btn_multiplicacion.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", 
                              command=self.limpiar, bg="#95a5a6", fg="white", width=10)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Frame para resultado
        self.frame_resultado = tk.LabelFrame(self.frame_principal, text="Resultado", 
                                           font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.frame_resultado.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    def crear_matriz1(self):
        filas = int(self.filas1.get())
        columnas = int(self.columnas1.get())
        self.mostrar_entrada_matriz(1, filas, columnas)
    
    def crear_matriz2(self):
        filas = int(self.filas2.get())
        columnas = int(self.columnas2.get())
        self.mostrar_entrada_matriz(2, filas, columnas)
    
    def mostrar_entrada_matriz(self, numero_matriz, filas, columnas):
        # Limpiar frame de matrices
        for widget in self.frame_matrices.winfo_children():
            if hasattr(widget, 'matriz_num') and widget.matriz_num == numero_matriz:
                widget.destroy()
        
        # Crear frame para la matriz
        frame_matriz = tk.LabelFrame(self.frame_matrices, 
                                   text=f"Matriz {numero_matriz}", 
                                   font=("Arial", 11, "bold"), bg="#f0f0f0")
        frame_matriz.matriz_num = numero_matriz
        
        if numero_matriz == 1:
            frame_matriz.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)
        else:
            frame_matriz.pack(side=tk.RIGHT, padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Crear grid de entradas
        entradas = []
        for i in range(filas):
            fila_entradas = []
            for j in range(columnas):
                entry = tk.Entry(frame_matriz, width=6, justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                fila_entradas.append(entry)
            entradas.append(fila_entradas)
        
        # Botón para capturar matriz
        btn_capturar = tk.Button(frame_matriz, 
                               text=f"Capturar Matriz {numero_matriz}",
                               command=lambda: self.capturar_matriz(numero_matriz, entradas),
                               bg="#f39c12", fg="white")
        btn_capturar.grid(row=filas, column=0, columnspan=columnas, pady=10)
    
    def capturar_matriz(self, numero_matriz, entradas):
        try:
            matriz = []
            for fila_entradas in entradas:
                fila = []
                for entry in fila_entradas:
                    valor = int(entry.get())
                    fila.append(valor)
                matriz.append(fila)
            
            if numero_matriz == 1:
                self.matriz1 = matriz
                messagebox.showinfo("Éxito", "Matriz 1 capturada correctamente")
            else:
                self.matriz2 = matriz
                messagebox.showinfo("Éxito", "Matriz 2 capturada correctamente")
                
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese solo números enteros")
    
    def sumar_matrices(self):
        if not self.validar_matrices_para_suma_resta():
            return
        
        resultado = []
        for i in range(len(self.matriz1)):
            fila = []
            for j in range(len(self.matriz1[0])):
                suma = self.matriz1[i][j] + self.matriz2[i][j]
                fila.append(suma)
            resultado.append(fila)
        
        self.mostrar_resultado("Suma (A + B)", resultado)
    
    def restar_matrices(self):
        if not self.validar_matrices_para_suma_resta():
            return
        
        resultado = []
        for i in range(len(self.matriz1)):
            fila = []
            for j in range(len(self.matriz1[0])):
                resta = self.matriz1[i][j] - self.matriz2[i][j]
                fila.append(resta)
            resultado.append(fila)
        
        self.mostrar_resultado("Resta (A - B)", resultado)
    
    def multiplicar_matrices(self):
        if not self.validar_matrices_para_multiplicacion():
            return
        
        filas_a = len(self.matriz1)
        columnas_b = len(self.matriz2[0])
        columnas_a = len(self.matriz1[0])
        
        resultado = []
        for i in range(filas_a):
            fila = []
            for j in range(columnas_b):
                suma = 0
                for k in range(columnas_a):
                    suma += self.matriz1[i][k] * self.matriz2[k][j]
                fila.append(suma)
            resultado.append(fila)
        
        self.mostrar_resultado("Multiplicación (A × B)", resultado)
    
    def validar_matrices_para_suma_resta(self):
        if self.matriz1 is None or self.matriz2 is None:
            messagebox.showerror("Error", "Debe capturar ambas matrices primero")
            return False
        
        if len(self.matriz1) != len(self.matriz2) or len(self.matriz1[0]) != len(self.matriz2[0]):
            messagebox.showerror("Error", 
                               "Para suma y resta, las matrices deben tener las mismas dimensiones")
            return False
        
        return True
    
    def validar_matrices_para_multiplicacion(self):
        if self.matriz1 is None or self.matriz2 is None:
            messagebox.showerror("Error", "Debe capturar ambas matrices primero")
            return False
        
        if len(self.matriz1[0]) != len(self.matriz2):
            messagebox.showerror("Error", 
                               "Para multiplicación, el número de columnas de la primera matriz "
                               "debe ser igual al número de filas de la segunda matriz")
            return False
        
        return True
    
    def mostrar_resultado(self, operacion, resultado):
        # Limpiar frame de resultado
        for widget in self.frame_resultado.winfo_children():
            widget.destroy()
        
        # Título del resultado
        titulo_resultado = tk.Label(self.frame_resultado, 
                                  text=f"Resultado de {operacion}:",
                                  font=("Arial", 12, "bold"), bg="#f0f0f0")
        titulo_resultado.pack(pady=5)
        
        # Crear frame para la matriz resultado
        frame_matriz_resultado = tk.Frame(self.frame_resultado, bg="#f0f0f0")
        frame_matriz_resultado.pack(pady=10)
        
        # Mostrar la matriz resultado
        for i, fila in enumerate(resultado):
            for j, valor in enumerate(fila):
                label = tk.Label(frame_matriz_resultado, text=str(valor), 
                               width=6, relief="solid", bg="white", 
                               font=("Arial", 10, "bold"))
                label.grid(row=i, column=j, padx=1, pady=1)
    
    def limpiar(self):
        # Limpiar matrices
        self.matriz1 = None
        self.matriz2 = None
        
        # Limpiar frames
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()
        
        for widget in self.frame_resultado.winfo_children():
            widget.destroy()
        
        messagebox.showinfo("Limpieza", "Todas las matrices han sido limpiadas")
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = CalculadoraMatrices()
    app.ejecutar()
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