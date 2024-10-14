<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Configurar evaluación</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">
                                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
                            </span>
                            <span style="color: #bdb9bd">
                                Evaluación <i class="fas fa-angle-right"></i>
                            </span>
                            <b> Configuración </b>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

        <section class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12 col-md-5">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b> Configurar evaluación </b> </h3>
                            </div>
                            <div class="card-body">
                                <div class="form-group">
                                    <label for="numeroPreguntas" class="mb-2">Total de preguntas por tema:</label>
                                    <input id="numeroPreguntas" type="number" class="form-control" v-model="configuraciones.total_preguntas">
                                </div>

                                <div class="form-group">
                                    <label for="rangoPorDefecto" class="mb-2">Rango de error por defecto:</label>
                                    <input min="0" max="1" step="0.001" id="rangoPorDefecto" type="number" class="form-control" v-model="configuraciones.rango_por_defecto">
                                </div>

                              <div class="form-group">
                                  <label for="ponderacionEstricta" class="mb-2">Ponderación estricta en preguntas de opción múltiple</label>
                                  <input id="ponderacionEstricta" type="checkbox" v-model="configuraciones.ponde_estricta" :true-value="1" :false-value="0">
                              </div>




                                <div class="form-group">
                                  <label class="mb-2">Versión de RBN:</label>
                                  <select class="form-control" id="rbmComboBox" v-model="configuraciones.rbm">
                                      <option v-for="rb in rbs" :value="rb.id">{{ rb.nombre }}</option>
                                  </select>
                              </div>




                            </div>

                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <b> Total: {{ preguntasPorTema.length }} registros </b>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <button type="button" @click="guardarConfiguracion" class="btn btn-primary">
                                                <i class="fas fa-save" style="border-radius: 25px;"></i> Guardar
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-12 col-md-7">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b> Temas que no cumplen con la configuración establecida
                                    </b> </h3>
                            </div>

                            <div class="card-body">

                                <div class="table-responsive">

                                    <v-table :data="preguntasPorTema" :currentPage.sync="currentPage" :pageSize="10"
                                        @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                        <thead slot="head">
                                            <th>Tema: </th>
                                            <th>Cantidad de Reactivos por Tema</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="tema in displayData">

                                                <td>{{ tema.nombre_tema }}</td>
                                                <td>
                                                    {{ tema.totalPreguntas }}
                                                    <i v-if="tema.totalPreguntas >= configuraciones.total_preguntas" class="fas fa-check-circle"
                                                        style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </v-table>
                                </div>
                            </div>

                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label> <b> Total: {{ preguntasPorTema.length }} registros </b> </label>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <smart-pagination :currentPage.sync="currentPage" :totalPages="totalPages"
                                                :maxPageLinks="3" />
                                        </div>
                                    </div>
                                </div>


                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="modal fade" id="modalDeInformacion" tabindex="-1" role="dialog"
                        aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">

                                    <h5 class="modal-title" id="exampleModalLabel"> Información </h5>


                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    Algo de información para el usuario
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
    data() {
        return {
            configuraciones: {},
            rbs: [],
            preguntasPorTema: [],
            currentPage: 1,
            totalPages: 0
        };
    },
    mounted() {
        this.obtenerPreguntasPorTema();
        this.obtenerRbs();
        this.obtenerConfiguraciones();
    },
    methods: {
        async obtenerPreguntasPorTema() {
            axios({
                method: 'GET',
                url: '/obtenerTotalPreguntasPorTema'
            }).then(
                result => {
                    let temas = result.data;
                    this.preguntasPorTema = result.data;

                },
                error => {
                    console.error(error)
                }
            )
        },
        obtenerRbs() {
            axios({
                method: 'GET',
                url: '/obtenerrbs'
            }).then(
                result => {
                    this.rbs = result.data[0]
                },
                error => {
                    console.error(error)
                }
            )
        },
        obtenerConfiguraciones() {
            axios({
                method: 'GET',
                url: '/obtenerConfiguracionEvaluacion'
            }).then(
                result => {
                    this.configuraciones = result.data;
                    console.log(this.configuraciones);
                },
                error => {
                    console.error(error)
                }
            )
        },
       
      guardarConfiguracion: async function () {
    const { total_preguntas, rango_por_defecto, rbm } = this.configuraciones;
    const ponderacionEstricta = this.configuraciones.ponde_estricta ? 1 : 0;

    try {
        await axios.post('/guardarconfiguracionEvaluacion', {
            ponderacionEstricta,
            totalPreguntas: total_preguntas,
            rangoDefecto: rango_por_defecto,
            rbmID: rbm
        });
        
        this.$swal.fire({
            icon: 'success',
            title: 'Configuración guardada',
            text: 'Configuración guardada con éxito',
        });

        this.obtenerPreguntasPorTema();
        this.obtenerRbs();
        this.obtenerConfiguraciones();
    } catch (err) {
        console.error(err);
    }
}
    },
}

</script>

<style>
div.gfg {
    width: 100%;
    height: 800px;
    overflow: auto;
    text-align: justify;
}
</style>