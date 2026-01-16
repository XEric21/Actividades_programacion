from menu import menu_bienvenida

menu_bienvenida()

from datos_alumno import datos_alumno

datos_alumno()

from notas_y_asistencia import notas_y_asistencia

notas_y_asistencia()

from calcular_promocion import calcular_promocion
calcular_promocion()
    

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

