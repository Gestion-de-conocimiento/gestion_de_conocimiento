import pyAgrum as gum
import numpy as np
import requests
import numpy as np
import mysql.connector
URL = "http://localhost/arbol/caminoslibreria"
r = requests.get(url = URL)
data = r.json()
caminos = data['caminos']
caminosvalidos=[]
posiciones=[]
for i in range(len(caminos)):
  for j in range(len(caminos[i])):
    if caminos[i][j]==82:
      caminosvalidos.append(caminos[i])
      posiciones.append(j)
      break
for i in range(len(caminosvalidos)):
  print(caminosvalidos[i],posiciones[i])
exit()
bn=gum.loadBN("RedBayesiana_Algebra.bifxml")
ie=gum.LazyPropagation(bn)
print(ie.posterior("82"))
print(ie.posterior("14"))
print(ie.posterior("24"))
print(ie.posterior("83"))
ie.setEvidence({'82': 1})
ie.makeInference()
print(ie.posterior("82"))
print(ie.posterior("14"))
print(ie.posterior("24"))
print(ie.posterior("83"))