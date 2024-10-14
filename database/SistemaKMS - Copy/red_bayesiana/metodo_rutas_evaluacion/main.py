#########################################################
# Universidad Politécnica de Victoria                   #
# 16/06/2022                                            #
# Programa para la obtención de una ruta de evaluación  #
# Froylán M. Wbario Martínez                            #
#########################################################
import requests
import matplotlib.pyplot as plt
import catsim.plot as catplot
import pyAgrum as gum
import pickle
import os.path
import random
import sys
import aiohttp
import asyncio
import json
from os import path
from catsim.simulation import *
from catsim.initialization import *
from catsim.selection import *
from catsim.estimation import *
from catsim.stopping import *
from catsim.irt import icc
from NODO import NODO
from RED_BAYESIANA import RED_BAYESIANA
from MPCN import MPCN
from PRIMER_TEMA import PRIMER_TEMA

caminos = open('caminos.json')
data = json.load(caminos)
caminos.close()
caminos = data['caminos']
RBMA = {}

# Obtención de parametros de la terminal
versionRbm = sys.argv[1]       # Version de la rbm
matriculaAlumno = sys.argv[2]  # Matricula del alumno    

# Especificación de rutas de almacenamiento
rutaRbma = "red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_"+str(matriculaAlumno)+".pkl"  #RBMA
rutaRbm = "red_bayesiana/metodo_rutas_evaluacion/rbm/rbm_"+str(versionRbm)+".bifxml"       #RBM

#rutaRbma = "rbma/rbma_"+str(matriculaAlumno)+".pkl"  #RBMA
#rutaRbm = "rbm/rbm_"+str(versionRbm)+".bifxml"       #RBM

# Instancia de la clase que gestiona la Red Bayesiana
CONTRUCTOR_BN = RED_BAYESIANA(rutaRbm)

# Carga de la RBM
RBM = CONTRUCTOR_BN.obtenerRedCompleta()

# Primer escenario, cuando el programa es llamado con tres parametros (dos especificados por el usuario)
#  1er - Nombre del archivo
#  2do - Matricula del alumno
#  3ero - Versión de la Red Bayesiana Maestra
if len(sys.argv) == 3:
    # Obtención del primer tema a evaluar
    primerTema = PRIMER_TEMA(data).calcularPrimerTema()
    
    # Inicialización de la RBMA del alumno
    for nodo in RBM.nodes():
        nodoRbm = NODO(RBM.variable(nodo).name(), 1)
        for tema in data['temas']:
            if RBM.variable(nodo).name() == str(tema['id']):
                nodoRbm.dificultad = tema['dificultad']
        RBMA[RBM.variable(nodo).name()] = nodoRbm
    
    # Inicialización de theta en un valor aleatorio (De esta manera se evita un mismo comienzo en el cuestionario por todos los alumnos)
    initializer = RandomInitializer()
    est_theta = initializer.initialize()
    
    # Datos del archivo de configuración
    redAlumno = [{'ultimo': primerTema,'matricula':matriculaAlumno,'theta': est_theta,'versionrbm':versionRbm, 
                  'theta_anterior': 0, 'detenerse': False },RBMA]
    
    # Almacenamiento de la RBMA de manera persistente
    with open(rutaRbma, 'wb') as outp:
        pickle.dump(redAlumno, outp, pickle.HIGHEST_PROTOCOL)
        
    primerTema = {
      "tema": primerTema
    }
    print( json.dumps(primerTema) )
    
