nombres = []
total_extras = []
precio_hora = 16.25


while True:
    nombre = input("Nombre: ")
    
    
    if nombre == "-":
        break
    
    horas_mes = float(input(f"Horas extras de {nombre}: "))
    
    nombres.append(nombre)
    total_extras.append(horas_mes)


for i in range(len(nombres)):
    dinero = total_extras[i] * precio_hora
    print(f"{nombres[i]}: {total_extras[i]} horas = {dinero:.2f}€")