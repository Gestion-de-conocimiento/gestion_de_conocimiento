import os
import pickle
import sys
import plotly.graph_objects as go
import time
from datetime import datetime

def generar_grafica(matricula):
    carpeta_pickle_rbma2 = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma2"
    carpeta_pickle_rbma = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
    
    carpeta_matricula_rbma2 = os.path.join(carpeta_pickle_rbma2, f"rbma_{matricula}")
    
    if not os.path.exists(carpeta_matricula_rbma2):
        return None
    
    archivos_rbma2 = sorted([f for f in os.listdir(carpeta_matricula_rbma2) if f.endswith(".pkl")])
    archivo_rbma = f"rbma_{matricula}.pkl"
    
    archivos = archivos_rbma2 + [archivo_rbma]
    
    if not archivos:
        return None

    evolucion_grado_0 = []
    evolucion_grado_1 = []
    evolucion_grado_2 = []
    fechas_intentos = []
    numeros_intento = []

    for idx, archivo in enumerate(archivos):
        if archivo in archivos_rbma2:
            archivo_pickle = os.path.join(carpeta_matricula_rbma2, archivo)
        else:
            archivo_pickle = os.path.join(carpeta_pickle_rbma, archivo)
        
        try:
            with open(archivo_pickle, "rb") as file:
                data = pickle.load(file)
        except Exception:
            continue

        # Obtener fecha con hora
        try:
            timestamp = os.path.getmtime(archivo_pickle)
            fecha = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M")
        except Exception:
            fecha = "Fecha desconocida"
        
        fechas_intentos.append(fecha)
        numeros_intento.append(idx + 1)

        grados = {0: 0, 1: 0, 2: 0}
        for nodo in data[1].values():
            grado = getattr(nodo, 'grado_de_conocimiento', None)
            if grado in grados:
                grados[grado] += 1

        evolucion_grado_0.append(grados[0])
        evolucion_grado_1.append(grados[1])
        evolucion_grado_2.append(grados[2])

    if not evolucion_grado_0:
        return None

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=fechas_intentos,
        y=evolucion_grado_0,
        mode='lines+markers',
        name='Bajo',
        line=dict(color='red'),
        marker=dict(size=8),
        hovertemplate="Intento: %{customdata[0]}<br>Fecha: %{x}<br>Cantidad: %{y}<extra></extra>",
        customdata=[[i] for i in numeros_intento]
    ))

    fig.add_trace(go.Scatter(
        x=fechas_intentos,
        y=evolucion_grado_1,
        mode='lines+markers',
        name='Regular',
        line=dict(color='yellow'),
        marker=dict(size=8),
        hovertemplate="Intento: %{customdata[0]}<br>Fecha: %{x}<br>Cantidad: %{y}<extra></extra>",
        customdata=[[i] for i in numeros_intento]
    ))

    fig.add_trace(go.Scatter(
        x=fechas_intentos,
        y=evolucion_grado_2,
        mode='lines+markers',
        name='Bueno',
        line=dict(color='green'),
        marker=dict(size=8),
        hovertemplate="Intento: %{customdata[0]}<br>Fecha: %{x}<br>Cantidad: %{y}<extra></extra>",
        customdata=[[i] for i in numeros_intento]
    ))

    fig.update_layout(
        title=f"Evolución del Grado de Conocimiento - Matrícula {matricula}",
        xaxis_title="Fecha y hora del intento",
        yaxis_title="Cantidad de temas",
        template="plotly_white"
    )

    carpeta_temporal = "/root/SistemaKMS/public/Servicios_de_analitica"
    os.makedirs(carpeta_temporal, exist_ok=True)

    timestamp = int(time.time())
    archivo_html = f"grafica_evolucion_grado_{matricula}_{timestamp}.html"
    ruta_html = os.path.join(carpeta_temporal, archivo_html)
    
    fig.write_html(ruta_html)

    return archivo_html

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    matricula = sys.argv[1]
    archivo_html = generar_grafica(matricula)

    if archivo_html:
        print(archivo_html)
    else:
        print("ERROR: No se pudo generar la gráfica")
