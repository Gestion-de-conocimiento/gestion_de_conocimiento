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
    const edadMinutos = (ahora - stats.mtimeMs) / 60000; // Usamos mtime

    if (edadMinutos > 1 && archivo.endsWith(".html")) {
      fs.unlinkSync(ruta);
      eliminados.push(archivo);
    }
  });

  return eliminados;
}


async function ejecutarScriptPython({ auth, response }) {
  try {
    const user = await auth.getUser();
    const matricula = user.matricula;

    const scriptPath = "/root/SistemaKMS/red_bayesiana/Servicios_De_Analitica/Alumno/DesempeñoAcademicoAlumno.py";
    const output = execSync(`python3 ${scriptPath} ${matricula}`, { encoding: "utf-8" }).trim();

    if (!output.endsWith(".html")) {
      throw new Error(`Salida inesperada del script: ${output}`);
    }

    await limpiarGraficasAntiguas();

    const graphUrl = `/Servicios_de_analitica/${output}`;
    console.log(`✅ Gráfica generada: ${graphUrl}`);

    return response.json({ message: "Gráfica generada con éxito", graphUrl });
  } catch (error) {
    console.error(`❌ Error: ${error.message}`);
    return response.status(500).json({ error: "Error al ejecutar el script", details: error.message });
  }
}

async function ejecutarScriptHistorico({ auth, response }) {
  try {
    const user = await auth.getUser();
    const matricula = user.matricula;

    const scriptPath = "/root/SistemaKMS/red_bayesiana/Servicios_De_Analitica/Alumno/Desempeño_historico_alumno.py";
    const output = execSync(`python3 ${scriptPath} ${matricula}`, { encoding: "utf-8" }).trim();

    if (!output.endsWith(".html")) {
      throw new Error(`Salida inesperada del script: ${output}`);
    }

    await limpiarGraficasAntiguas();

    const graphUrl = `/Servicios_de_analitica/${output}`;
    console.log(`✅ Histórico generado: ${graphUrl}`);

    return response.json({ message: "Historial generado con éxito", graphUrl });
  } catch (error) {
    console.error(`❌ Error: ${error.message}`);
    return response.status(500).json({ error: "Error al ejecutar el script histórico", details: error.message });
  }
}

// Ruta opcional si deseas probar limpieza manual desde Vue o navegador
async function limpiarGraficasDesdeRuta({ response }) {
  try {
    const eliminados = await limpiarGraficasAntiguas();
    return response.json({ eliminados, message: "Archivos eliminados correctamente" });
  } catch (error) {
    return response.status(500).json({ error: "Error limpiando gráficas", details: error.message });
  }
}

module.exports = {
  ejecutarScriptPython,
  ejecutarScriptHistorico,
  limpiarGraficasDesdeRuta
};
