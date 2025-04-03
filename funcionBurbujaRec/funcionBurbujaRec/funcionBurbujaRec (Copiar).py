import sys
import random
import json
import matplotlib.pyplot as plt
sys.setrecursionlimit(2000)

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
        print("Datos almacenados:", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")


listaTam=[10,50,100,500,1000]
for n in listaTam:
	tamanno_problema = n
	lista_random = [random.randint(0, 1000) for _ in range(tamanno_problema)]
	operaciones = burbuja(lista_random)
	guardar_datos(tamanno_problema, operaciones)

contador = 0
print(f" el contador es: {operaciones}")
cargar_datos()

#lgrafica=[(random.randint(0,10),random.randint(0,10)) for _ in range(10)]
#lgrafica=[(operaciones, tamanno_problema) for _ in range(10)]
#vx=[x for x,y in ltuplas]
#vy=[y for x,y in ltuplas]
#plt.plot(vx, vy, marka='o')
#plt.xlabel("tam. problema")
#plt.ylabel("operaciones")
#plt.title("algoritmo")
#plt.grid(True)
#plt.show()
