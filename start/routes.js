
/** @type {typeof import('@adonisjs/framework/src/Route/Manager')}*/
const Route = use('Route')     
const User = use('App/Models/User')
const Tema = use('App/Models/Tema')
const Helpers = use('Helpers')
const Database = use('Database')
const Hash = use('Hash')


Route.get('/preguntas/nodo','PreguntaController.preguntanodo')

Route.get('/saludar', 'SaludarController.metodoSaludar')


Route.post('/wolfram-query', 'WolframController.query')



//------------------------------------Correr Actualizar nodos--------------------------------------------------------------
Route.post("/ejecutar-script-python", "CuestionarioController.ejecutarScriptPython").middleware("auth");

//----------------------------------------------------------------------------------------------


//---------------------Rutas para la interfaz general del módulo de enseñanza--------------------$
// Ruta para ejecutar script Python con la matrícula del usuario
Route.post('/api/ejecutar-evaluacion', 'EvaluacionController2.ejecutarEvaluacion').middleware(['auth'])
Route.post('/api/temas-no-dominados/:id/marcar-revisado', 'VistaGeneralCont.marcarRevisado').middleware(['auth']);
Route.post('/api/temas-no-dominados/reset-progreso', 'VistaGeneralCont.resetProgreso').middleware(['auth']);
Route.get('/api/temas-no-dominados/:ids', 'VistaGeneralCont.getTemas').middleware(['auth']);




