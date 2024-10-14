import requests
import numpy as np
import random
import mysql.connector


def preguntasAbiertas(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("script xyz",1,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("xyz",(id[0][0]),1)
  cursor1.execute(sql, datos)

  
def preguntasNumericas(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("script xyz",2,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=(5/10,id[0][0],1)
  cursor1.execute(sql, datos)
  sql="insert into margen_errors(id_pregunta,aplicableArriba,aplicableAnbajo,rango) values (%s,%s,%s,%s)"
  datos=(id[0][0],1,1,0)
  cursor1.execute(sql, datos)

def preguntasVF(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("script xyz",3,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("verdadero",id[0][0],1)
  cursor1.execute(sql, datos)
  
def preguntasOMultiple(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("script xyz",4,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("xyz",(id[0][0]),1)
  cursor1.execute(sql, datos)
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("abc",(id[0][0]),0)
  cursor1.execute(sql, datos)
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("def",(id[0][0]),0)
  cursor1.execute(sql, datos)

def preguntasCalculadasS(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("script xyz {a} + {b}  ",5,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=(" {a} + {b} ",id[0][0],1)
  cursor1.execute(sql, datos)
  
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from opciones;")
  idopcion=cursor.fetchall()
  cursor1=conexion1.cursor()
  
  cursor1=conexion1.cursor()
  sql="insert into comodines(comodin,valor_comodin,id_opcion) values (%s,%s,%s)"
  datos=("{a}",'-1~100',idopcion[0][0])
  cursor1.execute(sql, datos)
  
  cursor1=conexion1.cursor()
  sql="insert into comodines(comodin,valor_comodin,id_opcion) values (%s,%s,%s)"
  datos=("{b}",'-1~100',idopcion[0][0])
  cursor1.execute(sql, datos)
  
  
  sql="insert into configuracion_preguntas_calculadas(id_pregunta,decimales) values (%s,%s)"
  datos=(id[0][0],0)
  cursor1.execute(sql, datos)
  
  sql="insert into margen_errors(id_pregunta,aplicableArriba,aplicableAnbajo,rango) values (%s,%s,%s,%s)"
  datos=(id[0][0],0,0,0)
  cursor1.execute(sql, datos)
"""
def preguntasCalculadasM(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("xyz {a}",6,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
 
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("{a}",id[0][0],1)
  cursor1.execute(sql, datos)
      
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from opciones;")
  idopcion=cursor.fetchall()
  cursor1=conexion1.cursor()
  
  cursor1=conexion1.cursor()
  sql="insert into comodines(comodin,valor_comodin,id_opcion) values (%s,%s,%s)"
  datos=("{a}",1,idopcion[0][0])
  cursor1.execute(sql, datos)
  
  sql="insert into configuracion_preguntas_calculadas(id_pregunta,decimales) values (%s,%s)"
  datos=(id[0][0],0)
  cursor1.execute(sql, datos)
  
   
  
  #2
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("{b}",id[0][0],0)
  cursor1.execute(sql, datos)
      
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from opciones;")
  idopcion=cursor.fetchall()
  cursor1=conexion1.cursor()
  
  cursor1=conexion1.cursor()
  sql="insert into comodines(comodin,valor_comodin,id_opcion) values (%s,%s,%s)"
  datos=("{b}",2,idopcion[0][0])
  cursor1.execute(sql, datos)
  
  sql="insert into configuracion_preguntas_calculadas(id_pregunta,decimales) values (%s,%s)"
  datos=(id[0][0],0)
  cursor1.execute(sql, datos)
  
  #3
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=("{c}",id[0][0],0)
  cursor1.execute(sql, datos)
      
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from opciones;")
  idopcion=cursor.fetchall()
  cursor1=conexion1.cursor()
  
  cursor1=conexion1.cursor()
  sql="insert into comodines(comodin,valor_comodin,id_opcion) values (%s,%s,%s)"
  datos=("{c}",3,idopcion[0][0])
  cursor1.execute(sql, datos)
  
  sql="insert into configuracion_preguntas_calculadas(id_pregunta,decimales) values (%s,%s)"
  datos=(id[0][0],0)
  cursor1.execute(sql, datos)
  
  sql="insert into margen_errors(id_pregunta,aplicableArriba,aplicableAnbajo,rango) values (%s,%s,%s,%s)"
  datos=(id[0][0],1,1,0)
  cursor1.execute(sql, datos)
  """
def preguntasExpresiones(conexion1,padres_ids):
  cursor1=conexion1.cursor()
  sql="insert into banco_preguntas(pregunta,tipo,id_tema) values (%s,%s,%s)"
  datos=("\\frac{1}{2}+3",7,padres_ids[0])
  cursor1.execute(sql, datos)
  cursor = conexion1.cursor()
  cursor.execute("select max(id) from banco_preguntas;")
  id=cursor.fetchall()
  cursor1=conexion1.cursor()
  sql="insert into opciones(opcion,id_pregunta,esrespuesta) values (%s,%s,%s)"
  datos=('7/2',id[0][0],1)
  cursor1.execute(sql, datos)
  sql="insert into margen_errors(id_pregunta,aplicableArriba,aplicableAnbajo,rango) values (%s,%s,%s,%s)"
  datos=(id[0][0],1,1,0)
  cursor1.execute(sql, datos)

  
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

conexion1=mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')   
for i in range(len(padres)):
 

  #preguntasNumericas(conexion1,padres_ids[i])
  preguntasAbiertas(conexion1,padres_ids[i])
  preguntasVF(conexion1,padres_ids[i])
   #preguntasOMultiple(conexion1,padres_ids[i])
  #preguntasCalculadasS(conexion1,padres_ids[i])
   #preguntasCalculadasM(conexion1,padres_ids[i])
  #preguntasExpresiones(conexion1,padres_ids[i])
conexion1.commit()
conexion1.close() 

print(len(padres))


