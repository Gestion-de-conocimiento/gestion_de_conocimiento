'use strict'

const execSync = require('child_process').execSync;

class AprenderController {
  async obtener_matricula({ response, params }) {
    let matricula = params.matricula;

    try {
      // Ejecutar el script Python y obtener la salida
      const salidaPython = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/DatosPickleEnsenanza.py " + matricula, 
  { encoding: 'utf-8' });


      // Parsear la salida JSON y devolverla como respuesta
      const data = JSON.parse(salidaPython);
      return response.json(data);

    } catch (error) {
  console.error("Ocurrió un error al ejecutar el script Python:", error);
  return response.status(500).json({ 
    error: "Error interno del servidor.",
    detalles: error.message 
  });
}

  }
  
 

}

module.exports = AprenderController