Route.get('/arbol',({view})=> view.render('arbol'))
Route.post('tema/cambiarPadre/:id','TemaController.cambiarPadre')
Route.post('tema/hacerHijoPadre/:id','TemaController.hacerHijoPadre')
Route.get('temas/arbol','TemaController.arbol')
Route.get('temas/:id','TemaController.show')
Route.post('tema/posicion','TemaController.posicion') 
Route.post('pregunta/add','PreguntaController.store')
Route.post('pregunta/addNumerica','PreguntaController.storeNumerica')
Route.post('pregunta/delete','PreguntaController.delete')
Route.get('configuracionCuestionario/margen','ConfiguracionController.cargarMargen')
Route.get('pregunta/show','PreguntaController.showall')
Route.post('tema/addsecundario','TemaController.registrar_secundario')
Route.post('tema/deleteNodoSecundario','TemaController.deleteNodoSecundarioRelation')
Route.post('alumno/add','UserController.realumno')
Route.get('alumno/show','UserController.alumnos')
Route.post('alumno/actualizar','UserController.actualizarA')
Route.get('alumno/showp','UserController.alumnosP')
Route.get('show/profesor','UserController.profesor')
Route.get('show/experto','UserController.experto')
Route.post('user/delete','UserController.delete')
Route.post('user/deleteExperto','UserController.deleteExperto')
Route.post('user/delete2','UserController.deletealumno')
Route.post('user/delete3','UserController.deleteprofesor')
Route.post('registrar','UserController.registrar')
Route.get('admin/show','UserController.admins')
Route.post('user/actualizar','UserController.actualizar')
Route.post('app/pregunta/add','PreguntaController.store')//
Route.post('app/preguntaOpcionMultiple/store','PreguntaController.storeMultiple')
Route.post('app/preguntaOpcionMultiple/update','PreguntaController.updateMultiple')
Route.get('app/pregunta/showMultiples','PreguntaController.mostrarPreguntasOpcionMultiple')
Route.get('/temas/posiblesNodosPadres/:id', 'TemaController.posiblesNodosPadres')
Route.get('/temas/obtenerPadres/:id', 'TemaController.obtenerPadres')
Route.get('/temas/obtenerPadresConNombre/:id', 'TemaController.obtenerPadresConNombre')
Route.get('/tema/relacionesPrimarias','TemaController.verrelacion')
Route.post('tema/addTema','TemaController.registrar');
Route.post('tema/actualizarColor','TemaController.actualizarColor')
Route.get('/tema/obtenerRadio','TemaController.obtenerRadio')
Route.post('tema/actualizarRadio/:radio', 'TemaController.actualizarRadio')
Route.get('/user/obtenerAlumnos','TemaController.obtenerAlumnos')
Route.get('/user/obtenerArbol/:id','TemaController.obtenerArbol')
Route.get('/obtenerConexiones/:id','TemaController.obtenerConexiones')
Route.get('/perfil', ({view}) =>  view.render('app'))
Route.get('/alumno/app', ({view})=> view.render('app') );
Route.get('/experto/app', ({view})=> view.render('app') );
Route.get('/profesor/app', ({view})=> view.render('app') );
Route.get('/pruebaimagenes', ({view})=> view.render('app') );
Route.get('pregunta/showCalculadas','PreguntaController.mostrarPreguntasCalculadas')
Route.get('/preguntasCalculadas', ({view})=> view.render('app') );
Route.post('/preguntaCalculada/store','PreguntaController.storeCalculada')
Route.post('/preguntaCalculada/delete','PreguntaController.deleteCalculadas')
Route.post('pregunta/getComodines','PreguntaController.getComodines')
Route.post('/preguntaCalculada/update','PreguntaController.updateCalculadas')
Route.get('pregunta/showVcomodines','PreguntaController.valorcomodin')
Route.get('preguntasOpcionMultipleCalculadas', ({view}) => view.render('app'))
Route.get('pregunta/showMultiplesCalculadas','PreguntaController.mostrarPreguntasOpcionMultipleCalculadas')
Route.post('preguntaOpcionMultipleCalculadas/store','PreguntaController.storeMultipleCalculadas')
Route.post('preguntaOpcionMultipleCalculadas/update','PreguntaController.updateMultipleCalculadas')
Route.post('preguntaOpcionMultipleCalculadas/delete', 'PreguntaController.deleteCalculadasMultiples')
Route.get('/pregunta/opciones/:id', 'PreguntaController.obtenerOpciones');
Route.get('/pregunta/opcionescalculadasmultiples/:id', 'PreguntaController.obtenerOpcionesCalculadaMultiple');
Route.get('/pregunta/respuestas/:id', 'PreguntaController.obtenerRespuestas');
Route.post('pregunta/add','PreguntaController.store')//
Route.post('pregunta/addNumerica','PreguntaController.storeNumerica') //
Route.get('questions/checkQuestionnaireStart','PreguntaController.checkQuestionnaireStart')
Route.get('/', 'UserController.checklogin')
Route.post('login','UserController.login')
Route.get('logout','UserController.logout')
Route.get('/saludame/:nombre/:edad', 'SaludarController.metodoSaludar');
Route.get('/pruebapython', 'PonderacionController.pruebaPython');
Route.get('temas/count','TemaController.temacount')

Route.get('/grafo', ({view}) =>  view.render('app') );
Route.get('/contacto', ({view}) =>  view.render('app')  );
Route.get('/grafoalumnos', ({view}) => view.render('app') );

Route.get('/arbol/obtenerCaminos/:id', 'PonderacionController.getPaths');

Route.get('/mdp/caminos/:id/:saltos', 'PonderacionController.obtenerCaminosPonderacion');

Route.get('/mdp/caminos/dificultad', 'TemaController.obtenerDificultadTemas');


Route.get('/arbol/obtenerResultados', 'PonderacionController.getResults');
Route.get('/arbol/obtenerRamas', 'PonderacionController.obtener_ramas');
Route.get('/imagen/pregunta/:id', 'PreguntaController.obtenerImagenesPregunta')
Route.get('/obtenercpts/:idhijo/:idpadres', 'CptController.obtenerCpts');
Route.get('/obtenerTodasLasImagenes', 'PreguntaController.obtenerTodasImagenes');
Route.get('/obtenerDatos', 'UserController.obtenerDatos');
Route.post('/verificarExistencia', 'UserController.verificarExistencia');
Route.get('/arbol/caminos', 'PonderacionController.obtener_caminos')
Route.get('/arbol/simulador/caminos', 'PonderacionController.obtener_caminos_simulador')

