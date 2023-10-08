#!/usr/bin/python3

# author almy
from googletrans import Translator


def traducir(palabra, idioma_origen, idioma_destino):
    translator = Translator()
    traduccion = translator.translate(palabra, src=idioma_origen, dest=idioma_destino)
    return traduccion.text

palabra = input("Ingrese una palabra: ")
idioma_destino = input("Seleccione un idioma de destino (1:alemán, 2: inglés, 3: español): ")

if idioma_destino == "1":
    traduccion = traducir(palabra, 'es', 'de')
    print("Traducción al alemán:", traduccion)

elif idioma_destino == "2":
    traduccion = traducir(palabra, 'es', 'en')
    print("Traducción al inglés:", traduccion)

elif idioma_destino == "3":
    idioma_origen = input("Seleccione el idioma de origen (1: alemán, 2: inglés): ")

    if idioma_origen == "1":
        traduccion = traducir(palabra, 'de', 'es')
        print("Traducir al español:", traduccion)

    elif idioma_origen == "2":
        traduccion = traducir(palabra, 'en', 'es')
        print("Traduccion al español:", traduccion)
    else:
        print("Idioma de origen no valido")

else:
    print("Opcion de idioma no valida")
