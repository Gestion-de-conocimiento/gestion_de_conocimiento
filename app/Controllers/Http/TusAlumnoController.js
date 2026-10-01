'use strict'

const Database = use('Database');

class TusAlumnoController {
  async cambiar({ auth, request, response }) {
    const { id_alumno, estado } = request.only(['id_alumno', 'estado']);

    if (auth.user.id_rol !== 3) {
      return response.status(403).json({ message: 'No autorizado' });
    }

    const estadosValidos = ['pendiente', 'aprendiendo', 'evaluando', 'terminado'];
    if (!estadosValidos.includes(estado)) {
      return response.status(400).json({ message: 'Estado inválido' });
    }

    const alumno = await Database.from('users').where('id', id_alumno).first();
    if (!alumno || alumno.id_rol !== 4) {
      return response.status(404).json({ message: 'Alumno no encontrado' });
    }

    await Database
      .from('users')
      .where('id', id_alumno)
      .update({ estado_alumno: estado });

    return response.json({ message: `Estado actualizado a ${estado}` });
  }
  
  

  async listar({ auth, response }) {
    if (auth.user.id_rol !== 3) {
      return response.status(403).json({ message: 'No autorizado' });
    }

    const alumnos = await Database
.select(
  'u.id',
  'u.nombre',
  'u.apellido_paterno',
  'u.apellido_materno',
  'u.estado_alumno',
  'u.matricula',
  'u.periodo',
  'u.foto'
)
      .from('users as u')
      .innerJoin('relacion_profesors as rp', 'rp.id_alumno', 'u.id')
      .where('rp.id_profesor', auth.user.id);

    return response.json(alumnos);
  }
}



module.exports = TusAlumnoController;
