while True:

    
    nombre = input("Nombre y Apellidos (ej: Juan Perez Garcia): ")
    partes = nombre.split()
    if len(partes) != 3:
        print("tiene que ser nombre, apellido, apellido")
        continue
    
    edad = input("Edad: ")
    if not edad.isdigit() or not (0 <= int(edad) <= 120):
        print("no puedes poner menos de 0 o mas de 120")
        continue
    
    telefono = input("telefono (9 numeros): ")
    if not telefono.isdigit() or len(telefono) != 9:
        print("Error en telefono: debe tener 9 numeros")
        continue
    
    nickname = input("Nickname: ")
    if not nickname.isalnum():
        print("Error en Nickname: debe ser solo letras y números")
        continue
    
    print("Datos bien")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Teléfono: {telefono}")
    print(f"Nickname: {nickname}")
    
  
    if input("quieres meter mas datos?(s/n): ").lower() != 's':

        break