Route.get('/arbol/caminoslibreria', 'PonderacionController.obtener_caminos_red_bayesiana')


Route.get('/arbol/caminosmodulo/:matricula/:rbm', 'PonderacionController.obtener_caminos_modulo')
Route.get('/obtenerTema/:matricula/:rbm/:saltos/:tema/:ponderacion', 'PonderacionController.obtener_tema')
Route.get('/obtenerPonderaciones/:matricula', 'PonderacionController.obtener_ponderaciones')



//Ruta para acceder al nuevo componente

Route.get('/ejemplo', ({view}) =>  view.render('app') );
//Se envia matrícula para la lectura del pickle
Route.get('/obtenerMatricula/:matricula','AprenderController.obtener_matricula')
//Route.get('/ObtenerMatricula/:matricula','CuestionarioController.Obtener_matricula')

Route.get('/Matricula/:matricula','EvaluacionController.obtener_matricula')
Route.get('/reactivos/:rama/:tema', 'EvaluacionController.obtenerReactivosPorRama');
Route.get('/temas-preguntas/:rama_id', 'EvaluacionController.obtenerTemasYPreguntasAleatorias');

//----------------------------------------------------------------------------------------------

Route.post('/temas/guardarProbabilidades', 'TemaController.storeProbabilidades');
Route.get('/obtenerEvidencias', 'TemaController.obtenerEvidencias')
Route.get('/obtenerTotalTemas', 'TemaController.obtenerTotalNodos')
Route.get('/preguntas/obtenerNumeroRespuestas/:id', 'PreguntaController.obtenerNumeroRespuestas');
Route.post('/preguntasCalculadas/delete', 'PreguntaController.preguntasCalculadasDelete');
Route.post('/subirr', 'UserController.subirimagen');
Route.post('/subirr2', 'UserController.subirimagenes');
Route.get('/arbol/poderacionesNodos', 'PonderacionController.obtenerPoderacionesNodos')
Route.get('/arbol/obtenerRA', 'PonderacionController.obtenerRA')
Route.post('pregunta/addExpresiones','PreguntaController.storeExpresiones')
//Route.get('pregunta/addExpresiones', ({view}) =>  view.render('toolbar') );


Route.get('/subirimagen', async ({view}) =>{
	const images = await Database.table('imagenes');
	return view.render('subir_imagenes.edge', {imagenes:images})	
});

Route.get('images/all', async ({ request, response }) => {
	const images = await Database.table('imagenes');
	return response.json(images)
	
});

Route.post('upload', async ({ request, response }) => {
  const profilePic = request.file('profile_pic', {
    types: ['image'],
    size: '2mb'
  })
  const name_pic = request.input('alias');
   const type=request.file('profile_pic').subtype;
   const name= `${new Date().getTime()}.${type}`
  await profilePic.move('public/preguntas/', {
		name: name
  })
  await Database.insert({nombre: name, alias:name_pic}).into('imagenes')
  if (!profilePic.moved()) {
    return profilePic.error()
  }
  response.redirect('/subirImagen')
})

Route.post('editardatos', async ({ request, response, auth }) => {
  
	const nombre = request.input('nombre');
	const apaterno = request.input('apellidopaterno');
	const amaterno = request.input('apellidomaterno');
	
	const contrasena = await request.input('contrasena');
	const repcontrasena = await request.input('contrasena2');
	
	if(contrasena || repcontrasena){
	   
		if( contrasena == repcontrasena ){

		   const safePassword = await Hash.make(contrasena)

		   await Database.raw('UPDATE users SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, password = ? WHERE id = ?',[nombre, apaterno, amaterno, safePassword ,auth.user.id])

		   response.redirect('/perfil?e=1')

		}else{

			response.redirect('/perfil?e=2')
		}
		
		
	}else{
		await Database.raw('UPDATE users SET nombre = ?, apellido_paterno = ?, apellido_materno = ? WHERE id = ?',[nombre, apaterno, amaterno ,auth.user.id])
		response.redirect('/perfil?e=1')
	}
	
})

