def trobar_maxim(llista):
    try:
        maxim = llista[0]
    except IndexError:
        print ("No hay contenido en la lista")
        return None

    for element in llista:
        if element > maxim:
            maxim = element
    return maxim

llista = []

valor_maxim = trobar_maxim(llista)

print(f"El valor maxim es: {valor_maxim}")