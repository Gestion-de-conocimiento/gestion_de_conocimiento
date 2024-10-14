'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class CptsSchema extends Schema {
  up () {
    this.create('cpts', (table) => {
      table.increments()
      //table.timestamps()
      table.integer('id_hijo').unsigned().references('id').inTable('temas')
      table.text('estado')
      table.text('id_padres')
      table.text('estados_padres')
      table.text('probabilidad')
      
      //table.string('nombre',80)
      //table.string('alias',100)
      
    })
  }

  down () {
    this.drop('cpts')
  }
}

module.exports = CptsSchema
