def letras_unicas(palabra):
    set_letras = set(palabra)
    lista = list(set_letras)
    lista.sort()
    
    return lista

print(letras_unicas('entretenido'))