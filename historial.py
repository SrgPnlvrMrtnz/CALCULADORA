palabras = []
exit = False

print("Escribre una palabra, si escribes la palabra 'historial', verás el historial, si solo quieres los tres últimos elementos, escribe 'ultimos', deja en blanco para finalizar")

while exit == False:

    palabra = input("Escribra su palabra: ")

    if (palabra == ""):

        exit = True

    elif (palabra.upper() == "historial".upper()):

        print("Historial: " , palabras)
    
    elif (palabra.upper() == "ultimos".upper()):

        print("Historial de los últimos 3 elementos: " , palabras[-3] , " " , palabras[-2] , " " , palabras[-1] , " ")
    else:
        palabras.append(palabra)   

