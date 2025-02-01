from suma import Suma
from resta import Resta
from multiplicacion import Multiplicacion
from division import Division
from suma_avanzada import Suma_avanzada

while True:

    print('''Bienvenido a esta calculadora Open Source digita el nùmero de tu opcion deseada    
                                                1 Suma
                                                2 Resta
                                                3 Multiplicacion
                                                4 Division
                                                5 Suma N numeros
                                                6 Salir''')

    opcion = int(input('Qué opcion deseas? ' ))

    if opcion == 1:
        Suma()
    
    elif opcion == 2:
        Resta()

    elif opcion == 3:
        Multiplicacion()

    elif opcion == 4:
        Division()

    elif opcion == 5:
        Suma_avanzada()

    elif opcion == 6:
        print('Hasta luego')
        break

    else:
        print('Digite una opcion disponible')
        pass