import os
import shutil
import re
import sys

def comparar_archivos_contenido(archivo1, archivo2):
    # Compara dos archivos por su tamaño y contenido byte por byte
    if os.path.getsize(archivo1) != os.path.getsize(archivo2):
        return False

    with open(archivo1, 'rb') as f1, open(archivo2, 'rb') as f2:
        while True:
            b1 = f1.read(4096)
            b2 = f2.read(4096)
            if b1 != b2:
                return False
            if not b1:
                return True

# Definir las rutas de las carpetas
carpeta_origen = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
carpeta_destino = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma2"

# Verificar que se pasó un argumento (la matrícula)
if len(sys.argv) < 2:
    print("Error: No se proporcionó la matrícula como argumento.")
    sys.exit(1)

# Obtener la matrícula desde los argumentos de la línea de comandos
matricula = sys.argv[1]

# Buscar archivos que contengan la matrícula en su nombre
archivos_encontrados = [f for f in os.listdir(carpeta_origen) if matricula in f and f.endswith('.pkl')]

# Verificar si se encontraron archivos
if not archivos_encontrados:
    print(f"No se encontraron archivos que contengan la matrícula {matricula}.")
else:
    for archivo in archivos_encontrados:
        # Definir la ruta completa del archivo de origen
        ruta_origen = os.path.join(carpeta_origen, archivo)
        
        # Crear la carpeta con el nombre del archivo en rbma2 si no existe
        carpeta_archivo = os.path.join(carpeta_destino, archivo)
        os.makedirs(carpeta_archivo, exist_ok=True)
        
        # Buscar el último número usado en los archivos de la carpeta
        archivos_existentes = [f for f in os.listdir(carpeta_archivo) if f.startswith(os.path.splitext(archivo)[0])]
        ultimo_numero = 0

        for nombre in archivos_existentes:
            match = re.search(r'_(\d{5})\.pkl$', nombre)
            if match:
                numero = int(match.group(1))
                if numero > ultimo_numero:
                    ultimo_numero = numero
        
        # Incrementar el número para el nuevo archivo
        nuevo_numero = ultimo_numero + 1
        nombre_archivo, extension = os.path.splitext(archivo)
        archivo_destino = f"{nombre_archivo}_{nuevo_numero:05d}{extension}"
        
        # Definir la ruta completa del archivo de destino
        ruta_destino = os.path.join(carpeta_archivo, archivo_destino)
        
        # Copiar el archivo
        shutil.copy2(ruta_origen, ruta_destino)

        # Verificar si el archivo copiado es idéntico al original por contenido
        if comparar_archivos_contenido(ruta_origen, ruta_destino):
            print(f"Archivo {archivo} copiado a {ruta_destino} y verificado.")
        else:
            print(f"El archivo {archivo} copiado a {ruta_destino} no coincide con el original.")
