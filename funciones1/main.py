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

    informe_final(n, a1, a2, n1, n2, n3, media_redondeada, asistencia, promociona)

    mas_alumnos = input("Quieres meter otro alumno? (si/no): ").lower()
    if mas_alumnos != "si":
        break
