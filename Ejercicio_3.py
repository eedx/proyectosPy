def repetido_cero(*args):
    lista = []
    i = 0
    for arg in args:
        lista.append(arg)
    for n in lista:
        if i + 1 == len(lista):
            return False
        if lista[i] == 0 and lista[i+1] == 0:
            repetido = True
            return repetido
        else:
            repetido = False
        i += 1
    return repetido

'''
También podría resolverse haciendo:
def repetido_cero(*args):
    i = 0
    for n in args:
        if i + 1 == len(args):
            return False
        if args[i] == 0 and args[i+1] == 0:
            return True
        i += 1
    return False
'''

print(repetido_cero(6,0,5,1,0,3,0,1))