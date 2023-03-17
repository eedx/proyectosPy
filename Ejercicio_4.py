def contar_primos(numero):
    rango = range(2, numero+1)
    primos = []
    i = 0
    
    if numero < 2:
        print('Por convención el 0 y 1 no se consideran primos')
        return 0
    
    for N in rango:
        divisor = []
        for n in rango:
            if N%n == 0:
                divisor.append(n)
        if len(divisor) == 1:
            primos.append(N)
            i += 1
    print(f'\nLos números primos hasta tu valor son {i}:\n{primos}')
    return i

valor = int(input('Ingresa un número: '))
contar_primos(valor)