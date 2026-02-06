tupla = (3, 4, 2, 5, 5, 5, 2, 3)
# Convertir la tupla a lista para ordenar
lista = list(tupla)
# Ordenar la lista
lista.sort()
# Convertir la lista ordenada de nuevo a tupla
tupla = tuple(lista)
# Mostrar el resultado
print("Tupla antes:", (3, 4, 2, 5, 5, 5, 2, 3))
print("Tupla ordenada:", tupla)