<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Preguntas</h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"> </i> </span> <span style="color: #bdb9bd">  Preguntas <i class="fas fa-angle-right"> </i> </span> <b> Calculadas de opcion mutliple </b>
                        </ol>
                    </div><!-- /.col -->
                </div><!-- /.row -->
            </div><!-- /.container-fluid -->
        </div>

        <section class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b> Listado de preguntas calculadas de opcion mutliple </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                        <button type="button" class="btn btn-primary float-right" data-toggle="modal"
                                            data-target="#exampleModal" @click="abrirModal">
                                            <i class="fas fa-edit"></i> Nueva
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <div class="card-body">

                                <div class="row mb-2">
                                    <div class="col-6" >
                                        <b> Termino de busqueda: </b>
                                        <input class="form-control" type="search" 
                                            placeholder="Término" 
                                            v-model="filters.pregunta.value" 
                                            style=" height: 38px;" />
                                        
                                    </div>
                                    <div class="col-6" >
                                        <b>Campo de busqueda: </b>
                                        <select class="form-control" name="campoBusqueda" id="campoBusqueda" @change="cambiarCampoDeBusqueda">
                                        <option value="pregunta">Pregunta</option>
                                        <option value="tema">Tema</option>
                                        </select>
                                    </div>
                                </div>

                                <div class="table-responsive">

                                    <v-table :data="pregunta" :filters="filters" :currentPage.sync="currentPage" :pageSize="5"
                                        @totalPagesChanged="totalPages = $event" style="width:100%" class="table table-hover">

                                        <thead slot="head">
                                            <v-th sortKey="pregunta" defaultSort="desc">Pregunta</v-th>
                                            <v-th sortKey="tema" defaultSort="desc">Tema</v-th>
                                            <th>Opciones</th>
                                            <v-th sortKey="comodin" defaultSort="desc">Comodines</v-th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="(pregunta,cont) in displayData" v-bind:key="pregunta.id">
                                                <td style="width: 300px; white-space: normal;">{{pregunta.pregunta}}</td>
                                                <td style="width: 300px; white-space: normal;">{{pregunta.tema}}</td>
                                                <td style="width: 300px; white-space: normal;">
                                                    <span v-for="(opcionA, in opciones[cont]">
                                                        <p v-if="opcionA.esrespuesta === 1"> <b> {{opcionA.opcion}}</b></p>
                                                        <p v-else> {{opcionA.opcion}} </p>
                                                        <br>
                                                    </span>
                                                </td>
                                                <td style="width: 300px; white-space: normal;">
                                                    <span v-for="(opcionA,cont2) in opciones[cont]">
                                                        <b> {{opcionA.opcion}} </b>
                                                        <span v-for="(opcionAa,cont3) in comodines[cont][cont2]">
                                                            <span v-for="(c) in opcionAa" v>
                                                                <br>{{c.comodin}}={{c.valor_comodin}}</span>

                                                            <br> </span>

                                                        <br> </span>
                                                </td>
                                                <td>
                                                   <!-- <a @click="abrirModal(pregunta.id_pregunta, pregunta.imagenes)" data-toggle="modal" data-target="#exampleModal"  class="btn btn-outline-warning"> 
                                                        <i class="fas fa-pen" style="color: #ffae00;"></i> 
                                                    </a>
                                                  </td>-->
                                                <td>
                                                    <a @click="editarPregunta(pregunta.id_pregunta,pregunta.pregunta,pregunta.tema,pregunta.id_tema, pregunta.decimales)"
                                                        data-toggle="modal" data-target="#exampleModal" class="btn btn-outline-warning"><i
                                                            class="fas fa-pen" style="color: #ffae00;"
                                                            title="Editar la pregunta"></i> <span
                                                            style="color: #ffae00;"></span>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="eliminarCalculadas(pregunta.id_pregunta, pregunta.imagenes)" class="btn btn-outline-danger"> 
                                                        <i class="fas fa-trash" style="color: #ff6258"></i> 
                                                    </a>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </v-table>
                                </div>
                            </div>

                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label> <b> Total: {{ pregunta.length }} registros </b> </label>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <smart-pagination :currentPage.sync="currentPage" :totalPages="totalPages" :maxPageLinks="3" />
                                        </div>
                                    </div>
                                </div>
                            </div>


                            <!-- Modal -->
                            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog"
                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-xl" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">


                                            <h4 v-if="editarPreguntaVar == false" class="modal-title" id="exampleModalLabel"> <b>
                                                    Registrar pregunta </b> </h4>
                                            <h4 v-if="editarPreguntaVar == true" class="modal-title" id="exampleModalLabel"> <b>
                                                    Editar pregunta </b> </h4>


                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">

                                            <div class="form-group">
                                                <label class="text-left mb-2" for="pregunta"> Reactivo: </label>
                                                <textarea v-model="reactivo" id="pregunta" class="form-control" rows="3"
                                                    placeholder="Escribe el reactivo">  </textarea>
                                            </div>

                                            <div class="form-group">
                                                <label class="text-left mb-2">
                                                    Tema:
                                                </label>
                                                <select id="id_tema" name="temas" class="form-control">

                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <span>Numero de cifras: </span>
                                                <select id="totalCifras" v-model="decimales" name="totalCifras" class="swal2-input">
                                                    <option id="0_decimal">0</option>
                                                    <option id="1_decimal">1</option>
                                                    <option id="2_decimal">2</option>
                                                    <option id="3_decimal">3</option>
                                                    <option id="4_decimal">4</option>
                                                    <option id="5_decimal">5</option>
                                                    <option id="6_decimal">6</option>
                                                    <option id="7_decimal">7</option>
                                                    <option id="8_decimal">8</option>
                                                    <option id="9_decimal">9</option>
                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <label class="text-left mb-2" for="opciones"> Opciones: </label>
                                                <div class="row">
                                                    <div class="col-md-8">
                                                        <input id="inputOpcion" class="form-control" type="text">
                                                    </div>
                                                    <p id="errorEncontrado" style="color:red;"></p>
                                                    <div class="col-md-4">
                                                        <button id="btnAgregarOption" @click="ExpresionCorrecta" type="button"
                                                            class="btn btn-success"> Agregar opción </button>
                                                    </div>
                                                </div>

                                                <div class="table-responsive">
                                                    <table class="table" id="opciones" style="text-align: center;">
                                                        <tr>
                                                            <th>Opcion</th>
                                                            <th>¿Respuesta?</th>
                                                            <th>Quitar</th>
                                                        </tr>
                                                    </table>
                                                    <div v-if="bandera == 1">
                                                        <button class="btn btn-success" @click="DetectarComodines"
                                                            style="display: table; width:100%;">Buscar comodines</button>
                                                        <table class="table" id="tabla_opciones_comdines"
                                                            style="text-align: center;">
                                                            <tr>
                                                                <th>Opción</th>
                                                                <th>Comodín</th>
                                                                <th>Valor</th>
                                                            </tr>
                                                        </table>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                                            <button type="button" @click="btnGuardarPregunta"
                                                class="btn btn-primary">Guardar</button>
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
    </div>

