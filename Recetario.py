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

def crear_receta():
	  #Esta función crea recetas dada su ubicación (categoría)
		#print(nombre)
		
		nombre = input('Ingresa el nombre de la receta: ')
		nombre = nombre + '.txt'
		archivo = open(Path(carpeta / nombre), 'x')
		return nombre

print(crear_receta())
def crear_cat():
    # Esta función crea categorías (carpetas) en la ubicación carpeta
    print(1)

def eliminar_receta(ruta_archivo):
    # Esta función elimina recetas (archivos) dada su ruta
    print(2)

def eliminar_cat(ruta_cat):
    # Esta función elimina categorías (carpetas) dada su ubicación
    print(3)

def menu():
    eleccion = ''
    volver = input('\n¿Deseas volver al menú principal (s/n)? ').lower()
    while volver != 's' and volver != 'n':
        volver = input('\n¿Deseas volver al menú principal (s/n)? ').lower()
    match volver:
        case 's':
            system('clear')
        case 'n':
            system('clear')
            eleccion = '6'
            print('\nPrograma finalizado\n')
    return eleccion

#bienvenida()
#eleccion_usuario = 'a'
'''while eleccion_usuario != '6':

    eleccion_usuario = sel_usuario()
    match eleccion_usuario:
        case '1':
            print('Leer recetas')
            #Leer receta
            #categorias = buscar_cat()
            #cat_elegida, directorio = elegir_cat(categorias)
            #recetas = buscar_receta(directorio)
            #receta_dir = elegir_receta(recetas)
            #leer_receta(receta_dir)
            eleccion_usuario = menu()
        case '2':
            print('Crear receta')
            #Crear receta
            eleccion_usuario = menu()
        case '3':
            print('Crear categoría')
            #Crear categoría
            eleccion_usuario = menu()
        case '4':
            print('Eliminar receta')
            #Eliminar receta
            eleccion_usuario = menu()
        case '5':
            print('Eliminar categoría')
            #Eliminar categoría
            eleccion_usuario = menu()
        case '6':
            #Finalizar programa
            print('\nPrograma finalizado\n')
            
    
'''
'''
bienvenida()
categorias = buscar_cat()
cat_elegida, directorio = elegir_cat(categorias)
recetas = buscar_receta(directorio)
receta_dir = elegir_receta(recetas)
leer_receta(receta_dir)
'''