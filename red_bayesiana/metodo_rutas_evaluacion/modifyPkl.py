import pickle
import sys
import mysql.connector
import numpy as np

# Argumentos del sistema
matriculaAlumno = sys.argv[1]
id_tema = str(sys.argv[2])  # <- importante: usar como str
ponderacion = int(sys.argv[3])
gradoCono = int(sys.argv[4])

file_path = f"red_bayesiana/metodo_rutas_evaluacion/rbma/rbma_{matriculaAlumno}.pkl"

# Clase original NODO
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

# === Funciones auxiliares ===

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def calcular_matriz_inferencia_final(ponderacion):
    bajo = 1 - sigmoide(ponderacion - 66)
    regular = sigmoide(ponderacion - 66) - sigmoide(ponderacion - 83)
    bueno = sigmoide(ponderacion - 83)

    total = bajo + regular + bueno
    partes = [bajo / total, regular / total, bueno / total]
    porcentajes = [int(round(p * 100)) for p in partes]

    diferencia = 100 - sum(porcentajes)
    if diferencia != 0:
        idx = np.argmax(partes) if diferencia > 0 else np.argmin(partes)
        porcentajes[idx] += diferencia

    return porcentajes

def matriz_por_grado(grado):
    if grado == 0:
        return [100, 0, 0]
    elif grado == 1:
        return [0, 100, 0]
    elif grado == 2:
        return [0, 0, 100]
    return [0, 0, 0]

def calcular_grado_por_ponderacion(ponderacion, nivel):
    if nivel in (0, 1):
        if ponderacion <= 66:
            return 0
        elif ponderacion <= 83:
            return 1
        else:
            return 2
    return -1

def cargar_datos(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def guardar_datos(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def obtener_jerarquia_mysql():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PROYECTO1KMS',
        database='kms'
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT id_tema, tema_rama FROM temas_orden_ensenanza WHERE tema_rama IS NOT NULL")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    jerarquia = {}
    for id_tema, tema_rama in resultados:
        tema_t = str(id_tema)
        padre_t = str(tema_rama)
        if padre_t not in jerarquia:
            jerarquia[padre_t] = []
        jerarquia[padre_t].append(tema_t)
    return jerarquia

def actualizar_objeto(rbma, id, nuevos_datos):
    if id in rbma[1]:
        nodo = rbma[1][id]
        for key, value in nuevos_datos.items():
            setattr(nodo, key, value)
        nodo.matriz_ponderacion = matriz_por_grado(nodo.grado_de_conocimiento)
        nodo.matriz_inferencia_final = calcular_matriz_inferencia_final(nodo.ponderacion)
        print(f"[✔] Nodo {id} actualizado: grado={nodo.grado_de_conocimiento}, ponderacion={nodo.ponderacion}, mif={nodo.matriz_inferencia_final}")
    else:
        print(f"[✘] Nodo {id} no encontrado")

def actualizar_nivel_superior(rbma, id_padre, jerarquia, nivel):
    ids_hijos = jerarquia.get(id_padre, [])
    hijos = [rbma[1][hid] for hid in ids_hijos if hid in rbma[1] and rbma[1][hid].ponderacion > 0]
    if not hijos:
        return

    suma = sum(h.ponderacion for h in hijos)
    promedio = suma / len(hijos)
    grado = calcular_grado_por_ponderacion(promedio, nivel)

    if id_padre in rbma[1]:
        nodo = rbma[1][id_padre]
        nodo.ponderacion = int(promedio)
        nodo.sumatoria_ponderaciones = int(suma)
        nodo.grado_de_conocimiento = grado
        nodo.matriz_ponderacion = matriz_por_grado(grado)
        nodo.matriz_inferencia_final = calcular_matriz_inferencia_final(promedio)
        print(f"[↑] Nodo nivel {nivel} {id_padre} → promedio={promedio:.2f}, grado={grado}, mif={nodo.matriz_inferencia_final}")

# === Función principal ===

def escribirDatos():
    print(f"[RUN] matricula={matriculaAlumno}, tema={id_tema}, ponderacion={ponderacion}, grado={gradoCono}")
    rbma = cargar_datos(file_path)
    jerarquia = obtener_jerarquia_mysql()

    # 1. Actualizar nodo tema
    actualizar_objeto(rbma, id_tema, {
        "grado_de_conocimiento": gradoCono,
        "sumatoria_ponderaciones": ponderacion,
        "ponderacion": ponderacion
    })

    # 2. Actualizar padre (rama)
    padre_rama = next((k for k, hijos in jerarquia.items() if id_tema in hijos), None)
    if padre_rama:
        actualizar_nivel_superior(rbma, padre_rama, jerarquia, nivel=1)

        # 3. Actualizar raíz
        abuelo_raiz = next((k for k, hijos in jerarquia.items() if padre_rama in hijos), None)
        if abuelo_raiz:
            actualizar_nivel_superior(rbma, abuelo_raiz, jerarquia, nivel=0)

    guardar_datos(file_path, rbma)
    print("✅ Datos actualizados y guardados correctamente.")

if __name__ == "__main__":
    escribirDatos()
