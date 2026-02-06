
nombres = []    
edades = []

while True:
    nombre = input("Introduce el nombre del alumno (o '-' para terminar): ")
    
    if nombre == '-':
        break
    
    edad_texto = input(f"pon su edad {nombre}: ")
    
    if edad_texto.isdigit():
        edad = int(edad_texto)
        
        nombres.append(nombre)
        edades.append(edad)
    else:
        print("no valida")        

print("mayores de edad:")     
for i in range(len(nombres)):          
    if edades[i] >= 18:                
        print(nombres[i] + " - " + str(edades[i]) + " años")  


if len(edades) >= 2:    
    edades_copia = edades.copy()
    edades_copia.sort(reverse=True)
    max1 = edades_copia[0]
    max2 = edades_copia[1]
    
    print("Los dos más mayores:")
    for i in range(len(nombres)):
        if edades[i] == max1 or edades[i] == max2:
            print(nombres[i] + " - " + str(edades[i]) + " años")