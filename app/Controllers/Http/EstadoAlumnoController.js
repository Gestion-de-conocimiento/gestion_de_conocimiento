'use strict'

const Database = use('Database');

class EstadoAlumnoController {
  async cambiar({ auth, response }) {
    try {
      const alumno = await auth.getUser();

      if (alumno.id_rol !== 4) {
        return response.status(403).json({ message: 'No autorizado' });
      }

      await Database
        .from('users')
        .where('id', alumno.id)
        .update({ estado_alumno: 'aprendiendo' });

      return response.json({ message: "Estado actualizado a 'aprendiendo'" });

    } catch (error) {
      console.error('❌ Error al actualizar estado:', error);
      return response.status(500).json({ error: 'Error interno del servidor' });
    }
  }
}

module.exports = EstadoAlumnoController;
