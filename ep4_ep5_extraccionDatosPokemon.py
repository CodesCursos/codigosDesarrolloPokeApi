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

'''
Este codigo permite descargar la informacion de
los 807 pokemon, esto se realiza en 2 partes:

En la primera parte se descargan 500 pokemon,
es aqui cuando la pokeapi restringe nuestra ip
y tenemos que esperar 1 hora para realizar la
descarga de los pokemon sobrantes,para esta
primera parte nuestra variable numeroPokemon
tendra el valor de 1 (numeroPokemon=1)

En la segunda parte ya habiendo transcurrido
una hora se descargaran los 307 pokemon restantes
y el valor de la variable numeroPokemon, debera
tener el valor de 501 (numeroPokemon=501), ya
que el ultimo pokemon extraido en la primera
parte fue el 500
'''

import requests
import time
url='https://pokeapi.glitch.me/pokemon/'
numeroPokemon=501
codigoRespuesta=200
while codigoRespuesta!=429:
    archivo=open('datosPokemon.txt','a',encoding='utf-8')
    peticion=requests.get(url+str(numeroPokemon))
    codigoRespuesta=peticion.status_code
    respuesta=peticion.text
    archivo.writelines(respuesta+'\n----------\n')
    print(codigoRespuesta)
    print(respuesta)
    numeroPokemon+=1 #numeroPokemon=numeroPokemon+1
    archivo.close()
    if codigoRespuesta==404:
        break
    time.sleep(2)#2 segundos
