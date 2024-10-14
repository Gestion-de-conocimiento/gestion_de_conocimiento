import requests
import mysql.connector
import numpy as np
URL = "http://localhost/arbol/caminoslibreria"
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')

r = requests.get(url = URL)
data = r.json()
numeros = []
letras = []
padres = []
nodos = data['nodos']
caminos = data['caminos']
temas = data['temas']
for i in range( len(nodos) ):
    for j in range( len(temas)):
        if(temas[j]['id'] == nodos[i]):
            letras.append(temas[j]['nombre'])
    numeros.append(i)

print("Cargando nodos")
indices = dict(zip(letras,numeros))
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

padres_ids.sort()   
tipo=[]
ramas=[]
vramas=[]

for i in range(len(padres_ids)):
  cursor = cnx.cursor()
  cursor.execute("select nivel from temas where id="+str(padres_ids[i][0])+";")
  t=cursor.fetchall()
  if t[0][0] < 2:
    tipo.append(1)
    ramas.append(padres_ids[i][0])
  else:
    tipo.append(0)
 
for i in range(len(ramas)):
  saltos=0
  ind=0
  for j in range(len(caminos)):
    if not( caminos[j][2] in ramas):
      if caminos[j][1]==ramas[i]:
        if len(caminos[j]) > saltos:
          saltos = len(caminos[j])
          ind=j
  vramas.append(saltos-2)
  #rint(ramas[i],caminos[ind],saltos,len(caminos[ind]))
vramas[0]=0
#for i in range(len(ramas)):
  #print(ramas[i],vramas[i])
 
for i in range(len(padres_ids)):
  d=0
  id=-1
  for j in range(len(caminos)):
    if padres_ids[i][0] in caminos[j]:  
      if caminos[j].index(padres_ids[i][0]) > d:  
        id=j
        d=caminos[j].index(padres_ids[i][0])
  v=0
  for k in range(0,d+1):
    #print(k)
    if caminos[id][k] in ramas:
      if caminos[id][k+1] in ramas:
        v+=vramas[ramas.index(caminos[id][k])]
    else:
      v+=1
    #print("v",v)
  cursor=cnx.cursor()
  if caminos[id][k] in ramas:
    print(padres_ids[i][0],vramas[ramas.index(caminos[id][k])])
    cursor.execute("update temas set dificultad=" + str(vramas[ramas.index(caminos[id][k])])+" where id ="+str(padres_ids[i][0])+";")
  else:
    cursor.execute("update temas set dificultad=" + str(v)+" where id ="+str(padres_ids[i][0])+";")
    print(padres_ids[i][0],v)
cnx.commit()
  
  #print(caminos[id])
print()
print()
for i in range(len(ramas)):
  print(ramas[i],vramas[i])