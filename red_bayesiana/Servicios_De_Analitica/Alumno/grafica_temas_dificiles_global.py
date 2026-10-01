# grafica_temas_dificiles_global.py
# Calcula la dificultad global por tema usando TODAS las matrículas detectadas
# en rbma/ y rbma2/. Ordena de más difícil → más fácil.

import os
import re
import time
import pickle
import statistics
import plotly.graph_objects as go

CARPETA_RBMA = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
CARPETA_RBMA2 = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma2"
CARPETA_SALIDA = "/root/SistemaKMS/public/Servicios_de_analitica"

PATRON_BASE = re.compile(r"^rbma_(.+)\.pkl$")   # extrae matrícula de rbma_<matricula>.pkl
PATRON_DIR = re.compile(r"^rbma_(.+)$")         # extrae matrícula de carpeta rbma_<matricula>

def formatear_delta(segundos):
    if segundos is None:
        return "—"
    if segundos < 0:
        segundos = 0
    minutos, s = divmod(int(segundos), 60)
    horas, m = divmod(minutos, 60)
    dias, h = divmod(horas, 24)
    parts = []
    if dias: parts.append(f"{dias} d")
    if h: parts.append(f"{h} h")
    if m: parts.append(f"{m} min")
    if not parts: parts.append(f"{s} s")
    return " ".join(parts)

def detectar_matriculas():
    mats = set()
    if os.path.isdir(CARPETA_RBMA):
        for f in os.listdir(CARPETA_RBMA):
            m = PATRON_BASE.match(f)
            if m:
                mats.add(m.group(1))
    if os.path.isdir(CARPETA_RBMA2):
        for d in os.listdir(CARPETA_RBMA2):
            ruta = os.path.join(CARPETA_RBMA2, d)
            if os.path.isdir(ruta):
                m = PATRON_DIR.match(d)
                if m:
                    mats.add(m.group(1))
    return sorted(mats)

def listar_pickles_en_orden(matricula):
    rutas = []
    base = os.path.join(CARPETA_RBMA, f"rbma_{matricula}.pkl")
    if os.path.exists(base):
        try:
            rutas.append((base, os.path.getmtime(base)))
        except Exception:
            pass
    inc_dir = os.path.join(CARPETA_RBMA2, f"rbma_{matricula}")
    if os.path.isdir(inc_dir):
        for f in os.listdir(inc_dir):
            if f.endswith(".pkl"):
                ruta = os.path.join(inc_dir, f)
                try:
                    rutas.append((ruta, os.path.getmtime(ruta)))
                except Exception:
                    pass
    rutas.sort(key=lambda x: x[1])  # mtime ascendente
    return rutas

def analizar_alumno(matricula):
    """Devuelve registros por tema para un alumno."""
    intentos = listar_pickles_en_orden(matricula)
    if not intentos:
        return []
    t0 = intentos[0][1]
    total_intentos = len(intentos)

    temas = {}  # tema_id -> {"dom_idx": None/int, "dom_time": None/float}
    for idx, (ruta, mtime) in enumerate(intentos, start=1):
        try:
            with open(ruta, "rb") as f:
                data = pickle.load(f)
        except Exception:
            continue
        try:
            nodos = data[1]
        except Exception:
            continue

        for clave, nodo in nodos.items():
            tema_id = getattr(nodo, "id", None) or str(clave)
            if tema_id not in temas:
                temas[tema_id] = {"dom_idx": None, "dom_time": None}
            if temas[tema_id]["dom_idx"] is None:
                grado = getattr(nodo, "grado_de_conocimiento", None)
                if grado == 2:
                    temas[tema_id]["dom_idx"] = idx
                    temas[tema_id]["dom_time"] = mtime

    registros = []
    for tema_id, r in temas.items():
        if r["dom_idx"] is not None:
            intentos_hasta = r["dom_idx"]
            tiempo_hasta = (r["dom_time"] - t0) if r["dom_time"] is not None else None
            dominado = True
            dificultad = intentos_hasta
        else:
            intentos_hasta = None
            tiempo_hasta = None
            dominado = False
            dificultad = total_intentos + 1  # empuja a "difícil"
        registros.append({
            "tema": str(tema_id),
            "alumno": str(matricula),
            "total_intentos": total_intentos,
            "dominado": dominado,
            "intentos_hasta_dominar": intentos_hasta,
            "tiempo_hasta_dominar_s": tiempo_hasta,
            "dificultad_score": dificultad
        })
    return registros

