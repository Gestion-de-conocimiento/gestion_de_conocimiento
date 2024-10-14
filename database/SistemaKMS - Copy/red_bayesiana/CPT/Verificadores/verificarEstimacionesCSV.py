import requests
import numpy as np
import random
import mysql.connector
cptA=[]
print("Cargando nodos...")
URL = "http://localhost/arbol/caminoslibreria"
r = requests.get(url = URL)
data = r.json()
numeros = []
letras = []
padres = []
nodos = data['nodos']
caminos = data['caminos']
temas = data['temas']
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')
mylist = [1, 2,  3]
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

cursor = cnx.cursor()
cursor.execute("select count(id) from temas")
ctemas=cursor.fetchall()[0][0]
cursor = cnx.cursor()
cursor.execute("select id from users where id_rol=2 and eliminado=0")
expertos=cursor.fetchall()
expertosBuenos=[]
probabilidadades=[]
for i in range(len(expertos)):
  cursor = cnx.cursor()
  cursor.execute("select count(id) from evidencia_expertos where id_usuario ="+str(expertos[i][0])+";")
  cuenta=cursor.fetchall()
  if cuenta[0][0]==ctemas:
    expertosBuenos.append(expertos[i][0])
NexpertosBuenos=[]

vEValidas=[]
vEInvalidas=[]
for i in range(len(expertosBuenos)):
  cursor = cnx.cursor()
  cursor.execute("select nombre,apellido_paterno,apellido_materno from users where id = "+str(expertosBuenos[i])+";")
  nexperto=cursor.fetchall()
  NexpertosBuenos.append(nexperto[0])
  vEValidas.append(0)
  vEInvalidas.append(0)
padres= padres[1::]
padres_ids= padres_ids[1::]

f = open ("validaciones.csv",'wb')
f2 = open ("validacionesI.csv",'wb')
texto="hijos,"
f.write(texto.encode())
f2.write(texto.encode()) 
for i in range(len(expertosBuenos)):
  texto=NexpertosBuenos[i][0]+" "+NexpertosBuenos[i][1]+" "+NexpertosBuenos[i][2]+","
  f.write(texto.encode())
  f2.write(texto.encode())
texto="\n"
f.write(texto.encode())
f2.write(texto.encode()) 
for i in range(len(padres)):
  texto=padres[i][0]+","
  f.write(texto.encode())
  f2.write(texto.encode())
  for j in range(len(expertosBuenos)):
    cursor = cnx.cursor()
    cursor.execute("select bueno from evidencia_expertos where id_tema="+str(padres_ids[i][0])+" and id_usuario ="+str(expertosBuenos[j])+";")
    buenoTH=cursor.fetchall()[0][0]
    texto="E:"+str(buenoTH)+" "
    texto2="E:"+str(buenoTH)+" "
    for k in range(1,len(padres[i])):
      cursor = cnx.cursor()
      cursor.execute("select bueno from evidencia_expertos where id_tema="+str(padres_ids[i][k])+" and id_usuario ="+str(expertosBuenos[j])+";")
      buenoTP=cursor.fetchall()[0][0] 
      if(buenoTH>buenoTP):
        texto2+=padres[i][k]+":"+str(buenoTP)+" "
        vEInvalidas[j]+=1
      else:
        vEValidas[j]+=1
      texto+=padres[i][k]+":"+str(buenoTP)+" "
    texto+=","
    texto2+=","
    f.write(texto.encode())
    f2.write(texto2.encode())
  texto="\n"
  f.write(texto.encode())
  f2.write(texto.encode())
  texto="Suma validas,"
  texto2="Suma invalidas,"
for i in range(len(expertosBuenos)):
  texto+=str(vEValidas[i])+","
  texto2+=str(vEInvalidas[i])+","
f.write(texto.encode())
f2.write(texto2.encode())
  