</template>



<script>
    import axios from 'axios'

    var opciones = [];
    var noOpcion = 0;
    //var opcion_comodin = "";
    //var opciones_comodines = [];
    var reactivo = "";

    function btnQuitarOpcion(opcion) {

        var id_fila = opcion.split('_')[1];
        var row = document.getElementById("fila_" + id_fila);
        row.parentNode.removeChild(row);

        var id_opc = "opt_" + id_fila;

        for (var i = 0; i < opciones.length; i++) {
            if (opciones[i][1] == id_opc) {
                opciones.splice(i, 1);
            }
        }
    }

    function checkRespuesta(opcion) {

        var id_check = opcion.split('_')[1];
        var id_opc = "opt_" + id_check;
        var total_opciones = opciones.length;
        var total_chequeados = 0;

        for (var i = 0; i < opciones.length; i++) {
            if (opciones[i][2] == 1) {
                total_chequeados++;
            }
        }

        if (total_chequeados + 1 == total_opciones) {


            if (document.getElementById(opcion).checked) {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error...',
                    text: 'No puedes poner todas las opciones como respuesta'
                })
            }

            document.getElementById(opcion).checked = false;
        }

        if (document.getElementById(opcion).checked) {
            for (var i = 0; i < opciones.length; i++) {
                if (opciones[i][1] == id_opc) {
                    opciones[i][2] = 1;
                }
            }
        } else {
            for (var i = 0; i < opciones.length; i++) {
                if (opciones[i][1] == id_opc) {
                    opciones[i][2] = 0;
                }
            }
        }
    }

    export default {
        data() {
            return {
                opciones_comodines: [],
                valorComodines: [],
                vcomodin: [],
                editarPreguntaVar: false,
                pregunta: [],
                opciones: [],

                comodines: [],
                comodin_inside: [],
                comodines_raw: [],
                id_editar: 0,
                id: '',
                id_tema: '',
                tema: '',
                reactivo: '',
                bandera: 0,
                cpreguntas: 0,
                respuesta: '',
                pregunta: '',
                row_count: 2,
                tipo: '',
                temasSeleccionado: {},
                temas: [],
                id: '',
                nombre_tema: '',
                nivel: '',
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta', 'tema']
                    }
                },
                currentPage: 1,
                totalPages: 0,
                cuenta: 0
            }
        },

        props: {
            seccion: String
        },

        created() {
            //this.getpreguntas();
            // this.getTemas();
            //console.log(this.$props.tipo)
        },

        async mounted() {

            await this.getpreguntas().then(data => {}).catch(err => console.log(err))

            this.getTemas();
            let uri = window.location.href;

            if (uri.includes("?")) {
                uri = window.location.href.split('?');
                var fil = uri[1].split('=')[1];
                this.filters.pregunta.value = fil.replace(/%20/g, " ");
            }
        },
        methods: {

            cambiarCampoDeBusqueda(){
              let x = document.getElementById("campoBusqueda").value;
              this.filters.pregunta.keys[0] = x;			
            },

            wrapText(str) {
                const palabrasSinEspacios = str.split(" ");
                let textoDePregunta = "";
                for (let i = 0; i < palabrasSinEspacios.length; i++) {
                    textoDePregunta = textoDePregunta + " " + palabrasSinEspacios[i];
                    if ((i % 7) == 0 && i != 0) {
                        textoDePregunta = textoDePregunta + "<br>"
                    }
                }
                return textoDePregunta;
            },
            
           eliminarCalculadas(id, imagenes) {
                this.$swal.fire({
                    title: '¿Estas seguro de eliminar el registro?',
                    text: "Esto no podrá revertirse",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Aceptar',
                    cancelButtonText: 'Cancelar',
                }).then((result) => {
                    if (result.value) 
                    {
                        console.log("Eliminando "+id)
                        axios.post("/preguntasCalculadas/delete", {id: id,imagenesAEliminar: imagenes
                            })
                            .then(res => {
                                this.id = "";
                                this.getpreguntas();
                                console.log(res);
                                const Toast = this.$swal.mixin({
                                    toast: true,
                                    position: "top-end",
                                    showConfirmButton: false,
                                    timer: 3000
                                });
                                this.$swal.fire({
                                    type: "success",
                                    title: "¡Pregunta Eliminada!"
                                });
                            })
                            .catch(err => {
                                console.log(err);
                                this.$swal({
                                    type: "info",
                                    title: "Error al eliminar"
                                });
                            });
                    }
                })
            },
         getpreguntas: async function () {
                return axios({
                    method: 'get',
                    url: 'pregunta/showMultiplesCalculadas'
                }).then(
                    result => {
                        this.pregunta = result.data.banco_preguntas[0];
                        this.opciones = result.data.opciones;
                        this.comodines = result.data.comodines;
                        this.cpreguntas = this.pregunta.length

                        //return result.data;
                    },
                    error => {
                        console.error(error)
                    }
                )
            },

            getTemas() {
                axios({
                    method: 'GET',
                    url: '/tema/all'
                }).then(
                    result => {
                        this.temas = result.data
                    },
                    error => {
                        console.error(error)
                    }
                )
            },

          editarPregunta(id, reactivo, tema, idtema, decimales) 
          {
                this.editarPreguntaVar = true;
                this.id_editar = id;
                
                //seleccionar tema por defecto(no sirve)
            /*
                var temas = document.getElementById("id_tema");
                var length = temas.options.length;
                for (i = length - 1; i >= 0; i--) 
                 temas.options[i] = null;       
                //console.log("id del tema ",idtema)
                //document.getElementById("id_tema").value=idtema;
                var option_selected = document.createElement("option");
                option_selected.text = tema;
                option_selected.value = idtema;
                temas.add(option_selected);*/
                
            
              /*  var cifras= document.getElementById("totalCifras")
                var cifra_selected = document.createElement("option");
                cifra_selected.text = decimales;
                cifra_selected.value = decimales+"_decimales";
                cifras.add(cifra_selected);
            */

                //Limpiar opciones
                opciones = [];

                //Limpiar el reactivo
                var pregunta = '';
                //pregunta.value = "";
                this.reactivo = reactivo;
                pregunta = this.reactivo;


                //Limpiar la tabla de opciones 
                var elmtTable = document.getElementById('opciones');
                var tableRows = elmtTable.getElementsByTagName('tr');
                var rowCount = tableRows.length;
                for (var x = rowCount - 1; x > 0; x--) {
                    elmtTable.removeChild(tableRows[x]);
                }

                //Obtener los datos de la prugunta con el id
                for (var i = 0; i < this.pregunta[0].length; i++) {
                    if (this.pregunta[0][i].id_pregunta == id) {
                        pregunta.value = this.pregunta[0][i].pregunta;
                    }
                }

                //Obtener las opciones
                var numero = 0;

                for (var i = 0; i < this.opciones[0].length; i++) {
                    if (this.opciones[0][i].id_pregunta == id) {

                        var o = [];
                        o[0] = this.opciones[0][i].opcion;
                        o[1] = "opt_" + numero;



                        if (this.opciones[0][i].esrespuesta == 1) {
                            o[2] = 1;
                        } else {
                            o[2] = 0;
                        }

                        opciones.push(o);
                        numero++;
                    }
                }



                for (var i = 0; i < opciones.length; i++) {

                    var opcion = opciones[i][0];
                    var table = document.getElementById("opciones");
                    var row = table.insertRow(-1);
                    row.id = "fila_" + noOpcion;
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    cell1.innerHTML = "" + opcion;

                    // creating checkbox element 
                    let checkbox = document.createElement('input');
                    checkbox.type = "checkbox";
                    checkbox.id = "check_" + noOpcion;

                    if (opciones[i][2] == 1) {
                        checkbox.checked = true;
                    }

                    checkbox.addEventListener('click', function () {
                        checkRespuesta(this.id)
                    });
                    cell2.appendChild(checkbox);

                    let button = document.createElement('button');
                    button.id = "btn_" + noOpcion;
                    button.innerHTML = 'Quitar';
                    button.className = "btn btn-danger";
                    button.addEventListener('click', function () {
                        btnQuitarOpcion(this.id)
                    });
                    cell3.appendChild(button);

                    noOpcion = noOpcion + 1;

                }

                noOpcion = 0;

            },
          
       

            abrirModal: async function () {
                this.editarPreguntaVar = false;

                var x = document.getElementById("id_tema");

                var length = x.options.length;
                for (i = length - 1; i >= 0; i--) {
                    x.options[i] = null;
                }

                for (var i = 0; i < this.temas[0].length; i++) {
                    var option = document.createElement("option");
                    option.text = this.temas[0][i].nombre_tema;
                    option.value = this.temas[0][i].id;
                    x.add(option);
                }

                //Limpiar opciones
                this.bandera = 0;
                this.opciones_comodines = [];
                opciones = [];
                this.reactivo = '';

                //Limpiar el reactivo
                var pregunta = document.getElementById("pregunta");
                pregunta.value = "";


                //Limpiar la tabla de opciones 
                var elmtTable = document.getElementById('opciones');
                var tableRows = elmtTable.getElementsByTagName('tr');
                var rowCount = tableRows.length;
                for (var x = rowCount - 1; x > 0; x--) {
                    elmtTable.removeChild(tableRows[x]);
                }

            },

            btnGuardarPregunta: async function () {
                var vacio = false;
                var comodinesCorrecto = true;
                var pregunta = document.getElementById("pregunta");
                var total_opciones = opciones.length;
                var tema = document.getElementById("id_tema").value;
                var total_chequeados = 0;
                var errores = 0;

                var totalCifras = document.getElementById("totalCifras").value;

                /*COMODINES*/
                if (!this.editarPreguntaVar) {
                    this.valorComodines = [];

                    for (var i = 0; i < this.comodines.length; i++) {
                        this.vcomodin = [];
                        for (var j = 0; j < this.comodines[i].length; j++) {
                            //console.log("entra7 "+i);
                            var v_comodin = document.getElementById(i + "-" + j).value;
                            //console.log("entra7 "+v_comodin);
                            this.vcomodin.push(v_comodin);
                            //this.valorComodines[i]=vcomodin;
                            var separada = v_comodin.split("~")
                            var incorrecto = false;
                            var number = /^\-{0,1}(?:[0-9]+){0,1}(?:\.[0-9]+){0,1}$/i;
                            var regex = RegExp(number);
                            if (separada.length != 2)
                                incorrecto = true;
                            else {
                                if (!(regex.test(separada[0]) && separada[0].length > 0))
                                    incorrecto = true;
                                else
                                if (!(regex.test(separada[1]) && separada[1].length > 0))
                                    incorrecto = true;
                                if (!incorrecto)
                                    if (parseInt(separada[0]) >= parseInt(separada[1]))
                                        incorrecto = true;
                            }
                            if (incorrecto) {
                                v_comodin = document.getElementById(i + "-" + j).value;
                                separada = v_comodin.split(",")
                                incorrecto = false;
                                for (var x = 0; x < separada.length; x++) {
                                    if (!(regex.test(separada[x]) && separada[x].length > 0))
                                        incorrecto = true;
                                }
                                if (incorrecto) {
                                    this.$swal({
                                        type: 'error',
                                        title: 'Comodines incorrectos'
                                    });
                                    comodinesCorrecto = false;
                                }
                            }
                        }
                        this.valorComodines.push(this.vcomodin);

                    }


                    for (var p = 0; p < opciones.length; p++) {
                        if (opciones[p][2] == 1) {
                            total_chequeados++;
                        }
                    }

                    if (total_chequeados == 0) {
                        errores++;
                        this.$swal.fire({
                            icon: 'error',
                            title: 'Error...',
                            text: 'Debes seleccionar al menos una respuesta'
                        })
                    }

                    if (total_opciones < 2) {
                        errores++;
                        this.$swal.fire({
                            icon: 'error',
                            title: 'Error...',
                            text: 'Deben ser como minimo dos opciones'
                        })
                    }

                    if (pregunta.value == "" || pregunta.value == null) {
                        errores++;
                        this.$swal.fire({
                            icon: 'error',
                            title: 'Error...',
                            text: 'El reactivo no debe estar vacio'
                        })

                        //}
                        //}
                    }
                    /*COMODINES END*/

                    if (comodinesCorrecto) {
                        axios.post('preguntaOpcionMultipleCalculadas/store', {
                                opciones: opciones,
                                rectivo: pregunta.value,
                                tema: tema,
                                comodines: this.comodines,
                                valorComodines: this.valorComodines,
                                cifras: totalCifras
                            })
                            .then((res) => {
                                this.$swal.fire({
                                    icon: 'success',
                                    title: 'Pregunta guardada',
                                    text: 'Pregunta guardada con exito',
                                })
                                // get modals
                                const modals = document.getElementsByClassName('modal');
                                // on every modal change state like in hidden modal
                                for (let i = 0; i < modals.length; i++) {
                                    modals[i].classList.remove('show');
                                    modals[i].setAttribute('aria-hidden', 'true');
                                    modals[i].setAttribute('style', 'display: none');
                                }
                                // get modal backdrops
                                const modalsBackdrops = document.getElementsByClassName('modal-backdrop');
                                // remove every modal backdrop
                                for (let i = 0; i < modalsBackdrops.length; i++)
                                    document.body.removeChild(modalsBackdrops[i]);
                                this.getpreguntas();
                            })
                    }
                } else {

                    if (this.editarPreguntaVar) {
                        //console.log("UPDATE");

                        axios.post('preguntaOpcionMultipleCalculadas/update', {
                                opciones: opciones,
                                rectivo: pregunta.value,
                                tema: tema,
                                id: this.id_editar
                            })
                            .then((res) => {
                                this.$swal.fire({
                                    icon: 'success',
                                    title: 'Pregunta actualizada',
                                    text: 'Pregunta actualizada con exito',
                                })

                                // Para cerrar el modal con el formulario
                                const modals = document.getElementsByClassName('modal');
                                for (let i = 0; i < modals.length; i++) {
                                    modals[i].classList.remove('show');
                                    modals[i].setAttribute('aria-hidden', 'true');
                                    modals[i].setAttribute('style', 'display: none');
                                }
                                const modalsBackdrops = document.getElementsByClassName('modal-backdrop');
                                for (let i = 0; i < modalsBackdrops.length; i++) {
                                    document.body.removeChild(modalsBackdrops[i]);
                                }
                                this.getpreguntas();

                            })
                            .catch((err) => {
                                console.log(err)
                            })

                    }

                }


            },
            btnAgregarOpcion: async function () {

                var opcion = document.getElementById("inputOpcion");
                this.opciones_comodines.push(opcion.value);
                var table = document.getElementById("opciones");

                if (!(opcion.value == "" || opcion.value == null)) {
                    var row = table.insertRow(this.row_count - 1);
                    row.id = "fila_" + noOpcion;
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    cell1.innerHTML = "" + opcion.value;

                    this.row_count = this.row_count + 1;

                    // creating checkbox element 
                    let checkbox = document.createElement('input');
                    checkbox.type = "checkbox";
                    checkbox.id = "check_" + noOpcion;
                    checkbox.addEventListener('click', function () {
                        checkRespuesta(this.id)
                    });
                    cell2.appendChild(checkbox);

                    let button = document.createElement('button');
                    button.id = "btn_" + noOpcion;
                    button.innerHTML = 'Quitar';
                    button.className = "btn btn-danger";
                    button.addEventListener('click', function () {
                        btnQuitarOpcion(this.id)
                    });
                    cell3.appendChild(button);

                    var opc = [];
                    opc[0] = "" + opcion.value;
                    opc[1] = "opt_" + noOpcion;
                    opc[2] = 0;
                    opciones.push(opc);
                    this.bandera = 1;

                    opcion.value = "";
                    noOpcion = noOpcion + 1;

                }
            },
            ExpresionCorrecta() {
                //console.log("entra");
                function ValidarLlavesParentesis(entrada, signoApertura, signoCierre) {
                    var llave = 0;
                    for (let i = 0; i < entrada.length; i++)
                        if (entrada.substring(i, i + 1) == signoApertura) {
                            llave++;
                        } else if (entrada.substring(i, i + 1) == signoCierre) {
                        llave--;
                        if (llave < 0)
                            i = entrada.length + 1;
                    }
                    if (llave == 0)
                        return true;
                    else {
                        if (signoApertura == "{")
                            document.getElementById("errorEncontrado").innerHTML = "Llaves incorrectas";
                        else
                            document.getElementById("errorEncontrado").innerHTML = "Paréntesis incorrectos";
                        return false;
                    }
                }

                function ObtenerFuncion(entrada) {
                    let parentesisaux = 0,
                        i, primero = true;
                    for (i = 0;
                        (parentesisaux > 0 || primero == true) && i < entrada.length; i++) {
                        if (entrada.substring(i, i + 1) == ")") {
                            primero = false;
                            parentesisaux--;
                        } else if (entrada.substring(i, i + 1) == "(") {
                            primero = false;
                            parentesisaux++;
                        }
                    }
                    return entrada.substring(0, i);
                }

                function TieneFunciones(entrada) {
                    var salida = false;
                    if (entrada.indexOf("abs (") != -1 || entrada.indexOf("acos (") != -1 || entrada.indexOf(
                        "acosh (") != -1 || entrada.indexOf("asin (") != -1 || entrada.indexOf("asinh (") != -1 ||
                        entrada.indexOf("atan2 (") != -1 || entrada.indexOf("atan (") != -1 || entrada.indexOf(
                            "atanh (") != -1 || entrada.indexOf("bindec (") != -1 || entrada.indexOf("ceil ") != -1 ||
                        entrada.indexOf("cos (") != -1 || entrada.indexOf("cosh (") != -1 || entrada.indexOf(
                        "decbin (") != -1 || entrada.indexOf("decoct (") != -1 || entrada.indexOf("deg2rad (") != -1 ||
                        entrada.indexOf("exp (") != -1 || entrada.indexOf("expm1 (") != -1 || entrada.indexOf(
                        "floor (") != -1 || entrada.indexOf("fmod (") != -1 || entrada.indexOf("is_finite (") != -1 ||
                        entrada.indexOf("is_infinite (") != -1 || entrada.indexOf("is_nan (") != -1 || entrada.indexOf(
                            "log10 (") != -1 || entrada.indexOf("log1p (") != -1 || entrada.indexOf("log (") != -1 ||
                        entrada.indexOf("max (") != -1 || entrada.indexOf("min (") != -1 || entrada.indexOf(
                        "octdec (") != -1 || entrada.indexOf("pi (") != -1 || entrada.indexOf("pow (") != -1 || entrada
                        .indexOf("rad2deg (") != -1 || entrada.indexOf("rand (") != -1 || entrada.indexOf("round (") !=
                        -1 || entrada.indexOf("sin (") != -1 || entrada.indexOf("sinh (") != -1 || entrada.indexOf(
                            "sqrt (") != -1 || entrada.indexOf("tan (") != -1 || entrada.indexOf("tanh (") != -1)
                        salida = true;
                    return salida;
                }

                function ReducirExpresion(entrada) {
                    var operacion = entrada;
                    for (var i = 0; i < operacion.length; i++)
                        if (operacion.substring(i, i + 9) == "dec + dec" || operacion.substring(i, i + 9) ==
                            "dec - dec" || operacion.substring(i, i + 9) == "dec * dec" || operacion.substring(i, i +
                            9) == "dec / dec") {
                            operacion = operacion.substring(0, i) + "dec" + operacion.substring(i + 9, operacion
                            .length);
                            i--;
                        }
                    return operacion;
                }

                function ReducirParametros(entrada) {
                    var operacion = entrada.substring(1, entrada.length);
                    for (var i = 0; i < operacion.length; i++)
                        if (operacion.substring(i, i + 9) == "dec , dec") {
                            operacion = operacion.substring(0, i) + "dec" + operacion.substring(i + 9, operacion
                            .length);
                            i--;
                        } else if (operacion.substring(i, i + 5) == "error") {
                        operacion = "error";
                        i = operacion.length;
                    }
                    return operacion;
                }

                function ValidarFunciones(fun, entrada) {
                    var operacion = entrada,
                        salida = "##",
                        TieneFuncionAnidada = false;
                    if (fun == "abs" || fun == "acos" || fun == "acosh" || fun == "asin" || fun == "asinh" || fun ==
                        "atan" || fun == "atanh" || fun == "ceil" || fun == "cos" || fun == "cosh" || fun == "decbin" ||
                        fun == "decoct" || fun == "deg2rad" || fun == "cos" || fun == "exp" || fun == "expm1" || fun ==
                        "floor" || fun == "is_finite" || fun == "is_infinite" || fun == "is_nan" || (fun == "log" &&
                            operacion.indexOf(",") == "-1") || fun == "log10" || fun == "log1p" || fun == "rad2deg" ||
                        fun == "sin" || fun == "sinh" || fun == "sqrt" || fun == "tan" || fun == "tanh") {
                        if (operacion == fun + " ( dec )")
                            if (fun == "decbin")
                                salida = "bin"
                        else if (fun == "octbin")
                            salida = "oct"
                        else
                            salida = "dec";
                        else
                        if (TieneFunciones(operacion.substring(fun.length + 2, operacion.length - 1)) == true)
                            TieneFuncionAnidada = true;
                        else
                            salida = "error";
                    } else if (fun == "atan2" || fun == "pow" || fun == "round" || fun == "log") {
                        if (operacion == fun + " ( dec , dec )")
                            salida = "dec";
                        else
                        if (TieneFunciones(operacion.substring(fun.length + 2, operacion.length - 1)) == true)
                            TieneFuncionAnidada = true;
                        else
                            salida = "error";
                    } else if (fun == "min" || fun == "max") {
                        var operacionAux = ReducirParametros(ReducirExpresion(operacion.substring(5, operacion.length -
                            1))).replace(/ /g, "");
                        if (operacionAux == "dec")
                            salida = "dec";
                        else
                        if (TieneFunciones(operacion.substring(fun.length + 2, operacion.length - 1)) == true)
                            TieneFuncionAnidada = true;
                        else
                            salida = "error";
                    } else if (fun == "bindec" && operacion.substring(8, 9) == " " && operacion.substring(operacion
                            .length - 2, operacion.length - 1) == " ") {
                        var numero = operacion.substring(9, operacion.length - 2);
                        if (numero.match(/[0-1]/gi).length == numero.length)
                            salida = "dec";
                        else {
                            errorEncontrado.innerHTML = "Numero binario no valido.";
                            salida = "error";
                        }
                    } else if (fun == "octdec" && operacion.substring(8, 9) == " " && operacion.substring(operacion
                            .length - 2, operacion.length - 1) == " ") {
                        var numero = operacion.substring(9, operacion.length - 2);
                        if (numero.match(/[0-7]/gi).length == numero.length)
                            salida = "dec";
                        else {
                            errorEncontrado.innerHTML = "Numero octal no valido.";
                            salida = "error";
                        }
                    } else if (fun == "pi") {
                        if (operacion == "pi ( )")
                            salida = "dec";
                        else
                            salida = "error";
                    }
                    if (TieneFuncionAnidada != false) {
                        while (TieneFunciones(operacion.substring(fun.length + 2, operacion.length - 1)) == true)
                            for (var i = fun.length + 2; i < operacion.length; i++)
                                if (operacion.substring(i, i + 1) == "(") {
                                    var index = operacion.substring(0, i - 1).lastIndexOf(" ") + 1;
                                    var funAux = ObtenerFuncion(operacion.substring(index, operacion.length - 2));
                                    var ResFuncion = ValidarFunciones(operacion.substring(index, i - 1), funAux);
                                    operacion = operacion.substring(0, index) + ResFuncion + operacion.substring(index +
                                        funAux.length, operacion.length);
                                    i = index + ResFuncion.length;
                                }
                        salida = ReducirParametros(ReducirExpresion(operacion.substring(fun.length + 2, operacion
                            .length - 2)));
                    }
                    return salida;
                }
                var operacion = document.getElementById("inputOpcion").value.toLowerCase().trim(),
                    operacionIncorrecta = false;
                var errorEncontrado = document.getElementById("errorEncontrado");
                errorEncontrado.innerHTML = "";
                if (ValidarLlavesParentesis(operacion, "{", "}") == true && ValidarLlavesParentesis(operacion, "(",
                    ")") == true) {
                    for (let i = 0; i < operacion.length; i++) {
                        if (operacion.substring(i, i + 1) == "{") {
                            const patron = new RegExp('^[A-Z]', 'i');
                            if (operacion.substring(i, operacion.substring(i, operacion.length).indexOf("}") + i + 1)
                                .indexOf(" ") == -1 && patron.test(operacion.substring(i + 1, i + 2)) == true) {
                                operacion = operacion.substring(0, i) + "dec" + operacion.substring(operacion.substring(
                                    i, operacion.length).indexOf("}") + i + 1, operacion.length);
                                i += 3;
                            } else {
                                errorEncontrado.innerHTML = "Comodin escrito de forma incorrecta.";
                                operacionIncorrecta = true;
                                i = operacion.length;
                            }
                        } else if (operacion.substring(i, i + 1) == "(") {
                            if (operacion.substring(i - 2, i + 1) == "+ (" || operacion.substring(i - 2, i + 1) ==
                                "- (" || operacion.substring(i - 2, i + 1) == "* (" || operacion.substring(i - 2, i +
                                1) == "/ (" || operacion.substring(i - 2, i + 1) == "( (" || i == 0) {
                                let EnParentesis = ObtenerFuncion(operacion.substring(i, operacion.length));
                                if (EnParentesis.substring(EnParentesis.length - 2, EnParentesis.length) == " )" &&
                                    EnParentesis.substring(EnParentesis.length - 3, EnParentesis.length) != "  )") {
                                    operacion = operacion.substring(0, i) + operacion.substring(i + 2, i + EnParentesis
                                        .length - 2) + operacion.substring(i + EnParentesis.length, operacion
                                        .length);
                                    i--;
                                } else {
                                    //console.log("parentesis incorrectos")
                                    operacionIncorrecta = true;
                                    i = operacion.length;
                                }
                            }
                            //Aqui solo se checan los parentecis sueltos, las funciones se evaluan mas adelante
                        } else if (operacion.substring(i, i + 1) == "0" || operacion.substring(i, i + 1) == "1" ||
                            operacion.substring(i, i + 1) == "2" || operacion.substring(i, i + 1) == "3" || operacion
                            .substring(i, i + 1) == "4" || operacion.substring(i, i + 1) == "5" || operacion.substring(
                                i, i + 1) == "6" || operacion.substring(i, i + 1) == "7" || operacion.substring(i, i +
                                1) == "8" || operacion.substring(i, i + 1) == "9") {
                            var aux = i,
                                ValAux = "";
                            do {
                                ValAux = operacion.substring(aux, aux + 1);
                                aux++;
                            } while (ValAux == "0" || ValAux == "1" || ValAux == "2" || ValAux == "3" || ValAux ==
                                "4" || ValAux == "5" || ValAux == "6" || ValAux == "7" || ValAux == "8" || ValAux ==
                                "9" || ValAux == ".")
                            if (/^([a-z])*$/.test(operacion.substring(i, i + 1)) == false && operacion.substring(aux -
                                    2, aux - 1) != ".") {
                                if (operacion.substring(i, aux - 1).indexOf(".") == operacion.substring(i, aux - 1)
                                    .lastIndexOf(".")) {
                                    if (operacion.substring(i - 9, i) != "bindec ( " && operacion.substring(i - 9, i) !=
                                        "octdec ( " && operacion.substring(i - 3, i + 2) != "log10" && operacion
                                        .substring(i - 4, i + 1) != "atan2" && operacion.substring(i - 3, i + 4) !=
                                        "deg2rad" && operacion.substring(i - 4, i + 1) != "expm1" && operacion
                                        .substring(i - 3, i + 2) != "log1p" && operacion.substring(i - 3, i + 4) !=
                                        "rad2deg") {
                                        operacion = operacion.substring(0, i) + "dec" + operacion.substring(aux - 1,
                                            operacion.length);
                                        i = i + 3;
                                    } else {
                                        i = aux;
                                    }
                                } else {
                                    errorEncontrado.innerHTML = "Numero escrito de forma incorrecta.";
                                    operacionIncorrecta = true;
                                    i = operacion.length;
                                }
                            } else {
                                errorEncontrado.innerHTML = "Numero escrito de forma incorrecta.";
                                operacionIncorrecta = true;
                                i = operacion.length;
                            }
                        } else if ((operacion.substring(i, i + 3) == "dec" && operacion.substring(i, i + 6) !=
                                "decbin" && operacion.substring(i, i + 6) != "decoct" && operacion.substring(i - 3, i +
                                    3) != "octdec" && operacion.substring(i - 3, i + 3) != "bindec") || (operacion
                                .substring(i, i + 3) == "bin" && operacion.substring(i, i + 6) != "bindec" && operacion
                                .substring(i - 3, i + 3) != "decbin") || (operacion.substring(i, i + 3) == "oct" &&
                                operacion.substring(i, i + 6) != "octdec" && operacion.substring(i - 3, i + 3) !=
                                "decoct")) {
                            errorEncontrado.innerHTML = "Entrada no valida.";
                            operacionIncorrecta = true;
                            i = operacion.length;
                        }
                    }
                    //-------------
                    if (operacionIncorrecta == false)
                        operacion = ReducirExpresion(operacion);
                    //-------------
                    var funciones = ["abs ", "acos ", "acosh ", "asin ", "asinh ", "atan ", "atanh ", "bindec ",
                        "ceil ", "cos ", "cosh ", "decbin ", "decoct ", "deg2rad ", "exp ", "expm1 ", "floor ",
                        "is_finite ", "is_infinite ", "is_nan ", "log ", "log10 ", "log1p ", "rad2deg ", "sin ",
                        "sinh ", "sqrt ", "tan ", "tanh ", "octdec ", "pi ", "atan2 ", "pow ", "round ", "min ",
                        "max "
                    ]
                    for (let i = 0; i < operacion.length; i++)
                        if (operacion.substring(i, i + 1) == "(") {
                            var indiceFuncion = operacion.substring(0, i - 1).lastIndexOf(" ") + 1;
                            var funcionActual = operacion.substring(indiceFuncion, i);
                            for (let j = 0; j < funciones.length; j++)
                                if (funcionActual == funciones[j]) {
                                    let fun = ObtenerFuncion(operacion.substring(i - funcionActual.length, operacion
                                        .length));
                                    let ResFuncion = ValidarFunciones(funcionActual.substring(0, funcionActual.length -
                                        1), fun);
                                    operacion = operacion.substring(0, i - funcionActual.length) + ResFuncion +
                                        operacion.substring(i - funcionActual.length + fun.length, operacion.length);
                                    i = i - funcionActual.length + ResFuncion.length;
                                    j = funciones.length;
                                }
                        }

                    if (operacionIncorrecta == false && ReducirExpresion(operacion) != "dec" && ReducirExpresion(
                            operacion) != "bin" && ReducirExpresion(operacion) != "oct") {
                        errorEncontrado.innerHTML = "Error de sintaxis.";
                        operacionIncorrecta = true;
                    }
                } else {
                    operacionIncorrecta = true;
                }
                this.comodines = [];

                if (!operacionIncorrecta == true)
                    this.btnAgregarOpcion()
            },
            DetectarComodines() {
                //console.log("entra");

                this.comodines = [];
                for (var x = 0; x < this.opciones_comodines.length; x++) {
                    this.comodin_inside = [];
                    var expresion = this.opciones_comodines[x];
                    var table = document.getElementById("tabla_opciones_comdines");
                    while (table.firstChild) {
                        table.removeChild(table.lastChild);
                    }
                    //console.log(expresion);
                    var guardarContenido = false;
                    var contenido = ""
                    var encontrado = false;
                    for (var i = 0; i < expresion.length; i++) {
                        if (expresion[i] == "{")
                            guardarContenido = true;
                        if (guardarContenido)
                            contenido += expresion[i]
                        if (expresion[i] == "}") {
                            guardarContenido = false;
                            for (var j = 0; j < this.comodin_inside.length; j++) {
                                if (this.comodin_inside[j] == contenido)
                                    encontrado = true;
                            }
                            if (!encontrado)
                                this.comodin_inside.push(contenido);
                            else
                                encontrado = false;
                            contenido = "";
                        }

                    }

                    this.comodines.push(this.comodin_inside);
                }
                for (var i = 0; i < this.comodines.length; i++) {
                    for (var j = 0; j < this.comodines[i].length; j++) {
                        //console.log("AQUI: " + this.comodines[i][j]);
                        var row = table.insertRow(-1);

                        var cell1 = row.insertCell(0);
                        var cell2 = row.insertCell(1);
                        var cell3 = row.insertCell(2);

                        cell1.innerHTML += this.opciones_comodines[i];

                        cell2.innerHTML = "" + this.comodines[i][j];
                        let entrada = document.createElement('input');
                        entrada.type = "text";
                        entrada.id = i + "-" + j;
                        cell3.appendChild(entrada);
                    }
                }
            },

            eliminar(id) {
                //Limpiar opciones
                opciones = [];

                //Obtener las opciones
                var numero = 0;

                for (var i = 0; i < this.opciones[0].length; i++) {
                    if (this.opciones[0][i].id_pregunta == id) {

                        var o = [];
                        o[0] = this.opciones[0][i].opcion;
                        o[1] = "opt_" + numero;



                        if (this.opciones[0][i].esrespuesta == 1) {
                            o[2] = 1;
                        } else {
                            o[2] = 0;
                        }

                        opciones.push(o);
                        numero++;
                    }
                }
                //console.log(opciones);


                this.$swal.fire({
                    title: '¿Estas seguro de eliminar el registro?',
                    text: "Esto no podrá revertirse",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Aceptar',
                    cancelButtonText: 'Cancelar',
                }).then((result) => {

                    if (result.value) {

                        ////

                        axios.post('preguntaOpcionMultipleCalculadas/delete', {
                                id: id,
                                opciones: opciones
                            }).then((res) => {
                                this.$swal({
                                    type: 'success',
                                    title: '¡Pregunta Eliminada!'
                                })
                                this.getpreguntas();
                            })
                            .catch((err) => {
                                console.log(err)
                                this.$swal({
                                    type: 'info',
                                    title: 'Error al eliminar',
                                })
                            })
                    }
                })

            }

        }
    }

</script>