Route.post('subirfotoperfil', async ({ request, response, auth }) => {
  const profilePic = request.file('profile_pic', {
    types: ['image'],
    size: '2mb'
  })
   const type=request.file('profile_pic').subtype;
   const name= `${new Date().getTime()}.${type}`
  await profilePic.move('public/imagenes/fotosperfil', {
		name: name
  })
	
	await Database.raw('UPDATE users SET foto = ? WHERE id = ?',[name, auth.user.id])
	
  if (!profilePic.moved()) {
    return profilePic.error()
  }
  response.redirect('/perfil')
})


// TODO ESTO ES UN TIPO DE FUNCIONALIDAD
Route.group(()=>{
	Route.get('/cuestionario', ({view})=> view.render('app') );
  
  
  // Obtiene las preguntas que son desplegadas en el cuestionario
	Route.get('/pregunta/showPreguntas/:id','PreguntaController.showPreguntas');
  
  // Obtiene la información de una pregunta
  Route.post('/showUnicaPregunta','PreguntaController.mostrarUnicaPregunta');
  
  
	Route.get('/cuestionario/obtenerconfiguracion','PreguntaController.obtenerconfiguracion');
	Route.get('/topic/getopic/:id','BayeController.NextTopic');
	Route.post('/score/add','PreguntaController.addScore');
  
}).middleware(['AccessValidator:1']);

//Rutas generales 
Route.group(()=>{
	Route.any('/tablero', 'AccesosRutaController.pasarSession')		
	Route.get('/usuario/geter','UserController.usuarioTipo')
	Route.get('/accesos/configuracion', ({view}) =>  view.render('app'));
	Route.get('/accesos/:id','AccesosRutaController.obtenerAccesosRol')
	Route.post('/guardarAccesoRutas', 'AccesosRutaController.guardarconfiguracion');
  Route.get('/recursosvistaespecial/mostrarrecursosvistaespecial', 'ControladorRecursosEnsenanza.mostrarTemasPorRama')
  
 
  
}).middleware(['VerificadorAuthRole:1,2,3,4'])

//Rutas de Administrador, Experto, Profesor
Route.group(()=>{
	Route.get('/pregunta/showPN','PreguntaController.showPreguntasNumericas')
 	Route.get('/pregunta/showPE','PreguntaController.showPreguntasExpresiones')
	Route.get('/pregunta/showPAB','PreguntaController.showPreguntasAbiertas')
  Route.get('/recurso/mostrarrecurso','controladorTema.mostrarRecursos')
  //__________________________Mostrar temas por rama en el módulo de enseñanza______________________________
  Route.get('/recurso/mostrarTemasPorRama', 'ControladorRecursosEnsenanza.mostrarTemasPorRama');
 
  //______________________________________________________________________________
	Route.get('/preguntasNumericas', ({view}) =>  view.render('app'))
}).middleware(['VerificadorAuthRole:1,2,3]'])

Route.group(()=>{
	Route.post('tema/addTema','TemaController.registrar')
}).middleware(['VerificadorAuthRole:1,2]'])

