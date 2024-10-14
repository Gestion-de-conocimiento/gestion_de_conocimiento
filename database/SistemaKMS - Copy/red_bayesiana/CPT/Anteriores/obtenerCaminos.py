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

for i in range(len(ramasynodos)-1,-1,-1):
  print(ramas[i])
  print()
  niveles=[0,0,0]
  cont=0
  for j in range(len(ramasynodos[i])): 
    cursor = cnx.cursor()
    #cursor.execute("select AVG(bueno),AVG(regular),AVG(bajo) from evidencia_expertos where id_tema ="+str(ramasynodos[i][j])+";")
    cursor.execute("select bueno,regular,bajo from evidencia_expertos where id_tema ="+str(ramasynodos[i][j])+";")
    cuenta=cursor.fetchall()
    nivelesi=[0,0,0]
    if len(cuenta) != 0:
      #print(cuenta)
      for k in range(len(cuenta)):
        nivelesi[0]+=cuenta[k][0]
        nivelesi[1]+=cuenta[k][1]
        nivelesi[2]+=cuenta[k][2]
      nivelesi[0]/=len(cuenta)
      nivelesi[1]/=len(cuenta)
      nivelesi[2]/=len(cuenta)  
      niveles[0]+=nivelesi[0]
      niveles[1]+=nivelesi[1]
      niveles[2]+=nivelesi[2]
      cont+=1
  niveles[0]=round(niveles[0]/cont)
  niveles[1]=round(niveles[1]/cont)
  niveles[2]=round(niveles[2]/cont)
  if niveles[0]+niveles[1]+niveles[2]<100:
     niveles[0]+=100-(niveles[0]+niveles[1]+niveles[2])
  if niveles[0]+niveles[1]+niveles[2]>100:
     niveles[0]-=(niveles[0]+niveles[1]+niveles[2])-100 
  cursor1=cnx.cursor()
  sql="insert into evidencia_expertos(id_tema,bajo,regular,bueno) values (%s,%s,%s,%s)"
  datos=(ramas[i] ,niveles[2], niveles[1], niveles[0])
  cursor1.execute(sql, datos)
  print("bueno ",niveles[0])
  print("regular ",niveles[1])
  print("bajo ",niveles[2])
  print("Suma ",niveles[0]+niveles[1]+niveles[2])
  pondramas[i]=niveles;

print(pondramas)
niveles=[0,0,0]  
for i in range(len(pondramas)):
  niveles[0]+=pondramas[i][0]
  niveles[1]+=pondramas[i][1]
  niveles[2]+=pondramas[i][2]
niveles[0]=round(niveles[0]/len(pondramas))
niveles[1]=round(niveles[1]/len(pondramas))
niveles[2]=round(niveles[2]/len(pondramas))
if niveles[0]+niveles[1]+niveles[2]<100:
     niveles[0]+=100-(niveles[0]+niveles[1]+niveles[2])
if niveles[0]+niveles[1]+niveles[2]>100:
     niveles[0]-=(niveles[0]+niveles[1]+niveles[2])-100 
print(niveles)
sql="insert into evidencia_expertos(id_tema,bajo,regular,bueno) values (%s,%s,%s,%s)"
datos=(1 ,niveles[2], niveles[1], niveles[0])
cursor1.execute(sql, datos)
cnx.commit()
cnx.close()
