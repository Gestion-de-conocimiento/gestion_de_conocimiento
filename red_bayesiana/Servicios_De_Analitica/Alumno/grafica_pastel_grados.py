# grafica_pastel_grados.py
import os
import sys
import time
import pickle
from datetime import datetime
import plotly.graph_objects as go

CARPETA_RBMA = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
CARPETA_RBMA2 = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma2"
CARPETA_SALIDA = "/root/SistemaKMS/public/Servicios_de_analitica"

def listar_todos_los_intentos(matricula: str):
    """Devuelve lista de tuplas (ruta, mtime) de TODOS los intentos para la matrícula."""
    rutas = []
    base = os.path.join(CARPETA_RBMA, f"rbma_{matricula}.pkl")
    if os.path.exists(base):
        rutas.append((base, os.path.getmtime(base)))

    inc_dir = os.path.join(CARPETA_RBMA2, f"rbma_{matricula}")
    if os.path.isdir(inc_dir):
        for f in os.listdir(inc_dir):
            if f.endswith(".pkl"):
                ruta = os.path.join(inc_dir, f)
                try:
                    rutas.append((ruta, os.path.getmtime(ruta)))
                except Exception:
                    pass

    rutas.sort(key=lambda x: x[1])  # ascendente
    return rutas

def generar_grafica_pastel(matricula: str):
    intentos = listar_todos_los_intentos(matricula)
    if not intentos:
        return None, "No se encontraron intentos para esa matrícula."

    # Tomamos el último intento (más reciente)
    ruta_ultima, mtime_ultima = intentos[-1]
    try:
        with open(ruta_ultima, "rb") as f:
            data = pickle.load(f)
    except Exception as e:
        return None, f"No se pudo abrir el último pickle: {e}"

    # Contar grados en el snapshot final
    try:
        nodos = data[1]  # diccionario de nodos/temas
    except Exception:
        return None, "Formato inesperado del pickle: no se encontró data[1]."

    conteos = {0: 0, 1: 0, 2: 0}
    for _, nodo in nodos.items():
        grado = getattr(nodo, "grado_de_conocimiento", None)
        if grado in conteos:
            conteos[grado] += 1

    total = sum(conteos.values())
    if total == 0:
        return None, "No hay temas para calcular porcentajes."

    # Datos para la gráfica
    etiquetas = ["Bajo", "Regular", "Bueno"]
    valores = [conteos[0], conteos[1], conteos[2]]
    colores = ["red", "yellow", "green"]
    porcentajes = [round(v * 100.0 / total, 2) for v in valores]

    fecha_ultima = datetime.fromtimestamp(mtime_ultima).strftime("%d-%m-%Y %H:%M")

    fig = go.Figure(data=[go.Pie(
        labels=etiquetas,
        values=valores,
        marker=dict(colors=colores),
        hovertemplate="%{label}: %{percent} (%{value} temas)<extra></extra>",
        text=[f"{p}%" for p in porcentajes],
        textinfo="label+text"  # muestra etiqueta + porcentaje
    )])

    fig.update_layout(
        title=f"Distribución de grados (último intento) - Matrícula {matricula}"
              f"<br><sup>Último intento: {fecha_ultima} | Total temas: {total}</sup>",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=80, b=20),
        template="plotly_white"
    )

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    timestamp = int(time.time())
    nombre_html = f"grafica_pastel_grados_{matricula}_{timestamp}.html"
    ruta_html = os.path.join(CARPETA_SALIDA, nombre_html)
    fig.write_html(ruta_html)

    return nombre_html, None

def main():
    # Pedir matrícula si no viene como argumento
    if len(sys.argv) >= 2:
        matricula = sys.argv[1].strip()
    else:
        matricula = input("Introduce la matrícula: ").strip()

    if not matricula:
        print("ERROR: Matrícula vacía.")
        sys.exit(1)

    nombre_html, err = generar_grafica_pastel(matricula)
    if err:
        print(f"ERROR: {err}")
        sys.exit(1)

    print(nombre_html)

if __name__ == "__main__":
    main()
