def Suma_avanzada():
    print('Ingresa los numeros a sumar cuando ya ingreses todos los numeros escribe fin para terminar')
    numeros=[]
    while True:
        entrada=input('Ingresa un número o fin para terminar: ')
        if entrada.lower() == "fin":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print('Ingrese una opcion valida')

    if numeros:
        resultado= sum(numeros)
        print(f'La suma de los numeros es: {resultado}')

    else:
        print('No se ingresaron numeros para sumar')