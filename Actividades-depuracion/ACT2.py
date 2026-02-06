def comptar_vocals(frase):
    comptador = 0
    vocals = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    for lletra in frase:
        if lletra in vocals:
            comptador +=1
    return comptador

frase = "Hola, Benvinguts a la classe de programació!"

nombre_vocals = comptar_vocals(frase)

print(f"Hi ha {nombre_vocals} vocals en la frase.")
