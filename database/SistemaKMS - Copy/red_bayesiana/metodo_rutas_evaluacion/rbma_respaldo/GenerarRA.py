import requests
import mysql.connector
import numpy as np
import pickle
from  NODO import NODO
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

for i in caminos:
  print(i)

  


nombre_rbma_pickle = "rbma_1530004.pkl" #pickle
#nombre_rbma_pickle = "rbma/rbma_1530004.pkl" #pickle
infile = open(nombre_rbma_pickle,'rb')
RBMA = pickle.load(infile)
infile.close()
nodos=[]
nodosGDCRB=[]
for i in RBMA[1]:
  if RBMA[1][i].grado_de_conocimiento!=-1:
     print([int(RBMA[1][i].id),int(RBMA[1][i].grado_de_conocimiento)])
  else:
      if  RBMA[1][i].matriz_inferencia_final[0]==0 and RBMA[1][i].matriz_inferencia_final[1]==0 and RBMA[1][i].matriz_inferencia_final[2]==0:
         nodos.append([int(RBMA[1][i].id),RBMA[1][i].matriz_inferencia.index(max(RBMA[1][i].matriz_inferencia))])
      else:
           nodos.append([int(RBMA[1][i].id),RBMA[1][i].matriz_inferencia_final.index(max(RBMA[1][i].matriz_inferencia_final))])  
          
          
for n in nodos:
   if n[1]<2:
    nodosGDCRB.append(n[0])

for n in nodosGDCRB:
  print(n)
  
contador=np.zeros(len(caminos)) 
for i in range(len(caminos)):
  for j in range(len(caminos[i])):
    if caminos[i][j] in nodosGDCRB:
                 contador[i]+=1

for i in range(len(caminos)):
  if contador[i]!=0:
    print(caminos[i],contador[i])
    
 