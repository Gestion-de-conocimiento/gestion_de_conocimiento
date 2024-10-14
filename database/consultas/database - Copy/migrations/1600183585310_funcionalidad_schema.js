'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class FuncionalidadSchema extends Schema {
  up () {
    this.create('funcionalidad', (table) => {
      	table.increments()
      	table.string('nombre',80)
      	table.string('descripcion', 80)
				table.integer('id_grupo').unsigned().references('id').inTable('grupo_funcionalidad').onDelete('CASCADE').onUpdate('CASCADE')
    })
  }

  down () {
    this.drop('funcionalidad')
  }
}

module.exports = FuncionalidadSchema
