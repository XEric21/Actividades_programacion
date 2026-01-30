# PROBLEMA: Pide al usuario un índice y muestra el elemento en esa posición
try:
    amigos = ["Ana", "Luis", "Carlos", "María"]

    # Sin try-except:
    indice = int(input(f"Elige un índice (0-{len(amigos)-1}): "))
    print(f"Tu amigo es: {amigos[indice]}")
except IndexError:
    print ("Te has pasado")
except ValueError:
    print ("No se pueden introducir letras o palabras")