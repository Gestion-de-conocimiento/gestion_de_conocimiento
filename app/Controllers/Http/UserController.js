'use strict'
const ExcelJS = require('exceljs')
const fs = require('fs')
const Helpers = use('Helpers')

const User = use('App/Models/User')
const {validate}= use('Validator')
const Hash = use('Hash')
const Database = use('Database')


class UserController {
		async registrar({request,response}){
        const{nombre,apellido_paterno,apellido_materno,edad,matricula,genero,password,nivel_academico,periodo,id_rol} = request.only(
        [
            'nombre',
			'apellido_paterno',
			'apellido_materno',
      'edad',
			'matricula','password',
      'genero',
			'nivel_academico',
      'periodo',
			'id_rol'
        ]) 
        
        await User.create({
            nombre,
			apellido_paterno,
			apellido_materno,
      edad,
			matricula,
      genero,
			password,
			nivel_academico,
      periodo,      
			id_rol
        })
        return response.send({message:'El usuario ha sido creado'})
    }
	
	
	async checklogin({session, view ,request, response, auth}){
		

		
		try{
			if( auth.user.id_rol == 1){
			  	return response.redirect('/tablero')
			} else if (auth.user.id_rol == 2) {
				return response.redirect('/tablero')        
			} else if (auth.user.id_rol == 3) {
				return response.redirect('/tablero')
			} else if (auth.user.id_rol == 4) {
				return response.redirect('/tablero')        
			}
		   	//auth.user.id_rol;
			
		}catch(e){
		   return view.render('login');
		}
		
		

	}
  
async descargarPlantillaAlumnos({ response }) {
  const rutaPlantilla = Helpers.publicPath('Documentos/Plantilla_Alumnos.xlsx')
  return response.download(rutaPlantilla)
}

  
  
  
  
  async actualizarEstadoAlumno({ auth, response }) {
  const userId = auth.user.id;

  // Total de temas que existen
  const totalTemas = await Database.from('temas').count('* as total');

  // Total de temas que el alumno ha marcado como revisados
  const temasRevisados = await Database
    .from('usuario_tema_avance')
    .where('user_id', userId)
    .andWhere('revisado', 1)
    .count('* as revisados');

  // Lógica del estado
  let estado = 'pendiente';
  if (temasRevisados[0].revisados > 0) {
    estado = 'en_progreso';
  }
  if (temasRevisados[0].revisados == totalTemas[0].total) {
    estado = 'listo';
  }

  // Guardar el nuevo estado en la base de datos
  await Database
    .from('users')
    .where('id', userId)
    .update({ estado_alumno: estado });

  // Retornar mensaje
  return response.json({
    message: `Estado actualizado a: ${estado}`,
    estado
  });
}


  
  
  	async usuarioTipo({auth}){
		return auth.user.id_rol;
	}
	
	async login({session, request, response, auth}){
		
		//IMPLEMENTACION DE VALIDATOR
		const validator= await validate(request.all(), {
				matricula: 'required',
				password: 'required',
		});

		if(validator.fails()){
			session.withErrors(validator.messages()).flashExcept(['password']);
			return response.redirect('/?error=1');
		}

		///VALIDAR SI EL NOMBRE DEL USUARIO ES CORRECTO
		const userFound = await User.findBy('matricula', request.input('matricula'));
		
		const activeUser = await Database.from('users').where('matricula', request.input('matricula') ).where('eliminado', 0)
		
		//return response.json( activeUser )
		
		var estaActivo = true
		if (activeUser.length == 0 ) {
			estaActivo = false
		}
		
		if(!userFound ||  !estaActivo ){
			session.withErrors(validator.messages()).flashExcept(['matricula']);
			return response.redirect('/?error=2');
		}

		const {matricula, password} = request.only(['matricula','password'])

		//validadr si la contraseña es valida
		const user= await User.findBy('matricula',matricula)	
		const isSame = await Hash.verify(password, user.password); 

		if(!isSame){
			return response.redirect('/?error=2');
		}

		//codicionar el rol para asiganr la ruta correcta
		//                                             //

		await auth.login(user)
		
		// Obtencion de rutas 
		const funcionalidad_rol =	await Database 
		.select('id_rol', 'estado', 'id_funcionalidad')
		.from('funcionalidad_rol')
		.where('id_rol', auth.user.id_rol)
		.where('estado', '1');
		//.where( auth.user.id_rol = 'id_rol');

		session.put('prueba', funcionalidad_rol )
		
		return response.redirect('/')

	}
  
