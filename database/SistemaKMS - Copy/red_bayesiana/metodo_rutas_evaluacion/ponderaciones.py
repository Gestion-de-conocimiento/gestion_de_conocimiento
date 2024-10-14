# Muestra una lista de temas evaluados y su ponedarción 
# Por cada uno de los alumnos
# Tomando como entrada la matricula
import pickle
import os.path
import sys
from os import path
import json

# Matricula del alumno
matriculaAlumno = sys.argv[1]

#RBMA
rutaRbma = "red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_"+str(matriculaAlumno)+".pkl"
#rutaRbma = "rbma/rbma_"+str(matriculaAlumno)+".pkl"
RBMA = {}

# Compara si la RBMA del alumno existe
if path.exists(rutaRbma):
    with open(rutaRbma, 'rb') as inp:
        RBMA = pickle.load(inp)
    alumno = RBMA[0]
    RBMA   = RBMA[1]
else:
    print("-1")
    exit()

temasEvaluados = []
temasEvaluadosIds = []
respuestas = []
ponderaciones = []
for nodo in RBMA:
    if RBMA[nodo].orden_evaluacion != -1:
        temasEvaluados.append(0)
        temasEvaluadosIds.append(0)
        respuestas.append(0)
        ponderaciones.append(0)

# Realiza un ordeamiento del historico de evaluación
i=0
for nodo in RBMA:
    if RBMA[nodo].orden_evaluacion != -1:
        temasEvaluadosIds[RBMA[nodo].orden_evaluacion] = RBMA[nodo].id
        temasEvaluados[RBMA[nodo].orden_evaluacion] = i

        if RBMA[nodo].ponderacion >= 70:
            respuestas[RBMA[nodo].orden_evaluacion] = True
        else:
            respuestas[RBMA[nodo].orden_evaluacion] = False
        
        ponderaciones[RBMA[nodo].orden_evaluacion] = RBMA[nodo].ponderacion;
        

    i=i+1

temas = []
for i in range(len(temasEvaluadosIds)):
  tema_obj = {
    "id": temasEvaluadosIds[i],
    "respuesta": respuestas[i],
    "ponderacion": ponderaciones[i]
  }
  temas.append(tema_obj)
  
temas_con_ultimo = {
  "temas_evaluados": temas,
  "ultimo": alumno["ultimo"],
  "habilidad": alumno["theta"],
  "detenerse": alumno["detenerse"],
  "habilidad_anterior": alumno['theta_anterior']
}
print(json.dumps(temas_con_ultimo))



        