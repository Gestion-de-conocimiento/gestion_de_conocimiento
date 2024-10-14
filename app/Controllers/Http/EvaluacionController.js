'use strict'

const Database = use('Database')
const execSync = require('child_process').execSync;
const fs = require('fs');
var listaTemas;

class EvaluacionController {

      async obtenerResultadosTemas({ response, params }) {
      console.log("Sdadasdasda");
        const output = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/DatosPickle.py " +  params.matricula, {encoding: 'utf-8'});
        
        return response.json(output);
    }
  
        async escribirDatos({ response, params }) {
           let parametros = params.matricula + " " + params.tema + " " + params.ponderacion + " " + params.grado
        const output = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/modifyPkl.py " +  parametros, {encoding: 'utf-8'});
        
        return response.json(output);
    }
  
    async obtener_Temas({ response, params }) {

    const matricula = Number(params.matricula);
		const rama_id = Number(params.rama);
    console.log("obtener_fda");
    // le llamo al python y la salida la parseo pa q se vea bien
    const salidaPython = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/DatosPickle.py " + matricula, {encoding: 'utf-8'} )
    const datosJson = JSON.parse(salidaPython);
    
    // agarramos la parte de 'resultado_array' del json que nos aventó el python y agarramos los temas de la rama en la que estamos
    // también tenemos que agarrar los id de cada tema después.
    let temas = datosJson.resultado_array;
    temas = temas.filter(tema => tema.rama === rama_id);
    const idsTemas = temas.map(tema => tema.tema);

    // hacemos un select de los temas obtenidos
    let temas_obtenidos_tabla = await Database.raw('SELECT id_tema FROM temas_orden_ensenanza WHERE tema_rama = ? AND id_tema IN (?)',[rama_id, idsTemas]);
    temas_obtenidos_tabla = temas_obtenidos_tabla[0];
      return response.json({temas_obtenidos_tabla})
    }
  
