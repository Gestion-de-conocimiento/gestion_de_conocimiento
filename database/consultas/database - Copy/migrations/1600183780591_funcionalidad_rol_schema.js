'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class FuncionalidadRolSchema extends Schema {
  up () {
    this.create('funcionalidad_rol', (table) => {
      table.increments()
      table.integer('id_rol').unsigned().references('id').inTable('rols')
      table.integer('id_funcionalidad').unsigned().references('id').inTable('funcionalidad').onDelete('CASCADE').onUpdate('CASCADE')
      table.integer('estado')
    })
  }

  down () {
    this.drop('funcionalidad_rol')
  }
}

module.exports = FuncionalidadRolSchema
