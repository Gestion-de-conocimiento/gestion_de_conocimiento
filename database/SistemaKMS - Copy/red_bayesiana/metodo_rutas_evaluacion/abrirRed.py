import sys
import pickle
import mysql.connector

matricula = sys.argv[1]
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')
#nombre_rbma_pickle = "red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_1530004.pkl"  #pickle
nombre_rbma_pickle = "red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_" + matricula + ".pkl"
#nombre_rbma_pickle = "rbma/rbma_1530004.pkl" #pickle
infile = open(nombre_rbma_pickle,'rb')
RBMA = pickle.load(infile)
infile.close()
cursor = cnx.cursor()
for i in RBMA[1]: 
  cursor.execute("select nombre_tema from temas where id ="+str(RBMA[1][i].id)+";")
  nombre=cursor.fetchall()
  if RBMA[1][i].grado_de_conocimiento!=-1:
    print(str(RBMA[1][i].id)+"/"+str(RBMA[1][i].grado_de_conocimiento),",")
    #print(str(nombre[0][0])+","+str(RBMA[1][i].grado_de_conocimiento+1))
  else:
      if  RBMA[1][i].matriz_inferencia_final[0]==0 and RBMA[1][i].matriz_inferencia_final[1]==0 and RBMA[1][i].matriz_inferencia_final[2]==0:
        print(str(RBMA[1][i].id)+"/"+str(RBMA[1][i].matriz_inferencia.index(max(RBMA[1][i].matriz_inferencia))),",")
        #print(str(nombre[0][0])+","+str(RBMA[1][i].matriz_inferencia.index(max(RBMA[1][i].matriz_inferencia))+1))
      else:
        print(str(RBMA[1][i].id)+"/"+str(RBMA[1][i].matriz_inferencia_final.index(max(RBMA[1][i].matriz_inferencia_final))+1),",")
        #print(str(nombre[0][0])+","+str(RBMA[1][i].matriz_inferencia_final.index(max(RBMA[1][i].matriz_inferencia_final))))