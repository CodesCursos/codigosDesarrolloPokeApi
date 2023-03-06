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
numeroPokemon='900'
peticion=requests.get(url+numeroPokemon)
codigoRespuesta=peticion.status_code
respuesta=peticion.text
print(codigoRespuesta)
print(respuesta)