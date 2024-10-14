import requests
import numpy as np
import random
import mysql.connector
URL = "http://159.203.185.170/arbol/caminoslibreria"
r = requests.get(url = URL)
data = r.json()
numeros = []
letras = []
padres = []
nodos = data['nodos']
caminos = data['caminos']
temas = data['temas']
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')
numeros = []
letras = []
for i in range( len(nodos) ):
    for j in range( len(temas)):
        if(temas[j]['id'] == nodos[i]):
            letras.append(temas[j]['nombre'])
    numeros.append(i)
padres_ids = []
for i in range(len(nodos)): 
    padres_nodo = []
    padres_nodo_id = []
    padres_nodo.append(letras[i])
    padres_nodo_id.append(nodos[i])
    for j in range(len(caminos)):
        for k in range( len(caminos[j]) ):
            if(caminos[j][k] == nodos[i] and k > 0 ):
                repetido = 0
                for l in range( len(padres_nodo) ):
                    if padres_nodo[l]  == letras[nodos.index(caminos[j][k-1])]:
                        repetido = 1
                        break
                if repetido == 0:
                    padres_nodo.append( letras[nodos.index(caminos[j][k-1])] )
                    padres_nodo_id.append( caminos[j][k-1] )
    padres.append(padres_nodo)
    padres_ids.append(padres_nodo_id) 
f = open ("catalogo.csv",'wb')
texto="id,nombre,rama \n"
f.write(texto.encode())
for i in range(len(padres)):
  actual=padres_ids[i][0]
  cont=0
  while(1==1):
    cursor = cnx.cursor()
    cursor.execute("select r.id_padre,r.id_hijo,t.nivel,t.nombre_tema as nombreHijo  from  relacion_primarias r inner join temas t on r.id_hijo = t.id where id_hijo ="+str(actual)+";")
    p=cursor.fetchall()
    if p != []:
      if p[0][2] == 1:
        if cont==0:
          pp="rama"
        else:
          pp=p[0][3]
        break
      else:
        actual=p[0][0]
        cont+=1
    else:
      pp="Area diciplinar"
      break
  print(padres_ids[i][0],padres[i][0],pp)
  texto=str(padres_ids[i][0])+","+str(padres[i][0])+","+str(pp)+"\n"
  f.write(texto.encode())