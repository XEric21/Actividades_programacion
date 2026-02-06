palabra = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if palabra == palabra2:
    print("Las palabras son exactamente iguales.")
elif palabra.lower() == palabra2.lower():
    print("Las palabras son iguales .")
else:
    print("Las palabras son  diferentes.")