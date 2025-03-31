import json

contador = 0

def busqueda_binaria(arreglo, objetivo):
    global contador
    inicio = 0
    fin = len(arreglo) - 1

    while inicio <= fin:
        contador += 1
        medio = (inicio + fin) // 2

        if arreglo[medio] == objetivo:
            return medio

        if arreglo[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def guardar_datos(tamanno, operaciones, archivo="datos_busqueda.json"):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = []

    datos.append((tamanno, operaciones))

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos(archivo="datos_busqueda.json"):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
        return [tuple(par) for par in datos]
    except FileNotFoundError:
        return []

lista = list(range(1, 101))
elemento_buscado = 75

contador = 0
resultado = busqueda_binaria(lista, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} esta en la posicion {resultado}")
else:
    print(f"El elemento {elemento_buscado} no esta en la lista")

print(f"Numero de operaciones realizadas: {contador}")

guardar_datos(len(lista), contador)

print("Datos guardados:", cargar_datos())
