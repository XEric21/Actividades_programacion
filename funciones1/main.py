from menu import menu_bienvenida
from datos_alumno import datos_alumno
from notas_y_asistencia import notas_y_asistencia
from calcular_promocion import calcular_promocion
from informe_final import informe_final
import time
from colorama import Fore, Back, Style, init

menu_bienvenida()

nombre, primer_apellido, segundo_apellido, edad = datos_alumno()

n1, n2, n3, asistencia = notas_y_asistencia()

media_redondeada, promociona = calcular_promocion(n1, n2, n3, asistencia)

informe_final(nombre, primer_apellido, segundo_apellido, n1, n2, n3, media_redondeada, asistencia, promociona)

