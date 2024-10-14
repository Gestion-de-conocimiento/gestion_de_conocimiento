import requests
import numpy as np
import mysql.connector
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')
URL = "http://159.203.185.170/arbol/caminoslibreria"
expertos = [84,85,113,121]
temas = [39,11,33,29,2]
cursor = cnx.cursor()

for i in range(len(temas)):
  for j in range(len(expertos)):
    print("Tema ",temas[i]," Experto ",expertos[j],"\n")
    cursor.execute("select bajo,regular,bueno from evidencia_expertos where id_tema = " + str(temas[i]) + " and id_usuario=" + str(expertos[j]) + ";")
    E=cursor.fetchall()
    print(E,"\n")