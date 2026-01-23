from colorama import Fore, Back, Style, init

def notas_y_asistencia():


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
    
    return n1, n2, n3, asistencia


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

    
   