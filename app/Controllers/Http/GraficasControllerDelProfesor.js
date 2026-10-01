// Limpieza de gráficas antiguas - GraficasController.js
const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");

// 🧹 Limpia archivos HTML con más de 1 minuto de antigüedad
async function limpiarGraficasAntiguas() {
  const carpeta = "/root/SistemaKMS/public/Servicios_de_analitica";
  const ahora = Date.now();
  const eliminados = [];

  fs.readdirSync(carpeta).forEach((archivo) => {
    const ruta = path.join(carpeta, archivo);
    const stats = fs.statSync(ruta);
    const edadMinutos = (ahora - stats.mtimeMs) / 60000; // Minutos

    if (edadMinutos > 1 && archivo.endsWith(".html")) {
      fs.unlinkSync(ruta);
      eliminados.push(archivo);
    }
  });

  return eliminados;
}

async function generarGrafica({ request, response }) {
  const { matricula, tipo } = request.only(['matricula', 'tipo']);

  try {
    await limpiarGraficasAntiguas();

    let script = '';
    if (tipo === 'distribucion') {
      script = "/root/SistemaKMS/red_bayesiana/Servicios_De_Analitica/Alumno/DesempeñoAcademicoAlumno.py";
    } else if (tipo === 'historico') {
      script = "/root/SistemaKMS/red_bayesiana/Servicios_De_Analitica/Alumno/Desempeño_historico_alumno.py";
    } else {
      return response.status(400).json({ error: "Tipo de gráfica inválido" });
    }

    const salida = execSync(`python3 ${script} ${matricula}`, { encoding: "utf-8" }).trim();

    if (!salida.endsWith(".html")) {
      throw new Error("El script no devolvió un archivo HTML válido: " + salida);
    }

    const url = `/Servicios_de_analitica/${salida}`;
    return response.json({ message: "Gráfica generada", graphUrl: url });
  } catch (error) {
    console.error("❌ Error al generar gráfica:", error);
    return response.status(500).json({ error: "Error ejecutando el script", details: error.message });
  }
}

module.exports = {
  generarGrafica
};
