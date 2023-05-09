from random import randint

intentos = 0
numero_secreto = randint(1,101)
nombre = input('Dime tu nombre: ')

print(f'{nombre} mama huevo!, he pesado un numero entre 1 y 100\nTienes 8 intentos')

while intentos < 8:
    estimado = int(input('cual es el numero?: '))
    intentos += 1

    if estimado > 100:
        print('Eres el mama huevo mas grande de la historia, el numero esta entre el 1 y el 100')

    if estimado < 1:
        print('Me estas jodiendo, vete a tu casa cabron, el numero esta entre el 1 y el 100')

    if estimado < numero_secreto:
        print('Coño el numero es mas alto, estas frio')

    if estimado > numero_secreto:
        print('El diablo, te pasaste, el numero es menor, como vos')

    if estimado == numero_secreto:
        print(f'Felicitaciones  {nombre}! mama huevazo, adivinaste en {intentos} intentos')
        break
if estimado != numero_secreto:
    print(f'Nombe se te acabaron los intentos, el numero era {numero_secreto}')