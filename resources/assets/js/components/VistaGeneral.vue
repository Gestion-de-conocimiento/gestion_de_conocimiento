<template>
  <div class="content-wrapper">
    <section class="content">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="card shadow">
              <div class="card-header">
                <div class="row">
                  <!-- Columna del título -->
                  <div class="col-sm-6">
                    <h3 class="card-title mt-2"><b>{{ nombreRama }}</b></h3>
                  </div>
                  <!-- Columna del progreso del tema -->
                  <div class="col-sm-6 text-right">
                    <p><strong>Tema no dominado {{ temaActual }} de {{ totalTemas }}</strong></p>
                  </div>
                </div>
              </div>

              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-bordered">
                    <thead class="thead-light">
                      <tr>
                        <th>Tema</th>
                        <th>Material</th>
                        <th>Revisado</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-if="temas.length > 0 && temaActual <= temas.length">
                        <td>{{ temas[temaActual - 1].nombre_tema_ordenado }}</td>
                        <td>
                          <a :href="temas[temaActual - 1].url" target="_blank">Ver material</a>
                        </td>
                        <td class="text-center">
                          <input type="checkbox" v-model="temas[temaActual - 1].revisado" @change="guardarAvance(temaActual - 1)" />
                        </td>
                      </tr>
                      <tr v-else>
                        <td colspan="3">No hay temas disponibles.</td>
                      </tr>
                    </tbody>
                  </table>
                  
                           <!-- Botones Anterior y Siguiente -->
                      <div class="d-flex justify-content-between">
                        <button class="btn btn-secondary" @click="temaAnterior" :disabled="temaActual === 1">Anterior</button>
                        <button class="btn btn-primary" @click="temaSiguiente">
                          {{ temaActual === totalTemas ? 'Evaluación' : 'Siguiente' }}
                        </button>
                      </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'VistaGeneral',
  data() {
    return {
      nombreRama: '',
      temaActual: 1,
      temas: [],  // Asegúrate de que esto sea un array
      temaIds: []
    };
  },
    computed: {
    totalTemas() {
      return this.temas.length;
    }
  },
  //Función que convierte el string JSON de vuelta a un objeto
  created() {
  this.nombreRama = this.$route.query.nombre || 'Nombre de rama no disponible';  
  const temasString = this.$route.query.temas;

  if (temasString) {
    try {
      this.temas = JSON.parse(temasString);
      
      // Filtrar los temas para omitir aquellos con grado de conocimiento 2
      const temasFiltrados = this.temas.filter(tema => tema.grado_de_conocimiento !== 2);
      console.log('Temas recibidos (sin grado 2):', temasFiltrados); // Imprime los temas filtrados en la consola

      // Extraer e imprimir solo los números de la propiedad 'tema'
      this.temaIds = temasFiltrados.map(tema => tema.tema).filter(num => num !== undefined);
      console.log('IDs de temas a enviar:', this.temaIds); // Aquí lo agregas

    } catch (error) {
      console.error('Error al parsear los temas:', error);
    }
  }
},
  methods: {
    temaAnterior() {
      if (this.temaActual > 1) {
        this.temaActual--;
      }
    },
 async temaSiguiente() {
  if (this.temas[this.temaActual - 1].revisado) {
    if (this.temaActual < this.totalTemas) {
      this.temaActual++;
    } else if (this.temaActual === this.totalTemas) {
      try {
        console.log("Ejecutando evaluación...");
        const response = await axios.post('/api/ejecutar-evaluacion');
        console.log("Respuesta del servidor:", response.data);
        alert('Evaluación completada y script Python ejecutado.');
        
        // Llama al método para reiniciar el progreso
        await this.resetProgreso();

        // Redirige a la página de evaluación
        this.$router.push({ path: '/Evaluacion' });
      } catch (error) {
        console.error('Error al ejecutar la evaluación:', error);
        alert('Hubo un error al ejecutar la evaluación. Inténtalo de nuevo.');
      }
    }
  } else {
    alert('Por favor, marca el tema como revisado antes de continuar.');
  }
},
   async guardarAvance(indiceTema) {
  try {
    const tema = this.temas[indiceTema];
    await axios.post(`/api/temas-no-dominados/${tema.id_tema}/marcar-revisado`, {
      revisado: tema.revisado,
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
        const idsString = this.temaIds.join(',');
        const response = await axios.get(`/api/temas-no-dominados/${idsString}`);
        this.temas = response.data;
        
        console.log("string de ids"+idsString)

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