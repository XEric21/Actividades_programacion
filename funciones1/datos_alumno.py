from colorama import Fore, Back, Style, init
nombres = []
primer_apellido_lista = []
segundo_apellido_lista = []
edad_lista = []
def datos_alumno():
    

    while True:
        nombre = str(input ("Dime cual es tu nombre: "))
        if nombre.replace(" ", "").isalpha():
            nombre = " ".join(nombre.split()).title() #Con split dividimos el nombre en partes, y se separan con los espacios, con join juntamos las partes con 1 espacio de separación, y con tittle hacemos que la primera letra de cada palabra esté en mayúscula.
            print(Fore.GREEN+"El nombre es válido ✅"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED+"El nombre no es válido ❌, por favor vuelve a introducirlo: "+Style.RESET_ALL)


    while True:
        primer_apellido = str(input ("Dime cual es tu primer apellido: "))
        if primer_apellido.replace(" ", "").isalpha(): 
            primer_apellido = " ".join(primer_apellido.split()).title() #Con split dividimos el nombre en partes, y se separan con los espacios, con join juntamos las partes con 1 espacio de separación, y con tittle hacemos que la primera letra de cada palabra esté en mayúscula.
            print(Fore.GREEN+"El primer apellido es válido ✅"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED+"El apellido no es válido ❌, por favor vuelve a introducirlo: "+Style.RESET_ALL)

    while True:
        segundo_apellido = str(input ("Dime cual es tu segundo apellido: "))
        if segundo_apellido.replace(" ", "").isalpha(): #Aquí reemplazamos los espacios, juntando las palabras
            segundo_apellido = " ".join(segundo_apellido.split()).title() #Con split dividimos el nombre en partes, y se separan con los espacios, con join juntamos las partes con 1 espacio de separación, y con tittle hacemos que la primera letra de cada palabra esté en mayúscula.
            print(Fore.GREEN+"El segundo apellido es válido ✅"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED+"El segundo apellido no es válido ❌, por favor vuelve a introducirlo: "+Style.RESET_ALL)

    while True:
        try:
            edad = int(input ("Dime cual es tu edad: "))
            if edad < 16:
                print(Fore.RED+"Esa edad no es válida ❌, vuelve a introducir una válida: "+Style.RESET_ALL)
            elif edad > 90:
                print(Fore.RED+"Esa edad no es válida ❌, vuelve a introducir una que sea válida: "+Style.RESET_ALL)
            else:
                print(Fore.GREEN+"La edad es válida"+Style.RESET_ALL)
                break
        except ValueError:
            print(Fore.RED+"La edad debe ser un número ❌, por favor vuelve a introducirla: "+Style.RESET_ALL)
    
    return nombre, primer_apellido, segundo_apellido, edad



