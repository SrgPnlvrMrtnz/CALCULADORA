palabras = []
exit = False

while exit == False:

    palabra = input("Escribre una palabra, si escribes la palabra 'historial', verás el historial")

    
    if (palabra == ""):

        exit = True

    else: 
        
        palabras.append(palabra)

    if (palabra.upper() == "historial".upper()):

        print("Historial: " , palabras)

