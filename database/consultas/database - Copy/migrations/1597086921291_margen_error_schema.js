'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class MargenErrorSchema extends Schema {
  up () {
    this.create('margen_errors', (table) => {
      table.increments()
      table.timestamps()
      table.integer('id_pregunta').unsigned().references('id').inTable('banco_preguntas').onDelete('CASCADE').onUpdate('CASCADE')
      table.boolean('aplicableArriba')
      table.boolean('aplicableAnbajo')
		  table.float('rango',20,10)
    })
  }

  down () {
    this.drop('margen_errors')
  }
}

module.exports = MargenErrorSchema
