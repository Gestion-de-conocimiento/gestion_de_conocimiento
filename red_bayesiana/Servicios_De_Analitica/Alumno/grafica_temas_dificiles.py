# grafica_temas_dificiles.py
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

    # Intento base en rbma/
    archivo_base = os.path.join(CARPETA_RBMA, f"rbma_{matricula}.pkl")
    if os.path.exists(archivo_base):
        try:
            rutas.append((archivo_base, os.path.getmtime(archivo_base)))
        except Exception:
            pass

    # Incrementales en rbma2/rbma_<matricula>/
    carpeta_incremental = os.path.join(CARPETA_RBMA2, f"rbma_{matricula}")
    if os.path.isdir(carpeta_incremental):
        for f in os.listdir(carpeta_incremental):
            if f.endswith(".pkl"):
                ruta = os.path.join(carpeta_incremental, f)
                try:
                    rutas.append((ruta, os.path.getmtime(ruta)))
                except Exception:
                    pass

    rutas.sort(key=lambda x: x[1])  # por mtime ascendente
    return rutas

def formatear_delta(segundos: float) -> str:
    """Convierte segundos a string legible: d h min (o s si < 1 min)."""
    if segundos is None:
        return "—"
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

def calcular_dificultad_por_tema(matricula: str):
    """
    Recorre todos los intentos y calcula, por tema:
      - intentos_hasta_dominar (int o None si no domina)
      - tiempo_hasta_dominar (segundos o None)
      - dominado (bool)
    Retorna (lista_ordenada, total_intentos, t0)
    """
    intentos = listar_pickles_en_orden(matricula)
    if not intentos:
        return None, 0, None, "No se encontraron intentos para esa matrícula."

    t0 = intentos[0][1]
    total_intentos = len(intentos)

    # Mapa por tema
    temas = {}  # tema_id -> dict

    for idx, (ruta, mtime) in enumerate(intentos, start=1):
        try:
            with open(ruta, "rb") as f:
                data = pickle.load(f)
        except Exception:
            continue

        try:
            nodos = data[1]  # diccionario de nodos/temas
        except Exception:
            continue

        for clave, nodo in nodos.items():
            tema_id = getattr(nodo, "id", None)
            if tema_id is None:
                tema_id = str(clave)

            registro = temas.get(tema_id)
            if registro is None:
                registro = {
                    "first_idx": idx,      # primer intento donde aparece
                    "dom_idx": None,       # primer intento con grado 2
                    "dom_time": None,      # mtime del intento de dominio
                    "dominado": False
                }
                temas[tema_id] = registro

            grado = getattr(nodo, "grado_de_conocimiento", None)
            if (grado == 2) and (registro["dom_idx"] is None):
                registro["dom_idx"] = idx
                registro["dom_time"] = mtime
                registro["dominado"] = True

    # Construir lista con métrica de dificultad
    resultados = []
    for tema_id, r in temas.items():
        if r["dominado"]:
            intentos_hasta = r["dom_idx"]  # desde primer intento global (consistente con tus gráficas previas)
            tiempo_hasta = r["dom_time"] - t0 if r["dom_time"] is not None else None
            dificultad = intentos_hasta
            estado = "Dominado"
        else:
            intentos_hasta = None
            tiempo_hasta = None
            dificultad = total_intentos + 1  # empuja a la parte difícil
            estado = "No dominado"

        resultados.append({
            "tema": str(tema_id),
            "estado": estado,
            "intentos_hasta_dominar": intentos_hasta,
            "tiempo_hasta_dominar_s": tiempo_hasta,
            "dificultad_score": dificultad
        })

    # Orden: más difícil primero
    resultados.sort(key=lambda x: (-x["dificultad_score"], x["intentos_hasta_dominar"] or 10**9))
    return resultados, total_intentos, t0, None

def generar_grafica_temas_dificiles(matricula: str):
    resultados, total_intentos, t0, err = calcular_dificultad_por_tema(matricula)
    if err:
        return None, err
    if not resultados:
        return None, "No se pudieron calcular temas."

    # Ejes para la gráfica
    temas = [r["tema"] for r in resultados]
    valores = [
        (r["intentos_hasta_dominar"] if r["intentos_hasta_dominar"] is not None else (total_intentos + 1))
        for r in resultados
    ]
    estados = [r["estado"] for r in resultados]
    tiempos_txt = [formatear_delta(r["tiempo_hasta_dominar_s"]) for r in resultados]

    # Colorear: rojo = No dominado, azul = Dominado
    colores = ["#d62728" if est == "No dominado" else "#1f77b4" for est in estados]

    fecha_inicial = datetime.fromtimestamp(t0).strftime("%d-%m-%Y %H:%M") if t0 else "?"

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=valores,
        y=temas,
        orientation='h',
        marker=dict(color=colores),
        text=[
            f"{v} intentos" if est == "Dominado" else f"{v} (sin dominar)"
            for v, est in zip(valores, estados)
        ],
        textposition="auto",
        hovertemplate=(
            "Tema: %{y}<br>"
            "Dificultad (intentos): %{x}<br>"
            "Estado: %{customdata[0]}<br>"
            "Tiempo hasta dominar: %{customdata[1]}<extra></extra>"
        ),
        customdata=list(zip(estados, tiempos_txt)),
        name="Dificultad por tema"
    ))

    fig.update_layout(
        title=(
            f"Temas más difíciles - Matrícula {matricula}"
            f"<br><sup>Se consideran {total_intentos} intentos. "
            f"Referencia temporal (primer intento): {fecha_inicial}</sup>"
        ),
        xaxis_title="Intentos hasta dominar (No dominado = total intentos + 1)",
        yaxis_title="Tema",
        template="plotly_white",
        margin=dict(l=140, r=30, t=80, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    timestamp = int(time.time())
    nombre_html = f"grafica_temas_dificiles_{matricula}_{timestamp}.html"
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

    nombre_html, err = generar_grafica_temas_dificiles(matricula)
    if err:
        print(f"ERROR: {err}")
        sys.exit(1)

    print(nombre_html)

if __name__ == "__main__":
    main()
