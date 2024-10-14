import requests
import numpy as np
import random
import mysql.connector
cptA=[]
print("Cargando nodos...")
URL = "http://localhost/arbol/caminoslibreria"
r = requests.get(url = URL)

exit()
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
cPadres=len(padres)
print("Cargando estimaciones...")
cursor = cnx.cursor()
cursor.execute("select count(id) from temas")
ctemas=cursor.fetchall()[0][0]
cursor = cnx.cursor()
cursor.execute("select id from users where id_rol=2 and eliminado=0")
expertos=cursor.fetchall()
expertosBuenos=[]
cexpertos=0;
probabilidadades=[]
for i in range(len(expertos)):
  cursor = cnx.cursor()
  cursor.execute("select count(id) from evidencia_expertos where id_usuario ="+str(expertos[i][0])+";")
  cuenta=cursor.fetchall()
  if cuenta[0][0]==ctemas:
    expertosBuenos.append(expertos[i][0])
    cexpertos+=1
for i in range(cexpertos):
  probabilidadades.append([]) 
for i in range(cexpertos):
  for j in range(len(padres)):
    
    cursor = cnx.cursor()
    cursor.execute("SELECT *  from evidencia_expertos where id_usuario = "+str(expertosBuenos[i])+" and id_tema = "+str(padres_ids[j][0])+" ;")
    ponderaciones=cursor.fetchall()
    probabilidadades[i].append(ponderaciones[0][5::])
probabilidadadesP=[]
for i in range(len(probabilidadades[0])):
  pp=[0,0,0]
  for j in range(len(expertosBuenos)):
    pp[0]+=probabilidadades[j][i][0]
    pp[1]+=probabilidadades[j][i][1]
    pp[2]+=probabilidadades[j][i][2]
  pp[0]=round(pp[0]/len(expertosBuenos))
  pp[1]=round(pp[1]/len(expertosBuenos))
  pp[2]=round(pp[2]/len(expertosBuenos))
  pp[0]+=pp[1]/2
  pp[1]=pp[2]+pp[1]/2
 

 
  if pp[0]+pp[1]<100:
     pp[0]+=100-(pp[0]+pp[1])
  if pp[0]+pp[1]<100:
     pp[0]-=(pp[0]+pp[1])-100
  probabilidadadesP.append(pp[0:2] )

dataset = []
evaluaciones=100000
niveles = [1, 2]
print("Generamdo dataset...")
for i in range(evaluaciones):
    r=[]
    for j in range(len(probabilidadadesP)):
        A = random.choices(niveles, weights = probabilidadadesP[j])[0]
        r.append(A)
    dataset.append(r)
#for a in(dataset):
  #print(a)
print("Guardando dataset...")      
f = open ("dataset2Niveles.csv",'wb')
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        texto=str(dataset[i][j])+","
        f.write(texto.encode())
    texto="\n"
    f.write(texto.encode())