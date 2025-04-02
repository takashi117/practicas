import random
import json
import sys
sys.setrecursionlimit(2000)
datos = []  # Lista donde guardaremos la informacion

contador = 0

def burbuja_rec(arreglo, n):
    global contador
    if n > 1:
        for i in range(n - 1):
            if arreglo[i] > arreglo[i + 1]:
                contador += 1  # Cuenta los intercambios
                aux = arreglo[i + 1]
                arreglo[i + 1] = arreglo[i]
                arreglo[i] = aux
        burbuja_rec(arreglo, n - 1)

def burbuja(arreglo):
    global contador
    contador = 0  # Reiniciar el contador antes de cada ejecucion
    n = len(arreglo)
    burbuja_rec(arreglo, n)
    return contador  # Retornar numero de operaciones

def guardar_datos(tamanno, operaciones):
    # Guarda el tamanno del problema y el numero de operaciones en un archivo JSON
    global datos
    datos.append((tamanno, operaciones))  # Agregar los nuevos datos

    # Guardar en JSON
    with open("datos.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos():
    # Carga y muestra los datos guardados en el JSON
    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
        ltuplas = [tuple(par) for par in datos]
        print("Datos almacenados:", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")

# Ejecutar pruebas con diferentes tamannos de lista
listaTam = [10, 50, 100, 500, 1000]
for n in listaTam:
    tamanno_problema = n  # Correccion del error
    lista_random = [random.randint(0, 1000) for _ in range(tamanno_problema)]
    operaciones = burbuja(lista_random)
    guardar_datos(tamanno_problema, operaciones)
    print(f"Tamanio: {tamanno_problema}, Operaciones: {operaciones}")  # Mostrar datos en cada iteracion

# Mostrar los datos almacenados en JSON
cargar_datos()
