import pickle
import sys
import os

# Verificar si se ha proporcionado la matrícula como argumento
if len(sys.argv) < 2:
    print("❌ Error: Matrícula no proporcionada")
    sys.exit(1)

# Matrícula del alumno obtenida como argumento
matriculaAlumno = sys.argv[1]
print(f"📌 Matrícula recibida en el script Python: {matriculaAlumno}")

# Definir la carpeta donde están los archivos pickle (USAR RUTA ABSOLUTA)
CARPETA_DATOS = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"

# Definir la carpeta correcta para los reportes
CARPETA_REPORTES = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/Reportes"

# Ruta del archivo pickle basado en la matrícula
file_path = os.path.join(CARPETA_DATOS, f"rbma_{matriculaAlumno}.pkl")

# Ruta para el archivo de reporte en la carpeta correcta
output_file = os.path.join(CARPETA_REPORTES, f"reporte_{matriculaAlumno}.txt")

def cargar_datos(file_path):
    """ Carga el archivo pickle si existe """
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def listar_archivos(carpeta):
    """ Lista los archivos en la carpeta si la matrícula no se encuentra """
    print("📂 No se encontró el archivo de la matrícula. Archivos disponibles en la carpeta:")
    try:
        archivos = os.listdir(carpeta)
        if archivos:
            for archivo in archivos:
                print(f"  - {archivo}")
        else:
            print("⚠️ No hay archivos en la carpeta.")
    except FileNotFoundError:
        print("🚨 ERROR: La carpeta especificada no existe. Verifica la ruta.")

def guardar_datos(file_path, data):
    """ Guarda los datos en un archivo pickle """
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def actualizar_grado_conocimiento(rbma, output_file):
    """ Actualiza los grados de conocimiento y genera un reporte """
    registros_desactualizados = []  
    registros_actualizados = []    

    for id, nodo in rbma[1].items():
        ponderacion = nodo.ponderacion
        grado_actual = nodo.grado_de_conocimiento

        # Cambiar grados de conocimiento de -1 a 0 sin incluir en el reporte
        if grado_actual == -1:
            nodo.grado_de_conocimiento = 0
            continue

        # Determinar el nuevo grado de conocimiento
        if 0 <= ponderacion <= 66:
            nuevo_grado = 0
        elif 66 < ponderacion <= 83:
            nuevo_grado = 1
        elif 83 < ponderacion <= 100:
            nuevo_grado = 2
        else:
            continue  

        # Verificar si hay inconsistencia
        if grado_actual != nuevo_grado:
            registros_desactualizados.append((id, ponderacion, grado_actual))
            nodo.grado_de_conocimiento = nuevo_grado
            registros_actualizados.append((id, ponderacion, nuevo_grado))

    guardar_datos(file_path, rbma)

    # 🔹 Crear la carpeta "Reportes/" si no existe antes de escribir el archivo
    os.makedirs(CARPETA_REPORTES, exist_ok=True)

    with open(output_file, 'w') as report:
        report.write("--------------------------------------\n")
        report.write("ID  PONDERACION  GRADO DE CONOCIMIENTO\n")
        report.write("--------------------------------------\n")

        for id, ponderacion, grado in registros_desactualizados:
            report.write(f"{id:<6}{ponderacion:<12}{grado}\n")

        report.write("--------------------------------------\n\n")
        report.write("Registros con grados de conocimiento actualizados:\n")
        report.write("--------------------------------------\n")
        report.write("ID  PONDERACION  GRADO DE CONOCIMIENTO\n")
        report.write("--------------------------------------\n")

        for id, ponderacion, grado in registros_actualizados:
            report.write(f"{id:<6}{ponderacion:<12}{grado}\n")

        report.write("--------------------------------------\n")

    print(f"📄 Reporte generado en: {output_file}")

if __name__ == "__main__":
    # Verificar si la carpeta de datos existe antes de buscar archivos
    if not os.path.exists(CARPETA_DATOS):
        print("🚨 ERROR: La carpeta donde deberían estar los archivos NO existe. Verifica la ruta.")
        sys.exit(1)

    # Verificar si el archivo de la matrícula existe antes de cargarlo
    if not os.path.exists(file_path):
        listar_archivos(CARPETA_DATOS)
        sys.exit(1)  # Termina el script si el archivo no existe

    # Cargar el archivo pickle
    rbma = cargar_datos(file_path)

    # Ejecutar la actualización si se cargaron los datos correctamente
    if rbma is not None:
        actualizar_grado_conocimiento(rbma, output_file)
    else:
        print("❌ No se pudo cargar el archivo. Verifica la matrícula e intenta de nuevo.")
