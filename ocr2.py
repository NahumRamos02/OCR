# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:51:52 2016

@author: crush
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import csv
#  ///////// /////    ////////     ///////////    ///////////    ///////
#Nombre:Area 
#Descripcion: calcula el area de la imagen 
#Argumentos:img= imagen que se esta analizando 
#Retorno: area= filas*columnas
def Area (img):
    [filas,columnas]=img.shape #img.shape sirve para obtener los valores de la imgen
    area=filas*columnas
    return area
#Nombre:Relacion 
#Descripcion: calcula la razon entre filas y columnas de la imagen 
#Argumentos:img= imagen que se esta analizando 
#Retorno: razon = filas/columnas
def Relacion(img):
    [numero_filas,numero_columnas]=img.shape
    razon=numero_filas/numero_columnas
    return razon
#Nombre: LineasVerticales5
#Descripcion: crea 5 lineas verticales en la imagen y cuentas veces se cortaron las 5 lineas 
#Argumentos: img = imagen a procesar 
#Retorno: cortado= total de cortes en las 5 lineas 
def lineasVerticales5 (img):
    [numero_filas,numero_columnas]=img.shape 
    movimiento_filas=numero_filas/5
    movimiento_filas=int(movimiento_filas)
    cortado=0

    for j in range(0,numero_filas,movimiento_filas):
        for i in range(0,numero_columnas):
            if img[j,i]!=img[j-1,i]:
                cortado+=1
    return cortado
    
#Nombre: LineasVerticales3
#Descripcion:Creo 3 lineas Verticales y cuento cuantos cortes hubo en las lineas creadas 
#Argumentos: img=imagen a procesar
#Retorno:    cortado= total de cortes que se encontraron 
def lineasVerticales3 (img):
    [filas,columnas]=img.shape 
    movimiento_filas=filas/3
    movimiento_filas=int(movimiento_filas)
    cortado=0

    for j in range(0,filas,movimiento_filas):
        for i in range(0,columnas):
            if img[j,i]!=img[j-1,i]:
                cortado+=1
    return cortado

#Nombre: LineasHorizontales5
#Descripcion: crea 5 lineas horizontales en la imagen y cuenta cuantas veces se encontr un corte en la linea 
#Argumentos:img=imagen a procesar 
#Retorno:cortado= total de cortes en las lineas 
def lineasHorizontales5 (img):
    [filas,columnas]=img.shape
    movimiento_columnas=columnas/5
    movimiento_columnas=int(movimiento_columnas)
    cortado=0
    for j in range(0,columnas,movimiento_columnas):
        for i in range(0,filas):
            if img[i,j]!=img[i-1,j]:
                cortado+=1 
    return cortado

#Nombre: LineasHorizontales3
#Descripcion:crea 3 lineas horizontales en la imagen y cuenta cuantas veces se encontr un corte en la linea 
#Argumentos:img=imagen a procesar 
#Retorno:  cortado= total de cortes en las lineas  
def lineasHorizontales3 (img):
    [filas,columnas]=img.shape
    movimiento_columnas=columnas/3
    movimiento_columnas=int(movimiento_columnas)
    cortado=0
    for j in range(0,columnas,movimiento_columnas):
        for i in range(0,filas):
            if img[i,j]!=img[i-1,j]:
                cortado+=1 
    return cortado
    
    
# Nombre:LineaHorizontal
#Descripcion: crea una linea horizontal en el centro de la imagen y cuento cuantas veces cambio su valor, de 0 a 1 o de 1 a 0
#Argumentos: fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retorno :cortado= el numero de cambios que detecto la funcion, puntos1= total de "1" en la imagen 
def lineaHorizontal(filas,columnas,img):
    area=filas*columnas    
    mitad=filas/2
    mitad=int(mitad)
    cortado=0
    puntos1=0
    for i in range(0,columnas):
    #print(img[d2,contador])
        if img[mitad,i]==1:
            puntos1+=1
        if img[mitad,i]!=img[mitad,i-1]:
            cortado+=1
    #print("lineas horizontales"+str(cortado))
   # print(mitad)
   # print("lo logre!")
    puntos1=area/puntos1
    return cortado,puntos1
    
