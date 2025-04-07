import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import json
import os  # Para verificar si el archivo existe

# Pedir al usuario que archivo quiere graficar
archivo = input("Ingrese el nombre del archivo a graficar (datos.json o datos_b.json): ")

# Verificar si el archivo existe antes de abrirlo
if not os.path.exists(archivo):
    print(f"El archivo '{archivo}' no existe.")
else:
    # Cargar datos desde el archivo seleccionado
    with open(archivo, "r") as f:
        l = json.load(f)
    
    # Convertir a tuplas
    ltuplas = [tuple(par) for par in l]

    # Verificar si hay datos para graficar
    if not ltuplas:
        print("No hay datos almacenados para graficar.")
    else:
        print(f"Datos cargados desde {archivo}: {ltuplas}")

        # Separar los datos en listas para la grafica
        vx = [x for x, y in ltuplas]
        vy = [y for x, y in ltuplas]

        # Graficar
        plt.plot(vx, vy, marker='o', label=archivo)
        plt.xlabel("Tam. problema")
        plt.ylabel("Operaciones")
        plt.title(f"Comparacion de {archivo}")
        plt.legend()
        plt.grid(True)
        plt.show()
