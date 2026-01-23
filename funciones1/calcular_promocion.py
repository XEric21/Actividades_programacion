from colorama import Fore, Back, Style, init

def calcular_promocion(n1, n2, n3, asistencia):

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
    
    return media_redondeada, promociona
