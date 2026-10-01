import pickle
import csv
import random  # Importa el módulo random

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
        self.matriz_ponderacion = [0, 0, 0]  
        self.matriz_inferencia = [0, 0, 0]  
        self.matriz_inferencia_final = [0, 0, 0]  
        self.dificultad = 0
        self.discriminacion = 0
        self.adivinacion = 0
        self.asintota = 0
        self.orden_evaluacion = -1

# Ruta de archivo
#file_path = r'rbma/rbma_2330257.pkl'
#csv_file_path = r'rbma/rbma_2330257.csv'
file_path = r'rbma/rbma_2430032.pkl'
csv_file_path = r'rbma/rbma_2430032.csv'
# Lista de IDs a los que quieres cambiar el grado_de_conocimiento
ids_a_actualizar = [
  
]

def cargar_datos(file_path):
    try:
        with open(file_path, 'rb') as file:
            rbma = pickle.load(file)
            print("Datos cargados exitosamente.")
            return rbma
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return None
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def guardar_datos(file_path, data):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
            print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función para convertir el archivo .pkl a .csv con manejo de errores
def convertir_a_csv(rbma, csv_file_path):
    try:
        # Verificar que rbma es una lista o tupla con al menos dos elementos
        if not isinstance(rbma, (list, tuple)) or len(rbma) < 2:
            raise ValueError("La estructura de rbma no es la esperada. Debe ser una lista o tupla con al menos dos elementos.")
        
        # Verificar que rbma[1] es un diccionario
        if not isinstance(rbma[1], dict):
            raise ValueError("rbma[1] debe ser un diccionario que contiene los nodos.")
        
        # Verificar que hay al menos un nodo en rbma[1]
        if not rbma[1]:
            raise ValueError("rbma[1] está vacío. No hay nodos para exportar.")
        
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribe la cabecera (columnas)
            writer.writerow(['ID', 'Clasificación', 'Ponderación', 'Sumatoria Ponderaciones', 'Contador', 
                             'Grado de Conocimiento', 'Matriz Ponderación', 'Matriz Inferencia', 
                             'Matriz Inferencia Final', 'Dificultad', 'Discriminación', 'Adivinación', 
                             'Asintota', 'Orden Evaluación'])
            
            # Escribe los datos de cada objeto
            for i in rbma[1]:
                obj = rbma[1][i]
                writer.writerow([
                    obj.id, 
                    obj.clasificacion, 
                    obj.ponderacion, 
                    obj.sumatoria_ponderaciones, 
                    obj.contador, 
                    obj.grado_de_conocimiento, 
                    ','.join(map(str, obj.matriz_ponderacion)),  # Convertir listas a cadenas
                    ','.join(map(str, obj.matriz_inferencia)),
                    ','.join(map(str, obj.matriz_inferencia_final)),
                    obj.dificultad, 
                    obj.discriminacion, 
                    obj.adivinacion, 
                    obj.asintota, 
                    obj.orden_evaluacion
                ])
        
        print(f"Archivo CSV creado exitosamente en {csv_file_path}")
    
    except Exception as e:
        print(f"Error al crear el archivo CSV: {e}")

# Función para crear un nuevo objeto
def crear_objeto(rbma, nuevo_objeto):
    try:
        rbma[1][nuevo_objeto.id] = nuevo_objeto
        guardar_datos(file_path, rbma)
        print(f"Objeto {nuevo_objeto.id} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el objeto: {e}")

# Función para leer todos los datos del .pkl
def leer_todos(rbma):
    try:
        for i in rbma[1]:
            obj = rbma[1][i]
            print(f"ID: {obj.id}, Clasificación: {obj.clasificacion}, Ponderación: {obj.ponderacion}, "
                  f"Sumatoria Ponderaciones: {obj.sumatoria_ponderaciones}, Contador: {obj.contador}, "
                  f"Grado de Conocimiento: {obj.grado_de_conocimiento}, Matriz Ponderación: {obj.matriz_ponderacion}, "
                  f"Matriz Inferencia: {obj.matriz_inferencia}, Matriz Inferencia Final: {obj.matriz_inferencia_final}, "
                  f"Dificultad: {obj.dificultad}, Discriminación: {obj.discriminacion}, Adivinación: {obj.adivinacion}, "
                  f"Asintota: {obj.asintota}, Orden Evaluación: {obj.orden_evaluacion}")
    except Exception as e:
        print(f"Error al leer los objetos: {e}")

