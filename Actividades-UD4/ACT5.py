import random

lista = [random.randint(1, 10) for _ in range(5)]

print(f" {lista}")
print()

print("U    D     C     M")

for numero in lista:
    unidades = numero
    decenas = numero * 10
    centenas = numero * 100
    miles = numero * 1000
    print(f"{unidades}   {decenas}    {centenas}   {miles}")