//Grupo de solo los temas (nodos)
Route.group(()=>{
	Route.post('tema/deleteTema1/:id','TemaController.deleteTemaAndHijos')
	Route.post('tema/deleteandcambiarPadre/:id','TemaController.deleteandcambiarPadre')//
	Route.post('tema/deleteTema','TemaController.deleteTemaAndHijos')
	Route.get('tema/all','TemaController.mostrarTemasConRelaciones')
	Route.get('tema/preguntas','TemaController.mostrarPreguntasPorTema')
	Route.get('tema/showTemasOnlyNombreID','TemaController.showTemasOnlyNombreID')
	Route.post('tema/addTema','TemaController.registrar') //
	Route.post('tema/editarNodo/:id','TemaController.editarNodo')//
	Route.get('tema/deleteTema','TemaController.deleteTemaAndHijos')
	Route.post('tema/deleteandcambiarPadre/:id','TemaController.deleteandcambiarPadre')
	Route.post('tema/editarNodo','TemaController.editarNodo') 
	Route.get('tema/relacionesPrimarias','TemaController.verrelacion')	
	Route.get('/historialexperto','AccesosRutaController.AbirArbol')
  Route.get('tema/temas','controladorTema.mostrarTemas')
  Route.post('ejercicio/anadir','controladorTema.agregarEjercicioUrl')
  Route.post('recurso/actualizarRecurso','controladorTema.updateRecurso')
	Route.get('temas',({view})=> view.render('app'))
}).middleware(['AccessValidator:2'])

Route.group(()=>{
	Route.get('profesor/count','UserController.profesorcount')
	Route.get('alumno/count','UserController.alumnocount')
	Route.get('admin/count','UserController.adminscount')
	Route.get('experto/count','UserController.expertocount')
	Route.get('pregunta/count','PreguntaController.preguntacount')
	Route.get('/temascount','TemaController.temacount')
	Route.get('/usuariosAdministrador', ({view}) =>  view.render('app'))
	Route.get('/usuariosAlumno', ({view}) =>  view.render('app'))
	Route.get('/usuariosExperto', ({view}) =>  view.render('app'))
	Route.get('/usuariosProfesor', ({view}) =>  view.render('app'))
	Route.get('/configurarCuestionario', ({view})=> view.render('app') );
  
  // 01/07/2022
  Route.get('/configuracion/modulo', ({view})=> view.render('app') );
  
  
	Route.get('/preguntasAbiertas', ({view}) =>  view.render('app'))
	Route.get('preguntasNumericas', ({view}) =>  view.render('app'))
	Route.get('preguntasVerdaderoFalso', ({view}) =>  view.render('app'))
	Route.get('preguntasOpcionMultiple', ({view}) => view.render('app'))
	Route.get('resolverCuestionario',({view}) => view.render('app'))
	Route.get('historial', ({view}) =>  view.render('app'))
	Route.get('temas',({view})=> view.render('app'))
	Route.post('app/pregunta/add','PreguntaController.store')//
	Route.post('app/preguntaOpcionMultiple/store','PreguntaController.storeMultiple')
	Route.post('app/preguntaOpcionMultiple/update','PreguntaController.updateMultiple')
	Route.get('pregunta/showMultiples','PreguntaController.mostrarPreguntasOpcionMultiple')
	Route.post('tema/addsecundario','TemaController.registrar_secundario')
	Route.post('tema/deleteNodoSecundario','TemaController.deleteNodoSecundarioRelation')
	Route.post('alumno/add','UserController.realumno')
	Route.get('alumno/show','UserController.alumnos')
	Route.post('alumno/actualizar','UserController.actualizarA')
	Route.get('alumno/showp','UserController.alumnosP')
	Route.get('show/profesor','UserController.profesor')
	Route.get('show/experto','UserController.experto')
	Route.post('user/delete2','UserController.deletealumno')
	Route.post('user/delete3','UserController.deleteprofesor')
	Route.post('registrar','UserController.registrar')
	Route.get('admin/show','UserController.admins')
	Route.post('user/actualizar','UserController.actualizar')
	Route.post('user/delete','UserController.delete')
	Route.get('app/nodos', ({view}) =>  view.render('app'))
	Route.get('app/preguntas/contestar', ({view}) =>  view.render('app'))
	Route.get('app/preguntas/nodo', ({view}) =>  view.render('app'))
	Route.post('tema/deleteandcambiarPadre/:id','TemaController.deleteandcambiarPadre')//
	Route.get('tema/editarNodo/:id:id2:nombre','TemaController.editarNodo')//
	Route.get('temas/arbol','TemaController.arbol')//
	Route.get('temas/:id','TemaController.show')//
	Route.post('pregunta/update','PreguntaController.updateAN')
	Route.post('pregunta/updateAbierta','PreguntaController.updateAbierta')
	Route.post('pregunta/updateExpresiones','PreguntaController.updateExpresiones')//para actualizar las preguntas expresiones (tipo 7)
	
  Route.post('pregunta/add','PreguntaController.store')//
	Route.post('preguntaOpcionMultiple/store','PreguntaController.storeMultiple')
	Route.post('preguntaOpcionMultiple/update','PreguntaController.updateMultiple')
	Route.get('/pregunta/showMultiples','PreguntaController.mostrarPreguntasOpcionMultiple')
	Route.post('pregunta/eliminar','PreguntaController.delete')
	Route.post('preguntaOpcionMultiple/update', 'PreguntaController.updateMultiple')	
	Route.post('app/pregunta/delete','PreguntaController.delete')//
	Route.get('tema/hijos/:id','TemaController.showTemasHijos')
	Route.get('tema/arbolu','TemaController.showausuario')
	Route.get('obtenerconfiguracion', 'ConfiguracionController.obtenerConfiguracionCuestionario');
	Route.get('obtenerTotalPorPregunta', 'ConfiguracionController.obtenerTotalPreguntas');
	Route.post('guardarconfiguracion', 'ConfiguracionController.guardarconfiguracion');
  
 
  Route.get('/obtenerrbs', 'CuestionarioController.obtenerrbs');
  Route.get('/obtenerConfiguracionRedBayesiana', 'ParametrosController.obtenerConfiguracion');
  
  Route.post('/guardarConfiguracionRB', 'ParametrosController.guardarconfiguracion');
  
  
}).middleware(['VerificadorAuthRole:1'])


