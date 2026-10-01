'use strict'

const Excel = require('exceljs')
const Hash = use('Hash')
const Helpers = use('Helpers')
const User = use('App/Models/User')
const Database = use('Database')

class ExcelController {
  /**
   * Descarga plantilla Excel con los campos requeridos
   */
  async descargarPlantillaAlumnos({ response }) {
    const workbook = new Excel.Workbook()
    const worksheet = workbook.addWorksheet('Alumnos')

    worksheet.addRow([
      'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Edad', 'Matrícula',
      'Género', 'Contraseña', 'Nivel Académico', 'Periodo', 'Profesor (correo o matrícula)'
    ])

    response.header(
      'Content-Type',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response.header('Content-Disposition', 'attachment; filename="Plantilla_Alumnos.xlsx"')

    await workbook.xlsx.write(response.response)
    return response
  }

  /**
   * Vista previa de alumnos desde Excel sin guardar aún
   */
  async previewAlumnosExcel({ request, response }) {
    const archivo = request.file('archivo', {
      types: ['application'],
      extnames: ['xlsx', 'xls'],
    })

    await archivo.move(Helpers.tmpPath(), {
      name: `preview_tmp_${Date.now()}.xlsx`,
      overwrite: true,
    })

    if (!archivo.moved()) {
      return response.status(400).send(archivo.error())
    }

    const workbook = new Excel.Workbook()
    await workbook.xlsx.readFile(archivo.filePath)
    const worksheet = workbook.getWorksheet(1)

    const previewData = []
    let existentes = 0
    let nuevos = 0

    for (let i = 2; i <= worksheet.rowCount; i++) {
      const fila = worksheet.getRow(i)
      const matricula = fila.getCell(5).value
      const existe = await User.findBy('matricula', matricula)
      if (existe) {
        existentes++
      } else {
        nuevos++
      }

      previewData.push({
        nombre: fila.getCell(1).value,
        apellido_paterno: fila.getCell(2).value,
        apellido_materno: fila.getCell(3).value,
        edad: fila.getCell(4).value,
        matricula: fila.getCell(5).value,
        genero: fila.getCell(6).value,
        contrasena: fila.getCell(7).value,
        nivel_academico: fila.getCell(8).value,
        periodo: fila.getCell(9).value,
        profesor: fila.getCell(10).value,
      })
    }

    return response.send({
      preview: previewData,
      existentes,
      nuevos,
    })
  }

  /**
   * Registra los alumnos desde el archivo Excel
   */
  async cargarAlumnosExcel({ request, response, auth }) {
    const archivo = request.file('archivo', {
      types: ['application'],
      extnames: ['xlsx', 'xls'],
    })

    await archivo.move(Helpers.tmpPath(), {
      name: `alumnos_tmp_${Date.now()}.xlsx`,
      overwrite: true,
    })

    if (!archivo.moved()) {
      return response.status(400).send(archivo.error())
    }

    const workbook = new Excel.Workbook()
    await workbook.xlsx.readFile(archivo.filePath)
    const worksheet = workbook.getWorksheet(1)

    const usuarioActual = await auth.getUser()
    const esProfesor = usuarioActual.id_rol === 3

    for (let i = 2; i <= worksheet.rowCount; i++) {
      const fila = worksheet.getRow(i)
      const matricula = fila.getCell(5).value

      const yaExiste = await User.findBy('matricula', matricula)
      if (yaExiste) continue

      const nuevoAlumno = await User.create({
        nombre: fila.getCell(1).value,
        apellido_paterno: fila.getCell(2).value,
        apellido_materno: fila.getCell(3).value,
        edad: fila.getCell(4).value,
        matricula: matricula,
        genero: fila.getCell(6).value,
        password: await Hash.make(fila.getCell(7).value),
        nivel_academico: fila.getCell(8).value,
        periodo: fila.getCell(9).value,
        id_rol: 4,
        estado_alumno: 'pendiente',
      })

      let idProfesor = null

      if (esProfesor) {
        idProfesor = usuarioActual.id
      } else {
        const profesorReferencia = fila.getCell(10).value
        if (profesorReferencia) {
          const profesor = await User
            .query()
            .where('id_rol', 3)
            .andWhere((builder) => {
              builder
                .where('correo', profesorReferencia)
                .orWhere('matricula', profesorReferencia)
            })
            .first()

          if (profesor) idProfesor = profesor.id
        }
      }

      if (idProfesor) {
        await Database.table('relacion_profesors').insert({
          user_id: nuevoAlumno.id,
          profesor_id: idProfesor,
        })
      }
    }

    return response.send({ mensaje: 'Alumnos registrados correctamente' })
  }
}

module.exports = ExcelController