  async cargarAlumnosExcel({ request, response, auth }) {
  const archivo = request.file('archivo', {
    types: ['application'],
    extnames: ['xlsx']
  })

  if (!archivo) {
    return response.status(400).send({ error: 'Archivo no proporcionado' })
  }

  const nombre = `alumnos_${Date.now()}.xlsx`
  await archivo.move(Helpers.tmpPath(), { name: nombre })

  if (!archivo.moved()) {
    return response.status(500).send(archivo.error())
  }

  const workbook = new ExcelJS.Workbook()
  await workbook.xlsx.readFile(`${Helpers.tmpPath()}/${nombre}`)
  const hoja = workbook.getWorksheet(1)

  for (let i = 2; i <= hoja.rowCount; i++) {
    const fila = hoja.getRow(i)
    const [
      nombre, apellido_paterno, apellido_materno, edad, matricula,
      genero, password, nivel_academico, periodo, id_rol
    ] = fila.values.slice(1)

    const safePassword = await Hash.make(password)

    const [idInsertado] = await Database
      .insert({
        nombre, apellido_paterno, apellido_materno, edad, matricula,
        genero, password: safePassword, nivel_academico, periodo, id_rol
      })
      .into('users')

    // Puedes asumir que el usuario que los sube es un profesor
    await Database.insert({
      id_profesor: auth.user.id,
      id_alumno: idInsertado
    }).into('relacion_profesors')
  }

  return response.send({ message: 'Alumnos cargados correctamente' })
}
	
	async enviarCorreo({session, request, response, auth}){
		
 
	}
	
	
	async logout({session,response,auth}){
		await auth.logout();
		return response.redirect('/');
	}
	
	//traer todos los admin
		async admins({response}){
			const users = await Database.from('users').where('id_rol', 1)
			return response.json(users)
        }  
  
  	//traer todos los experto
		async experto({response}){
				const users = await Database.from('users').where('id_rol', 2)
        return response.json(users)
        }  
  
  	//traer todos los profesor
		async profesor({response}){
				const users = await Database.from('users').where('id_rol', 3)
        return response.json(users)
        }  
//traer todos los alumnos
		async alumnos({response}){
			
	const alumnos =	await Database 
  .select('u.nombre as nombre_alumno, u.id as id_alumnos, u.apellido_paterno as apellido_paterno, u.apellido_materno as apellido_materno,u.edad as edad,u.matricula as matricula,u.genero as genero, u.nivel_academico as nivel_academico,u.periodo as periodo,rp.id_profesor as id_profesor,u2.nombre as nombre_profesor,u2.apellido_paterno as apellido_profesor')
  .from('users as u')
  .innerJoin('relacion_profesors as rp', 'u.id', 'rp.id_alumno')
  .leftJoin('users as u2', 'u2.id', 'rp.id_profesor')
  
	  const alumno = await Database.
	  raw('SELECT u.eliminado as eliminado, u.nombre as nombre_alumno, u.id as id_alumnos, u.apellido_paterno as apellido_paterno, u.apellido_materno as apellido_materno,u.edad as edad,u.matricula as matricula,u.genero as genero, u.nivel_academico as nivel_academico,u.periodo as periodo,rp.id_profesor as id_profesor,u2.nombre as nombre_profesor,u2.apellido_paterno as apellido_profesor from users u inner join relacion_profesors rp on rp.id_alumno = u.id  left join users u2 on u2.id = rp.id_profesor')
        return response.json(alumno)
			
        }   
  async alumnosP({response}){
      
  const alumno = await Database.raw('SELECT u.nombre as nombre_alumno, u.id as id_alumnos, u.apellido_paterno as apellido_paterno, u.apellido_materno as apellido_materno,u.edad as edad,u.matricula as matricula,u.genero as genero, u.nivel_academico as nivel_academico,u.periodo as periodo,rp.id_profesor as id_profesor,u2.nombre as nombre_profesor,u2.apellido_paterno as apellido_profesor from users u inner join relacion_profesors rp on rp.id_alumno = u.id  left join users u2 on u2.id = rp.id_profesor WHERE rp.id_profesor = ?',[auth.user.id])
       
				  
       return response.json(alumno)
        } 
    
  async assingTree(id_alumno)	{
    const temas = await Database.raw('SELECT id, nivel FROM temas')
    
    for (var i = 0; i < temas[0].length; i++) {
      //const user = await Database.raw('INSERT INTO users(nombre,apellido_materno,apellido_paterno,matricula,nivel_academico,id_rol,password) VALUES(?,?,?,?,?,?,?)',[nombre,apellido_materno,apellido_paterno,matricula,nivel_academico,id_rol,safePassword])
      if(temas[0][i].nivel > 1)
        var tema_alumno = await Database.raw('INSERT INTO relacion_nodo_alumnos(id_alumno,id_tema,ponderacion,clasificacion,historial) VALUES(?,?,?,?,?)',[id_alumno,temas[0][i].id,"3","4","0"]);
      else
        var tema_alumno = await Database.raw('INSERT INTO relacion_nodo_alumnos(id_alumno,id_tema,ponderacion,clasificacion,historial) VALUES(?,?,?,?,?)',[id_alumno,temas[0][i].id,"3","6","0"]);
    }
  }
  