# <Matricula> <Saltos> <Tema objetivo> <Ponderación>
elif len(sys.argv) == 6:
    # Parametros de entada por medio de la terminal 
    saltos = sys.argv[3]                    # Número de saltos que compone los subgrafos
    temaObjetivo = sys.argv[4]              # Tema objetivo, nodo central del subgrafo
    ponderacionObjetiva = int(sys.argv[5])  # Ponderación objetiva que obtuvo en el último tema evaluado
    
    alumno = {}
    RBMA = {}
    
    # Compara si la RBMA del alumno existe
    if path.exists(rutaRbma):
        with open(rutaRbma, 'rb') as inp:
            RBMA = pickle.load(inp)
        alumno = RBMA[0]
        RBMA   = RBMA[1]
        rutaRbm = "red_bayesiana/metodo_rutas_evaluacion/rbm/rbm_" + alumno['versionrbm'] + ".bifxml"
        #rutaRbm = "rbm/rbm_" + alumno['versionrbm'] + ".bifxml"
    else:
        print("Error al abrir la rbma")
        exit()
    
    # Especificación de parametros para la definición de las sub-redes
    CONTRUCTOR_BN.configurarParametros([temaObjetivo,ponderacionObjetiva,saltos,caminos])
    SRB = CONTRUCTOR_BN.obtenerSubRed()
    CAMINOS_SRB = CONTRUCTOR_BN.obtenerCaminosSubRed()
    
    # Pasa 
    INSTANCIA_MPCN = MPCN(RBMA, SRB, CAMINOS_SRB, temaObjetivo, ponderacionObjetiva, rutaRbm)
    INSTANCIA_MPCN.hacerInferencias()
    
    # Se obtiene la RBMA actualizada con las inferenicas promediadas de la SRB  
    RBMA = INSTANCIA_MPCN.obtenerRBMA()
    
    # Calcula y normaliza las caracteristicas de Pseudoadivinacion, Discriminzacion y Dificultad
    items = INSTANCIA_MPCN.obtenerItems()
    
    temasEvaluados = []
    temasEvaluadosIds = []
    respuestas = []
    for nodo in RBMA:
        if RBMA[nodo].orden_evaluacion != -1:
            temasEvaluados.append(0)
            temasEvaluadosIds.append(0)
            respuestas.append(0)

    # Realiza un ordeamiento del historico de evaluación
    i=0
    for nodo in RBMA:
        if RBMA[nodo].orden_evaluacion != -1:
            temasEvaluadosIds[RBMA[nodo].orden_evaluacion] =  RBMA[nodo].id
            temasEvaluados[RBMA[nodo].orden_evaluacion] = i
            
            if RBMA[nodo].ponderacion >= 70:
                respuestas[RBMA[nodo].orden_evaluacion] = True
            else:
                respuestas[RBMA[nodo].orden_evaluacion] = False
            
        i=i+1
        
    
    # Elementos del CAT
    #   RandomInitializer: Inincializa la habilidad del alumno
    initializer = RandomInitializer()
    selector = MaxInfoSelector()
    estimator = NumericalSearchEstimator()
    
    # Error estandar - entre menos valor, más precisión en la estimación
    stopper = MinErrorStopper(0.7)
    
    nuevaHabilidad = estimator.estimate(items=items, administered_items=temasEvaluados, response_vector=respuestas, est_theta= alumno['theta'])
    detenerse = stopper.stop(administered_items=items[temasEvaluados], theta=nuevaHabilidad)
    siguienteItem = selector.select(items=items, administered_items=temasEvaluados, est_theta=nuevaHabilidad)
    
    ''' evaluacion = {
      "tema": RBMA[ list(RBMA)[siguienteItem] ].id,
      "detenerse": detenerse,
      "habilidad_anterior": alumno["theta"],
      "habilidad_siguiente": nuevaHabilidad
    }
    
    print(json.dumps(evaluacion)) '''
    
    print( json.dumps({"mensaje": "Tema evaluado correctamente"}) )
    
    alumno['theta_anterior'] = alumno['theta']
    alumno['theta'] = nuevaHabilidad
    alumno['ultimo'] = RBMA[ list(RBMA)[siguienteItem] ].id
    alumno['detenerse'] = detenerse
    
    redAlumno = [alumno,RBMA]
    
    # Almacena el estatus de evaluación
    with open(rutaRbma, 'wb') as outp:
        pickle.dump(redAlumno, outp, pickle.HIGHEST_PROTOCOL)
    
else:
    print("-1")
