# Sin protección:
try:
    num1 = float(input("Primer número: "))

    num2 = float(input("Segundo número: "))

    operacion = input("Operación (+, -, *, /): ")


    if operacion == '+':
            print(num1 + num2)
    elif operacion == '-':
            print(num1 - num2)
    elif operacion == '*':
            print(num1 * num2)

    elif operacion == '/':
        print(num1 / num2)
except ZeroDivisionError:
      print ("No se puede dividir entre 0")
except ValueError:
    print ("No se pueden introducir letras o palabras")