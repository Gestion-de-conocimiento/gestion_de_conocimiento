'use strict';

const Database = use('Database');

class VistaGeneralCont {
  
  async getTemas({ params, auth, response }) {
  try {
    const userId = auth.user.id;
    const ids = params.ids.split(','); // Convertir el string en un arreglo de IDs

    console.log('IDs de temas a consultar:', ids); // Log para verificar los IDs recibidos

    // Obtener los temas filtrados por los IDs
    const temas = await Database
      .select('t.id_tema', 't.nombre_tema_ordenado', 't.url', 'a.revisado') // Cambiar 't.id_auto' a 't.id_tema'
      .from('temas_orden_ensenanza as t')
      .leftJoin('usuario_tema_avance as a', function() {
        this.on('t.id_tema', 'a.tema_id').on('a.user_id', userId); // Cambiar 't.id_auto' a 't.id_tema'
      })
      .whereIn('t.id_tema', ids) // Filtrar por los IDs
      .orderBy('t.orden_ensenanza');

    // Log para verificar los temas obtenidos
    console.log('Temas obtenidos:', temas);

    // Si no se obtienen temas, retornar un mensaje claro
    if (temas.length === 0) {
      return response.status(404).send('No se encontraron temas para los IDs proporcionados');
    }

    return response.json(temas);
  } catch (error) {
    console.error('Error al obtener los temas:', error);
    return response.status(500).send('Error al obtener los temas');
  }
}

  async marcarRevisado({ params, request, auth, response }) {
    try {
      const { id } = params;
      const userId = auth.user.id;
      const { revisado } = request.only(['revisado']);

      const avanceExistente = await Database
        .table('usuario_tema_avance')
        .where('user_id', userId)
        .where('tema_id', id)
        .first();

      if (avanceExistente) {
        await Database
          .table('usuario_tema_avance')
          .where('user_id', userId)
          .where('tema_id', id)
          .update({ revisado });
      } else {
        await Database
          .table('usuario_tema_avance')
          .insert({ user_id: userId, tema_id: id, revisado });
      }

      return response.status(200).send('Estado actualizado correctamente');
    } catch (error) {
      console.error('Error al actualizar el estado:', error);
      return response.status(500).send('Error al actualizar el estado');
    }
  }

  async resetProgreso({ auth, response }) {
    try {
      const userId = auth.user.id;

      // Borrar el progreso del usuario
      await Database
        .table('usuario_tema_avance')
        .where('user_id', userId)
        .delete();

      return response.status(200).send('Progreso reiniciado correctamente');
    } catch (error) {
      console.error('Error al reiniciar el progreso:', error);
      return response.status(500).send('Error al reiniciar el progreso');
    }
  }
}

module.exports = VistaGeneralCont;



