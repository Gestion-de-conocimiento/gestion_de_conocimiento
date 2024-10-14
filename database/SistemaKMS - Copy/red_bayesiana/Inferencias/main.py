import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import requests
from nodo import NODO
from subredbayesiana import SUB_RED_BAYESIANA

URL = "http://104.248.232.150/arbol/caminoslibreria"
respuestaDelServidor = requests.get(url = URL).json()
caminos = respuestaDelServidor['caminos']
saltos = 1
tema_objetivo = 73
ponderacion_objetiva = 90
caminos_ordenados = {}
NODOS = {}
RED_BAYESIANA = SUB_RED_BAYESIANA(['MPCN.py',tema_objetivo,ponderacion_objetiva,saltos]).obtenerSubRed()
ie=gum.LazyPropagation(RED_BAYESIANA)

def eliminarRepetidos(m):
    sr = []
    sr.append(m[0])
    for i in range(1, len(m)):
        v=0
        for a in sr:
            if m[i]== a:
                v=1
        if v==0:
            sr.append(m[i])
    return sr
def obtenerSaltos(nodo, saltos, caminos):
    caminos_ordenados = {}
    adelante=[]
    atras=[]
    for a in caminos:
        for i in range(len(a)):
            if a[i] == nodo:
                if len(a)-1-i >=saltos:
                    adelante.append(a[i+1:i+saltos+1])
                else:
                    adelante.append(a[i+1:i+len(a)-i])
                if i >=saltos:
                    atras.append(a[i-saltos:i])
                else:
                    atras.append(a[0:i])
    eadelante=[]
    if len (adelante)>0:
        eadelante =eliminarRepetidos(adelante)
    eatras=[]
    if len (adelante)>0:
        eatras=eliminarRepetidos(atras)

    for i in range(len(eadelante)):
        for j in range(len(eadelante)):
            if len(eadelante[i])<len(eadelante[j]):
                eadelante[i]=eadelante[j]
                eadelante[j]=eadelante

    for i in range(len(eatras)):
        for j in range(len(eatras)):
            if len(eatras[i])<len(eatras[j]):
                eatras2=eatras[i]
                eatras[i]=eatras[j]
                eatras[j]=eatras2

    for i in range(len(eatras)):
        eatras[i]=eatras[i][::-1]

    caminos_ordenados['arriba']  = eatras
    caminos_ordenados['abajo'] = eadelante
    return caminos_ordenados
caminos_ordenados = obtenerSaltos(tema_objetivo, saltos, caminos)
for nodo in RED_BAYESIANA.nodes():
    nombre_nodo = RED_BAYESIANA.variable(nodo).name()
    instancia_NODO = NODO(nombre_nodo, 1)
    instancia_NODO.ponderacion = 0
    instancia_NODO.sumatoria_ponderaciones = 0
    instancia_NODO.contador = 1
    instancia_NODO.grado_de_conocimiento = 0
    instancia_NODO.matriz_ponderacion = []  # MP
    instancia_NODO.matriz_inferencia = []  #
    instancia_NODO.matriz_inferencia_final = []  # i_prima
    instancia_NODO.clasificacion = 1
    if nombre_nodo == str(tema_objetivo):
        instancia_NODO.poderacion = ponderacion_objetiva
        instancia_NODO.clasificacion = 3
    else:
        instancia_NODO.poderacion = 0
    NODOS[nombre_nodo] = instancia_NODO

for camino in caminos_ordenados['abajo']:
    ponderacion = ponderacion_objetiva
    saltos = 1
    for nodo in camino:
        nodo_str = str(nodo)
        ponderacion = ponderacion * 0.5

        if saltos > 3:
            if NODOS[nodo_str].clasificacion != 4:
                NODOS[nodo_str].clasificacion = 5
                NODOS[nodo_str].ponderacion = 2
                NODOS[nodo_str].sumatoria_ponderaciones = 0
        else:
            if NODOS[nodo_str].clasificacion == 5:
                NODOS[nodo_str].sumatoria_ponderaciones = ponderacion
                NODOS[nodo_str].contador = 1
            else:
                NODOS[nodo_str].sumatoria_ponderaciones = NODOS[nodo_str].sumatoria_ponderaciones + ponderacion
                NODOS[nodo_str].contador = NODOS[nodo_str].contador + 1

            NODOS[nodo_str].ponderacion = NODOS[nodo_str].sumatoria_ponderaciones  / NODOS[nodo_str].contador
            NODOS[nodo_str].clasificacion = 4
        saltos = saltos + 1

for camino in caminos_ordenados['arriba']:
    ponderacion = ponderacion_objetiva
    for nodo in camino:
        nodo_str = str(nodo)
        ponderacion = ponderacion * 1.25
        if ponderacion > 100:
            ponderacion = 100

        NODOS[nodo_str].clasificacion = 4
        NODOS[nodo_str].sumatoria_ponderaciones = NODOS[nodo_str].sumatoria_ponderaciones + ponderacion
        NODOS[nodo_str].ponderacion = NODOS[nodo_str].sumatoria_ponderaciones  / NODOS[nodo_str].contador
        NODOS[nodo_str].contador = NODOS[nodo_str].contador + 1

gdcs = {}
for nodo in NODOS:
    matriz_ponderacion = [0,0,0]
    if NODOS[nodo].ponderacion >= 0 and NODOS[nodo].ponderacion <= 66:
        matriz_ponderacion[0] = 100
        NODOS[nodo].grado_de_conocimiento = 0
    elif NODOS[nodo].ponderacion  > 66 and NODOS[nodo].ponderacion <= 83:
        matriz_ponderacion[1] = 100
        NODOS[nodo].grado_de_conocimiento = 1
    else:
        matriz_ponderacion[2] = 100
        NODOS[nodo].grado_de_conocimiento = 2
    NODOS[nodo].matriz_ponderacion = matriz_ponderacion

i_prima = {}
ie.setEvidence({str(tema_objetivo): NODOS[str(tema_objetivo)].grado_de_conocimiento })
ie.makeInference()
for nodo in NODOS:
    i_ = []
    i_.append(ie.posterior(RED_BAYESIANA.variable(nodo).name())[0] * 100)
    i_.append(ie.posterior(RED_BAYESIANA.variable(nodo).name())[1] * 100)
    i_.append(ie.posterior(RED_BAYESIANA.variable(nodo).name())[2] * 100)
    NODOS[nodo].matriz_inferencia = i_

for nodo in NODOS:
    sumatoria_inferencias = 0
    NODOS[nodo].matriz_inferencia_final = []
    for i in range(len(NODOS[nodo].matriz_inferencia)):
        sumatoria_inferencias = NODOS[nodo].matriz_inferencia[i] + NODOS[nodo].matriz_ponderacion[i]
        sumatoria_inferencias = sumatoria_inferencias / 2
        NODOS[nodo].matriz_inferencia_final.append(sumatoria_inferencias)

    print(NODOS[nodo].matriz_inferencia_final)

#print(NODOS['73'])

#for propiedad in NODOS['73']:
#    print(propiedad)