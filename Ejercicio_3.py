def repetido_cero(*args):
    lista = []
    i = 0
    for arg in args:
        lista.append(arg)
    for n in lista:
        if lista[i] == 0 and lista[i+1] == 0:
            repetido = True
            return repetido
        else:
            repetido = False
        i += 1
    return repetido


print(repetido_cero(6,0,5,1,0,3,0,1))