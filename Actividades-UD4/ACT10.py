tupla1 = ('C', 'h', 'R', 'm', 'A', 's', 'M', 'o', 'T', 'y', 'c') 
mayus = tuple(char for char in tupla1 if char.isupper())
minus = tuple(char for char in tupla1 if char.islower())

tupla2 = mayus + minus
print("Tupla original:", tupla1)
print("Tupla resultante:", tupla2)