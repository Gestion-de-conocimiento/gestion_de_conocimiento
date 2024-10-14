import requests
import numpy as np
import random
import mysql.connector
cptA=[]
print("Cargando nodos...")
URL = "http://localhost/arbol/simulador/caminos"
r = requests.get(url = URL)
data = r.json()
nodos = data['nodos']
caminos = data['caminos']
temas = data['temas']
ramas = data['ramas']
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')

numeros = []
letras = []
for i in range( len(nodos) ):
    for j in range( len(temas)):
        if(temas[j]['id'] == nodos[i]):
            letras.append(temas[j]['nombre'])
    numeros.append(i)
indices = dict(zip(letras,numeros))
padres = []
padres_ids = []
mylist = [1, 2,  3]
for i in range(len(nodos)):
    es_rama = False
    for j in range(len(ramas)):
        if nodos[i] == ramas[j]["id"]:
            es_rama = True
            break
    if not es_rama: 
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
                        es_rama2 = False
                        for l in range(len(ramas)):
                            if caminos[j][k-1] == ramas[l]["id"]:
                                es_rama2 = True
                                break
                        if not es_rama2:
                            padres_nodo.append( letras[nodos.index(caminos[j][k-1])] )
                            padres_nodo_id.append( caminos[j][k-1] )
        #print(padres_nodo)
        padres.append(padres_nodo)
        padres_ids.append(padres_nodo_id)
cPadres=len(padres)
print("Cargando estimaciones...")

probabilidadades=[]
for i in range(len(padres)):
 # print(padres[i][0],padres_ids[i][0])
  cursor = cnx.cursor()
  cursor.execute("SELECT *  from evidencia_expertos where id_tema = "+str(padres_ids[i][0])+" ;")
  ponderaciones=cursor.fetchall()
  pn=[0,0,0]
  for a in ponderaciones:
    pn[0]+=float(a[5])
    pn[1]+=float(a[6])
    pn[2]+=float(a[7])
  pn[0]/=len(ponderaciones)
  pn[1]/=len(ponderaciones)
  pn[2]/=len(ponderaciones)
  probabilidadades.append(pn)
print("Generando dataset...")

dataset = []
evaluaciones=59049
for i in range(evaluaciones):
    r=[]
    for j in range(len(probabilidadades)):
        A = random.choices(mylist, weights = probabilidadades[j])[0]
        r.append(A)
    dataset.append(r)

#for i in range(evaluaciones):
#  print(dataset[i])
 
print("Guardando dataset...")
                 
f = open ("dataset.csv",'wb')
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        texto=str(dataset[i][j])+","
        f.write(texto.encode())
    texto="\n"
    f.write(texto.encode())
#for i in range(evaluaciones):
#    print(dataset[i])
