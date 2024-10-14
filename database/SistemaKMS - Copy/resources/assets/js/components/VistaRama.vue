<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Tema</th>
          <th>Material de Estudio</th>
          <th>Progreso</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tema in temas" :key="tema.id">
          <td>{{ tema.nombre }}</td>
          <td>{{ tema.material }}</td>
          <td>
            <input 
              type="checkbox" 
              :checked="tema.progreso" 
              @change="actualizarProgreso(tema.id, $event)" 
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['rama'],
  data() {
    return {
      temas: [],          // Lista de temas a mostrar
      usuarioId: 1        // ID del usuario (puede ser obtenido de un contexto o API)
    };
  },
  methods: {
    async fetchTemas() {
      try {
        // Solicitar los datos de los temas para la rama actual
        const result = await axios.get(`/temas/${this.rama}`);
        this.temas = result.data;
      } catch (error) {
        console.error("Error al obtener temas:", error);
      }
    },
    async actualizarProgreso(idTema, event) {
      try {
        const estado = event.target.checked;
        // Enviar la actualización del progreso a la API
        await axios.post('/actualizarProgreso', {
          id_tema: idTema,
          usuario_id: this.usuarioId,
          estado: estado
        });
      } catch (error) {
        console.error("Error al actualizar el progreso:", error);
      }
    }
  },
  mounted() {
    // Obtener los temas cuando el componente se monta
    this.fetchTemas();
  }
};
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
}
input[type="checkbox"] {
  cursor: pointer;
}
</style>