   //registro de alumno     
  async realumno({request,response}){
     const safePassword = await Hash.make(request.input('password'))
  
        const{nombre,nivel_academico,apellido_materno,edad,apellido_paterno,password,matricula,genero,periodo,id_profesor,id_rol} = request.only(
        [
            'nombre',
						'apellido_paterno',
						'apellido_materno',
            'edad',
						'matricula' ,
            'genero',
            'password',
						'nivel_academico',
            'periodo',
            'id_profesor',
						'id_rol'
          
        ]) 
        
     const user = await Database.raw('INSERT INTO users(nombre,apellido_materno,apellido_paterno,edad,matricula,genero,nivel_academico,periodo,id_rol,password) VALUES(?,?,?,?,?,?,?,?,?,?)',[nombre,apellido_materno,apellido_paterno,edad,matricula,genero,nivel_academico,periodo,id_rol,safePassword])
    // const damealumno = await Database.from('users').getMax('id').where('id_rol',id_rol) 
		 //const users = await Database.from('users').where('matricula', matricula)
		 const ids = await Database.select('id').from('users').where('matricula', matricula);
		 await Database.insert({id_profesor:id_profesor,id_alumno:ids[0].id}).into('relacion_profesors')
     //await Database.raw('INSERT INTO relacion_profesors(id_profesor,id_alumno) values(?,?)', [id_profesor,users.id])
    await this.assingTree(ids[0].id);
    
     return response.send({message:'El alumno ha sido creado'})
    }
  async info ({response}){
    	 const ids = await Database.select('id').from('users').where('matricula',1630031);
    return response.json(ids[0].id)
  }
  //eliminar usuario
  async deleteExperto({request,response}){
	  
	  const{id, estado} = request.only(
        [
          	'id',
			'estado'
        ])

		var estadoo;
		if(estado == 0 || estado == null){
			estadoo = 1;
		}else{
			estadoo = 0;
		}
	   
		await User
	  	.query()
	  	.where('id', id)
	  	.update({	eliminado:estadoo})
	
    return response.json({message:'Se ha eliminado el usuario'})
  }
  
  async delete({request,response}){
	  
	  const{id} = request.only(['id'])


    const user = await Database.raw('DELETE FROM users WHERE id = ?',[id])
     // const relacion = await Database.raw('DELETE FROM relacion_profesors WHERE id_profesor = ?',[id])
	
    return response.json({message:'Se ha eliminado el usuario'})
  }
  
  async deleteprofesor({request,response}){
   /* const{id} = request.only(
        [
          'id'
         
        ])*/
	
	const{id, estado} = request.only(
        [
          	'id',
			'estado'
        ])

		var estadoo;
		if(estado == 0){
			estadoo = 1;
		}else{
			estadoo = 0;
		}
	   
		await User
	  	.query()
	  	.where('id', id)
	  	.update({	eliminado:estadoo})
	

     //const user = await Database.raw('DELETE FROM users WHERE id = ?',[id])
     // const relacion = await Database.raw('DELETE FROM relacion_profesors WHERE id_profesor = ?',[id])
    return response.json({message:'Se ha eliminado el usuario'})
  }
	
   async deletealumno({request,response}){
	   
    	const{id, estado} = request.only(
        [
          	'id',
			'estado'
        ])

		var estadoo;
		if(estado == 0){
			estadoo = 1;
		}else{
			estadoo = 0;
		}
	   
		await User
	  	.query()
	  	.where('id', id)
	  	.update({	eliminado:estadoo})
	   
    //const user = await Database.raw('DELETE FROM users WHERE id = ?',[id])
    //const relacion = await Database.raw('DELETE FROM relacion_profesors WHERE id_alumno = ?',[id])
   
    return response.json({message:'Se ha eliminado el usuario'})
  }
  //usuario
  async actualizar({request,response}){
    
    let contrasena = request.input('password');
    
    
    const{id,nombre,apellido_paterno,apellido_materno,edad,password,matricula,genero,nivel_academico,periodo,id_rol}= request.only(
    [
        'id',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'password',
        'matricula',
        'genero',
        'nivel_academico',
        'periodo',
        'id_rol',

    ])  
    
    if(contrasena === "" || contrasena === null || contrasena === false || contrasena === undefined){
      
      await User
      .query()
      .where('id', id)
      .update({ nombre:nombre,apellido_paterno:apellido_paterno,apellido_materno:apellido_materno,edad:edad,matricula:matricula,genero:genero,nivel_academico:nivel_academico,periodo:periodo,id_rol:id_rol})
      
    }else{
      
      const safePassword = await Hash.make(request.input('password'));
      
      await User
      .query()
      .where('id', id)
      .update({ nombre:nombre,apellido_paterno:apellido_paterno,apellido_materno:apellido_materno,edad:edad,password:safePassword,matricula:matricula,genero:genero,nivel_academico:nivel_academico,periodo:periodo,id_rol:id_rol})
    
    }
    
    
 
    
    
   
    //return response.json({message:'Actualizado', })  
    
    return response.json({id,nombre,apellido_paterno,apellido_materno,edad,password,matricula,genero,nivel_academico,periodo,id_rol})
  }
  
