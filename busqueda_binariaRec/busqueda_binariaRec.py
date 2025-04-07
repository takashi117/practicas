import sys
import random
import json

contador=0
datos=[]

#funciones
def busqueda_binariaRec(arreglo, inicio, final, objetivo):
    global contador
    contador +=1
    medio=(inicio+final)//2
    
    if(inicio>final):
        #print(f"No se encontro tu elemento: {objetivo} en el arreglo")
        return -1
    
    if(arreglo[medio]==objetivo):
        return medio
    
    elif(objetivo>arreglo[medio]):
        inicio=medio+1
        return busqueda_binariaRec(arreglo, inicio, final, objetivo)
    else:
        final=medio-1
        return busqueda_binariaRec(arreglo, inicio, final, objetivo)

def busqueda_binariaM(arreglo, objetivo):
    tamanno_arreglo=len(arreglo)
    inicio=0
    final=tamanno_arreglo-1
    
    return busqueda_binariaRec(arreglo, inicio, final, objetivo)

def guardar_datos(tamanno, operaciones):
    global datos
    datos.append((tamanno, operaciones))
        
    with open("datos_burRec.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos():
    try:
        with open("datos_burRec.json", "r") as f:
            datos = json.load(f)
        ltuplas = [tuple(par) for par in datos]
        print("\nDatos almacenados (tamanno del problema , operaciones realizadas):\n", ltuplas)
    except FileNotFoundError:
        print("No hay datos almacenados.")
        
def burbuja_rec(arreglo, n):
    if n > 1:
        for i in range(n - 1):
            if arreglo[i] > arreglo[i + 1]:
                aux = arreglo[i + 1]
                arreglo[i + 1] = arreglo[i]
                arreglo[i] = aux
        burbuja_rec(arreglo, n - 1)

def burbuja(arreglo):
    n = len(arreglo)
    burbuja_rec(arreglo, n)
    return contador


#funcion principal
lista_tamArreglo=[5,10,20,50]
lista_objetivos=[random.randint(0, 100) for _ in range(2)]

for n in lista_tamArreglo:
    tamanno_problema=n
    lista_random=[random.randint(0, 100) for _ in range(tamanno_problema)]
    burbuja(lista_random)
    for i in lista_objetivos:
        print(f"tu objetivo: {i}\nTu arreglo de {len(lista_random)} elementos:\n{lista_random}")
        resultado=busqueda_binariaM(lista_random, i)
        if(resultado !=-1):
            print(f"el objetivo {i} esta en la posicion {resultado+1} con un contador: {contador}\n")
            guardar_datos(tamanno_problema,contador)
            print("guardado\n")
            contador=0

        else:
            print(f"No se encontro tu objetivo\nContador: {contador}\n")
            guardar_datos(tamanno_problema,contador)
            print("guardado\n")
            contador=0
            
cargar_datos()

