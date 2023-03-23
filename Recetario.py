from os import system
from pathlib import Path
import os

carpeta = Path(Path.home(), 'Recetas')
abecedario = 'abcdefghijklmnñopqrstuvwxyz'

# ANTES DE PASAR A VSCODE CAMBIAR BIENVENIDA()
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
    opciones = ['1', '2', '3', '4', '5', '6']
    while eleccion not in opciones or eleccion in abecedario:
        eleccion = input('Por favor selecciona una opción válida: ')
    return eleccion

def buscar_cat():
    directorios = []
    categorias = []
    for cat in Path(carpeta).glob('*'):
        directorios.append(cat)
        categorias.append(os.path.basename(cat))
    categorias.sort()
    directorios.sort()
    
    return categorias

def elegir_cat(lista_categorias):
    num = 1
    opciones = []
    print('\nLas categorías encontradas son las siguientes:\n')
    for c in lista_categorias:
        print(f'{num}. {c}')
        opciones.append(str(num))
        num += 1
    eleccion = input('\nSeleccione una para continuar: ')
    while eleccion not in opciones or eleccion in abecedario:
        eleccion = input('Por favor selecciona una opción válida: ')
    eleccion = int(eleccion)-1

    cat = lista_categorias[eleccion]
    ubicacion = Path(carpeta, cat)
    return cat, ubicacion
    
def buscar_receta(ubicacion):
    directorios = []
    recetas = []
    for txt in Path(ubicacion).glob('*.txt'):
        directorios.append(txt)
        recetas.append(Path(txt))
    directorios.sort()
    recetas.sort()
    return recetas

def elegir_receta(lista_recetas):
    num = 1
    opciones = []
    print('\nLas recetas encontradas son las siguientes:\n')
    for r in lista_recetas:
        print(f'{num}. {r.stem}')
        opciones.append(str(num))
        num += 1
    eleccion = input('\nSeleccione una para continuar: ')
    while eleccion not in opciones or eleccion in abecedario:
        eleccion = input('Por favor selecciona una opción válida: ')
    eleccion = int(eleccion)-1

    rec = lista_recetas[eleccion]
    ubicacion = Path(carpeta, rec)
    return ubicacion

def leer_receta(ubicacion_receta):
    archivo = open(ubicacion_receta)
    print(f'\n{archivo.read()}\n')
    archivo.close()

bienvenida()
'''eleccion_usuario = sel_usuario()
match eleccion_usuario:
    case '1':
        #Leer receta
        categorias = buscar_cat()
        cat_elegida, directorio = elegir_cat(categorias)
        recetas = buscar_receta(directorio)
        receta_dir = elegir_receta(recetas)
        leer_receta(receta_dir)
    case '2':
        #Crear receta
    case '3':
        #Crear categoría
    case '4':
        #Eliminar receta
    case '5':
        #Eliminar categoría
    case '6':
        #Finalizar programa'''

categorias = buscar_cat()
cat_elegida, directorio = elegir_cat(categorias)
recetas = buscar_receta(directorio)
receta_dir = elegir_receta(recetas)
leer_receta(receta_dir)