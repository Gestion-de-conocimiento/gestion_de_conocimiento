'use strict'

const Database = use('Database')
const execSync = require('child_process').execSync;
const fs = require('fs');

class PonderacionController {
   
  async pruebaDeFuncionamiento(){
    return "Prueba"
  }
  
  async arrayEquals(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length !== b.length) return false;
    
    for (var i = 0; i < a.length; ++i) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  }
  
  //NODO OBJETIVO ID
  async getPaths({params,response, auth}){
    
    var i = 0;
    var j = 0;
    
    let temas = await Database.raw('select temas.id as id, temas.nombre_tema as nombre, temas.nivel as nivel, relacion_nodo_alumnos.ponderacion, relacion_nodo_alumnos.clasificacion, relacion_nodo_alumnos.historial from temas inner join relacion_nodo_alumnos on temas.id = relacion_nodo_alumnos.id_tema where id_alumno = ? order by nivel desc;', [auth.user.id]);
    temas = temas[0];
    const relaciones =  await Database.select('id_padre','id_hijo').from('relacion_primarias');

    let total_relaciones = relaciones.length;
    let total_temas = temas.length;
    var texto = "nodos\n";
    
    for(  i = 0; i <  total_temas; i++){
      if(i == total_temas-1){
         texto = texto +  temas[i].id;
      }else{
        texto = texto +  temas[i].id + ",";
      }
    }
    texto = texto + "\nrelaciones\n";
    for ( i = 0; i < total_relaciones; i++) {
      var padre = relaciones[i].id_padre;
      var hijo = relaciones[i].id_hijo;
      texto = texto + padre + "-" + hijo + "\n";
    }
    
    fs.writeFileSync('nodos', texto);
    
    const output = execSync('g++ dag.cpp -o dag', { encoding: 'utf-8' });  // the default is 'buffer'
    const caminos = execSync('./dag ' + total_temas, { encoding: 'utf-8' });
    
    var paths = JSON.parse(caminos);    
    var total_caminos = paths.caminos.length;
    var total = 0;
    var nodo;
    var nodo_objetivo = params.id;
    var nodo_objetivo_props = temas.find(element => element.id == nodo_objetivo )
    var caminos_arriba = [];
    var caminos_abajo = [];
    var nodos_arriba = [];
    var nodos_abajo = [];
	  
	  var caminos_promedio = [];
    
   for ( i = 0; i < total_caminos; i++) {
      var total_nodo_camino = paths.caminos[i].length; // Total de nodos por camino
      for ( j = 0; j < total_nodo_camino; j++) {
        if(paths.caminos[i][j] == nodo_objetivo){
			
			caminos_promedio.push( paths.caminos[i] );
			
			//caminos arriba
		  var hay_repetido = false;
		  for(var k = 0; k < caminos_arriba.length; k++){
			if( await this.arrayEquals(caminos_arriba[k], paths.caminos[i].slice(2, j) ) ){
			  hay_repetido = true;
			}
		  }
		  if(!hay_repetido){
			 caminos_arriba.push( paths.caminos[i].slice(2, j)  ); // Hacia arriba
		  }
			
			//caminos abajo
          hay_repetido = false;
          for( k = 0; k < caminos_abajo.length; k++){
            if( await this.arrayEquals(caminos_abajo[k], paths.caminos[i].slice(j+1, total_nodo_camino) ) ){
              hay_repetido = true;
            }
          }
          if(!hay_repetido){
             caminos_abajo.push( paths.caminos[i].slice(j+1, total_nodo_camino)  ); // Hacia arriba
          }
			
			
        }
      }
    } 
    
    //Ordenar caminos hacia arriba   
    for(i = 0; i < caminos_arriba.length; i++){
        total = 0;
        for( j = 0; j < caminos_arriba[i].length; j++){
            nodo = await temas.find(element => element.id == caminos_arriba[i][j]);
            //caminos_arriba[i][j] = nodo;
            var hay_repetido = false;
            for(var k = 0; k < nodos_arriba.length; k++){
              if( nodo.id == nodos_arriba[k].id ){
                 hay_repetido = true;
              }
            }
            if( !hay_repetido ){
               nodos_arriba.push(nodo);
            }
          
            if( nodo.clasificacion != 2 ){
               total = total + 1;
            }
        }
        caminos_arriba[i] = caminos_arriba[i].reverse(); // 
        total = total + (caminos_arriba[i].length * 100);
        var obj_total = {nodos: caminos_arriba[i], total:total};
        caminos_arriba[i] = obj_total;
    }
    let len = caminos_arriba.length-1;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (caminos_arriba[j].total > caminos_arriba[j + 1].total) {
                let tmp = caminos_arriba[j];
                caminos_arriba[j] = caminos_arriba[j + 1];
                caminos_arriba[j + 1] = tmp;
            }
        }
    }
    
    // Ordenar caminos hacia abajo
    for(i = 0; i < caminos_abajo.length; i++){
        total = 0;
        for( j = 0; j < caminos_abajo[i].length; j++){
            nodo = await temas.find(element => element.id == caminos_abajo[i][j]);
            var hay_repetido = false;
            for(var k = 0; k < nodos_abajo.length; k++){
              if( nodo.id == nodos_abajo[k].id ){
                 hay_repetido = true;
              }
            }
            if( !hay_repetido ){
               nodos_abajo.push(nodo);
            }
            if( nodo.clasificacion != 2 ){
               total = total + 1;
            }
        }
        total = total + (caminos_abajo[i].length * 100);
        caminos_abajo[i] = {nodos: caminos_abajo[i], total:total};
    }
    len = caminos_abajo.length-1;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (caminos_abajo[j].total > caminos_abajo[j + 1].total) {
                let tmp = caminos_abajo[j];
                caminos_abajo[j] = caminos_abajo[j + 1];
                caminos_abajo[j + 1] = tmp;
            }
        }
    }
    
    var conjunto_de_caminos = [];
    // Ponderacion de nodos hacia abajo
    for(i = 0; i < caminos_abajo.length; i++){
      var caminos2 = [];
      var nodo_objetivo_borde = false;
      var total_saltos = 3;
      for(j = 0; j < caminos_abajo[i].nodos.length; j++){
        var nodo_actual = nodos_abajo.findIndex(x => x.id == caminos_abajo[i].nodos[j]);
        if( j == 0 ){
           if( nodos_abajo[nodo_actual].clasificacion == 2){
             var ponderacion = ((nodo_objetivo_props.ponderacion * 0.5) + (nodos_abajo[nodo_actual].ponderacion * nodos_abajo[nodo_actual].historial ) ) / (Number(nodos_abajo[nodo_actual].historial) + 1);
             nodos_abajo[nodo_actual].ponderacion = Math.round(ponderacion*10)/10 ;
             nodos_abajo[nodo_actual].historial = Number(nodos_abajo[nodo_actual].historial) + 1;
           }else if( nodos_abajo[nodo_actual].clasificacion == 3 || nodos_abajo[nodo_actual].clasificacion == 4 ){
             nodos_abajo[nodo_actual].ponderacion =  Math.round(nodo_objetivo_props.ponderacion * 0.5 * 10)/10;
             nodos_abajo[nodo_actual].historial = Number(nodos_abajo[nodo_actual].historial) + 1;
             nodos_abajo[nodo_actual].clasificacion = 2;
           }else{
             nodos_abajo[nodo_actual].ponderacion = nodo_objetivo_props.ponderacion;
             nodos_abajo[nodo_actual].historial = Number(nodo_objetivo_props.historial);
			 total_saltos = total_saltos + 1;
           }
        }else if(j < total_saltos){
			
           var nodo_anterior = nodos_abajo.findIndex(x => x.id == caminos_abajo[i].nodos[j-1]);
          if( nodos_abajo[nodo_actual].clasificacion == 2){
             var ponderacion = ( (nodos_abajo[nodo_anterior].ponderacion * 0.5)  + (nodos_abajo[nodo_actual].ponderacion * nodos_abajo[nodo_actual].historial ) ) / ( Number(nodos_abajo[nodo_actual].historial) + 1);
             nodos_abajo[nodo_actual].ponderacion = Math.round(ponderacion * 10)/10;
             nodos_abajo[nodo_actual].historial = Number(nodos_abajo[nodo_actual].historial) + 1;
           }else if( nodos_abajo[nodo_actual].clasificacion == 3 || nodos_abajo[nodo_actual].clasificacion == 4 ){
             nodos_abajo[nodo_actual].ponderacion = Math.round(nodos_abajo[nodo_anterior].ponderacion * 0.5 * 10)/10;
             nodos_abajo[nodo_actual].historial = Number(nodos_abajo[nodo_actual].historial) + 1;
             nodos_abajo[nodo_actual].clasificacion = 2;
           }else{
              nodos_abajo[nodo_actual].ponderacion  = nodos_abajo[nodo_anterior].ponderacion;
              nodos_abajo[nodo_actual].historial    = Number(nodos_abajo[nodo_anterior].historial);
              total_saltos = total_saltos + 1;
           }
			
        }else{
          if( nodos_abajo[nodo_actual].clasificacion == 4 ){
              nodos_abajo[nodo_actual].ponderacion = 2;
              nodos_abajo[nodo_actual].clasificacion = 3;
          }
        }
      }
      conjunto_de_caminos.push(caminos2);
    }
    
    //CAMINOS HACIA ARRIBA
    for(i = 0; i < caminos_arriba.length; i++){
      for(j = 0; j < caminos_arriba[i].nodos.length; j++){
        var nodo_actual = nodos_arriba.findIndex(x => x.id == caminos_arriba[i].nodos[j]);
        if( j == 0 ){
			
           if( nodos_arriba[nodo_actual].clasificacion == 2){
			  var ponderacion_viene = nodo_objetivo_props.ponderacion * 1.25;
			   
			   if(ponderacion_viene > 100)
				  ponderacion_viene = 100;

             var ponderacion = ((ponderacion_viene) + (nodos_arriba[nodo_actual].ponderacion * nodos_arriba[nodo_actual].historial ) ) / (Number(nodos_arriba[nodo_actual].historial) + 1);
			 if(ponderacion > 100)
				 ponderacion = 100;
				   
             nodos_arriba[nodo_actual].ponderacion = Math.round(ponderacion*10)/10 ;
             nodos_arriba[nodo_actual].historial = Number(nodos_arriba[nodo_actual].historial)+1;  
		   }else if( nodos_arriba[nodo_actual].clasificacion == 4 ){
			 
			   var ponderacion_viene = nodo_objetivo_props.ponderacion * 1.25;
			   if( ponderacion_viene > 100 )
				   ponderacion_viene = 100;
			   
			 var ponderacion = Math.round(ponderacion_viene * 10)/10;
			 if(ponderacion > 100)
				 ponderacion = 100;
             nodos_arriba[nodo_actual].ponderacion = ponderacion;
             nodos_arriba[nodo_actual].historial = Number(nodos_arriba[nodo_actual].historial) + 1;
             nodos_arriba[nodo_actual].clasificacion = 2;
		   
		   }else{
             nodos_arriba[nodo_actual].ponderacion = nodo_objetivo_props.ponderacion;
             nodos_arriba[nodo_actual].historial = Number(nodo_objetivo_props.historial);
           }
			
        }else{
          var nodo_anterior = nodos_arriba.findIndex(x => x.id == caminos_arriba[i].nodos[j-1]);
          if( nodos_arriba[nodo_actual].clasificacion == 2){
			  
			  var ponderacion_viene = nodos_arriba[nodo_anterior].ponderacion * 1.25;
			  if(ponderacion_viene > 100)
				 ponderacion_viene = 100;

             var ponderacion = ( (ponderacion_viene)  + (nodos_arriba[nodo_actual].ponderacion * nodos_arriba[nodo_actual].historial ) ) / (Number(nodos_arriba[nodo_actual].historial) + 1);
			 if(ponderacion > 100)
				 ponderacion = 100;
             nodos_arriba[nodo_actual].ponderacion = Math.round(ponderacion * 10)/10;
             nodos_arriba[nodo_actual].historial = Number(nodos_arriba[nodo_actual].historial) + 1;
		  
		  }else if( nodos_arriba[nodo_actual].clasificacion == 4 ){
			  
			  var ponderacion_viene = nodos_arriba[nodo_anterior].ponderacion * 1.25;
			  if(ponderacion_viene > 100)
				 ponderacion_viene = 100;
				 
			 var ponderacion = Math.round(ponderacion_viene * 10)/10;  
			 if(ponderacion > 100)
				ponderacion = 100;
             nodos_arriba[nodo_actual].ponderacion = ponderacion;
             nodos_arriba[nodo_actual].historial = Number(nodos_arriba[nodo_actual].historial) + 1;
             nodos_arriba[nodo_actual].clasificacion = 2;
           
		  }else{
              nodos_arriba[nodo_actual].ponderacion  = nodos_arriba[nodo_anterior].ponderacion;
              nodos_arriba[nodo_actual].historial  = Number(nodos_arriba[nodo_anterior].historial);
           }
        }
      }
    }
    
    /*for(i=0; i < nodos_abajo.length; i++){
      if( nodos_abajo[i].clasificacion != 1){
         await Database.raw('update relacion_nodo_alumnos set ponderacion = ?, clasificacion = ?, historial = ? where id_tema = ? and id_alumno = ?;', [ nodos_abajo[i].ponderacion, nodos_abajo[i].clasificacion, nodos_abajo[i].historial, nodos_abajo[i].id, auth.user.id ])
      }
    }
    
    for(i=0; i < nodos_arriba.length; i++){
      if( nodos_arriba[i].clasificacion != 1){
         await Database.raw('update relacion_nodo_alumnos set ponderacion = ?, clasificacion = ?, historial = ? where id_tema = ? and id_alumno = ?;', [ nodos_arriba[i].ponderacion, nodos_arriba[i].clasificacion, nodos_arriba[i].historial, nodos_arriba[i].id, auth.user.id ])
      }
    }*/
    
    return response.json({nodos_abajo: nodos_abajo, nodos_arriba: nodos_arriba, nodo_objetivo:nodo_objetivo_props});
    //return response.json({arriba: caminos_arriba, abajo: caminos_abajo});
    //return response.json(conjunto_de_caminos);
	  
	  //return response.json(caminos_promedio);
  }
  
  
  async getResults({params,response,auth}){
	  let temas = await Database.raw('select DISTINCT temas.id as id, temas.nombre_tema as nombre, temas.nivel as nivel, relacion_nodo_alumnos.ponderacion, relacion_nodo_alumnos.clasificacion, relacion_nodo_alumnos.historial from temas inner join relacion_nodo_alumnos on temas.id = relacion_nodo_alumnos.id_tema where relacion_nodo_alumnos.id_alumno = ? and temas.nivel > 1 and relacion_nodo_alumnos.clasificacion != 4 order by nivel desc;', [auth.user.id]);
	  
	  return response.json(temas[0]);
  }
  
  async getScores(caminos){
    //TODO:
    // Ponderar nodos
    // Aplicar reglas del metodo de ponderacion
    // 
  }
	
	async obtener_caminos({response, auth}){
		var i = 0;
		var j = 0;

		let temas = await Database.raw('select temas.id as id, temas.nombre_tema as nombre, temas.nivel as nivel from temas order by nivel desc;');
		temas = temas[0];
		const relaciones =  await Database.select('id_padre','id_hijo').from('relacion_primarias');

		let total_relaciones = relaciones.length;
		let total_temas = temas.length;
		var texto = "nodos\n";

		for(  i = 0; i <  total_temas; i++){
		  if(i == total_temas-1){
			 texto = texto +  temas[i].id;
		  }else{
			texto = texto +  temas[i].id + ",";
		  }
		}
		texto = texto + "\nrelaciones\n";
		for ( i = 0; i < total_relaciones; i++) {
		  var padre = relaciones[i].id_padre;
		  var hijo = relaciones[i].id_hijo;
		  texto = texto + padre + "-" + hijo + "\n";
		}

		fs.writeFileSync('nodos', texto);

		var output = execSync('g++ dag.cpp -o dag', { encoding: 'utf-8' });  // the default is 'buffer'
		var caminos = execSync('./dag ' + total_temas, { encoding: 'utf-8' });
		
		
		
		var paths = JSON.parse(caminos);
		
		for(i=0; i < paths.caminos.length; i++){
			for(j=0; j < paths.caminos[i].length; j++){
				for( var k = 0; k <  total_temas; k++){
					if(temas[k].id == paths.caminos[i][j]){
					    paths.caminos[i][j] = {id:paths.caminos[i][j], nivel:temas[k].nivel}
						break;
					}
				}
			}
		}
		
		
	
		return response.json(paths);
		//return paths.caminos[0];
	}
	
	
	
	async obtener_caminos_simulador({response}){
		var i = 0;
		var j = 0;
		var k = 0;
		

		let temas = await Database.raw('select temas.id as id, temas.nombre_tema as nombre, temas.nivel as nivel from temas order by nivel desc;');
		temas = temas[0];
		const relaciones =  await Database.select('id_padre','id_hijo').from('relacion_primarias');

		let total_relaciones = relaciones.length;
		let total_temas = temas.length;
		var texto = "nodos\n";

		for(  i = 0; i <  total_temas; i++){
		  if(i == total_temas-1){
			 texto = texto +  temas[i].id;
		  }else{
			texto = texto +  temas[i].id + ",";
		  }
		}
		texto = texto + "\nrelaciones\n";
		for ( i = 0; i < total_relaciones; i++) {
		  var padre = relaciones[i].id_padre;
		  var hijo = relaciones[i].id_hijo;
		  texto = texto + padre + "-" + hijo + "\n";
		}

		fs.writeFileSync('nodos', texto);

		var output = execSync('g++ dag.cpp -o dag', { encoding: 'utf-8' });  // the default is 'buffer'
		var caminos = execSync('./dag ' + total_temas, { encoding: 'utf-8' });

		var paths = JSON.parse(caminos);
		
		var caminoss = paths.caminos//respuesta de servidor
		
		var caminos_primera_rama = []
		
		
		for(i=0;i<caminoss.length;i++){
			if( caminoss[i][1] == 2 ){
			   //caminos_primera_rama.push(caminoss[i]);
				caminos_primera_rama.push( caminoss[i].slice(2, caminoss[i].length) ); 
			}
		}
		
		
		
		//for(var i = 0; i < caminoss.length; i++){
		//	caminoss[i] = caminoss[i].slice(1, caminoss[i].length);
		//}
		
		var solo_arreglo = []
		for( j=0; j < caminos_primera_rama.length; j++){
			for( k=0; k < caminos_primera_rama[j].length; k ++){
				solo_arreglo.push(caminos_primera_rama[j][k]);
			}
		}
		
		let uniqueArray = solo_arreglo.filter((c, index) => {
			return solo_arreglo.indexOf(c) === index;
		});
		
		
		return response.json({caminos: caminos_primera_rama, nodos: uniqueArray, temas:temas });
	
	}
	
	
	
	async obtener_ramas({response, auth}){
		let ramas = await Database.raw('select id, nivel from temas where nivel = 1;');
		return response.json(ramas);
	}
  
}

module.exports = PonderacionController
