animales = "gato, perro, canario, pescado, conejo, hámster"

lista_animales = animales.split(", ")

tupla = tuple((animal, len(animal)) for animal in lista_animales)

print("lista:", animales)
print("Tupla :", tupla)