import time
from colorama import Fore, Back, Style, init

def informe_final(nombre, primer_apellido, segundo_apellido, n1, n2, n3, media_redondeada, asistencia, promociona):
    
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
        

