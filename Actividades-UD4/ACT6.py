
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    numero_texto = input("Introduce un número de mes (1-12): ")
    
    if numero_texto.isdigit():
        numero_mes = int(numero_texto)
        
        if 1 <= numero_mes <= 12:
            nombre_mes = meses[numero_mes - 1]
            cantidad_dias = dias[numero_mes - 1]
            
            print(f"El mes {numero_mes} es {nombre_mes} y tiene {cantidad_dias} días")
            break
        else:
            print(" El numero debe estar entre 1 y 12")
    else:
        print("Pon un numero valido")