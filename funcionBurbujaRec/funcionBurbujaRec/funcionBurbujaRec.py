import sys
import random
import json
sys.setrecursionlimit(2000)
#Datos globales
contador = 0
datos = []

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
	global datos
	datos.append((tamanno, operaciones))

	with open("datos.json", "w") as f:
        	json.dump(datos, f, indent=4)

def cargar_datos():
    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
        ltuplas = [tuple(par) for par in datos]
        print("\nDatos almacenados (tamanno del problema , operaciones realizadas):\n", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")

#funcion principal
listaTam=[10,50,100,200,500,1000]
condImprimir=False
if listaTam[len(listaTam)-1]<=1000:
    condImprimir=True
    
for n in listaTam:
    tamanno_problema = n
    lista_random=[random.randint(0, 1000) for _ in range(tamanno_problema)]
    if condImprimir == True:
        print(f"\nlista en desorden:\n{lista_random}")
    operaciones = burbuja(lista_random)
    if condImprimir == True:
        print(f"\nlista ordenada:\n{lista_random} con un contador: {operaciones}")
    guardar_datos(tamanno_problema, operaciones)
cargar_datos()
