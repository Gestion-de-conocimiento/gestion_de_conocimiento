'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class RelacionNodoAlumnoSchema extends Schema {
  up () {
    this.create('relacion_nodo_alumnos', (table) => {
      	table.increments()
     	table.timestamps()
      	table.integer('id_alumno').unsigned().references('id').inTable('users').onDelete('CASCADE').onUpdate('CASCADE')
      	table.integer('id_tema').unsigned().references('id').inTable('temas').onDelete('CASCADE').onUpdate('CASCADE')
      	table.integer('ponderacion').unsigned()
      	table.integer('clasificacion').notNullable()
		table.string('historial',30).notNullable()
      
    })
  }

  down () {
    this.drop('relacion_nodo_alumnos')
  }
}

module.exports = RelacionNodoAlumnoSchema