# Función para buscar un registro por id
def leer_por_id(rbma, id):
    try:
        if id in rbma[1]:
            obj = rbma[1][id]
            print(f"ID: {obj.id}, Clasificación: {obj.clasificacion}, Ponderación: {obj.ponderacion}, "
                  f"Sumatoria Ponderaciones: {obj.sumatoria_ponderaciones}, Contador: {obj.contador}, "
                  f"Grado de Conocimiento: {obj.grado_de_conocimiento}, Matriz Ponderación: {obj.matriz_ponderacion}, "
                  f"Matriz Inferencia: {obj.matriz_inferencia}, Matriz Inferencia Final: {obj.matriz_inferencia_final}, "
                  f"Dificultad: {obj.dificultad}, Discriminación: {obj.discriminacion}, Adivinación: {obj.adivinacion}, "
                  f"Asintota: {obj.asintota}, Orden Evaluación: {obj.orden_evaluacion}")
        else:
            print(f"Objeto con ID {id} no encontrado.")
    except Exception as e:
        print(f"Error al leer el objeto: {e}")

# Función para actualizar un objeto en base a un id
def actualizar_objeto(rbma, id, nuevos_datos):
    try:
        if id in rbma[1]:
            obj = rbma[1][id]
            for key, value in nuevos_datos.items():
                setattr(obj, key, value)
            guardar_datos(file_path, rbma)
            print(f"Objeto {id} actualizado exitosamente.")
        else:
            print(f"Objeto con ID {id} no encontrado.")
    except Exception as e:
        print(f"Error al actualizar el objeto: {e}")

# Función para eliminar un registro del .pkl
def eliminar_objeto(rbma, id):
    try:
        if id in rbma[1]:
            del rbma[1][id]
            guardar_datos(file_path, rbma)
            print(f"Objeto {id} eliminado exitosamente.")
        else:
            print(f"Objeto con ID {id} no encontrado.")
    except Exception as e:
        print(f"Error al eliminar el objeto: {e}")

# Función para actualizar el grado_de_conocimiento a un valor específico para los IDs en la lista
def actualizar_grado_conocimiento(rbma, ids_a_actualizar, nuevo_grado):
    try:
        for i in ids_a_actualizar:
            if i in rbma[1]:
                obj = rbma[1][i]
                obj.grado_de_conocimiento = nuevo_grado  # Asignar el nuevo grado
                print(f"El grado de conocimiento del nodo {i} ha sido actualizado a {nuevo_grado}.")
            else:
                print(f"Objeto con ID {i} no encontrado.")
        guardar_datos(file_path, rbma)
    except Exception as e:
        print(f"Error al actualizar el grado de conocimiento: {e}")

# Función para verificar si los IDs en rbma[1] usan el mismo tipo de dato que los IDs en ids_a_actualizar
def verificar_tipo_ids(rbma, ids_a_actualizar):
    try:
        tipos_ids_rbma = {type(i) for i in rbma[1].keys()}
        tipos_ids_actualizar = {type(i) for i in ids_a_actualizar}
        
        print(f"Tipos de IDs en rbma[1]: {tipos_ids_rbma}")
        print(f"Tipos de IDs en ids_a_actualizar: {tipos_ids_actualizar}")
        
        if tipos_ids_rbma == tipos_ids_actualizar:
            print("Los tipos de datos coinciden.")
        else:
            print("Los tipos de datos NO coinciden. Considera hacer una conversión de tipos.")
            # Convertir ids_a_actualizar al tipo de los IDs en rbma[1] (asumiendo que todos son del mismo tipo)
            tipo_comun = list(tipos_ids_rbma)[0]
            try:
                ids_a_actualizar[:] = [tipo_comun(i) for i in ids_a_actualizar]
                print(f"IDs convertidos al tipo: {tipo_comun.__name__}")
            except Exception as e:
                print(f"Error al convertir los IDs: {e}")

    except Exception as e:
        print(f"Error al verificar los tipos de IDs: {e}")