#Nombre:LineaVertical
#Descripcion: Crea una linea vertical en el centro de la imagen, y cuanta cuantas veces cambio su valor de 0 a 1 o de 1 a 0
#Argumentos:fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retrono:cortado=numero de cambios que detecto la funcion  puntos1= total de "1" en la imagen
def lineaVertical(filas,columnas,img):
    
    area=filas*columnas    
    mitad=0
    cortado=0
    mitad=columnas/2
    mitad=int(mitad)
    puntos1=0
    for i in range(0,filas):
    #print(img[d2,contador])
        if img[i,mitad]==1:
            puntos1+=1
        if img[i,mitad]!=img[i-1,mitad]:
            cortado+=1
    #print("cortes verticales: "+str(cortado))
    #print(mitad)
    puntos1=area/puntos1
    return cortado,puntos1
    
#Nombre:PixelesNegrosyBlancos
#Descripcion:cuento cuantos pixeles son 0 y cuantos son 1
#Argumentos:fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retrono:  blancos=numero de pixeles que son 1 negros= numero de pixeles que son 0   
def pixelesNegrosYBlancos(filas,columnas,img):
    
    area=filas*columnas    
    negros=0
    blancos=0
    for l in range(0,filas):
        for m in range(0,columnas):
            if img[l,m]==1:
                blancos+=1
            else:
                negros+=1
    blancos=area/blancos
    negros=area/negros    
    return blancos,negros

#Nombre:BuscarArchivo
#Descripcion:busca y guarda el nombre de los archivos que tenga en el directorio con terminacion PNG
#Argumentos:ruta= es la ruta donde voy a buscar los archivos PNG
#Retrono:lstFiles=lista con todos los nombres que encontro con terminacion PNG
def BuscarArchivos(ruta): 
    path =ruta
    #Lista vacia para incluir los ficheros
    lstFiles = []
 
     #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
#Crea una lista de los ficheros png que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".png"):
                lstFiles.append(nombreFichero+extension)
                        
    #print(lstFiles)            
    #print ("LISTADO FINALIZADO")
    #print (len(lstFiles))
                        
    return lstFiles

#Nombre: Gato
#Descripcion: creo un hashtag en la imagen, y analizo el cuadro del centro, apartir del centro 
#             agrego cierto nuemero de pixeles hacia arriba,abajo derecha e izquierda, para crear el cuadro en la zona centrica 
#Argumentos: fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retorno: puntosnegros= nuemro de pixeles en 0, contador=total de pixeles analizados 
def Gato(filas,columnas,img):
    area=filas*columnas
    mitadfilas=filas/2# encuentro la pocicion central de las filas
    mitadcolumnas=columnas/2#encuentro la pocicion central de las columnas 
    #se castean para no tener valores flotantes
    mitadfilas=int(mitadfilas)
    mitadcolumnas=int(mitadcolumnas)
    
    ##### aumento y aumento 2 son los pixeles que voy a sumar a lo lados para tener un 20% de la imagen para generar el gato 
    aumento=filas/5 
    aumento2=columnas/5
    aumento=int(aumento)# casteo la variable en caso de que se obtenga un valor decimal 
    aumento2=int(aumento2)# casteo la variable en caso de que se obtenga un valor decimal 
    x1=mitadfilas-aumento # de la mitad de la imagen para abajo
    x2=mitadfilas+aumento # de la mitad de la imagen para arriba
    y1=mitadcolumnas-aumento2# de la mitad de la imagen para izquierda
    y2=mitadcolumnas+aumento2# de la mitad de la imagen para la derecha
    puntosnegros=0
    contador=0 # es para conocer cuantos pixeles hay en la zona que estoy tratando 
    
    for i in range (x1,x2):
        for j in range(y1,y2):
            #print ("  x  "+str(j)+"  y  "+str(i))
            if img[i,j]==0:
                puntosnegros+=1 # si encutro un "0" en la imagen, guardo cuantas veces lo encontre 
            contador+=1
            #img[i,j]=2
    #print (" pixeles negros= "+str(puntosnegros))
    #print("total de pixeles= "+str(contador))
    
    puntosnegros=area/puntosnegros    
    return puntosnegros,contador
    
