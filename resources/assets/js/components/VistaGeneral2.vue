<template>
  <div>
    <!-- Leyenda -->
    <div class="text-right">
      <p><strong>Tema no dominado {{ temaActual }} de {{ totalTemas }}</strong></p>
    </div>
    
    <!-- Tabla -->
    <table class="table table-bordered">
      <thead class="thead-light">
        <tr>
          <th>Tema</th>
          <th>Material</th>
          <th>Revisado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="temas.length > 0">
          <td>{{ temas[temaActual - 1].nombre_tema_ordenado }}</td>
          <td>
            <a :href="temas[temaActual - 1].url" target="_blank">Ver material</a>
          </td>
          <td class="text-center">
            <div>
              <input type="checkbox" v-model="temas[temaActual - 1].revisado" @change="guardarAvance(temaActual - 1)" />
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Botones -->
    <div class="d-flex justify-content-between">
      <button class="btn btn-secondary" @click="temaAnterior" :disabled="temaActual === 1">Anterior</button>
      <button class="btn btn-primary" @click="temaSiguiente">
        {{ temaActual === totalTemas ? 'Evaluación' : 'Siguiente' }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      temaActual: 1,
      temas: []
    };
  },
  computed: {
    totalTemas() {
      return this.temas.length;
    }
  },
  methods: {
    temaAnterior() {
      if (this.temaActual > 1) {
        this.temaActual--;
      }
    },
    async temaSiguiente() {
      if (this.temaActual < this.totalTemas) {
        this.temaActual++;
      } else if (this.temaActual === this.totalTemas) {
        try {
          // Ejecutar la evaluación (script Python)
          const response = await axios.post('/api/ejecutar-evaluacion');
          console.log(response.data); // Mensaje de éxito o error
          alert('Evaluación completada y script Python ejecutado.');

          // Si la evaluación se ejecuta correctamente, reiniciar el progreso
          await this.resetProgreso();
        } catch (error) {
          console.error('Error al ejecutar la evaluación:', error);
          alert('Hubo un error al ejecutar la evaluación. Inténtalo de nuevo.');
        }
      }
    },
    async guardarAvance(indiceTema) {
      try {
        const tema = this.temas[indiceTema];
        await axios.post(`/api/temas-no-dominados/${tema.id_auto}/marcar-revisado`, {
          revisado: tema.revisado
        });
      } catch (error) {
        console.error('Error al guardar el avance:', error);
      }
    },
    async resetProgreso() {
      try {
        await axios.post('/api/temas-no-dominados/reset-progreso');
      } catch (error) {
        console.error('Error al reiniciar el progreso:', error);
      }
    },
    async fetchTemas() {
      try {
        const response = await axios.get('/api/temas-no-dominados');
        this.temas = response.data;

        // Mover al primer tema no revisado
        const primerTemaNoRevisado = this.temas.findIndex(tema => !tema.revisado);
        this.temaActual = primerTemaNoRevisado !== -1 ? primerTemaNoRevisado + 1 : this.temas.length;
      } catch (error) {
        console.error('Error al obtener los temas:', error);
      }
    },
  },
  mounted() {
    this.fetchTemas();
  }
};
</script>

<style scoped>
.table th,
.table td {
  text-align: center;
  vertical-align: middle;
}
input[type="checkbox"] {
  width: 20px;
  height: 20px;
}
</style>