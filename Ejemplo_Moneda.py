from random import *

lista_numeros = [2, 5, 6, 3, 4, 8]

def lanzar_moneda():
    resultado = choice(['Cara', 'Cruz'])
    return resultado

'''
Esto podría definirse también haciendo:
def lanzar_moneda():
    resultado = randint(1,2)
    if resultado == 1:
        moneda = 'Cara'
        return moneda
    else:
        moneda = 'Cruz'
        return moneda
    '''

def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print('La lista se autodestruirá')
        lista = []
        return lista
    elif moneda == 'Cruz':
        print('La lista fue salvada')
        return lista
      
print(lanzar_moneda())
print(probar_suerte(lanzar_moneda(), lista_numeros))