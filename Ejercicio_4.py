def contar_primos(numero):
    rango = range(1, numero+1)
    primos = []

    for N in rango:
        divisor = []
        for n in rango:
            if N%n == 0:
                divisor.append(n)
        if len(divisor) <= 2:
            primos.append(N)
    print(f'\nLos números primos desde el 0 hasta tu valor son:\n{primos}')

valor = int(input('Ingresa un número: '))
contar_primos(valor)