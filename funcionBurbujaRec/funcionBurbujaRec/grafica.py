import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import json

with open("datos.json","r")as f: l=json.load(f)
ltuplas=[tuple(par) for par in l]
print(ltuplas)

l=[(random.randint(0,10),random.randint(0,10)) for _ in range (10)]

vx=[x for x,y in ltuplas]
vy=[y for x,y in ltuplas]

plt.plot(vx, vy, marker='o')
plt.xlabel("tam. problema")
plt.ylabel("operaciones")
plt.title("Algoritmo")
plt.grid(True)
plt.show()
