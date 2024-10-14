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
"""    
for i in range(len(padres)):
  print(padres[i],padres_ids[i])
"""

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
    
    
for i in range(len(expertosBuenos)):
  print("Experto: ",expertosBuenos[i])
  for j in range(len(padres)):
    print("Verificación del tema: ",padres[j][0])
    for k in range(1,len(padres[j])): 
      print("Padre:",padres[j][k])
      cursor = cnx.cursor()
      cursor.execute("select bueno from evidencia_expertos where id_tema="+str(padres_ids[j][0])+" and id_usuario ="+str(expertosBuenos[i])+";")
      buenoTH=cursor.fetchall()[0][0]
      print("Estimacion bueno, hijo:",buenoTH)
      cursor = cnx.cursor()
      cursor.execute("select bueno from evidencia_expertos where id_tema="+str(padres_ids[j][k])+" and id_usuario ="+str(expertosBuenos[i])+";")
      buenoTP=cursor.fetchall()[0][0] 
      print("Estimacion bueno, padre:",buenoTP)
      if(buenoTH<buenoTP):
        print("Estimacion valida")
      else:
        print("Estimacion invalida")
        
      print()
    print()
  print()

 