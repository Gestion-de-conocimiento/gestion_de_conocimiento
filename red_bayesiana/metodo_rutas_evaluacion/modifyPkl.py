import pickle
import sys
import json
import mysql.connector

"""  
Archivo con funciones predefinidas para modificar un .pkl
"""
# Matricula del alumno obtenida como argumento
matriculaAlumno = sys.argv[1]

id_tema = sys.argv[2]

ponderacion = int(sys.argv[3])

gradoCono = int(sys.argv[4])

# Ruta al archivo pickle RBMA
file_path = f"red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_{matriculaAlumno}.pkl"





"""
Clase NODO extraída de red_bayesiana/metodo_rutas_evaluacion/NODO.py
"""
class NODO:
    def __init__(self, id, clasificacion):
        self.id = id
        self.clasificacion = clasificacion
        self.ponderacion = 0
        self.sumatoria_ponderaciones = 0
        self.contador = 1
        self.grado_de_conocimiento = -1
        self.matriz_ponderacion = [0,0,0]  
        self.matriz_inferencia = [0,0,0]  
        self.matriz_inferencia_final = [0,0,0]  
        self.dificultad = 0
        self.discriminacion = 0
        self.adivinacion = 0
        self.asintota = 0
        self.orden_evaluacion = -1


""" 
Función para cargar datos del pkl

@param file_path dirección del archivo pkl
"""
def escribirDatos():
      id = id_tema
      nuevos_datos = {}
      campo = "grado_de_conocimiento" 
      valor = gradoCono + 0
      nuevos_datos[campo] = valor
      actualizar_objeto(rbma, id, nuevos_datos)
      campo = "sumatoria_ponderaciones" 
      valor = ponderacion + 0
      nuevos_datos[campo] = valor
      actualizar_objeto(rbma, id, nuevos_datos)
            
            
def cargar_datos(file_path):
    with open(file_path, 'rb') as file: # Se abre como 'rb' de 'read binary'
        return pickle.load(file)

"""
Función para guardar los datos en el .pkl

@param file_path dirección del archivo pkl
"""
def guardar_datos(file_path, data):
    with open(file_path, 'wb') as file: # Se abre como 'wb' de 'write binary'
        pickle.dump(data, file) 

"""  
Función para crear

@param rbma Matriz de datos cargados
@param nuevo_objeto Nuevo objeto a guardar
"""
def crear_objeto(rbma, nuevo_objeto):
    rbma[1][nuevo_objeto.id] = nuevo_objeto
    guardar_datos(file_path, rbma)
    print(f"Objeto {nuevo_objeto.id} creado exitosamente.")

""" 
Función para leer todos los datos del .pkl

@param rbma Matriz con datos cargados
"""
def leer_todos(rbma):
    for i in rbma[1]:
        obj = rbma[1][i]
        print(obj.id, obj.clasificacion, obj.ponderacion, obj.sumatoria_ponderaciones, obj.contador, obj.grado_de_conocimiento, obj.matriz_ponderacion, obj.matriz_inferencia, obj.matriz_inferencia_final, float(obj.dificultad), float(obj.discriminacion), float(obj.adivinacion), obj.asintota, obj.orden_evaluacion)

"""  
Función para buscar un registro por id

@param rbma Matriz con los datos cargados
@param id ID de objeto a leer
"""
def leer_por_id(rbma, id):
    if id in rbma[1]:
        obj = rbma[1][id]
        print(obj.id, obj.clasificacion, obj.ponderacion, obj.sumatoria_ponderaciones, obj.contador, obj.grado_de_conocimiento, obj.matriz_ponderacion, obj.matriz_inferencia, obj.matriz_inferencia_final, float(obj.dificultad), float(obj.discriminacion), float(obj.adivinacion), obj.asintota, obj.orden_evaluacion)
    else:
        print(f"Objeto con ID {id} no encontrado.")


"""  
Función para actualizar un objeto en base a un id

@param rbma Matriz con los datos guardados
@param id ID del objeto a actualizar
@param nuevos_datos 
"""
def actualizar_objeto(rbma, id, nuevos_datos):
    if id in rbma[1]:
        obj = rbma[1][id]
        for key, value in nuevos_datos.items():
            setattr(obj, key, value)
        guardar_datos(file_path, rbma)
        print(f"Objeto {id} actualizado exitosamente.")
    else:
        print(f"Objeto con ID {id} no encontrado.")

"""  
Función para eliminar un registro del .pkl

@param rbma Matriz con los datos guardados
@param id ID del objeto a elimianr
"""
def eliminar_objeto(rbma, id):
    if id in rbma[1]:
        del rbma[1][id] # Borramos el objeto en la posición rbma[1][id]
        guardar_datos(file_path, rbma)
        print(f"Objeto {id} eliminado exitosamente.")
    else:
        print(f"Objeto con ID {id} no encontrado.")

"""  
Función para imprimir el menú de opciones
"""
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Crear un nuevo objeto")
    print("2. Leer todos los objetos")
    print("3. Leer un objeto por ID")
    print("4. Actualizar un objeto")
    print("5. Eliminar un objeto")
    print("6. Salir")

"""  
Función para pedirle al usuario los nuevos datos del nodo
"""
def obtener_datos_nodo():
    id = input("Ingrese el id del nodo: ")
    clasificacion = input("Ingrese la clasificación del nodo: ")
    return NODO(id, clasificacion)

"""  
Método main

if ponderacion < 66: 
  gradoCono = 0;
elif ponderacion < 83:
gradoCono = 1  
elif ponderacion >= 83:
  gradoCono = 2
else
  gradoCono = -2
""""""

            ida = id_tema
            nuevos_datos = {}
            while True:
                #campo = input("Ingrese el campo a actualizar (o 'salir' para terminar): ")
                campo = "grado_de_conocimiento" 
                if campo == "salir":
                    break
                #valor = input(f"Ingrese el nuevo valor para {campo}: ")
                
                valor = gradoCono
                nuevos_datos[campo] = valor
            actualizar_objeto(rbma, id, nuevos_datos)
"""
if __name__ == "__main__":
    # Cargar datos
    rbma = cargar_datos(file_path)
    escribirDatos()