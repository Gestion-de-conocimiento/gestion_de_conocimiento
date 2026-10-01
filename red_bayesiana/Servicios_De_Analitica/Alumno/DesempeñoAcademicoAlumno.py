import os
import pickle
import sys
import plotly.graph_objects as go
import time

def generar_grafica(matricula):
    carpeta_pickle = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
    archivo_pickle = os.path.join(carpeta_pickle, f"rbma_{matricula}.pkl")

    if not os.path.exists(archivo_pickle):
        return None  # Si no existe, devolvemos None

    with open(archivo_pickle, "rb") as file:
        data = pickle.load(file)

    grados = {0: 0, 1: 0, 2: 0}
    for nodo in data[1].values():
        grado = nodo.grado_de_conocimiento
        if grado in grados:
            grados[grado] += 1

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Bajo", "Regular", "Bueno"],
        y=[grados[0], grados[1], grados[2]],
        marker=dict(color=["red", "yellow", "green"])
    ))

    fig.update_layout(
        title="Distribución del Grado de Conocimiento",
        xaxis_title="Nivel",
        yaxis_title="Cantidad de temas",
        template="plotly_white"
    )

    # Crear carpeta temporal si no existe
    carpeta_temporal = "/root/SistemaKMS/public/Servicios_de_analitica"
    os.makedirs(carpeta_temporal, exist_ok=True)

    # Guardar el HTML de la gráfica con un timestamp para evitar sobreescritura
    timestamp = int(time.time())  # Obtiene el tiempo actual en segundos
    archivo_html = f"grafica_{matricula}_{timestamp}.html"
    ruta_html = os.path.join(carpeta_temporal, archivo_html)
    
    fig.write_html(ruta_html)

    return archivo_html  # Solo devolvemos el nombre del archivo, no la ruta completa

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No se proporcionó matrícula")
        sys.exit(1)

    matricula = sys.argv[1]
    archivo_html = generar_grafica(matricula)

    if archivo_html:
        print(archivo_html)  # Solo imprime el nombre del archivo
    else:
        print("ERROR: No se pudo generar la gráfica")
