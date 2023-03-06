#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     07/01/2023
# Copyright:   (c) LENOVO 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask,jsonify,url_for
import json
import os
from flask_cors import CORS
aplicacion=Flask(__name__)
CORS(aplicacion)

@aplicacion.route('/')
def bienvenida():
    return 'Bienvenido a la api pokemon'

@aplicacion.route('/AcercaDe')
def acercaDePagina():
    return 'Esta es la api pokemon clonada'

@aplicacion.route('/PokeApi/Artesanal/<numeroOnombre>')
def pokeApiArtesanal(numeroOnombre):
    archivo=open('datosPokemon2.txt','r',encoding='utf-8-sig')
    datosPokemon=archivo.read()
    archivo.close()
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
            respuesta=jsonPokemon
            break
    return jsonify(respuesta)


@aplicacion.route('/muestraPokemon/<numeroOnombre>')
def mostrarPokemon(numeroOnombre):
    sprites=os.listdir('./static/spritesPokemon')
    numeroPokemon=0
    seEncontro=False
    sprites.sort(key=lambda z:int(z.split('.')[0].split('-')[0]))
    for sprite in sprites:
        numeroPokemon=sprite.split('.')[0]
        numeroPokemon=numeroPokemon.split('-')[0]
        if numeroOnombre==numeroPokemon or \
        numeroOnombre.upper() in sprite.upper():
            pokemonElegido=sprite
            seEncontro=True
            break
    if seEncontro==False:
        return 'Pokemon no hallado'
    else:
        return '<img src="'+url_for('static',
        filename='spritesPokemon/'+pokemonElegido)+'">'


if __name__=='__main__':
    aplicacion.run(host='0.0.0.0',port=8020,debug=True)