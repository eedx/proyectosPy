from os import system
from pathlib import Path

carpeta = Path(Path.home(), 'Recetas')

# ANTES DE PASAR A VSCODE CAMBIAR
# system('clear') por system('cls')

def bienvenida():
    system('clear')
    print('\nBienvenido al recetario v1.0')
    print(f'Nos encontramos en la ruta:\n{carpeta}\n')
    contar_recetas()

def contar_recetas():
    conteo = 0
    for txt in Path(carpeta).glob('**/*.txt'):
        conteo += 1
    print(f'Dentro de este recetario se encuentran {conteo} recetas')

def sel_usuario():
    print('''
    1. Leer receta
    2. Crear receta
    3. Crear categoría
    4. Eliminar receta
    5. Eliminar categoría
    6. Finalizar programa
    ''')
    eleccion = input('Por favor selecciona una opción para continuar: ')
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    opciones = ['1', '2', '3', '4', '5', '6']
    while eleccion not in opciones or eleccion in abecedario:
        eleccion = input('Por favor selecciona una opción válida: ')
    return eleccion

def elegir_cat():
  cat_selec = input('Por favor selecciona una categoría: ')
  abecedario = 'abcdefghijklmnñopqrstuvwxyz'
  opciones = ['1', '2', '3', '4', '5', '6']
  conteo = 0
  categorias = []
  # for root, dirs, files in os.walk(Path(carpeta)):
  for cat in Path(carpeta).glob('*'):
    conteo += 1
    categorias.append(cat)
  categorias.sort()
  while cat_selec not in opciones or cat_selec in abecedario:
    cat_selec = input('Por favor selecciona una opción válida: ')
  cat_selec = int(cat_selec)
  return categorias, cat_selec



bienvenida()
sel_usuario()