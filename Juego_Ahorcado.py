from random import choice

lista_palabras = {'ahorcado':'________',
                  'jugador':'_______',
                  'pelicula':'________',
                  'interesante':'___________',
                  'paralelismo':'___________'}


# 1. El sistema debe escoger una palabra de una lista ✔
def seleccion_palabra(diccionario):
  seleccion = choice(list(diccionario.keys()))
  guiones = diccionario[seleccion]
  
  return seleccion, guiones

# 1.1. Se deberán mostrar guiones en lugar de las letras ✔
palabra, guion = seleccion_palabra(lista_palabras)
print(f'\n{list(guion)}')

# 2. La función principal deberá recibir ingresos del usuario y comprobar si gana o pierde ✔
def intento_jugador(seleccion, guiones):
  vidas = 4
  seleccion_l = list(seleccion)
  guion_l = list(guiones)
  # 2.1. El usuario escogerá una letra tras otra (mientras tenga vidas) ✔
  while vidas >= 0:  
    i = 0   
    intento = input('\nIngresa una letra: ').lower()
    
    # 3. El sistema verificará si la letra se encuentra en la palabra ✔
    if intento in seleccion:
      # 3.1. Si es correcto, se mostrará su lugar en vez de un guión ✔
      for letra in seleccion_l:
        if intento == letra:
          guion_l[i] = guion_l[i].replace('_', intento)
        i += 1  
      print(guion_l)

    # 3.2. Si la letra no se encuentra en la palabra, perderá una vida ✔
    else:
      vidas -= 1
      # 3.2.1. Si todas las vidas se acaban y el usuario no ha adivinado, pierde ✔
      if vidas == 0:
        perdedor = f'\nHas perdido, la palabra era: {seleccion.capitalize()}'
        return perdedor
      else:
        print(f'\nPerdiste una vida, te quedan: {vidas}')
        print(guion_l)

    # 4. Si el usuario adivina todas las letras primero, gana ✔
    if guion_l == seleccion_l:
      ganador = f'\nFelicidades, has ganado adivinando la palabra:\n{seleccion.capitalize()}'
      return ganador

  # 5. El sistema verifica si el usuario gana o pierde y devuelve el mensaje correspondiente ✔

print(intento_jugador(palabra, guion))