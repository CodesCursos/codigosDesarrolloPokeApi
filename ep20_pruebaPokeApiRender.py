#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     25/01/2023
# Copyright:   (c) LENOVO 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests

url='https://pokeapi-zxmh.onrender.com/PokeApi/Artesanal/'
nombreoNumeroPokemon='1'
peticion=requests.get(url+nombreoNumeroPokemon)
respuesta=peticion.text
print(respuesta)