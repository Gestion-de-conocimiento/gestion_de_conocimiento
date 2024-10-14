#################
#
#
#
#
#
#################

import pickle
import csv
import os


def exportarCsv(matricula, tipo):
  
  if tipo == 1:
    nombre_rbma_pickle = "rbma/rbma_"+matricula+".pkl" #pickle
  else:
    nombre_rbma_pickle = "rbma/" + matricula
  
  infile = open(nombre_rbma_pickle,'rb')
  RBMA = pickle.load(infile)
  infile.close()

  header = ['tema', 'clasificacion', 'ponderacion', 'sumatoria_ponderaciones', 'contador', 'grado_de_conocimiento', 'matriz_ponderacion', 'matriz_inferencia', 'matriz_inferencia_final', 'dificultad', 'discriminacion', 'adivinacion', 'asintota', 'orden_evaluacion']

  temas = []

  for i in RBMA[1]:
    tema = [ RBMA[1][i].id, RBMA[1][i].clasificacion, RBMA[1][i].ponderacion, RBMA[1][i].sumatoria_ponderaciones, RBMA[1][i].contador, RBMA[1][i].grado_de_conocimiento, RBMA[1][i].matriz_ponderacion, RBMA[1][i].matriz_inferencia, RBMA[1][i].matriz_inferencia_final, float(RBMA[1][i].dificultad), float(RBMA[1][i].discriminacion), float(RBMA[1][i].adivinacion), RBMA[1][i].asintota, RBMA[1][i].orden_evaluacion ]
    temas.append(tema)
    
  
  
  if tipo == 1:
    nombreArchivoCsv = "csv/rbma_"+matricula+".csv"
    
  else:
    nombreArchivoCsv = "csv/"+matricula[:len(matricula) - 4] +".csv"
  
  with open(nombreArchivoCsv, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # Escriba la cabecera
    writer.writerow(header)
    # Escribe las multiples filas
    writer.writerows(temas)

def obtenerListaArchivos(carpeta):
  
  archivos = []
  for file in os.listdir("rbma"):
    if file.endswith(".pkl"):
        archivos.append(file)
        
  return archivos
        
        
  ''' archivos = []
  dir_path = carpeta

  # Iterate directory
  for path in os.listdir(dir_path):
      # check if current path is a file
      if os.path.isfile(os.path.join(dir_path, path)):
          archivos.append(path)
  return archivos '''
    
def listarArchivos(carpeta):
  dir_path = carpeta

  # Iterate directory
  for path in os.listdir(dir_path):
      # check if current path is a file
      if os.path.isfile(os.path.join(dir_path, path)):
          #res.append(path)
          print(path)

          

          
print("Elige una opcion")
print("1) N cantidad de archivos")
print("2) Masivamente")
print("3) Por generación")
print("4) Mostrar archivos disponibles")
print("5) Mostrar archivos procesados")
opcionMenu = input(" > ")
print("Opcion elegida " + str(opcionMenu) )

if(opcionMenu == "1"):
  numeroArchivos = int(input(" Especifique la cantidad de archivos: "))
  archivo = ""
  for x in range(numeroArchivos):
    matricula = input(" Matricula del archivo " + str(x+1) + " de " + str(numeroArchivos) + ":")
    print("Porcesando Archivo con matricula ... " + matricula)
    exportarCsv(matricula, 1)

elif (opcionMenu == "2"):
  print("Procesando todos los archivos ...")
  #print( obtenerListaArchivos('rbma') )
  archivos = obtenerListaArchivos('rbma')
  
  for archivo in archivos:
    exportarCsv( archivo , 2)
  
elif (opcionMenu == "3"):
  print("Ingrese la generación que desea procesar 15, 16, 17 ")
elif (opcionMenu == "4"):
  print("============Archivos para procesar==============")
  listarArchivos('rbma')
  print("==========================")
else:
  print("============Archivos procesados==============")
  listarArchivos('csv')
  print("==========================")
  