#Nombre: LineasHorizontales2
#Descripcion:
#Argumentos:
#Retorno:    
def lineasVerticalesyHorizontales2(img):
    
    [filas,columnas]=img.shape   # obtengo el numero de filas y columnas de la imagen  
    area=filas*columnas
    mitadfila=filas/2 # encuentro la mitad de la imagen(largo)
    mitadcolumna=columnas/2#33 encutro la mitad de la imagen (ancho)
    mitadfila=int(mitadfila) # se castean en caso de obtener algun valor decimal
    mitadcolumna=int(mitadcolumna) # se castean en caso de obtener algun valor decimal

    aux1=mitadfila+(filas/10)
    aux2=mitadfila-(filas/10)
    aux3=mitadcolumna+(columnas/10)
    aux4=mitadcolumna-(columnas/10)
    blancos1=0 #cuantos "1" encontre en la primera linea
    blancos2=0 # cuantos "1" encontre en la segunda linea 
    cortado1=0 # cuantos cortes detecte en la primera linea 
    cortado2=0 # cuntos cortes deetecte en la segunda linea 
    
     #pinta rayas horizontales
    for i in range(0,columnas):
        # este bloque encuentra los "1"
        if img[aux1,i]==1:
            blancos1+=1
        if img[aux2,i]==1:
            blancos1+=1
        # Este bloque encuentra los cortes 
        if img[aux1,i]!=img[aux1,i-1]:
            cortado1+=1
        if img[aux2,i]!=img[aux2,i-1]:
            cortado1+=1
    #pinta rayas verticales  
    for i in range (0,filas):
         # este bloque encuentra los "1"
        if img[i,aux3]!=img[i-1,aux3]:
            cortado2+=1
        if img[i,aux4]!=img[i-1,aux4]:
            cortado2+=1
        # Este bloque encuentra los cortes     
        if img[i,aux3]==1:
            blancos2+=1
        if img[i,aux4]==1:
            blancos2+=1
    blancos1=area/blancos1
    blancos2=area/blancos2    
    return blancos1,blancos2,cortado1,cortado2
        

#  /////////////////////////////////////////////////////////////////////////////////////////////////

def main(opc):
    
    if opc=="si":
        ruta='numeros/'
        archivo= open('dataset.csv', 'w', newline='')
        salida = csv.writer(archivo)
        contador=1
        for i in range(0,10):
            print(" obteniendo caracteristicas de "+str(i))
            ruta=ruta+str(i) # agrego el nombre de la carpeta a la ruta 
            ls=BuscarArchivos(ruta) # creo la lista con los nombres de los archivos que encontre 
            
            for j in range(0,len(ls)):
                rutaimagen=ruta+'/'+ls[j] #creo la ruta de la imagen 
                img=mpimg.imread(rutaimagen)
                [fila,columna]=img.shape
                dato1=Relacion(img)
                dato2=Area(img)
                [dato3,negro1]=lineaVertical(fila,columna,img)
                [dato4,negro2]=lineaHorizontal(fila,columna,img)
                [x1,x2,x3,x4]=lineasVerticalesyHorizontales2(img)
                dato5=lineasHorizontales5(img)
                dato6=lineasVerticales5(img)
                dato7=lineasHorizontales3(img)
                dato8=lineasVerticales3(img)
                dato9=x1+x2 #cuantos "1" encontre en los dos cortes 
                dato10=x3+x4# cuantos cambios de valor encontre en los dos cortes 
                dato11=dato2/negro1
                dato12=dato2/negro2
                dato13=(dato3+dato4)/fila # relacion entre los cambios quedetecte en una cruz en la imagen entre las filas 
                [dato14,dato15]=pixelesNegrosYBlancos(fila,columna,img)
                [dato16,dato17]=Gato(fila,columna,img)
                salida.writerow([dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15,dato16,dato17,i,contador])
                #print(str(d1)+","+str(d2)+","+str(d3)+","+str(d4)+","+str(d5)+","+str(d6)+","+str(d7)+" Clase "+str(i))
                contador+=1
            ruta='numeros/'#reinicio la ruta para un nuevo numero
        print("Termine!")   
        archivo.close()

print("crear el dataset?")
opcion=input()

main(opcion)

    


   





















   
    