# Función para verificar si los IDs en rbma[1] existen
def verificar_ids_existen(rbma, ids_a_actualizar):
    try:
        for id in ids_a_actualizar:
            if id in rbma[1]:
                print(f"ID {id} existe.")
            else:
                print(f"ID {id} NO existe.")
    except Exception as e:
        print(f"Error al verificar los IDs: {e}")

# Función para obtener datos del nodo
def obtener_datos_nodo():
    try:
        id_input = input("Ingrese el ID del nodo: ")
        clasificacion = input("Ingrese la clasificación del nodo: ")
        # Convertir ID al tipo adecuado si es necesario
        try:
            id = int(id_input)
        except ValueError:
            id = id_input  # Si no es entero, mantener como cadena
        return NODO(id, clasificacion)
    except Exception as e:
        print(f"Error al obtener datos del nodo: {e}")
        return None

# Función para imprimir el menú de opciones
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Crear un nuevo objeto")
    print("2. Leer todos los objetos")
    print("3. Leer un objeto por ID")
    print("4. Actualizar un objeto")
    print("5. Eliminar un objeto")
    print("6. Convertir archivo .pkl a .csv")
    print("7. Actualizar el grado de conocimiento para nodos específicos")
    print("8. Verificar tipos de IDs")
    print("9. Salir")

# Método main
if __name__ == "__main__":
    # Cargar datos
    rbma = cargar_datos(file_path)
    
    if rbma is None:
        print("No se pudo cargar el archivo .pkl. Saliendo del programa.")
    else:
        while True:
            mostrar_menu()
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                nuevo_objeto = obtener_datos_nodo()
                if nuevo_objeto:
                    crear_objeto(rbma, nuevo_objeto)
            
            elif opcion == "2":
                leer_todos(rbma)
            
            elif opcion == "3":
                id_input = input("Ingrese el ID del nodo a leer: ")
                # Convertir el ID al tipo adecuado si es necesario
                tipo_id = type(next(iter(rbma[1].keys())))
                try:
                    id_converted = tipo_id(id_input)
                except ValueError:
                    print(f"El ID debe ser del tipo {tipo_id.__name__}.")
                    continue
                leer_por_id(rbma, id_converted)
            
            elif opcion == "4":
                id_input = input("Ingrese el ID del nodo a actualizar: ")
                # Convertir el ID al tipo adecuado si es necesario
                tipo_id = type(next(iter(rbma[1].keys())))
                try:
                    id_converted = tipo_id(id_input)
                except ValueError:
                    print(f"El ID debe ser del tipo {tipo_id.__name__}.")
                    continue
                if id_converted in rbma[1]:
                    obj = rbma[1][id_converted]
                    # Asignar un valor aleatorio a grado_de_conocimiento entre -1, 0, 1, y 2
                    obj.grado_de_conocimiento = random.choice([-1, 0, 1, 2])
                    guardar_datos(file_path, rbma)
                    print(f"El grado de conocimiento del nodo {id_converted} ha sido actualizado a {obj.grado_de_conocimiento}.")
                else:
                    print(f"Objeto con ID {id_converted} no encontrado.")
            
            elif opcion == "5":
                id_input = input("Ingrese el ID del nodo a eliminar: ")
                # Convertir el ID al tipo adecuado si es necesario
                tipo_id = type(next(iter(rbma[1].keys())))
                try:
                    id_converted = tipo_id(id_input)
                except ValueError:
                    print(f"El ID debe ser del tipo {tipo_id.__name__}.")
                    continue
                eliminar_objeto(rbma, id_converted)
            
            elif opcion == "6":
                convertir_a_csv(rbma, csv_file_path)
            
            elif opcion == "7":
                try:
                    nuevo_grado = int(input("Ingrese el nuevo grado de conocimiento: "))
                    actualizar_grado_conocimiento(rbma, ids_a_actualizar, nuevo_grado)
                except ValueError:
                    print("El grado de conocimiento debe ser un número entero.")
            
            elif opcion == "8":
                # Verificar tipos de IDs
                verificar_tipo_ids(rbma, ids_a_actualizar)
                # Opcional: Verificar si los IDs existen
                verificar_ids_existen(rbma, ids_a_actualizar)
            
            elif opcion == "9":
                print("Saliendo...")
                break
            
            else:
                print("Opción no válida, intente de nuevo.")
