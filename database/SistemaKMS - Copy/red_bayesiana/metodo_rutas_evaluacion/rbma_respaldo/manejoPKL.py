import pickle
from NODO import NODO


nombre_rbma_pickle = "rbma_1530004.pkl" #pickle
infile = open(nombre_rbma_pickle,'rb')
student_pkl = pickle.load(infile)
infile.close()

print(student_pkl)

for i in student_pkl[1]:
  print(student_pkl[1][i].id)
  print(student_pkl[1][i].grado_de_conocimiento)
  print(student_pkl[1][i].matriz_inferencia_final)

