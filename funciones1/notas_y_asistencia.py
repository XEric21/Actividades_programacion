from colorama import Fore, Back, Style, init

def notas_y_asistencia():


    while True:
        try:
            n1 = input("Tu nota de la primera evaluación: ").replace(",", ".")
            n1 = float(n1)               
            if 0 <= n1 <= 10:
                print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
        except ValueError:
            print ("Solo se pueden poner números")



    while True:
        try:
            n2 = input("Tu nota de la segunda evaluación: ").replace(",", ".")
            n2 = float(n2)
            if 0 <= n2 <= 10:
                print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
        except ValueError:
            print ("Solo se pueden poner números")

    while True:
        try:
            n3 = input("Tu nota de la tercera evaluación: ").replace(",", ".")
            n3 = float(n3)
            if 0 <= n3 <= 10:
                    print(Fore.GREEN + "La nota es válida ✅" + Style.RESET_ALL)
                    break
            else:
                    print(Fore.RED + "Esa nota no es válida ❌" + Style.RESET_ALL)
        except ValueError:
            print ("Solo puedes poner números")
       



    while True:
        try:
            asistencia = input("Pon tu asistencia: ").replace(",", ".")
            asistencia = float(asistencia)
            if 0 <= asistencia <= 100:
                    print(Fore.GREEN + "La asistencia es válida ✅" + Style.RESET_ALL)
                    break
            else:
                    print(Fore.RED + "Esa asistencia no es válida ❌" + Style.RESET_ALL)
        except ValueError: 
             print ("Solo puedes poner números")
    
    return n1, n2, n3, asistencia


    
   