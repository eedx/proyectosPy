from random import choice

lista_palabras = {'ahorcado':'--------',
                  'jugador':'-------',
                  'pelicula':'--------',
                  'interesante':'-----------',
                  'paralelismo':'-----------'}
'''
lista_palabras = ['ahorcado', 'jugador', 'pelicula', 'interesante', 'paralelismo']
'''
# 1. El sistema debe escoger una palabra (función 1)

def seleccion_palabra(lista):
  seleccion = choice(list(lista.keys()))
  guiones = lista.values()
  
  return seleccion, guiones

palabra = seleccion_palabra(lista_palabras)
print(palabra)
# 1.1. Se deberán mostrar guiones en lugar de las letras


# 2. El usuario escogerá una letra tras otra

# 3. El sistema verificará si la letra se encuentra en la palabra
# 3.1. Si la letra se encuentra en la palabra, se mostrará su lugar
# 3.1.1. Si el usuario adivina todas las letras primero, gana
# 3.2. Si la letra no se encuentra en la palabra, perderá una vida
# 3.2.1. Si las vidas se acaban y el usuario no ha adivinado, pierde

# 4. El sistema verifica si el usuario gana o pierde y devuelve un mensaje
