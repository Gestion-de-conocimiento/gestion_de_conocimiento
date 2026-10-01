# grafica_intentos_por_tema.py
import os
import sys
import time
import pickle
from datetime import datetime
import plotly.graph_objects as go

CARPETA_RBMA = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
CARPETA_RBMA2 = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma2"
CARPETA_SALIDA = "/root/SistemaKMS/public/Servicios_de_analitica"

def listar_pickles_en_orden(matricula: str):
    """
    Devuelve lista de tuplas (ruta, mtime) de TODOS los intentos para la matrícula,
    ordenados por fecha de modificación (ascendente).
    Considera:
      - /rbma/rbma_<matricula>.pkl (si existe)
      - /rbma2/rbma_<matricula>/*.pkl (si existe la carpeta)
    """
    rutas = []

    # Intento "base" en rbma/
    archivo_base = os.path.join(CARPETA_RBMA, f"rbma_{matricula}.pkl")
    if os.path.exists(archivo_base):
        rutas.append((archivo_base, os.path.getmtime(archivo_base)))

    # Intentos incrementales en rbma2/rbma_<matricula>/
    carpeta_incremental = os.path.join(CARPETA_RBMA2, f"rbma_{matricula}")
    if os.path.isdir(carpeta_incremental):
        for f in os.listdir(carpeta_incremental):
            if f.endswith(".pkl"):
                ruta = os.path.join(carpeta_incremental, f)
                try:
                    rutas.append((ruta, os.path.getmtime(ruta)))
                except Exception:
                    # Si falla obtener mtime, lo ignoramos
                    pass

    rutas.sort(key=lambda x: x[1])  # por mtime ascendente
    return rutas

def formatear_delta(segundos: float) -> str:
    """
    Convierte segundos a un string amigable (días, horas, minutos).
    """
    if segundos < 0:
        segundos = 0
    minutos, s = divmod(int(segundos), 60)
    horas, m = divmod(minutos, 60)
    dias, h = divmod(horas, 24)
    parts = []
    if dias:
        parts.append(f"{dias} d")
    if h:
        parts.append(f"{h} h")
    if m:
        parts.append(f"{m} min")
    if not parts:
        parts.append(f"{s} s")
    return " ".join(parts)

def generar_grafica_intentos_por_tema(matricula: str):
    intentos = listar_pickles_en_orden(matricula)
    if not intentos:
        return None, "No se encontraron intentos para esa matrícula."

    # Timestamp del PRIMER intento (referencia para tiempos)
    t0 = intentos[0][1]

    # Para cada tema, guardaremos el índice del primer intento donde grado==2,
    # y el tiempo (mtime) de ese intento.
    # También guardamos el nombre/id del tema.
    temas_master = {}  # tema_id -> (indice_master, mtime_master)

    # Para obtener nombres/ids estables de temas, detectamos en el primer intento
    # si hay atributo 'id'; si no, usaremos la clave del diccionario como id.
    for idx, (ruta, mtime) in enumerate(intentos, start=1):
        try:
            with open(ruta, "rb") as f:
                data = pickle.load(f)
        except Exception:
            # si no se puede abrir, seguimos
            continue

        # data[1] debería ser el diccionario de nodos/temas
        nodos = {}
        try:
            nodos = data[1]
        except Exception:
            continue

        for clave, nodo in nodos.items():
            # Identificador del tema
            tema_id = getattr(nodo, "id", None)
            if tema_id is None:
                tema_id = str(clave)

            # Si ya está registrado como dominado, no recalculamos
            if tema_id in temas_master:
                continue

            grado = getattr(nodo, "grado_de_conocimiento", None)
            if grado == 2:
                # Este es el PRIMER intento donde se domina
                temas_master[tema_id] = (idx, mtime)

    if not temas_master:
        return None, "Ningún tema alcanzó grado 2 (dominado) en los intentos disponibles."

    # Construimos arreglos para la gráfica
    temas = []
    intentos_hasta_dominar = []
    tiempos_hasta_dominar = []  # texto para hover

    # Ordenar por intentos (más rápidos primero)
    for tema_id, (i_master, t_master) in sorted(temas_master.items(), key=lambda kv: kv[1][0]):
        temas.append(str(tema_id))
        intentos_hasta_dominar.append(i_master)
        delta_txt = formatear_delta(t_master - t0)
        tiempos_hasta_dominar.append(delta_txt)

    # Fechas legibles para hover y título
    fecha_inicial = datetime.fromtimestamp(t0).strftime("%d-%m-%Y %H:%M")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=intentos_hasta_dominar,
        y=temas,
        orientation='h',
        text=[f"{n} intentos" for n in intentos_hasta_dominar],
        textposition="auto",
        hovertemplate=(
            "Tema: %{y}<br>"
            "Intentos hasta dominar: %{x}<br>"
            "Tiempo transcurrido: %{customdata}<extra></extra>"
        ),
        customdata=tiempos_hasta_dominar,
        name="Intentos hasta dominar"
    ))

    fig.update_layout(
        title=f"Intentos por tema hasta dominar (grado 2) - Matrícula {matricula}",
        xaxis_title="Intentos hasta dominar",
        yaxis_title="Tema",
        template="plotly_white",
        margin=dict(l=120, r=30, t=70, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    # Nota en el subtítulo con la referencia de tiempo
    fig.update_layout(
        title=dict(
            text=f"Intentos por tema hasta dominar (grado 2) - Matrícula {matricula}"
                 f"<br><sup>Primer intento: {fecha_inicial}</sup>"
        )
    )

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    timestamp = int(time.time())
    nombre_html = f"grafica_intentos_por_tema_{matricula}_{timestamp}.html"
    ruta_html = os.path.join(CARPETA_SALIDA, nombre_html)
    fig.write_html(ruta_html)
    return nombre_html, None

def main():
    # Puedes pasar la matrícula por argumento o te la pedimos
    if len(sys.argv) >= 2:
        matricula = sys.argv[1].strip()
    else:
        matricula = input("Introduce la matrícula: ").strip()

    if not matricula:
        print("ERROR: Matrícula vacía.")
        sys.exit(1)

    nombre_html, err = generar_grafica_intentos_por_tema(matricula)
    if err:
        print(f"ERROR: {err}")
        sys.exit(1)

    print(nombre_html)

if __name__ == "__main__":
    main()
