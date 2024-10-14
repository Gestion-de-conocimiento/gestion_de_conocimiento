'use strict'
const Database = use('Database')

class ControladorRecursosEnsenanza {
  async mostrarTemasPorRama({ request, response }) {
    // Obtener el valor de tema_rama del parámetro de consulta
    const tema_rama = request.input('tema_rama');

    // Consulta SQL para filtrar los registros por tema_rama
    const recursos = await Database
      .raw(`
        SELECT 
          SUBSTRING(a.nombre_tema_ordenado, LOCATE(' ', a.nombre_tema_ordenado) + 1) AS nombre_tema,
          a.url AS url
        FROM 
          temas_orden_ensenanza a
        WHERE 
          a.tema_rama = ?  -- Filtra por tema_rama
      `, [tema_rama]);

    return response.json(recursos);
  }
}

module.exports = ControladorRecursosEnsenanza;
