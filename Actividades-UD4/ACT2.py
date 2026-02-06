frase = input("Introduce una frase: ")

palabras = frase.split()

print("Las palabras son")
for palabra in palabras:
    print(palabra)

print("Número de palabras en la frase:", len(palabras))