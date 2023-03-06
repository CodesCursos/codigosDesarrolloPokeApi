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
import requests
import time
archivo=open('datosPokemon.txt','r',encoding='utf-8')
infoPokemon=archivo.readlines()
archivo.close()
url='https://nexus.traction.one/images/pokemon/pokemon'
listaSprites=[]
for linea in infoPokemon:
    if url in linea:
        linea=linea.replace('"sprite": "','')
        linea=linea.replace('",','')
        linea=linea.replace('\n','')
        linea=linea.strip()
        listaSprites.append(linea)
        print(linea)
        print('------------')

for sprite in listaSprites:
    peticion=requests.get(sprite)
    contenidoImagen=peticion.content
    nombreImagen=sprite.split('/')[-1]
    print(f'descargando {nombreImagen}...')
    archivo=open(nombreImagen,'wb')
    archivo.write(contenidoImagen)
    archivo.close()
    time.sleep(2)