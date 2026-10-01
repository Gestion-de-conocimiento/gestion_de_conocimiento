import xml.etree.ElementTree as ET
import numpy as np
import csv
import sys
import os
import pickle
import pandas as pd
import re
import time

# === PROMEDIO DE PICKLES ===
def promediar_pickles():
    PICKLES_DIR = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma"
    PROMEDIOS_DIR = "/root/SistemaKMS/red_bayesiana/ActualizarBC/Promedios"
    os.makedirs(PROMEDIOS_DIR, exist_ok=True)

    final_df = pd.DataFrame()
    patron = re.compile(r"rbma_\d+\.pkl")

    import types
    class NODO:
        def __init__(self, id, clasificacion):
            self.id = id
            self.clasificacion = clasificacion
            self.ponderacion = 0

    sys.modules["NODO"] = types.SimpleNamespace(NODO=NODO)

    for filename in os.listdir(PICKLES_DIR):
        if filename.endswith('.pkl') and patron.match(filename):
            path = os.path.join(PICKLES_DIR, filename)
            with open(path, 'rb') as f:
                rbma = pickle.load(f)

            data = [(nodo.id, nodo.ponderacion) for nodo in rbma[1].values()]
            df = pd.DataFrame(data, columns=["tema", filename])

            final_df = df if final_df.empty else pd.merge(final_df, df, on="tema", how="outer")

    if not final_df.empty:
        final_df['promedio'] = final_df.iloc[:, 1:].mean(axis=1)
        out_path = os.path.join(PROMEDIOS_DIR, 'promedio.csv')
        final_df.to_csv(out_path, index=False)
        print(f"✅ Promedio generado: {out_path}")
        return out_path
    else:
        print("⚠️ No se encontraron datos válidos")
        sys.exit(1)

# === SIGMOIDE ===
def sigmoide(val, k=0.2):
    return 1 / (1 + np.exp(-k * val))

def generar_distribucion(archivo_csv):
    df = pd.read_csv(archivo_csv)
    DIST_DIR = "/root/SistemaKMS/red_bayesiana/ActualizarBC/DistribucionEstados"
    os.makedirs(DIST_DIR, exist_ok=True)
    resultados = []

    for _, row in df.iterrows():
        p = row['promedio']
        bajo = 1 - sigmoide(p - 66)
        regular = sigmoide(p - 66) - sigmoide(p - 83)
        bueno = sigmoide(p - 83)

        total = bajo + regular + bueno
        bajo, regular, bueno = [round(x / total, 6) for x in (bajo, regular, bueno)]

        ajuste = 1 - (bajo + regular + bueno)
        bueno += ajuste

        resultados.append([row['tema'], p, bajo, regular, bueno])

    out_path = os.path.join(DIST_DIR, 'distribucion_estados.csv')
    pd.DataFrame(resultados, columns=['id', 'promedio', 'bajo', 'regular', 'bueno']).to_csv(
        out_path, index=False, float_format="%.6f")
    print(f"✅ Distribución estados generado: {out_path}")
    return out_path

# === BIFXML TEMPORAL ===
def generar_bifxml_temp(csv_file):
    df = pd.read_csv(csv_file)
    DATA_DIR = "/root/SistemaKMS/red_bayesiana/ActualizarBC/DatosReales"
    os.makedirs(DATA_DIR, exist_ok=True)

    timestamp = int(time.time())
    bifxml_out = os.path.join(DATA_DIR, f"rbm_tmp_{timestamp}.bifxml")

    root = ET.Element('BIF')
    for _, row in df.iterrows():
        defn = ET.SubElement(root, 'DEFINITION')
        ET.SubElement(defn, 'FOR').text = str(int(row['id']))
        table = ET.SubElement(defn, 'TABLE')
        table.text = f"{row['bajo']} {row['regular']} {row['bueno']}"

    ET.ElementTree(root).write(bifxml_out, encoding='utf-8', xml_declaration=True)
    print(f"✅ BIFXML temporal generado: {bifxml_out}")
    return bifxml_out

# === Obtener siguiente número secuencial ===
def obtener_siguiente_numero():
    carpeta = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbm"
    patron = re.compile(r"rbm_(\d+)\.bifxml")
    max_n = 0
    for nombre in os.listdir(carpeta):
        match = patron.match(nombre)
        if match:
            n = int(match.group(1))
            if n > max_n:
                max_n = n
    return max_n + 1

# === FUSIÓN ===
def extraer_probabilidades(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    datos = {}
    for defn in root.findall(".//DEFINITION"):
        nodo = defn.find("FOR").text
        tabla = [float(x) for x in defn.find("TABLE").text.strip().split()]
        datos[nodo] = np.array(tabla)
    return datos, tree, root

def fusionar(peso_alumnos, rbm_expertos_path, rbm_tmp_path):
    numero = obtener_siguiente_numero()
    rbm_out = f"/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbm/rbm_{numero}.bifxml"
    csv_out = "/root/SistemaKMS/red_bayesiana/ActualizarBC/resultados_fusionados.csv"

    dict_exp, _, _ = extraer_probabilidades(rbm_expertos_path)
    dict_alum, tree_alum, root_alum = extraer_probabilidades(rbm_tmp_path)

    filas_csv = [["Nodo", "Bajo (Exp)", "Reg (Exp)", "Bueno (Exp)",
                  "Bajo (Alum)", "Reg (Alum)", "Bueno (Alum)",
                  "Bajo (Fusion)", "Reg (Fusion)", "Bueno (Fusion)"]]

    for defn in root_alum.findall(".//DEFINITION"):
        nodo = defn.find("FOR").text
        tabla = defn.find("TABLE")
        if nodo in dict_exp and nodo in dict_alum:
            p_exp, p_alum = dict_exp[nodo], dict_alum[nodo]

            if len(p_alum) != len(p_exp):
                p_alum = np.tile(p_alum, len(p_exp) // len(p_alum))

            fusion = (1 - peso_alumnos) * p_exp + peso_alumnos * p_alum

            for i in range(0, len(fusion), 3):
                suma = sum(fusion[i:i+3])
                fusion[i:i+3] = [round(x / suma, 6) for x in fusion[i:i+3]]

                filas_csv.append([nodo] +
                                 [round(x,6) for x in p_exp[i:i+3]] +
                                 [round(x,6) for x in p_alum[i:i+3]] +
                                 [round(x,6) for x in fusion[i:i+3]])

            tabla.text = "\n" + "\n".join(
                " ".join(f"{x:.6f}" for x in fusion[i:i+3])
                for i in range(0, len(fusion),3)
            ) + "\n"

    tree_alum.write(rbm_out, encoding='utf-8', xml_declaration=True)
    print(f"✅ Fusionado generado: {rbm_out}")

    with open(csv_out, 'w', newline='') as f:
        csv.writer(f).writerows(filas_csv)
    print(f"✅ CSV fusionado generado: {csv_out}")

# === EJECUCIÓN ===
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ Uso: python3 ActualizarBC.py <peso_alumnos> <rbm_expertos>")
        sys.exit(1)

    peso = float(sys.argv[1])
    rbm_expertos_path = sys.argv[2]

    promedio_path = promediar_pickles()
    distrib_path = generar_distribucion(promedio_path)
    rbm_tmp_path = generar_bifxml_temp(distrib_path)
    fusionar(peso, rbm_expertos_path, rbm_tmp_path)