   // actualizar usuario alumno
  async actualizarA({request,response}){
   
    const safePassword = await Hash.make(request.input('password'))
    
    const{id,nombre,nivel_academico,apellido_materno,apellido_paterno,edad,matricula,genero,periodo,password,id_profesor}= request.only(
        [
            'id',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'edad',
            'password',
            'matricula',
            'genero',
            'nivel_academico',
            'periodo',
            'id_profesor'
           
        ])  
 
    
   const update =  await Database.raw('UPDATE users SET nombre = ?,apellido_paterno = ?, apellido_materno = ?,edad = ?, password = ?, matricula = ?, genero = ?, nivel_academico = ?, periodo = ? WHERE id =  ? ',[nombre,apellido_paterno,apellido_materno,edad,safePassword,matricula,genero,nivel_academico,periodo,id])
  
   const update_relacion =  await Database.raw('UPDATE relacion_profesors SET id_profesor = ? WHERE id_alumno = ?', [id_profesor,id])
    return response.json({message:'Actualizado'})  
  }
  
  async alumnocount({response}){
        const user = await Database.raw('SELECT COUNT(id) as totalAlumnos FROM users WHERE id_rol = ?',[4])
        return response.json(user)
  }
    async profesorcount({response}){
         const user = await Database.raw('SELECT COUNT(id) as totalDocentes FROM users WHERE id_rol = ?',[3])
        return response.json(user)
  }
    async expertocount({response}){
           const user = await Database.raw('SELECT COUNT(id) as totalExpertos FROM users WHERE id_rol = ?',[2])
        return response.json(user)
  }
    async adminscount({response}){
         const user = await Database.raw('SELECT COUNT(id) as totalAdministradores FROM users WHERE id_rol = ?',[1])
        return response.json(user)
  }
	
	
	async obtenerDatos({response,auth}){
         const user = await Database.raw('SELECT * FROM users WHERE id = ?',[auth.user.id])
        return response.json(user)
  }
	
  async verificarExistencia({request,response}){
        const{correo}= request.only(['correo'])
        
         const user = await Database.raw('SELECT * FROM users WHERE matricula = ?',[correo])
        return response.json(user)
  }
  
	async subirimagen({request, response}){
		
		const profilePic = request.file('imagen', {
			types: ['image'],
			size: '2mb'
		})

		const nombreImagen = request.input('nombreImagen');
		const alias = request.input('alias');
		const idPregunta = request.input('idPregunta');
		let ultimoId = "";
		
		await profilePic.move('public/imagenes/preguntas', {
			name: nombreImagen
		})
		
		ultimoId = await Database.insert({nombre: nombreImagen, alias:alias}).into('imagenes');
		await Database.insert({id_pregunta : idPregunta, id_imagen :ultimoId}).into('pregunta_imagen');
		if (!profilePic.moved()) {
			return profilePic.error()
		}
		
		response.redirect('/pruebaimagenes')
		
	}
	
	
	async verificarExistencia({request,response}){
        const{correo}= request.only(['correo'])
        
         const user = await Database.raw('SELECT * FROM users WHERE matricula = ?',[correo])
        return response.json(user)
  }
	
	async verificarLogin({view, auth, response}){
		
		if( auth.user ){
			 return view.render('app');
		}else{
			
			return response.redirect('/');
		}
		
	}  

	async subirimagenes({request, response}){
		
		const profilePic = request.file('imagen', {
			types: ['image'],
			size: '2mb'
		})
		
		console.log(profilePic);
		
		const nombreImagen = request.input('nombreImagen');
		const alias = request.input('alias');
		await profilePic.move('public/imagenes/preguntas/', {
			name: nombreImagen
		})
		
		await Database.insert({nombre: nombreImagen, alias:alias}).into('imagenes');
		if (!profilePic.moved()) {
			return profilePic.error()
		}
		
		response.redirect('/subirImagenes')
		
	}
	
	
}

module.exports = UserController
