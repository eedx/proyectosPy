from random import *
nombre = input('Ingresa tu nombre: ')
reintentar = 's'

print(f'\nPerfecto {nombre}, he pensado un número entre el 1 y el 100. \nTienes solo ocho intentos para adivinar cuál es')

while reintentar == 's':
    reintentar = 'n'
    numero = randint(1, 100)
    i = 0
    while i < 8:
        i += 1
        intento = int(input('\nIngresa un número: '))
        if i == 8 and intento != numero:
            print(f'\nFin del juego, has perdido\nEl número era el {numero}')
            break
        while intento < 0 or intento > 100:
            intento = int(input('\nEse número no es válido, por favor ingresa un número entre 0 y 100: '))
        if intento < numero:
            print(f'\nIntenta con un número más alto, intentos restantes: {8-i}') 
        elif intento > numero:
            print(f'\nIntenta con un número más bajo, intentos restantes: {8-i}')
        else:
            print(f'\nEs correcto, has adivinado con el número {intento} en tu intento #{i}')
            break
    reintentar = str(input('\n¿Deseas volver a jugar? (S/N) ')).lower()
    while reintentar != 's' and reintentar != 'n':
        reintentar = str(input('\nIngresa un valor válido ¿Deseas volver a jugar? (S/N) ')).lower()
    if reintentar == 'n':
        break
