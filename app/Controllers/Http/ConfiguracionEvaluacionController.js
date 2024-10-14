'use strict'

const Database = use('Database')

class ConfiguracionEvaluacionController {
	async obtenerTotalPreguntasTema({ response }) {
    try {
        const preguntasPorTema = await Database.raw('SELECT temas.nombre_tema, temas.nivel, COUNT(*) AS totalPreguntas FROM banco_preguntas RIGHT JOIN temas ON banco_preguntas.id_tema = temas.id GROUP BY temas.id HAVING temas.nivel > 1;');
        return response.json(preguntasPorTema[0]);
    } catch (error) {
        return response.status(500).json({ message: 'Error al obtener preguntas por tema' });
    }
}

	
	async guardarConfiguracionEvaluacion({request}){
			
		const ponderacionEstricta = Number(request.post().ponderacionEstricta);
		const totalPreguntas = Number(request.post().totalPreguntas);
		const rangoDefecto = Number(request.post().rangoDefecto);
		const rbmID = Number(request.post().rbmID);
			
		const configuracion = await Database.raw('INSERT INTO configuracion_evaluaciones (ponde_estricta, total_preguntas, rango_por_defecto, rbm, created_at, updated_at) VALUES (?,?,?,?,NOW(),NOW())',[ponderacionEstricta, totalPreguntas, rangoDefecto, rbmID]);
		return "success";
	}

	async obtenerConfiguracionEvaluacion({response}){
		const configuracion = await Database.raw('SELECT ponde_estricta, total_preguntas, rango_por_defecto, rbm FROM configuracion_evaluaciones ORDER BY id DESC LIMIT 1;');
		return response.json(configuracion[0][0]);
	}
	
}

module.exports = ConfiguracionEvaluacionController