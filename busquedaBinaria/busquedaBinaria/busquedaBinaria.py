import json

contador = 0
datos= []

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

def guardar_datos(tamanno, operaciones):
    global datos
    datos.append((tamanno, operaciones))

    with open("datos_b.json", "w") as f:
        	json.dump(datos, f, indent=4)

def cargar_datos():
    try:
        with open("datos_b.json", "r") as f:
            datos = json.load(f)
        ltuplas = [tuple(par) for par in datos]
        print("Datos almacenados:", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")

lista = list(range(1, 100))
elemento_buscado = 75

contador = 0
resultado = busqueda_binaria(lista, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} esta en la posicion {resultado}")
else:
    print(f"El elemento {elemento_buscado} no esta en la lista")

print(f"Numero de operaciones realizadas: {contador}")

guardar_datos(len(lista), contador)

cargar_datos()
