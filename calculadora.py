def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

exit2 = False
historial = ""
while exit2 == False:
    exit = False
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    condicion = input("quieres sumar(+), restar(-), dividir(/) o multiplicar(*)?")
    historial =f"({historial}  {str(num1)} {condicion} {str(num2)} )"

    if condicion == "+":
        print (sumar(num1, num2))
        num1 = sumar(num1, num2)
    elif condicion == "-":
        print (restar(num1, num2))
        num1 = restar(num1, num2)
    elif condicion == "/":
        print (dividir(num1, num2))
        num1 = dividir(num1, num2)
    elif condicion == "*":
        print (multiplicar(num1, num2))
        num1 = multiplicar(num1, num2)

    while exit == False:
        confirmar = input("Quieres ver el historial? Y/N")
        if confirmar == "Y":
            print(historial)
        confirmar = input("Quieres reiniciar la calculadora? Y/N")
        if confirmar == "Y":
            exit = True
            break
        confirmar = input("Quieres seguir calculando? Y/N")
        if confirmar == "N":
            exit = True
            exit2 = True
        elif confirmar == "Y":

            num2 = int(input("Ingresa un numero: "))

            condicion = input("quieres sumar(+), restar(-), dividir(/) o multiplicar(*)?")

            historial ="(" + historial + " " + str(num1) + " " + condicion + " " + str(num2) + ")"

            if condicion == "+":
                print (sumar(num1, num2))
                num1 = sumar(num1, num2)
            elif condicion == "-":
                print (restar(num1, num2))
                num1 = restar(num1, num2)
            elif condicion == "/":
                print (dividir(num1, num2))
                num1 = dividir(num1, num2)
            elif condicion == "*":
                print (multiplicar(num1, num2))
                num1 = multiplicar(num1, num2)
