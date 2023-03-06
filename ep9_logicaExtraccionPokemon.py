#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     08/01/2023
# Copyright:   (c) LENOVO 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
datosPokemon='[{"name":"charmander","number":3}]\n----------\n'+\
'[{"name":"caterpie","number":10}]\n----------\n'+\
'[{"name":"bulbasaur","number":1}]'

numeroOnombre='bulbasaur'
numeroOnombre=numeroOnombre.upper()
listaDatos=datosPokemon.split('\n----------\n')
respuesta={
  "error": 404,
  "message": "Oh snap! No Pokémon has been discovered in this "+\
  "region. You should head home: https://pokedevs.gitbook.io"
    }
for pokemon in listaDatos:
    #print(pokemon)
    jsonPokemon=json.loads(pokemon)
    nombrePokemon=jsonPokemon[0]['name'].upper()
    numeroPokemon=jsonPokemon[0]['number']
    #print(nombrePokemon+'----'+str(numeroPokemon))
    if nombrePokemon==numeroOnombre or \
    str(numeroPokemon)==numeroOnombre:
        respuesta=pokemon
        break
    print('++++++++++++++')

print(respuesta)