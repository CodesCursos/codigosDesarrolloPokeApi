#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     12/01/2023
# Copyright:   (c) LENOVO 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import json
archivo=open('datosPokemon2.txt','r',encoding='utf-8-sig')
datosPokemon=archivo.read()
archivo.close()
listaDatos=datosPokemon.split('\n----------\n')
sprites=os.listdir('.\spritesPokemon')
print(sprites)
numeroPokemon=0
for sprite in sprites:
    numeroPokemon=sprite.split('.')[0]
    if '-' in numeroPokemon:
        numeroPokemon=numeroPokemon.split('-')[0]
    numeroPokemon=int(numeroPokemon)
    numeroPokemon-=1 #numeroPokemon=numeroPokemon-1
    pokemonDatos=json.loads(listaDatos[numeroPokemon])
    nombrePokemon=pokemonDatos[0]['name']
    nombrePokemon=nombrePokemon.replace("'",'')
    nombrePokemon=nombrePokemon.replace(":",'')
    nombrePokemon=nombrePokemon.replace(" ",'')
    nuevoNombre=sprite.split('.')[0]+'-'+nombrePokemon+'.png'
    print(f'{sprite} por  {nuevoNombre}')
    os.rename('./spritesPokemon/'+sprite,'./spritesPokemon/'+nuevoNombre)
    print(nombrePokemon)
    print(numeroPokemon)
    print('-------------')