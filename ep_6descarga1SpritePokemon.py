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
urlSprite='https://nexus.traction.one/images/pokemon/pokemon/112.png'
peticion=requests.get(urlSprite)
contenidoArchivo=peticion.content
#print(contenidoArchivo)
archivo=open('112.png','wb')
archivo.write(contenidoArchivo)
archivo.close()