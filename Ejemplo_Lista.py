lista_numeros = []


def reducir_lista(lista):
  set_l = set(lista)
  maximo = 0
  for n in set_l:
    if n > maximo:
      maximo = n
  set_l.discard(maximo)
  lista_reducida = list(set_l)
  return lista_reducida


def promedio(lista):
  suma = 0
  i = 0
  for n in lista:
    suma += n
    i += 1
  avg = suma / i
  return avg


lista_numeros = [8, 7, 1, 2, 2, 3, 4, 515, 5, 5, 5, 6]
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))
