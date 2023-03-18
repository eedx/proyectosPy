from random import choice

lista_palabras = {'ahorcado':'________',
                  'jugador':'_______',
                  'pelicula':'________',
                  'interesante':'___________',
                  'paralelismo':'___________'}
'''
lista_palabras = ['ahorcado', 'jugador', 'pelicula', 'interesante', 'paralelismo']
'''
# 1. El sistema debe escoger una palabra (función 1) ✔
# 1.1. Se deberán mostrar guiones en lugar de las letras ✔

def seleccion_palabra(diccionario):
  seleccion = choice(list(diccionario.keys()))
  guiones = diccionario[seleccion]
  
  return seleccion, guiones

palabra, guion = seleccion_palabra(lista_palabras)
print(guion)

# 2. El usuario escogerá una letra tras otra ✔

def intento_jugador(seleccion, guiones):
  vidas = 4
  i = 0
  while vidas > 0:  
    intento = input('Ingresa una letra: ').lower()
    if intento in seleccion:
      for letra in seleccion:
        if intento == letra:
          acierto = guiones.replace(guiones[i], intento)
          print(acierto)
          print(letra)
          print(guiones[i])
        i += 1
    else:
      vidas -= 1
      if vidas == 0:
        print(f'Has perdido, la palabra era: {seleccion}')
        break
      else:
        print(f'Perdiste una vida, te quedan: {vidas}')


print(intento_jugador(palabra, guion))
  

# 3. El sistema verificará si la letra se encuentra en la palabra
# 3.1. Si la letra se encuentra en la palabra, se mostrará su lugar
# 3.1.1. Si el usuario adivina todas las letras primero, gana
# 3.2. Si la letra no se encuentra en la palabra, perderá una vida ✔
# 3.2.1. Si las vidas se acaban y el usuario no ha adivinado, pierde

# 4. El sistema verifica si el usuario gana o pierde y devuelve un mensaje
