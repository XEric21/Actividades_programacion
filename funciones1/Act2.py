import time
from colorama import Fore, Back, Style, init
centro = "CIPFP LUIS SUÑER"
print(Fore.BLUE+"|------ Control de Promoción del " +  centro + "------|") 
print("|-----------------------------------------------------|"+Style.RESET_ALL)
print(Fore.YELLOW+"|--------------- Entrando al sistema... --------------|")
print("|-----------------------------------------------------|"+Style.RESET_ALL)
time.sleep(3)
print(Fore.GREEN +"|--------------------- Cargando... -------------------|"+ Style.RESET_ALL)
time.sleep(5)
print(Fore.BLUE+"|----------------------------------------------------------|")
print("|--------------- Hola, Bienvenido/a al sistema ------------|"+Style.RESET_ALL)
print(Fore.YELLOW+"|========= Registro del alumnado del " +  centro +"========|")
print("|----------------------------------------------------------|"+Style.RESET_ALL)

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
    edad = int(input ("Dime cual es tu edad: "))
    if edad < 16:
        print(Fore.RED+"Esa edad no es válida ❌, vuelve a introducir una válida: "+Style.RESET_ALL)
    elif edad > 90:
        print(Fore.RED+"Esa edad no es válida ❌, vuelve a introducir una que sea válida: "+Style.RESET_ALL)
    else:
        print(Fore.GREEN+"La edad es válida"+Style.RESET_ALL)
        break





while True:
    n1 = input("Tu nota de la primera evaluación: ").replace(",", ".")
    
    if n1.replace(".", "", 1).isdigit(): #Cambiamos
        n1 = float(n1)
        if 0 <= n1 <= 10:
            print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Solo puedes poner números ❌" + Style.RESET_ALL)



while True:
    n2 = input("Tu nota de la segunda evaluación: ").replace(",", ".")
    
    if n2.replace(".", "", 1).isdigit():
        n2 = float(n2)
        if 0 <= n2 <= 10:
            print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Solo puedes poner números ❌" + Style.RESET_ALL)




while True:
    n3 = input("Tu nota de la tercera evaluación: ").replace(",", ".")
    
    if n3.replace(".", "", 1).isdigit():
        n3 = float(n3)
        if 0 <= n3 <= 10:
            print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Solo puedes poner números ❌" + Style.RESET_ALL)



while True:
    asistencia = input("Pon tu asistencia: ").replace(",", ".")
    
    if asistencia.replace(".", "", 1).isdigit():
        asistencia = float(asistencia)
        if 0 <= asistencia <= 100:
            print(Fore.GREEN + "La asistencia es válida ✅" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Esa asistencia no es válida ❌" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Solo puedes poner números ❌" + Style.RESET_ALL)
    

media = (n1 + n2 + n3) /3
media_redondeada = round(media, 2)

if media_redondeada < 5:
    print(Fore.RED+"Suspendido ❌"+Style.RESET_ALL)
else:
    print(Fore.GREEN+"Nota aprobada ✅"+Style.RESET_ALL)

if asistencia < 85:
    print(Fore.RED+"No llegas a la asistencia mínima ❌"+Style.RESET_ALL)
else:
    print(Fore.GREEN+"Cumples con la asistencia ✅ "+Style.RESET_ALL)

promociona = False 
if media_redondeada >=5  and asistencia>= 85:
    print(Fore.GREEN+"Aprueba ✅"+Style.RESET_ALL)
    promociona = True
else:
    print(Fore.RED+"Suspende ❌"+Style.RESET_ALL)
    promociona = False
print(Fore.BLUE+"|==================== INFORME FINAL ====================|"+Style.RESET_ALL)
time.sleep(3)
print(Fore.GREEN + f"Nombre y apellidos: {nombre} {primer_apellido} {segundo_apellido}" + Style.RESET_ALL)
print(Fore.GREEN+"|Nota de evaluacion 1:"+Style.RESET_ALL, n1)
print(Fore.GREEN+"|Nota de evaluacion 2:"+Style.RESET_ALL, n2)
print(Fore.GREEN+"|Nota de evaluacion 3:"+Style.RESET_ALL, n3)
print(Fore.YELLOW+"|Media del curso :"+Style.RESET_ALL, media_redondeada)
print(Fore.YELLOW+"|Asistencia total:"+Style.RESET_ALL, asistencia)

if promociona:
    print(Fore.GREEN+"¿Promociona?: ✅ Sí" +Style.RESET_ALL)
else:
    print(Fore.RED+"¿Promociona?: ❌ No" +Style.RESET_ALL)