  async obtener_datos({ response, params }) {

    const matricula = Number(params.matricula);
		const rama_id = Number(params.rama);
    const tema_id = Number(params.tema);
    console.log("obtener_fda");
    // le llamo al python y la salida la parseo pa q se vea bien
    const salidaPython = execSync("python3 red_bayesiana/metodo_rutas_evaluacion/DatosPickle.py " + matricula, {encoding: 'utf-8'} )
    const datosJson = JSON.parse(salidaPython);
    
    // agarramos la parte de 'resultado_array' del json que nos aventó el python y agarramos los temas de la rama en la que estamos
    // también tenemos que agarrar los id de cada tema después.
    let temas = datosJson.resultado_array;
    temas = temas.filter(tema => tema.rama === rama_id);
    temas = temas.filter(tema => tema.tema == tema_id);
    const idsTemas = temas.map(tema => tema.tema);
		//return response.json({temas})

    // hacemos un select de los temas obtenidos
    let temas_obtenidos_tabla = await Database.raw('SELECT id_tema FROM temas_orden_ensenanza WHERE tema_rama = ? AND id_tema IN (?)',[rama_id, idsTemas]);
    temas_obtenidos_tabla = temas_obtenidos_tabla[0];

    // agarramos la config de mi tabla, la de total preguntas por tema, la variable es un numero así secote
    let configEvaluacion = await Database.raw('SELECT ponde_estricta, total_preguntas, rango_por_defecto FROM configuracion_evaluaciones ORDER BY id DESC LIMIT 1;');
    let max_preg_conf = configEvaluacion[0][0].total_preguntas;
    let ponde_estricta_config = configEvaluacion[0][0].ponde_estricta;
    let rango_defecto_config = configEvaluacion[0][0].rango_por_defecto;

    
      
    for(const tema of temas){
const configuraciones = await Database.raw('SELECT  * FROM configuracion_cuestionarios');
		
		const preguntasMultiples = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 4 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
		
		const preguntasBoleanas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 3 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
		
		const preguntasNumericas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, '+
			't.nombre_tema as tema, m.aplicableArriba, m.aplicableAnbajo, rango ' +
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 2 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
		
		const preguntasAbiertas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 1 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
		
    const preguntaCalculadas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta,'+
			' b.tipo as tipo, t.nombre_tema as tema ,c.decimales, m.aplicableArriba, m.aplicableAnbajo, rango '+
      'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
      'INNER JOIN configuracion_preguntas_calculadas c on c.id_pregunta = b.id ' +
      'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 5 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
    
    const preguntaCalculadasMultiples = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta,'+
			' b.tipo as tipo, t.nombre_tema as tema ,c.decimales '+
      'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
      'INNER JOIN configuracion_preguntas_calculadas c on c.id_pregunta = b.id ' +
 			'WHERE b.tipo = 6 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
    
    const preguntaExpresiones = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.descripcion as descripcion,b.pregunta as pregunta, b.tipo as tipo, '+
			't.nombre_tema as tema, m.aplicableArriba, m.aplicableAnbajo, rango ' +
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 7 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + max_preg_conf)
		
		var banco_preguntas = [];var banqui_pregunta =[];
		banqui_pregunta = banqui_pregunta.concat(preguntasBoleanas[0]);
		banqui_pregunta = banqui_pregunta.concat(preguntasMultiples[0]);
		banqui_pregunta = banqui_pregunta.concat(preguntasNumericas[0]);
		banqui_pregunta = banqui_pregunta.concat(preguntasAbiertas[0]);
		banqui_pregunta = banqui_pregunta.concat(preguntaCalculadas[0]);
    banqui_pregunta = banqui_pregunta.concat(preguntaCalculadasMultiples[0]);
    banqui_pregunta = banqui_pregunta.concat(preguntaExpresiones[0]);


		banqui_pregunta.sort(() => Math.random() - 0.5);
       banco_preguntas = banqui_pregunta.slice(0,max_preg_conf);
      /*for(var i=0 ;i <= max_preg_conf; i=i+1){
		  banco_preguntas.concat(banqui_pregunta[i])
      }*/
		return response.json({banco_preguntas:banco_preguntas})
  }
  }

  
  async getPreguntas(response,params){
    let temas  = params.tema;
      for(const tema of temas){
const configuraciones = await Database.raw('SELECT  * FROM configuracion_cuestionarios');
		
		const preguntasMultiples = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 4 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_multiples)
		
		const preguntasBoleanas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 3 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_boleanas)
		
		const preguntasNumericas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, '+
			't.nombre_tema as tema, m.aplicableArriba, m.aplicableAnbajo, rango ' +
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 2 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_numericas)
		
		const preguntasAbiertas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta, b.tipo as tipo, t.nombre_tema as tema '+
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'WHERE b.tipo = 1 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_abiertas)
		
    const preguntaCalculadas = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta,'+
			' b.tipo as tipo, t.nombre_tema as tema ,c.decimales, m.aplicableArriba, m.aplicableAnbajo, rango '+
      'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
      'INNER JOIN configuracion_preguntas_calculadas c on c.id_pregunta = b.id ' +
      'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 5 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_calculadas)
    
    const preguntaCalculadasMultiples = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.pregunta as pregunta,'+
			' b.tipo as tipo, t.nombre_tema as tema ,c.decimales '+
      'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
      'INNER JOIN configuracion_preguntas_calculadas c on c.id_pregunta = b.id ' +
 			'WHERE b.tipo = 6 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_calculadas_multiples)
    
    const preguntaExpresiones = await Database.raw(
			'SELECT b.id as id_pregunta, b.id_tema as id_tema, b.descripcion as descripcion,b.pregunta as pregunta, b.tipo as tipo, '+
			't.nombre_tema as tema, m.aplicableArriba, m.aplicableAnbajo, rango ' +
			'FROM banco_preguntas b ' +
			'INNER JOIN temas t on t.id = b.id_tema ' +
			'INNER JOIN margen_errors m on m.id_pregunta =  b.id ' +
			'WHERE b.tipo = 7 AND b.id_tema = '+ tema.tema + 
			' ORDER BY RAND() ' +
			'LIMIT ' + configuraciones[0][0].num_preguntas_expresion)
		
		var banco_preguntas = [];
		banco_preguntas = banco_preguntas.concat(preguntasBoleanas[0]);
		banco_preguntas = banco_preguntas.concat(preguntasMultiples[0]);
		banco_preguntas = banco_preguntas.concat(preguntasNumericas[0]);
		banco_preguntas = banco_preguntas.concat(preguntasAbiertas[0]);
		banco_preguntas = banco_preguntas.concat(preguntaCalculadas[0]);
    banco_preguntas = banco_preguntas.concat(preguntaCalculadasMultiples[0]);
    banco_preguntas = banco_preguntas.concat(preguntaExpresiones[0]);


		banco_preguntas.sort(() => Math.random() - 0.5);
		
	
		return response.json({banco_preguntas:banco_preguntas})
    }
}
}

module.exports = EvaluacionController
