
'use strict'

const Database = use('Database');
const execSync = require('child_process').execSync;
const fs = require('fs');

class PonderacionController {

    // Método de prueba para verificar el funcionamiento
    async pruebaDeFuncionamiento() {
        return "Prueba";
    }
  async ejecutarScriptPython({ auth, response }) {
        try {
            // 🔹 Obtener la matrícula del usuario autenticado
            const user = await auth.getUser();
            const matricula = user.matricula; // Asegúrate de que el usuario tenga este campo

            // 🔹 Ruta del script de Python
            const scriptPath = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/ActualizaGradosDeConocimiento.py";

            // 🔹 Ejecutar el script con la matrícula del usuario
            const output = execSync(`python3 ${scriptPath} ${matricula}`, { encoding: 'utf-8' });
          

            console.log(`✅ Script ejecutado correctamente:\n${output}`);
            return response.json({ message: "Script ejecutado correctamente", output });

        } catch (error) {
            console.error(`❌ Error al ejecutar el script: ${error.message}`);
            return response.status(500).json({ error: "Error al ejecutar el script", details: error.message });
        }
    }

    // Método para obtener el primer tema usando parámetros matricula y rbm
    async obtenerPrimerTema({ response, params }) {
        let matricula = params.matricula;
        let rbm = params.rbm;
        let parametros = " " + matricula + " " + rbm;

        // Ejecuta el script Python con los parámetros
        const output = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/main.py " + parametros, { encoding: 'utf-8' });

        // Retorna la salida del script como respuesta JSON
        return response.json(output);
    }

    // Método para obtener los registros de la tabla 'rbs' de la base de datos
    async obtenerrbs({ response }) {
        const rbs = await Database.raw('SELECT * FROM rbs');
        return response.json(rbs);
    }

   
}



module.exports = PonderacionController