#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     06/01/2023
# Copyright:   (c) LENOVO 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests

url='https://pokeapi.glitch.me/pokemon/'
nombrePokemon='caterpie'
peticion=requests.get(url+nombrePokemon)
respuesta=peticion.text
print(respuesta)