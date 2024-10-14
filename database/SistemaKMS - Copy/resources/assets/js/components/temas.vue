<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Temas</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd"> <i class="fas fa-home"></i> <i class="fas fa-angle-right">
                                </i> </span> <span style="color: #bdb9bd"> Area Disciplinar <i
                                    class="fas fa-angle-right"> </i> </span> <b>Temas </b>
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
                                <h3 class="card-title mt-2"> <b> Número de preguntas por tema </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                    </div>
                                </div>
                            </div>

                            <div class="card-body">

                                <div class="row mb-2">

                                    <div class="col-12">
                                        <b> Termino de busqueda: </b>
                                        <input class="form-control" type="search" placeholder="Término"
                                            v-model="filters.nombre_tema.value" style=" height: 38px;" />
                                    </div>
                                </div>


                                <div class="table-responsive">
                                    <v-table :data="temas" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                        <thead slot="head">
                                            <v-th sortKey="nombre0_tema" defaultSort="desc">Tema</v-th>
                                            <v-th defaultSort="desc"> Abiertas</v-th>
                                            <v-th defaultSort="desc"> Númericas </v-th>
                                            <v-th defaultSort="desc"> Verdadero / Falso </v-th>
                                            <v-th defaultSort="desc"> Opción Múltiple </v-th>
                                            <v-th defaultSort="desc"> Calculadas </v-th>
                                            <v-th defaultSort="desc"> Calculadas Múltiples </v-th>
                                            <v-th defaultSort="desc"> Preguntas Expresiones </v-th>
                                            <v-th defaultSort="desc"> Total por tema </v-th>
                                          
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="temas in displayData" :key="temas.id">

                                                <td>
                                                    {{temas.nombre_tema}}</td>
                                                <td>
                                                    <span class="badge badge-primary"> {{temas.totalAbiertas}} </span>
                                                </td>
                                                <td>
                                                    <span v-if="temas.totalNumericas > 0" class="badge badge-primary">
                                                        {{temas.totalNumericas}} </span>
                                                    <span v-else class="badge badge-danger"> {{temas.totalNumericas}}
                                                    </span>
                                                </td>


                                                <td>
                                                    <span v-if="temas.totalBooleanas > 0" class="badge badge-primary">
                                                        {{temas.totalBooleanas}} </span>
                                                    <span v-else class="badge badge-danger"> {{temas.totalBooleanas}}
                                                    </span>
                                                </td>

                                                <td>
                                                    <span v-if="temas.totalMultiple > 0" class="badge badge-primary">
                                                        {{temas.totalMultiple}} </span>
                                                    <span v-else class="badge badge-danger "> {{temas.totalMultiple}}
                                                    </span>
                                                </td>
                                                <td>
                                                    <span v-if="temas.totalCalculadas > 0" class="badge badge-primary">
                                                        {{temas.totalCalculadas}} </span>
                                                    <span v-else class="badge badge-danger "> {{temas.totalCalculadas}}
                                                    </span>
                                                </td>
                                                <td>
                                                    <span v-if="temas.totalCMultiple > 0" class="badge badge-primary">
                                                        {{temas.totalCMultiple}} </span>
                                                    <span v-else class="badge badge-danger "> {{temas.totalCMultiple}}
                                                    </span>
                                                </td>
                                                <td>
                                                    <span v-if="temas.totalExpresiones > 0" class="badge badge-primary">
                                                        {{temas.totalExpresiones}} </span>
                                                    <span v-else class="badge badge-danger "> {{temas.totalExpresiones}}
                                                    </span>
                                                </td>
                                              <td>
                                                    <span v-if="temas.totalPorTema > 0" class="badge badge-primary">
                                                        {{temas.totalPorTema}} </span>
                                                    <span v-else class="badge badge-danger "> {{temas.totalPorTema}}
                                                    </span>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </v-table>
                                </div>
                            </div>
                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label> <b> Total: {{ temas.length }} temas registros{{temas.totalPreguntas}} </b> </label>
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
            </div>
        </section>
    </div>
</template>

<script>
    import axios from 'axios'


    export default {
        data() {
            return {
                verificarPreguntas: false,
                configuracion: [],
                temas: [],
                filters: {
                    nombre_tema: {
                        value: '',
                        keys: ['nombre_tema']
                    }
                },
                currentPage: 1,
                totalPages: 0,
                temasOnlyNombreID: []
            }
        },
        mounted() {
            this.getTemas();
            this.obtenerConfiguracion();
        },
        methods: {
            obtenerConfiguracion() {
                axios({
                    method: 'get',
                    url: 'cuestionario/obtenerconfiguracion'
                }).then(
                    result => {
                        this.configuracion = result.data;

                        for (var i = 0; i < this.temas.length; i++) {
                            if (this.temas[i].tipo > 1) {
                                //console.log(this.temas[i].totalAbiertas);    
                                if (this.configuracion.num_preguntas_abiertas > this.temas[i].totalAbiertas ||
                                    this.configuracion.num_preguntas_numericas > this.temas[i].totalNumericas ||
                                    this.configuracion.num_preguntas_boleanas > this.temas[i].totalBooleanas ||
                                    this.configuracion.num_preguntas_multiples > this.temas[i].totalCMultiple ||
                                    this.configuracion.num_preguntas_calculadas > this.temas[i].totalCalculadas ||
                                    this.configuracion.num_preguntas_calculadas_multiples > this.temas[i].totalCMultiple) {
                                    this.verificarPreguntas =
                                        "El total de preguntas registradas por cada tema, no cumple los requerimientos para el inicio del cuestionario.";
                                    break;
                                }
                            }
                        }
                    }, error => {
                        console.error(error)
                    }
                )
            },


            getTemas() {
                axios({
                    method: 'GET',
                    url: 'tema/preguntas'
                }).then(
                    result => {
                        console.log(result.data[0])
                        this.temas = result.data[0];
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
        }
    }

</script>
