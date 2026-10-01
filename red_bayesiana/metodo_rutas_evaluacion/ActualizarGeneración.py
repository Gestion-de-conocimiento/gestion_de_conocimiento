import pickle
import os

# Definir la carpeta donde están los archivos pickle (USAR RUTA ABSOLUTA)
CARPETA_DATOS = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
CARPETA_REPORTES = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/Reportes"

def cargar_datos(file_path):
    """ Carga el archivo pickle si existe """
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


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

    # Crear la carpeta "Reportes/" si no existe antes de escribir el archivo
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
    # Verificar si la carpeta de datos existe
    if not os.path.exists(CARPETA_DATOS):
        print("🚨 ERROR: La carpeta donde deberían estar los archivos NO existe. Verifica la ruta.")
        exit(1)

    # Obtener la lista de archivos pickle en la carpeta
    archivos_pickles = [f for f in os.listdir(CARPETA_DATOS) if f.endswith(".pkl")]

    if not archivos_pickles:
        print("⚠️ No hay archivos pickle en la carpeta.")
        exit(1)

    # Procesar cada archivo pickle encontrado
    for archivo in archivos_pickles:
        file_path = os.path.join(CARPETA_DATOS, archivo)
        matricula = archivo.replace("rbma_", "").replace(".pkl", "")
        output_file = os.path.join(CARPETA_REPORTES, f"reporte_{matricula}.txt")

        print(f"📌 Procesando archivo: {archivo}")

        # Cargar los datos del archivo pickle
        rbma = cargar_datos(file_path)

        if rbma is not None:
            actualizar_grado_conocimiento(rbma, output_file)
        else:
            print(f"❌ No se pudo cargar el archivo {archivo}. Verifica el contenido.")
