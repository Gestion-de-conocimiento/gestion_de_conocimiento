import sys
import xml.etree.ElementTree as ET
import numpy as np
import plotly.graph_objects as go
import mysql.connector

if len(sys.argv) < 2:
    print("❌ Uso: python3 Graficar_base_de_conocimiento.py <rbm_name>")
    sys.exit(1)

# Argumento: rbm_n
rbm_name = sys.argv[1]
filename = f"/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbm/{rbm_name}.bifxml"

# Conectar a MySQL
try:
    cnx = mysql.connector.connect(
        user='root',
        password='PROYECTO1KMS',
        host='localhost',
        database='kms'
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT id, nombre_tema FROM temas")
    id_a_tema = {str(id): nombre for id, nombre in cursor.fetchall()}
    cursor.close()
    cnx.close()
except Exception as e:
    print(f"❌ Error al conectar a MySQL: {e}")
    sys.exit(1)

# Parsear BIFXML
try:
    tree = ET.parse(filename)
    root = tree.getroot()
except Exception as e:
    print(f"❌ Error al leer el BIFXML: {e}")
    sys.exit(1)

nodo_valores = {}
for defn in root.findall(".//DEFINITION"):
    nodo = defn.find("FOR").text
    nombre_tema = id_a_tema.get(nodo, f"Nodo {nodo}")
    tabla = defn.find("TABLE").text.strip().split()

    filas = []
    for i in range(0, len(tabla), 3):
        trio = list(map(float, tabla[i:i+3]))
        suma = sum(trio)
        if suma > 0:
            # Normalizamos para que la suma sea exactamente 100
            trio = [(x / suma) * 100 for x in trio]
        filas.append(trio)

    promedios = np.mean(filas, axis=0)
    nodo_valores[nombre_tema] = [round(x, 2) for x in promedios]

# Datos para la gráfica
temas = sorted(nodo_valores.keys())
bajo = [nodo_valores[t][0] for t in temas]
regular = [nodo_valores[t][1] for t in temas]
bueno = [nodo_valores[t][2] for t in temas]

# Generar gráfica
fig = go.Figure()
fig.add_trace(go.Bar(name='Bajo', x=temas, y=bajo, marker_color='red'))
fig.add_trace(go.Bar(name='Regular', x=temas, y=regular, marker_color='yellow'))
fig.add_trace(go.Bar(name='Bueno', x=temas, y=bueno, marker_color='green'))

fig.update_layout(
    barmode='stack',
    title=f'Distribución de niveles por tema ({rbm_name})',
    xaxis_title='Tema',
    yaxis_title='Porcentaje (%)',
    legend_title='Nivel',
    template='plotly_white',
    height=600
)

output_file = f"/root/SistemaKMS/public/Servicios_de_analitica/grafica_{rbm_name}.html"
fig.write_html(output_file)
print(f"grafica_{rbm_name}.html")
