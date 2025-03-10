<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Configurar cuestionario</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">
                                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
                            </span>
                            <span style="color: #bdb9bd">
                                Cuestionario <i class="fas fa-angle-right"></i>
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
                                <h3 class="card-title mt-2"><b> Configurar cuestionario </b></h3>
                                <div class="card-tools">
                                    <div style="width: 150px;">
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="form-group">
                                    <label class="mb-2">Total de preguntas por tema:</label>
                                    <input id="numeroPreguntas" type="number" class="form-control"
                                        placeholder="# Preguntas" v-model="configuraciones.num_preguntas" disabled>
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect1">Cantidad de preguntas numéricas:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_numericas"
                                        id="numeroPreguntasNumericas" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect2">Cantidad de preguntas abiertas:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_abiertas"
                                        id="numeroPreguntasBreves" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect2">Cantidad de preguntas calculadas:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_calculadas"
                                        id="numeroPreguntasCalculadas" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect2">Cantidad de preguntas calculadas múltiples:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_calculadas_multiples"
                                        id="numeroPreguntasCalculadasMultiples" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect3">Cantidad de preguntas verdadero / falso:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_boleanas"
                                        id="numeroPreguntasBooleanas" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect3">Cantidad de preguntas opción múltiples:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_multiples"
                                        id="numeroPreguntasMultiples" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect3">Cantidad de preguntas de expresiones:</label>
                                    <input @keyup="totalPreg" v-model="configuraciones.num_preguntas_expresion"
                                        id="numeroPreguntasExpresion" class="form-control">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect1">Rango de error por defecto:</label>
                                    <input min="0" max="1" step="0.001" id="rangoPorDefecto" type="number"
                                        class="form-control" placeholder="# Preguntas"
                                        :value="configuraciones.rango_por_defecto">
                                </div>

                                <div class="form-group">
                                    <label class="mb-2">Ponderación estricta en preguntas de opción múltiple:</label>
                                    <label>
                                        <input id="ponderacionEstricta" type="checkbox" value="first_checkbox"> Sí
                                    </label>
                                </div>

                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect1">Versión de RBN:</label>
                                    <select class="form-control" id="exampleFormControlSelect1">
                                        <option v-for="rb in rbs" :value="rb.id">{{rb.nombre}}</option>
                                    </select>
                                </div>
                            </div>
                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label><b>Total: {{ preguntasPorTema.length }} registros</b></label>
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
                                <h3 class="card-title mt-2"><b>Temas que no cumplen con la configuración establecida</b></h3>
                                <div class="card-tools">
                                    <div style="width: 150px;">
                                    </div>
                                </div>
                            </div>

                            <div class="card-body">
                                <div class="row mb-2">
                                    <div class="col-12">
                                        <b>Término de búsqueda:</b>
                                        <input class="form-control" type="search" placeholder="Ej. tablas de multiplicar"
                                            v-model="filters.nombre.value"
                                            style="height: 37px; margin: 0px;" />
                                    </div>
                                </div>

                                <div class="table-responsive">
                                    <v-table :data="preguntasPorTema" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="10" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                        <thead slot="head">
                                            <th>Tema:</th>
                                            <th>Abiertas</th>
                                            <th>Numérica</th>
                                            <th>Booleana</th>
                                            <th>Múltiple</th>
                                            <th>Calculada</th>
                                            <th>Calculada Múltiple</th>
                                            <th>Expresiones</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="tema in displayData"
                                                v-if="(tema.totalPreguntasAbiertas < configuraciones.num_preguntas_abiertas) ||
                                                    (tema.totalPreguntasNumericas < configuraciones.num_preguntas_numericas) ||
                                                    (tema.totalPreguntasBooleanas < configuraciones.num_preguntas_boleanas) ||
                                                    (tema.totalPreguntasMultiples < configuraciones.num_preguntas_multiples) ||
                                                    (tema.totalPreguntasCalculadas < configuraciones.num_preguntas_calculadas) ||
                                                    (tema.totalPreguntasCalculadasMultiples < configuraciones.num_preguntas_calculadas_multiples)||
                                                    (tema.totalPreguntasExpresiones < configuraciones.num_preguntas_expresion)">
                                                <td>{{ tema.nombre_tema }}</td>
                                                <td>
                                                    {{ tema.totalPreguntasAbiertas }}
                                                    <i v-if="tema.totalPreguntasAbiertas >= configuraciones.num_preguntas_abiertas"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                                <td>
                                                    {{ tema.totalPreguntasNumericas }}
                                                    <i v-if="tema.totalPreguntasNumericas >= configuraciones.num_preguntas_numericas"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                                <td>
                                                    {{ tema.totalPreguntasBooleanas }}
                                                    <i v-if="tema.totalPreguntasBooleanas >= configuraciones.num_preguntas_boleanas"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                                <td>
                                                    {{ tema.totalPreguntasMultiples }}
                                                    <i v-if="tema.totalPreguntasMultiples >= configuraciones.num_preguntas_multiples"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                                <td>
                                                    {{ tema.totalPreguntasCalculadas }}
                                                    <i v-if="tema.totalPreguntasCalculadas >= configuraciones.num_preguntas_calculadas"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                                <td>
                                                    {{ tema.totalPreguntasCalculadasMultiples }}
                                                    <i v-if="tema.totalPreguntasCalculadasMultiples >= configuraciones.num_preguntas_calculadas_multiples"
                                                       class="fas fa-check-circle" style="color:green"></i>
                                                    <i v-else class="fas fa-times-circle" style="color:red"></i>
                                                </td>
                                              <td>
                                                    {{ tema.totalPreguntasExpresiones }}
                                                    <i v-if="tema.totalPreguntasExpresiones >= configuraciones.num_preguntas_expresion"
                                                       class="fas fa-check-circle" style="color:green"></i>
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
                                        <label><b>Total: {{ preguntasPorTema.length }} registros</b></label>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <smart-pagination :currentPage.sync="currentPage" :totalPages="totalPages" :maxPageLinks="3" />
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
                id: "",
                rbs: [],
                numero_preguntas: [],
                configuraciones: {
                    num_preguntas_numericas: 0,
                    num_preguntas_multiples: 0,
                    num_preguntas_boleanas: 0,
                    num_preguntas_calculadas: 0,
                    num_preguntas_abiertas: 0,
                    num_preguntas_calculadas_multiples: 0,
                    num_preguntas_expresion: 0
                },
                totalPreguntas: 0,
                preguntasPorTema: [],
                filters: {
                    nombre: {
                        value: '',
                        keys: ['nombre_tema']
                    }
                },
                currentPage: 1,
                totalPages: 0
            };
        },
        created() {

        },
        mounted() {


            this.obtenerConfiguraciones();
            this.obtenerTotales();
            this.obtenerRbs();

        },
        methods: {
            
            obtenerRbs(){
                
                // Obtiene toda la información del a tabla donde se almacenan las versiones de la red bayesiana
                axios({
                    method: 'GET',
                    url: '/obtenerrbs'
                }).then(
                    result => {

                        
                        //console.log(result.data[0])
                        
                        this.rbs = result.data[0]

                    },
                    error => {
                        console.error(error)
                    }
                )
            },

            totalPreg() {


                this.configuraciones.num_preguntas_numericas = (this.configuraciones.num_preguntas_numericas === "") ?
                    0 : parseInt(this.configuraciones.num_preguntas_numericas);
                this.configuraciones.num_preguntas_multiples = (this.configuraciones.num_preguntas_multiples === "") ?
                    0 : parseInt(this.configuraciones.num_preguntas_multiples);
                this.configuraciones.num_preguntas_boleanas = (this.configuraciones.num_preguntas_boleanas === "") ? 0 :
                    parseInt(this.configuraciones.num_preguntas_boleanas);
                this.configuraciones.num_preguntas_calculadas = (this.configuraciones.num_preguntas_calculadas === "") ?
                    0 : parseInt(this.configuraciones.num_preguntas_calculadas);
                this.configuraciones.num_preguntas_abiertas = (this.configuraciones.num_preguntas_abiertas === "") ? 0 :
                    parseInt(this.configuraciones.num_preguntas_abiertas);
                this.configuraciones.num_preguntas_calculadas_multiples = (this.configuraciones
                    .num_preguntas_calculadas_multiples === "") ? 0 : parseInt(this.configuraciones
                    .num_preguntas_calculadas_multiples);
                              this.configuraciones.num_preguntas_expresion = (this.configuraciones.num_preguntas_expresion === "") ?
                    0 : parseInt(this.configuraciones.num_preguntas_expresion);


                this.configuraciones.num_preguntas = parseInt(this.configuraciones.num_preguntas_numericas) +
                    parseInt(this.configuraciones.num_preguntas_multiples) +
                    parseInt(this.configuraciones.num_preguntas_boleanas) +
                    parseInt(this.configuraciones.num_preguntas_calculadas) +
                    parseInt(this.configuraciones.num_preguntas_abiertas) +
                    parseInt(this.configuraciones.num_preguntas_calculadas_multiples)+
                    parseInt(this.configuraciones.num_preguntas_expresion)

            },

            checkPonderacionEstricta() {

                var checkEstricta = document.getElementById("ponderacionEstricta");


                if (this.configuraciones.ponde_estricta == 1) {
                    checkEstricta.checked = true;
                } else {
                    checkEstricta.checked = false;
                }
            },


            obtenerTotales() {
                //obtenerTotalPorPregunta
                axios({
                    method: 'GET',
                    url: '/obtenerTotalPorPregunta'
                }).then(
                    result => {

                        let temas = result.data.temas[0];
                        let preguntas = result.data.totalPreguntasPorTipo[0];

                        for (let i = 0; i < temas.length; i++) {
                            temas[i].totalPreguntasMultiples = 0;
                            temas[i].totalPreguntasCalculadas = 0;
                            temas[i].totalPreguntasAbiertas = 0;
                            temas[i].totalPreguntasNumericas = 0;
                            temas[i].totalPreguntasBooleanas = 0;
                            temas[i].totalPreguntasCalculadasMultiples = 0;
                            temas[i].totalPreguntasExpresiones = 0;
                        }

                        console.log(preguntas);

                        for (let i = 0; i < temas.length; i++) {
                            for (let j = 0; j < preguntas.length; j++) {
                                if (temas[i].nombre_tema === preguntas[j].nombre_tema) {
                                    switch (parseInt(preguntas[j].tipo)) {
                                        case 1:
                                            temas[i].totalPreguntasAbiertas = preguntas[j].totalPreguntas;
                                            break;
                                        case 2:
                                            temas[i].totalPreguntasNumericas = preguntas[j].totalPreguntas;
                                            break;
                                        case 3:
                                            temas[i].totalPreguntasBooleanas = preguntas[j].totalPreguntas;
                                            break;
                                        case 4:
                                            temas[i].totalPreguntasMultiples = preguntas[j].totalPreguntas;
                                            break;
                                        case 5:
                                            temas[i].totalPreguntasCalculadas = preguntas[j].totalPreguntas;
                                            break;
                                        case 6:
                                            temas[i].totalPreguntasCalculadasMultiples = preguntas[j]
                                            .totalPreguntas;
                                             break;
                                        case 7:
                                            temas[i].totalPreguntasExpresiones = preguntas[j]
                                            .totalPreguntas;
                                            break;
                                    }
                                }
                            }
                        }


                        //console.log(temas);
                        this.preguntasPorTema = temas;

                    },
                    error => {
                        console.error(error)
                    }
                )
            },

            obtenerConfiguraciones() {
                axios({
                    method: 'GET',
                    url: '/obtenerconfiguracion'
                }).then(
                    result => {
                        this.configuraciones = result.data[0];
                        //console.log(this.configuraciones);
                        this.checkPonderacionEstricta();
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            guardarConfiguracion: async function () {
                var totalPreguntas = document.getElementById("numeroPreguntas").value;
                var totalNumericas = document.getElementById("numeroPreguntasNumericas").value;
                var rangoDefecto = document.getElementById("rangoPorDefecto").value;
                var totalBreves = document.getElementById("numeroPreguntasBreves").value;
                var totalCalculadas = document.getElementById("numeroPreguntasCalculadas").value;
                var totalBooleanas = document.getElementById("numeroPreguntasBooleanas").value;
                var totalMultiples = document.getElementById("numeroPreguntasMultiples").value;
                var totalCalculadasMultiples = document.getElementById("numeroPreguntasCalculadasMultiples").value;
                var totalExpresiones = document.getElementById("numeroPreguntasExpresion").value;

              //var ponderacionEstricta = document.getElementById("ponderacionEstricta").value;

                var checkEstricta = document.getElementById("ponderacionEstricta");

                if (checkEstricta.checked) {
                    var ponderacionEstricta = 1;
                } else {
                    var ponderacionEstricta = 0;
                }

                axios.post('/guardarconfiguracion', {
                        totalPreguntas: totalPreguntas,
                        totalNumericas: totalNumericas,
                        rangoDefecto: rangoDefecto,
                        totalBreves: totalBreves,
                        totalCalculadas: totalCalculadas,
                        totalBooleanas: totalBooleanas,
                        totalMultiples: totalMultiples,
                        totalCalculadasMultiples: totalCalculadasMultiples,
                        totalExpresiones: totalExpresiones,
                        ponderacionEstricta: ponderacionEstricta,
                    })
                    .then((res) => {
                        this.$swal.fire({
                            icon: 'success',
                            title: 'Configuracion guardada',
                            text: 'Configuracion guardada con exito',
                        })
                        this.obtenerConfiguraciones();
                        this.obtenerTotales();
                        this.checkPonderacionEstricta();
                    })
                    .catch((err) => {
                        console.log(err)
                    })
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