def agregar_por_tema(registros):
    """Agrega a nivel tema y calcula métricas globales de dificultad."""
    por_tema = {}
    for r in registros:
        por_tema.setdefault(r["tema"], []).append(r)

    resumen = []
    for tema, lst in por_tema.items():
        vistos = len(lst)
        no_dom = sum(1 for x in lst if not x["dominado"])
        pct_no_dom = (no_dom * 100.0 / vistos) if vistos else 0.0

        diffs = [x["dificultad_score"] for x in lst]
        avg_diff = sum(diffs) / len(diffs) if diffs else 0.0
        med_diff = statistics.median(diffs) if diffs else 0.0

        intentos_dom = [x["intentos_hasta_dominar"] for x in lst if x["intentos_hasta_dominar"] is not None]
        avg_dom = (sum(intentos_dom) / len(intentos_dom)) if intentos_dom else None
        med_dom = (statistics.median(intentos_dom) if intentos_dom else None)

        tiempos_dom = [x["tiempo_hasta_dominar_s"] for x in lst if x["tiempo_hasta_dominar_s"] is not None]
        med_tiempo_dom = statistics.median(tiempos_dom) if tiempos_dom else None

        resumen.append({
            "tema": tema,
            "vistos_por": vistos,
            "no_dom": no_dom,
            "pct_no_dom": pct_no_dom,
            "avg_dificultad": avg_diff,
            "med_dificultad": med_diff,
            "avg_intentos_dom": avg_dom,
            "med_intentos_dom": med_dom,
            "med_tiempo_dom_s": med_tiempo_dom,
        })

    # Orden: más difícil primero (promedio mayor; si empata, mayor % no dominados)
    resumen.sort(key=lambda x: (x["avg_dificultad"], x["pct_no_dom"]), reverse=True)
    return resumen

def generar_grafica_global():
    mats = detectar_matriculas()
    if not mats:
        return None, "No se detectaron matrículas en rbma/ ni rbma2/."

    registros = []
    for m in mats:
        registros.extend(analizar_alumno(m))
    if not registros:
        return None, "No hay registros a partir de los pickles."

    resumen = agregar_por_tema(registros)
    if not resumen:
        return None, "No se pudo generar el resumen por tema."

    temas = [r["tema"] for r in resumen]
    valores = [r["avg_dificultad"] for r in resumen]
    textos = [f"{v:.2f}" for v in valores]

    # customdata formateado (evita f-strings anidados)
    customdata = []
    for r in resumen:
        avg_dom_str = f"{r['avg_intentos_dom']:.2f}" if r["avg_intentos_dom"] is not None else "—"
        med_dom_str = f"{r['med_intentos_dom']:.0f}" if r["med_intentos_dom"] is not None else "—"
        tiempo_med_str = formatear_delta(r["med_tiempo_dom_s"])
        customdata.append([
            f"{r['med_dificultad']:.2f}",           # 0
            str(r["vistos_por"]),                    # 1
            str(r["no_dom"]),                        # 2
            f"{r['pct_no_dom']:.1f}",                # 3
            avg_dom_str,                             # 4
            med_dom_str,                             # 5
            tiempo_med_str                           # 6
        ])

    hovertemplate = (
        "Tema: %{y}<br>"
        "Dificultad promedio: %{x:.2f}<br>"
        "Mediana dificultad: %{customdata[0]}<br>"
        "Vistos por: %{customdata[1]} alumnos<br>"
        "No dominados: %{customdata[2]} (%{customdata[3]}%)<br>"
        "Intentos (solo dominados) - media: %{customdata[4]}, mediana: %{customdata[5]}<br>"
        "Tiempo mediano hasta dominar: %{customdata[6]}"
        "<extra></extra>"
    )

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=valores,
        y=temas,
        orientation='h',
        text=textos,
        textposition="auto",
        customdata=customdata,
        hovertemplate=hovertemplate,
        name="Dificultad promedio (mayor = más difícil)"
    ))

    fig.update_layout(
        title=(
            "Temas más difíciles (global, todas las matrículas)"
            "<br><sup>La dificultad es el promedio de intentos hasta dominar; "
            "si no se dominó, cuenta como (total de intentos del alumno + 1).</sup>"
        ),
        xaxis_title="Dificultad promedio (intentos)",
        yaxis_title="Tema",
        template="plotly_white",
        margin=dict(l=150, r=30, t=90, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    nombre_html = f"grafica_temas_dificiles_global_{int(time.time())}.html"
    ruta_html = os.path.join(CARPETA_SALIDA, nombre_html)
    fig.write_html(ruta_html)
    return nombre_html, None

if __name__ == "__main__":
    nombre_html, err = generar_grafica_global()
    if err:
        print(f"ERROR: {err}")
        raise SystemExit(1)
    print(nombre_html)
