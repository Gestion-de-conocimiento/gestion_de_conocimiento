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
for i in range(len(padres)):
 print(i,padres[i][0])

exit()
for i in range(len(expertos)):
  cursor = cnx.cursor()
  cursor.execute("select count(id) from evidencia_expertos where id_usuario ="+str(expertos[i][0])+";")
  cuenta=cursor.fetchall()
  if cuenta[0][0]==ctemas:
    expertosBuenos.append(expertos[i][0])
    cexpertos+=1
probabilidadades=[]

for i in range(len(padres)):
  cursor = cnx.cursor()
  cursor.execute("SELECT *  from evidencia_expertos where id_usuario = 85 and id_tema = "+str(padres_ids[i][0])+" ;")
  ponderaciones=cursor.fetchall()
  probabilidadades.append(ponderaciones[0][5::])

#for i in range(len(padres)):
#  print(probabilidadades[i])
#exit()


probabilidadades = list(probabilidadades)

for i in range(len(probabilidadades)):
  probabilidadades[i]=list(probabilidadades[i])
  probabilidadades[i][0]+=probabilidadades[i][1]/2
  probabilidadades[i][1]=probabilidadades[i][2]+probabilidadades[i][1]/2
  probabilidadades[i]=probabilidadades[i][0:2]

dataset = []
mylist = [1, 2]

evaluaciones=25
for i in range(evaluaciones):
    r=[]
    for j in range(len(probabilidadades)):
        A = random.choices(mylist, weights = probabilidadades[j])[0]
        r.append(A)
    dataset.append(r)
#for i in range(evaluaciones):
#  print(dataset[i])
#exit()
print("Guardando dataset...")      
f = open ("datasetSolo1Experto2Niveles.csv",'wb')
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        texto=str(dataset[i][j])+","
        f.write(texto.encode())
    texto="\n"
    f.write(texto.encode())