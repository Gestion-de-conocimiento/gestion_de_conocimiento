'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class ConfiguracionPreguntasCalculadasSchema extends Schema {
  up () {
    this.create('configuracion_preguntas_calculadas', (table) => {
      table.increments()
      table.integer('id_pregunta').unsigned().references('id').inTable('banco_preguntas').onDelete('CASCADE').onUpdate('CASCADE')
       table.integer('decimales')
      table.timestamps()
    })
  }

  down () {
    this.drop('configuracion_preguntas_calculadas')
  }
}

module.exports = ConfiguracionPreguntasCalculadasSchema
