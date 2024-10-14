'use strict'

/*
|--------------------------------------------------------------------------
| RolSeeder
|--------------------------------------------------------------------------
|
| Make use of the Factory instance to seed database with dummy data or
| make use of Lucid models directly.
|
*/

/** @type {import('@adonisjs/lucid/src/Factory')} */
const Factory = use('Factory')
const Database = use('Database') 
const Hash = use('Hash')
class RolSeeder {
  async run () {
		 //const users = await Database.table('rols') console.log(rols)	
		//const user = await Factory.model('App/Models/Rol') .create({ tipo_rol: 'admin' })
		const Administrador = await Database.from('rols').insert([{tipo_rol: 'Administrador'}])		
		const Experto = await Database.from('rols').insert([{tipo_rol: 'Experto'}])
		const Maestro = await Database.from('rols').insert([{tipo_rol: 'Maestro'}])
		const Alumno = await Database.from('rols').insert([{tipo_rol: 'Alumno'}])

		const u1= await Database.from('users').insert([{nombre: 'Juan Diego',
																									 apellido_paterno: 'Lumbreras',
																									apellido_materno: 'Vega',
																									matricula: '1530334',
																									password:await Hash.make('123'),
																									nivel_academico:'2',
																									id_rol: '1'}])
			const u2= await Database.from('users').insert([{nombre: 'Eduardo',
																									 apellido_paterno: 'Apellido Pat',
																									apellido_materno: 'Apellido mat',
																									matricula: '1630031',
																									password:await Hash.make('123'),
																									nivel_academico:'2',
																									id_rol: '2'}])
			const u3= await Database.from('users').insert([{nombre: 'Victor',
																									 apellido_paterno: 'Apellido Pat',
																									apellido_materno: 'Apellido mat',
																									matricula: '123',
																									password:await Hash.make('123'),
																									nivel_academico:'2',
																									id_rol: '3'}])	
			
			
			
			const u4 = await Database.from('users').insert([{nombre: 'Froylan',
															apellido_paterno: 'Wbario',
															apellido_materno: 'Martinez',
															matricula: '1530006',
															password:await Hash.make('123'),
															nivel_academico:'2',
															id_rol: '1'}])	
		
	
		//await Database.raw('DROP TRIGGER IF EXISTS TEMA_AD')
		//await Database.raw('CREATE TRIGGER TEMA_AD AFTER DELETE ON temas FOR EACH ROW DELETE FROM relacion_primarias WHERE relacion_primarias.id_hijo=OLD.id')
		//await Database.raw('DROP TRIGGER IF EXISTS RELACION_TEMA_AD')
		//await Database.raw('CREATE TRIGGER RELACION_TEMA_AD AFTER DELETE ON relacion_primarias FOR EACH ROW DELETE FROM temas WHERE temas.id=OLD.id_hijo;')


		await Database.from('temas').insert([{
			'nombre_tema':'Matematicas',
			'nivel':0,
			'freex': 100,
			'freey': 30
		}])
		
		await Database.from('configuracion_cuestionarios').insert([{                 
 			'ponde_estricta':1,           
 			'num_preguntas':0,            
 			'num_preguntas_abiertas':0,   
 			'num_preguntas_boleanas':0,   
 			'num_preguntas_multiples':0,  
 			'num_preguntas_calculadas':0,
 			'num_preguntas_numericas':0,  
 			'rango_por_defecto':0.01  
		}])
  }
}


module.exports = RolSeeder