Route.get('/obtenerPrimerTema/:matricula/:rbm', 'CuestionarioController.obtenerPrimerTema');

Route.get('/obtenerPrimerTema/:matricula/:rbm', 'CuestionarioController.obtenerPrimerTema');
Route.get('/obtenerResultadosTemaE/:matricula', 'EvaluacionController.obtenerResultadosTemas');
Route.get('/obtenerTemas/:matricula/:rama', 'EvaluacionController.obtener_Temas');
Route.get('/guardarEvaluacion/:matricula/:tema/:ponderacion/:grado', 'EvaluacionController.escribirDatos');
Route.get('/obtenerPreguntasA/:matricula/:rama/:tema', 'EvaluacionController.obtener_datos');
Route.get('/obtenerTemaE/:matricula/:rbm/:saltos/:tema/:ponderacion', 'PonderacionController.obtener_tema');
Route.get('/obtenerPonderacionesE/:matricula', 'EvaluacionController.obtener_ponderaciones');
Route.get('/arbol/caminosmoduloE/:matricula/:rbm', 'EvaluacionController.obtener_caminos_modulo');

Route.get('/recuperarPass', async ({view}) =>{
	return view.render('recuperarPass')	
});
Route.get('obtenerConfiguracionEvaluacion','ConfiguracionEvaluacionController.obtenerConfiguracionEvaluacion');
Route.get('/obtenerTotalPreguntasPorTema','ConfiguracionEvaluacionController.obtenerTotalPreguntasTema');
Route.get('/enviarCorreo', 'UserController.enviarCorreo');
Route.post('guardarconfiguracionEvaluacion', 'ConfiguracionEvaluacionController.guardarConfiguracionEvaluacion');
Route.get('/*', 'UserController.verificarLogin');

  // Se esta trabajando aqui para el módulo MOGRE
  //Route.get('/obtenerrbs', 'CuestionarioController.obtenerrbs');

//Route.get('/toolbar', ({view})=> view.render('toolbar'))
Route.get('/toolbar', async ({view}) =>{
	return view.render('toolbar')	
});