import pickle
import sys
import json
import mysql.connector

# Matricula del alumno obtenida como argumento
matriculaAlumno = sys.argv[1]

# Ruta al archivo pickle RBMA
rutaRbma = f"red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_{matriculaAlumno}.pkl"
#rutaRbma="rbma/rbma_2404001.pkl"
#rutaRbma = f"red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_1830142.pkl"


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
        
# Función para conectar a la base de datos y consultar los datos necesarios
def consultar_datos_desde_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="PROYECTO1KMS",
            database="kms",
            connect_timeout=30  # Tiempo de conexión en segundos
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor()

            # Consulta SQL para obtener id_tema, orden_ensenanza y tema_rama
            consulta = "SELECT id_tema, orden_ensenanza, tema_rama FROM temas_orden_ensenanza"
            cursor.execute(consulta)

            # Almacenar los resultados en arrays separados
            id_temas = []
            orden_ensenanzas = []
            tema_ramas = []

            for (id_tema, orden_ensenanza, tema_rama) in cursor:
                id_temas.append(id_tema)
                orden_ensenanzas.append(orden_ensenanza)
                tema_ramas.append(tema_rama)

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()

            return id_temas, orden_ensenanzas, tema_ramas

    except mysql.connector.Error as error:
        print("Error al conectar o consultar la base de datos:", error)
        return None, None, None

# Abrir el archivo pickle y cargar los datos
try:
    with open(rutaRbma, 'rb') as infile:
        RBMA = pickle.load(infile)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {rutaRbma}.")
    sys.exit(1)
except pickle.PickleError:
    print("Error al cargar el archivo pickle.")
    sys.exit(1)

# Lista para almacenar temas filtrados por grado_de_conocimiento -1, 0, 1
temas_filtrados = []

# Iterar sobre los temas y filtrar por grado_de_conocimiento -1, 0, 1
conteo_grado_menos_uno = 0
conteo_grado_cero = 0
conteo_grado_uno = 0

for i in RBMA[1]:
    nodo = RBMA[1][i]
    
    # Filtrar por grados de conocimiento -1, 0, 1
    if nodo.grado_de_conocimiento in [-1,0,1]:
        # Contar cada grado de conocimiento
        if nodo.grado_de_conocimiento == -1:
            conteo_grado_menos_uno += 1
        elif nodo.grado_de_conocimiento == 0:
            conteo_grado_cero += 1
        elif nodo.grado_de_conocimiento == 1:
            conteo_grado_uno += 1
        
        # Guardar los temas filtrados
        tema = {
            "id": nodo.id,
            "grado_de_conocimiento": nodo.grado_de_conocimiento
        }
        temas_filtrados.append(tema)

# Ordenar temas filtrados por el grado_de_conocimiento
temas_filtrados_ordenados = sorted(temas_filtrados, key=lambda x: x["grado_de_conocimiento"])

# Convertir ids en enteros si es necesario
ids = [int(tema['id']) for tema in temas_filtrados_ordenados]
grados_de_conocimiento = [tema['grado_de_conocimiento'] for tema in temas_filtrados_ordenados]

# Consultar datos desde la base de datos
id_temas_bd, orden_ensenanzas_bd, tema_ramas_bd = consultar_datos_desde_bd()

if id_temas_bd is not None:
    # Convertir id_temas_bd a enteros si es necesario
    id_tema_set = set(str(id) for id in id_temas_bd)  # Convertir a string para asegurar consistencia

    # Crear diccionarios para acceso rápido a orden_ensenanza y rama
    orden_ensenanza_dict = dict(zip(map(str, id_temas_bd), orden_ensenanzas_bd))
    rama_dict = dict(zip(map(str, id_temas_bd), tema_ramas_bd))

    # Nuevo array para almacenar los resultados
    resultado_array = []

    # Recorre el primer array (ids y grados_de_conocimiento)
    for tema_item, grado in zip(ids, grados_de_conocimiento):
        tema_item_str = str(tema_item)  # Convertir a string para acceder a los diccionarios
        if tema_item_str in id_tema_set:
            resultado_array.append({
                'tema': tema_item,
                'grado_de_conocimiento': grado,
                'orden_ensenanza': orden_ensenanza_dict.get(tema_item_str, 'Desconocido'),
                'rama': rama_dict.get(tema_item_str, 'Desconocida')
            })

    # Ordenar resultado_array por 'rama', 'orden_ensenanza', 'grado_de_conocimiento', y 'tema'
    resultado_array_ordenado = sorted(
        resultado_array,
        key=lambda x: (x['rama'], x['orden_ensenanza'], x['grado_de_conocimiento'], x['tema'])
    )

    # Preparar los datos para enviar como respuesta JSON
    data = {
        "conteo_temas": {
            "menos": conteo_grado_menos_uno,
            "cero": conteo_grado_cero,
            "uno": conteo_grado_uno
        },
        "temas_filtrados_ordenados": temas_filtrados_ordenados,
        "resultado_array": resultado_array_ordenado  # Utilizar el array ordenado
    }

    # Imprimir la respuesta en formato JSON
    print(json.dumps(data, indent=4))
else:
    print("Error al consultar datos desde la base de datos.")