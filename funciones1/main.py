#Este es el programa final, con excepciones, funciones y listas. El programa permite ingresar los datos de varios alumnos, calcular su media y promocion, y luego buscar informes individuales de cada alumno.

import time
from menu import menu_bienvenida
from datos_alumno import datos_alumno
from notas_y_asistencia import notas_y_asistencia
from calcular_promocion import calcular_promocion
from informe_final import informe_final
from listas_datos_alumno import (
    nombres, primer_apellido_lista, segundo_apellido_lista, edad_lista,
    notas1, notas2, notas3, asistencias, medias, promociones)

menu_bienvenida()

while True:

    n, a1, a2, e = datos_alumno()
    nombres.append(n)
    primer_apellido_lista.append(a1)
    segundo_apellido_lista.append(a2)
    edad_lista.append(e)

    n1, n2, n3, asistencia = notas_y_asistencia()
    notas1.append(n1)
    notas2.append(n2)
    notas3.append(n3)
    asistencias.append(asistencia)

    media_redondeada, promociona = calcular_promocion(n1, n2, n3, asistencia)
    medias.append(media_redondeada)
    promociones.append(promociona)

    mas_alumnos = input("Quieres meter otro alumno? (si/no): ").lower()
    if mas_alumnos != "si":
        break
ver_informes = input("Quieres ver algun informe? (si/no)").lower()

while ver_informes == "si":
    buscar_alumno = input ("Que alumno quieres buscar?: ").lower()

    alumno_encontrado= False

    for i, nombre in enumerate(nombres):
        if nombre.lower() == buscar_alumno:
            alumno_encontrado = True
            informe_final(
            nombres[i],
            primer_apellido_lista[i],
            segundo_apellido_lista[i],
            notas1[i],
            notas2[i],
            notas3[i],
            medias[i],
            asistencias[i],
            promociones[i]
        )
            break
    
    if not alumno_encontrado:
        print ("Ese alumno no esta")
    ver_informes = input ("Quieres ver otro? si/no: ").lower()

print ("Saliendo...")