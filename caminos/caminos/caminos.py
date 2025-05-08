todos_caminos=[]
camino_actual=[]


def caminos(x,y):
    if(x==0 and y==0):
        return 1
    elif(x<0 or y<0):
        return 0
    else:
        return caminos(x-1,y) + caminos(x,y-1)
    
cor_x=0
cor_Y=0
cor_x = int(input("Ingresa la cordenada x: "))
cor_y = int(input("Ingresa la cordenada y: "))

print(f"el numero de caminos desde {cor_x} , {cor_y} es de {caminos(cor_x,cor_y)}")