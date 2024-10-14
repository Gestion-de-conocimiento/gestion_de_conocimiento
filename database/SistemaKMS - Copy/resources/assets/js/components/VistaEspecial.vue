<template>
    <div class="content-wrapper">
      
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">{{ nombreRama }}</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"> </i> </span> 
                            <span style="color: #bdb9bd"> Recursos <i class="fas fa-angle-right"> </i> </span> 
                            <b> registrados </b>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

        <section class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b>{{ nombreRama }}</b> </h3>
                                <div class="card-tools">
                                    
                                </div>
                            </div>
                           <div class="card-body">
    <div class="table-responsive">
        <v-table :data="temasOrdenEnsenanza" :filters="filters" :currentPage.sync="currentPage" :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%" class="table table-hover">
            <thead slot="head">
                <v-th sortKey="nombre_tema">Tema</v-th>
                <v-th sortKey="url">Material de estudio</v-th>
            </thead>
            <tbody slot="body" slot-scope="{ displayData }">
                <tr v-for="temasOrdenEnsenanza in displayData" :key="temasOrdenEnsenanza.id">
                    <td style="width:30%">{{ temasOrdenEnsenanza.nombre_tema }}</td>
                    <td style="width:30%">
                        <a :href="temasOrdenEnsenanza.url" target="_blank">{{ temasOrdenEnsenanza.url }}</a>
                    </td>
                </tr>
            </tbody>
        </v-table>
    </div>
</div>

                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label> <b>Total: {{ temasOrdenEnsenanza.length }} registros </b> </label>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <smart-pagination :currentPage.sync="currentPage" :totalPages="totalPages" :maxPageLinks="5" />
                                        </div>
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
import axios from "axios";

export default {
  name: 'VistaEspecial',

  data() {
    return {
      nombreRama: '',
      currentPage: 1,
      totalPages: 0,
      temasOrdenEnsenanza: [],
      filters: {
        pregunta: {
          value: '',
          keys: ['pregunta']
        }
      },
      ramaId: null,  // Nueva propiedad para almacenar el ID de la rama
    };
  },

  created() {
    this.nombreRama = this.$route.query.nombre || 'Nombre de rama no disponible';
    this.ramaId = this.getRamaId(this.nombreRama);  // Asigna el ID de la rama basado en el nombre
  },

  async mounted() {
    await this.getRecurso();
  },

  methods: {
    // Método para obtener el ID de la rama basado en el nombre de la rama
    getRamaId(nombreRama) {
      const ramas = {
        'Aritmética': 2,
        'Algebra': 3,
        'Geometría': 4,
        'Algebra lineal': 5,
        'Trigonometría': 6,
        'Funciones matemáticas': 7,
        'Cálculo diferencial': 8,
        'Cálculo integral': 9,
      };
      return ramas[nombreRama] || null;  // Retorna el ID de la rama o null si no se encuentra
    },

    // Función para obtener los recursos filtrados por rama
    async getRecurso() {
      try {
        if (!this.ramaId) {
          console.error('Rama no válida');
          return;
        }

        // Realiza la solicitud a la API pasando el parámetro de tema_rama
        const result = await axios.get('/recrusosvistaespecial/mostrarrecursosvistaespecial', {
          params: { tema_rama: this.ramaId }  // Envia el valor del ID de la rama
        });

        // Asegúrate de que result.data[0] existe y es un array
        this.temasOrdenEnsenanza = Array.isArray(result.data[0]) ? result.data[0] : [];
        console.log(this.temasOrdenEnsenanza);  // Verifica que se esté asignando correctamente
      } catch (error) {
        console.error(error);  // Manejo de errores
      }
    },
  }
};
</script>

<style scoped>
/* Tus estilos permanecen igual */
</style>