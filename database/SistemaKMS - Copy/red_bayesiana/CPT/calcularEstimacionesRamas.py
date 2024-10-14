import requests
import numpy as np
import mysql.connector
cnx = mysql.connector.connect(user='root', password='PROYECTO1KMS', host='localhost', database='kms')
URL = "http://159.203.185.170/arbol/caminoslibreria"
r = requests.get(url = URL)
data = r.json()
caminos = data['caminos']
ramas = []
for i in range(len(caminos)):
	ramas.append(caminos[i][1])
ramas=list(set(ramas))
ramasynodos=[]
for i in range(len(ramas)):
	prov=[]
	for j in range(len(caminos)):
		if caminos[j][1]==ramas[i]:
			for k in range(2,len(caminos[j])):
			 prov.append(caminos[j][k])
	ramasynodos.append(prov)		 
for i in range(len(ramasynodos)):
	ramasynodos[i]=list(set(ramasynodos[i]))
prov=[]
pondramas= [[],[],[],[],[],[],[],[]]
for i in range(len(ramasynodos)):
	for j in range(len(ramasynodos)):
		if len(ramasynodos[i]) > len(ramasynodos[j]):
			prov= ramasynodos[i]
			ramasynodos[i]= ramasynodos[j]
			ramasynodos[j]= prov
			prov= ramas[i]
			ramas[i]= ramas[j]
			ramas[j]= prov
for i in range(len(ramas)):
  cursor = cnx.cursor()
  cursor.execute("delete from evidencia_expertos where id_tema ="+str(ramas[i])+";")
cursor = cnx.cursor()
cursor.execute("select id from temas where nivel=0;")
AD=cursor.fetchall()[0][0]
cursor = cnx.cursor()
cursor.execute("delete from evidencia_expertos where id_tema ="+str(AD)+";")
cnx.commit() 
cursor = cnx.cursor()
cursor.execute("select count(id) from temas")
ctemas=cursor.fetchall()[0][0]
cursor = cnx.cursor()
cursor.execute("select id from users where id_rol=2 and eliminado =0")
expertos=cursor.fetchall()
expertosBuenos=[]
cexpertos=0;
for i in range(len(expertos)):
  cursor = cnx.cursor()
  cursor.execute("select count(id) from evidencia_expertos where id_usuario ="+str(expertos[i][0])+";")
  cuenta=cursor.fetchall()
  if cuenta[0][0]==ctemas-len(ramas)-1:
    expertosBuenos.append(expertos[i][0])
    cexpertos+=1
ADExpertos=[]
for i in range(len(expertosBuenos)):
  ADExpertos.append([0,0,0])
for i in range(len(ramasynodos)-1,-1,-1):
  niveles=[0,0,0]
  cont=0
  for j in range(len(expertosBuenos)):
    niveles=[0,0,0]
    for k in range(len(ramasynodos[i])):
      cursor = cnx.cursor()
      cursor.execute("select bueno,regular,bajo from evidencia_expertos where id_tema ="+str(ramasynodos[i][k])+" and id_usuario="+str(expertosBuenos[j])+" ;")
      cuenta=cursor.fetchall()
      niveles[0]+=cuenta[0][0]
      niveles[1]+=cuenta[0][1]
      niveles[2]+=cuenta[0][2]
    niveles[0]=round(niveles[0]/len(ramasynodos[i]))
    niveles[1]=round(niveles[1]/len(ramasynodos[i]))
    niveles[2]=round(niveles[2]/len(ramasynodos[i]))
    if niveles[0]+niveles[1]+niveles[2]<100:
      niveles[0]+=100-(niveles[0]+niveles[1]+niveles[2])
    if niveles[0]+niveles[1]+niveles[2]>100:
      niveles[0]-=(niveles[0]+niveles[1]+niveles[2])-100 
    cursor1=cnx.cursor()
    sql="insert into evidencia_expertos(id_usuario,id_tema,bajo,regular,bueno) values (%s,%s,%s,%s,%s)"
    datos=(expertosBuenos[j],ramas[i] ,niveles[2], niveles[1], niveles[0])
    cursor1.execute(sql, datos)
    ADExpertos[j][0]+=niveles[0]
    ADExpertos[j][1]+=niveles[1]
    ADExpertos[j][2]+=niveles[2]
for i in range (len(ADExpertos)):
  for j in range(3):
    ADExpertos[i][j]=round(ADExpertos[i][j]/len(ramas))
  if ADExpertos[i][0]+ADExpertos[i][1]+ADExpertos[i][2]<100:
      ADExpertos[i][0]+=100-(ADExpertos[i][0]+ADExpertos[i][1]+ADExpertos[i][2])
  if ADExpertos[i][0]+ADExpertos[i][1]+ADExpertos[i][2]>100:
      ADExpertos[i][0]-=(ADExpertos[i][0]+ADExpertos[i][1]+ADExpertos[i][2])-100 
for i in range (len(expertosBuenos)):
  sql="insert into evidencia_expertos(id_usuario,id_tema,bajo,regular,bueno) values (%s,%s,%s,%s,%s)"
  datos=(expertosBuenos[i],AD , ADExpertos[i][2],  ADExpertos[i][1],  ADExpertos[i][0])
  cursor1.execute(sql, datos)
cnx.commit() 
cnx.close()