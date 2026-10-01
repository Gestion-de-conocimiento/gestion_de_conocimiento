'use strict';

const fs = require('fs');
const path = require('path');
const dayjs = require('dayjs');
const { execSync } = require('child_process');
const Database = use('Database');
const ConfiguracionActualizacion = use('App/Models/ConfiguracionActualizacion');
const axios = require('axios');

class ActualizarBCController {
  /**
   * Guarda o actualiza la configuración en la tabla configuracion_actualizacions.
   */
  async update({ request, response }) {
    try {
      const data = request.only([
        'modo',
        'minimo_pickles',
        'minimo_temas_dominados',
        'tiempo_en_dias',
        'peso_real'
      ]);

      // DEBUG: payload recibido
      console.log('[DEBUG update] payload:', data);

      const existente = await Database.from('configuracion_actualizacions').first();

      if (existente) {
        await Database
          .table('configuracion_actualizacions')
          .where('id', existente.id)
          .update({ ...data, updated_at: new Date() });
      } else {
        await Database
          .table('configuracion_actualizacions')
          .insert({ ...data, created_at: new Date(), updated_at: new Date() });
      }

      return response.json({ message: 'Configuración guardada correctamente', config: data });

    } catch (err) {
      console.error("❌ Error al guardar configuración:", err);
      // Devolver mensaje y primeras líneas de stack al front para depuración
      return response
        .status(500)
        .json({
          error: err.message,
          stack: err.stack.split('\n').slice(0, 5)
        });
    }
  }

  /**
   * Retorna la configuración actual.
   */
  async show({ response }) {
    try {
      const config = await ConfiguracionActualizacion.query().first();
      if (!config) return response.status(404).json({ error: 'Configuración no encontrada' });
      return response.json(config);
    } catch (err) {
      console.error("❌ Error al obtener configuración:", err);
      return response.status(500).json({ error: 'Error al obtener configuración' });
    }
  }

  /**
   * Verifica si se deben cumplir las condiciones para ejecutar actualización automática.
   */
  async estado({ response }) {
    try {
      const config = await ConfiguracionActualizacion.query().first();
      if (!config) return response.status(404).json({ error: 'Configuración no encontrada' });

      const rutaPickles = '/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbma';
      const archivos = fs.readdirSync(rutaPickles).filter(f => f.endsWith('.pkl'));
      const totalPickles = archivos.length;

      let picklesAptos = 0;
      let fechaUltimo = null;

      for (const archivo of archivos) {
        const archivoPath = path.join(rutaPickles, archivo);
        try {
          const contenido = fs.readFileSync(archivoPath);
          const data = JSON.parse(contenido.toString());

          const dominados = Object.values(data).filter(e => e.grado === 2).length;
          if (dominados >= config.minimo_temas_dominados) picklesAptos++;

          const stats = fs.statSync(archivoPath);
          const modificado = dayjs(stats.mtime);
          if (!fechaUltimo || modificado.isAfter(fechaUltimo)) {
            fechaUltimo = modificado;
          }
        } catch (err) {
          console.error(`⚠️ Error procesando ${archivo}: ${err.message}`);
        }
      }

      // Log de depuración para comprobar valores
      console.log(
        `[DEBUG estado] modo=${config.modo} | picklesAptos=${picklesAptos} | minimo_pickles=${config.minimo_pickles}`
      );

      let tiempoRestante = '---';
      let tiempoCumplido = false;

      // Cambiado 'cantidad' por 'pickles'
      if (config.modo !== 'pickles' && fechaUltimo) {
        const proximo = fechaUltimo.add(config.tiempo_en_dias, 'day');
        const ahora = dayjs();
        const dif = proximo.diff(ahora, 'day');
        tiempoRestante = dif > 0 ? `${dif} días` : '0 días';
        if (dif <= 0) tiempoCumplido = true;
      }

      const cumpleCantidad = config.modo !== 'tiempo' && picklesAptos >= config.minimo_pickles;

      const debeActualizar =
        (config.modo === 'pickles' && cumpleCantidad) ||
        (config.modo === 'tiempo'  && tiempoCumplido) ||
        (config.modo === 'ambos'   && (cumpleCantidad || tiempoCumplido));

      if (debeActualizar) {
        console.log('[✔] Condiciones cumplidas. Ejecutando actualización automática...');
        await axios.post('http://localhost:3333/api/actualizar-bc');

        await Database.table('log_actualizaciones').insert({
          motivo: config.modo,
          total_pickles: totalPickles,
          pickles_aptos: picklesAptos,
          observaciones: `Actualización disparada automáticamente por modo "${config.modo}".`
        });
      }

      return response.json({ totalPickles, picklesAptos, tiempoRestante });

    } catch (err) {
      console.error("❌ Error en estado de actualización:", err);
      return response.status(500).json({ error: 'Error en estado de actualización' });
    }
  }

  /**
   * Devuelve el historial de actualizaciones registradas.
   */
  async historial({ response }) {
    try {
      const registros = await Database
        .from('log_actualizaciones')
        .orderBy('fecha', 'desc')
        .limit(50);

      return response.json(registros);
    } catch (err) {
      console.error("❌ Error al obtener historial:", err);
      return response.status(500).json({ error: 'Error al obtener historial' });
    }
  }

  /**
   * Lista los archivos de red disponibles en la carpeta rbm.
   */
  async listarRedes({ response }) {
    try {
      const dirPath = "/root/SistemaKMS/red_bayesiana/metodo_rutas_evaluacion/rbm";
      if (!fs.existsSync(dirPath)) {
        return response.status(500).json({ error: 'Directorio no encontrado: ' + dirPath });
      }

      const archivos = fs.readdirSync(dirPath).filter(f => f.endsWith('.bifxml'));
      return response.json(archivos);
    } catch (err) {
      console.error("❌ Error al listar redes:", err);
      return response.status(500).json({ error: 'Error al listar redes bayesianas' });
    }
  }

  /**
   * Ejecuta el script de graficación de red bayesiana.
   */
  async graficarRedBayesiana({ request, response }) {
    try {
      const { red } = request.only(["red"]);
      const nombreSinExtension = red.replace(/\.bifxml$/, "");

      const scriptPath = "/root/SistemaKMS/red_bayesiana/Servicios_De_Analitica/Experto/Graficar_base_de_conocimiento.py";
      const output = execSync(`python3 ${scriptPath} ${nombreSinExtension}`, {
        encoding: "utf-8"
      }).trim();

      const lineas = output.split('\n');
      const htmlLine = lineas.find(line => line.trim().endsWith('.html'));

      if (!htmlLine) {
        throw new Error("El script no devolvió un archivo HTML válido: " + output);
      }

      const graphUrl = `/Servicios_de_analitica/${htmlLine.trim()}`;
      return response.json({ graphUrl });

    } catch (error) {
      console.error("❌ Error al graficar red:", error.message);
      return response.status(500).json({
        error: "Error al graficar la red",
        details: error.message
      });
    }
  }
}

module.exports = ActualizarBCController;
