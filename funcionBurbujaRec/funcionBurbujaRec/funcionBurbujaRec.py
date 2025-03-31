import random
import json

contador = 0

def burbuja_rec(arreglo, n):
    global contador
    if n > 1:
        for i in range(n - 1):
            if arreglo[i] > arreglo[i + 1]:
                contador += 1
                aux = arreglo[i + 1]
                arreglo[i + 1] = arreglo[i]
                arreglo[i] = aux
        burbuja_rec(arreglo, n - 1)

def burbuja(arreglo):
    global contador
    contador = 0
    n = len(arreglo)
    burbuja_rec(arreglo, n)
    return contador

def guardar_datos(tamanno, operaciones):
    datos = []

    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
    except FileNotFoundError:
        pass

    datos.append((tamanno, operaciones))

    with open("datos.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos():
    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
        ltuplas = [tuple(par) for par in datos]
        print("Datos almacenados:", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")

tamanno_problema = 10
lista_random = [random.randint(0, 1000) for _ in range(tamanno_problema)]

print(f"La lista aleatoria es {lista_random}")
operaciones = burbuja(lista_random)
print(f"La lista ordenada es: {lista_random} y el contador es: {operaciones}")

guardar_datos(tamanno_problema, operaciones)
cargar_datos()
