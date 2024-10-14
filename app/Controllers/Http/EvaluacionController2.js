'use strict'

const { exec } = require('child_process');
const Helpers = use('Helpers');

class EvaluacionController {
  async ejecutarEvaluacion({ auth, response }) {
    try {
      // Obtener al usuario en sesión
      const user = await auth.getUser();

      // Obtener la matrícula (si es un correo, quitar lo que está después del '@')
      let matricula = user.matricula;
      if (matricula.includes('@')) {
        matricula = matricula.split('@')[0];
      }

      console.log(`Matrícula obtenida: ${matricula}`); // Log adicional

      // Ruta del archivo Python
      const pythonScript = '/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/pruebaU.py'; // Usar ruta absoluta directa

      // Verificar si el script existe
      const fs = require('fs');
      if (!fs.existsSync(pythonScript)) {
        console.error(`El script Python no existe en la ruta: ${pythonScript}`);
        return response.status(500).send('Error: Script de evaluación no encontrado.');
      }

      // Ejecutar el script con la matrícula como argumento
      console.log(`Ejecutando script: python3 ${pythonScript} ${matricula}`);
      exec(`python3 ${pythonScript} ${matricula}`, (error, stdout, stderr) => {
        if (error) {
          console.error(`Error ejecutando el script: ${error.message}`);
          return response.status(500).send(`Error ejecutando el script de evaluación: ${error.message}`);
        }
        if (stderr) {
          console.error(`Error en la ejecución del script: ${stderr}`);
          return response.status(500).send(`Error en la ejecución del script: ${stderr}`);
        }

        // Devolver tanto stdout como stderr
        console.log(`Resultado del script: ${stdout}`);
        response.send(stdout);
      });
    } catch (error) {
      console.error('Error durante la evaluación:', error);
      return response.status(500).send('Error durante la evaluación');
    }
  }
}

module.exports = EvaluacionController;