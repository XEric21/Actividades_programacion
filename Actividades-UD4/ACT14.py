cosa1 = {10, 20, 30, 40, 50}        
cosa2 = {30, 40, 50, 60, 70}

iguales = cosa1.intersection(cosa2)
print("iguales:", iguales)

todos_sin_duplicados = cosa1.union(cosa2)
print("todo sin doble:", todos_sin_duplicados)

cosa1.difference_update(cosa2)
print("cosa 1 despues de quitarle lo que haya en cosa2:", cosa1)

cosa1.discard(30)
cosa1.discard(40)
print("quitar 30 y 40:", cosa1)
exclusivos = cosa1.symmetric_difference(cosa2)
print("cosas en una lista y no en otra:", exclusivos)