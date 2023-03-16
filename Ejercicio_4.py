def contar_primos(numero):
    rango = range(1, numero)
    primos = []

    for N in rango:
        divisor = []
        for n in rango:
            if N%n == 0:
                divisor.append(n)
        if len(divisor) <= 2:
            primos.append(N)
    print(primos)

contar_primos(21)