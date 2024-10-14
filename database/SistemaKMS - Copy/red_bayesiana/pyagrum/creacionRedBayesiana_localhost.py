# http://www-desir.lip6.fr/~phw/aGrUM/docs/last/notebooks/
import requests
import matplotlib.pyplot as plt
import os
import pyAgrum as gum

URL = "http://localhost/arbol/caminoslibreria"
r = requests.get(url = URL)

data = r.json()
numeros = []
letras = []
padres = []
nodos = data['nodos']
caminos = data['caminos']
temas = data['temas']
grafo_txt = ""

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

bn=gum.BayesNet('RedBayesianaKMS')
nodos_ = {}
for tema in temas:
    nodos_[tema['nombre'].strip()] = bn.add(gum.LabelizedVariable( tema['nombre'].strip().replace(u'\xa0', u' ') , tema['nombre'].strip().replace(u'\xa0', u' '), 3)) 

for p in padres:
    for j in p[1:]:
        bn.addArc( nodos_[j.strip().replace(u'\xa0', u' ')], nodos_[p[0].strip().replace(u'\xa0', u' ')])

print(gum.availableBNExts())
print(bn)
#gum.saveBN(bn,"redbayesiana.dsl")

for i in range(len(padres)):
    for j in range(len(padres[i])):
        padres[i][j] = padres[i][j].strip()
        
urls = []
for i in range(len(padres_ids)):
    padresStr = ""
    esPrimero = True
    for t in padres_ids[i]:
        if not esPrimero:
            padresStr = padresStr + "_" + str(t)
        esPrimero = False
    
    if padresStr == "":
        padresStr = "_"
    
    url = "http://localhost/obtenercpts/" + str(padres_ids[i][0]) + "/" + padresStr
    tpcs = requests.get(url).json()[0]
    #print(url)
    
    for t in tpcs:
        probabilidades = t['estados_padres'].split("_")[1:]
        pp = padres[i][1:]
        
        if t['estado'] == '1':
            dic = {}            
            for j in range( len(probabilidades) ):
                dic[pp[j]] = int(probabilidades[j]) - 1
            probs = []
            probs.append(t['probabilidad'])
        else:
            probs.append(t['probabilidad'])
        
        if t['estado'] == '3':
            print(dic)
            print(padres[i][0])
            bn.cpt(padres[i][0])[dic] = probs
            
print(gum.availableBNExts())
print(bn)
gum.saveBN(bn,"redbayesiana_servidor_localhost.bifxml")
        
        
