<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Preguntas </h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd"> <i class="fas fa-home"></i> <i class="fas fa-angle-right">
                                </i> </span> <span style="color: #bdb9bd"> Preguntas <i class="fas fa-angle-right"> </i>
                            </span> <b>Calculadas </b>
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
                                <h3 class="card-title mt-2"> <b> Preguntas calculadas </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                        <button type="button" class="btn btn-primary float-right"  data-toggle="modal"
                                            data-target="#exampleModal" @click="abrirModal(-1)">
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
                                        <option value="opcion">Respuesta</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="table-responsive">
                                    <v-table :data="preguntaNumerica" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" class="table table-hover">

                                        <thead slot="head">
                                            <tr>
                                                <th>Pregunta </th>
                                                <th>Tema</th>
                                                <th>Respuesta </th>
                                                <th>Valores</th>
                                                <th>Margen</th>
                                                <th>Margen arriba</th>
                                                <th>Margen abajo</th>
                                                <th>Decimales</th>
                                                <th>Imagenes</th>
                                                <th>Editar</th>
                                                <th>Eliminar</th>
                                            </tr>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="(preguntaNumerica) in displayData" v-bind:key="preguntaNumerica.id">
                                                <td>{{preguntaNumerica.pregunta}}
                                                </td>
                                                <td>
                                                    {{preguntaNumerica.tema}}
                                                </td>
                                                <td>
                                                    {{preguntaNumerica.opcion}}
                                                </td>
                                                <td>
                                                    <p v-for="(valorComodines) in valorComodines" v-if="preguntaNumerica.id_opcion === valorComodines.id_opcion">
                                                        {{valorComodines.comodin}}={{valorComodines.valor_comodin}}
                                                    </p>
                                                </td>
                                                <td>{{preguntaNumerica.rango}}</td>
                                                <td>{{preguntaNumerica.aplicableArriba}}</td>
                                                <td>{{preguntaNumerica.aplicableAnbajo}}</td>
                                                <td>{{preguntaNumerica.decimales}}</td>
                                                <td>
                                                    <a data-toggle="modal" data-target="#modalParaVerImagenes" @click="desplegarImagenesEnModal(preguntaNumerica.imagenes)" class="btn btn-outline-primary">
                                                        <i class="fas fa-eye" style="color: #2196f3"></i>
                                                    </a>
                                                </td>

                                                <td class="text-center">
                                                    <a @click="abrirModal(preguntaNumerica.id_pregunta, preguntaNumerica.imagenes)" data-toggle="modal" data-target="#exampleModal"  class="btn btn-outline-warning"> 
                                                        <i class="fas fa-pen" style="color: #ffae00;"></i> 
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="eliminarCalculadas(preguntaNumerica.id_pregunta, preguntaNumerica.imagenes)" class="btn btn-outline-danger">
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
                                        <label> <b> Total: {{ preguntaNumerica.length }} registros </b> </label>
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
            </div>
        </section>


        <div class="row">
            <div class="modal animated animate__bounceIn" id="exampleModal" role="dialog"
                aria-labelledby="exampleModalLabel" aria-hidden="true" data-focus="false">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content" >

                        <div class="modal-body">

                            <h3 class="modal-title" id="exampleModalLabel"></h3>


                            <p class="text-left"> <b> Pregunta: </b></p>
                            <textarea @focus="limpiarCampos('pregunta')" rows="4" id="pregunta" type="text"
                                class="form-control" placeholder="pregunta"
                                style="margin:0px; font-size: 15px; line-height: 20px;"> </textarea>

                            <span id="msjInputPregunta"> </span>

                            <div style="display: table; width:100%;">


                                <p class="text-left"> <b> Respuesta: </b></p>
                                <div class="row">
                                    <div class="col-md-8" style="padding:0px;">

                                        <input @focus="limpiarCampos('respuesta')" id="respuesta"
                                            class="form-control" placeholder="respuesta"
                                            style="margin:0px; font-size: 15px; line-height: 20px; height: 37px;">
                                    </div>
                                    <div class="col-md-4" style="padding:0px;">
                                        <button class="btn btn-success" @click="ExpresionCorrecta"
                                            style="height:37px;"> <i
                                                class="fas fa-search"></i> Buscar comodines</button>
                                    </div>
                                </div>
                                <p id="errorEncontrado" style="color:red;"></p>
                                <span id="msjInputRespuesta"> </span>

                            </div>

                            <div class="table-responsive">
                                <table class="table" id="opciones" style="text-align: center;">
                                    <tr>
                                        <th>Opcion</th>
                                        <th>Valores</th>
                                    </tr>
                                </table>
                            </div>

                            <p class="text-left"> <b> Numero de cifras: </b></p>
                            <select id="totalCifras" v-model="decimales" name="totalCifras" class="form-control"
                                style="height:37px; margin: 0px 0px 10px 0px; font-size: 15px;">
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


                            <p class="text-left"> <b> Aplicar margen de error: </b></p>
                            <table style="width: 100%;  margin: 0px 0px 10px;">
                                <tr>
                                    <th>
                                        <div class="checkbox">
                                            <label>
                                                <input
                                                    style="width:20px; height:20px; border:2px solid #555;"
                                                    type="checkbox" id="arriba" name="arriba" value="si"
                                                    checked>&nbsp;&nbsp;Aplicar hacia arriba
                                            </label>
                                        </div>

                                    </th>
                                    <th>
                                        <div class="checkbox">
                                            <label><input
                                                    style="width:20px; height:20px; border:2px solid #555;"
                                                    type="checkbox" id="abajo" name="abajo" value="si" checked>
                                                &nbsp;&nbsp;Aplicar hacia abajo
                                            </label>
                                        </div>
                                    </th>
                                </tr>
                            </table>


                            <p class="text-left"> <b> Margen: </b></p>
                            <input id="margen" type="number" @focus="limpiarCampos('margen')"
                                class="form-control" placeholder="margen"
                                style="height:37px; margin: 0px 0px 10px 0px; font-size: 15px;">

                            <span id="msjInputMargen"> </span>

                            <p class="text-left" for="id_tema_2"> <b> Tema: </b></p>

                            <!-- <select id="id_tema" name="temas" class="swal2-input">

                            </select> -->

                            <Select2 :options="temas" v-model="id_tema" @select="limpiarCampos('tema')"
                                id="id_tema" />
                            <span id="msjSelectTema"> </span>

                            <p class="text-left mt-2 mb-0"> <b> Imagenes: </b> </p>
                            <div @dragover="dragover" @dragleave="dragleave" @drop="drop"
                                style="border: 0.5px dashed black; width: 100%;">
                                <input type="file" id="assetsFieldHandle"
                                    class="w-px h-px opacity-0 overflow-hidden absolute" @change="onChange"
                                    ref="file" accept=".pdf,.jpg,.jpeg,.png" hidden />
                                <div class="row">
                                    <div class="col-md-12">
                                        <label for="assetsFieldHandle" class="block cursor-pointer">
                                            <div>
                                                <p id="mensajito" class="text-center">
                                                    <i class="fas fa-cloud-download-alt"></i>
                                                    Arrastra la imagen o da clic aquí para subir
                                                </p>
                                            </div>
                                        </label>
                                    </div>
                                </div>
                                <table style="list-style-type: none; width:100%"
                                    v-if="this.subidor.imagenesVistaPrevia.length" v-cloak>
                                    <tr>
                                        <th>Imagen</th>
                                        <th>Acción</th>
                                    </tr>
                                    <tr v-for="imagen in subidor.imagenesVistaPrevia">
                                        <td class="d-flex justify-content-center"> <img :src="imagen.imagen"
                                                style=" width: 15em;"> </td>
                                        <td>
                                            <button class="btn btn-danger" type="button" @click="remove(imagen)"
                                                title="Remove file">
                                                <i class="fas fa-trash-alt"></i>
                                            </button>
                                        </td>
                                    </tr>
                                </table>
                            </div>

                            <button type="button" class="btn btn-secondary float-right btn-lg mt-4 "
                                data-dismiss="modal" > <i class="fas fa-ban"></i>
                                Cerrar
                            </button>

                            <button type="button" @click="btnGuardarPregunta(GuardarEditar)"
                                class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                > <i class="fas fa-save"></i> Guardar
                            </button>

                        </div>


                    </div>
                </div>
            </div>
            <div class="modal animated animate__bounceIn" id="modalParaVerImagenes" tabindex="-1" role="dialog"
                aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content" >
                        <div class="modal-body">

                            <h3 class="modal-title" id="exampleModalLabel"> Imagenes adjuntas en la pregunta
                            </h3>
                            <div style="width: 100%;">
                                <table style="list-style-type: none; width:100%">
                                    <tr>
                                        <th>
                                            Imagen
                                        </th>
                                        <th>
                                            Nombre
                                        </th>
                                    </tr>
                                    <tr v-for="imagen in imagenesParaDesplegarEnModal">
                                        <td class="d-flex justify-content-center">
                                            <img :src="'/imagenes/preguntas/'+imagen.nombre"
                                                style=" width: 15em;">
                                        </td>
                                        <td>
                                            {{ imagen.alias }}
                                        </td>
                                    </tr>
                                </table>
                                <span v-if="imagenesParaDesplegarEnModal.length == 0" class="text-center">
                                    Esta pregunta no tiene imagenes adjuntas
                                </span>
                            </div>
                            <button type="button" data-dismiss="modal"
                                class="btn btn-secondary float-right btn-lg mt-4 " >
                                <i class="fas fa-ban"></i> Cerrar
                            </button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    import Cargador from '@/components/subirImagenes';

    export default {
        data() {
            return {
                pregunta: [],
                preguntaNumerica: [],
                vComodin: [],
                comodines: [],
                valorComodines: [],
                id: "",
                id_tema: "",
                respuesta: "",
                pregunta: "",
                margen: "",
                margend: "",
                arriba: null,
                abajo: null,
                tipo: "",
                temasSeleccionado: {},
                temas: [],
                id: "",
                nombre_tema: "",
                nivel: "",
                decimales: 0,
                GuardarEditar: 0,
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta', 'tema']
                    }
                },
                currentPage: 1,
                totalPages: 0,
                todasLasImagenes: [],
                totalImagenesEnPregunta: 0,
                ultimaImagenEnPreguntaAEditar: 0,
                imagenesParaDesplegarEnModal: [],
                subidor: {}
            };
        },
        created() {
            this.subidor = new Cargador();
        },

        mounted() {
            this.getPreguntaNumerica(), this.getTemas(), this.getMargen(), this.getComodines();
            let uri = window.location.href;
            if (uri.includes("?")) {
                uri = window.location.href.split('?');
                var fil = uri[1].split('=')[1];
                this.filters.pregunta.value = fil.replace(/%20/g, " ");
            }
        },
        methods: {
            cambioSelect(val) {
                //this.limpiarCampos("tema");
            },
            cambiarCampoDeBusqueda() {
                let x = document.getElementById("campoBusqueda").value;
                this.filters.pregunta.keys[0] = x;
            },
            async desplegarImagenesEnModal(imagenes) {
                this.imagenesParaDesplegarEnModal = imagenes;
            },
            onChange(e) {
                this.subidor.onChange(e);
            },
            remove(imagen) {
                this.subidor.remove(imagen);
            },
            dragover(event) {
                this.subidor.dragover(event);
            },
            dragleave(event) {
                this.subidor.dragleave(event);
            },
            drop(event) {
                this.subidor.drop(event);
            },
            async subirImagenes(id) {
                this.subidor.subirImagenes(id);
            },
            async getPreguntaNumerica() {
                await axios({
                    method: "GET",
                    url: "/obtenerTodasLasImagenes"
                }).then(
                    result => {
                        this.todasLasImagenes = result.data.todasImagenes[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
                await axios({
                    method: "GET",
                    url: "/pregunta/showCalculadas"
                }).then(
                    result => {
                        this.preguntaNumerica = result.data.banco_preguntas[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
                for (let i = 0; i < this.preguntaNumerica.length; i++) {
                    this.preguntaNumerica[i].imagenes = [];
                    for (let j = 0; j < this.todasLasImagenes.length; j++) {
                        if (this.preguntaNumerica[i].id_pregunta == this.todasLasImagenes[j].idpregunta) {
                            this.preguntaNumerica[i].imagenes.push(this.todasLasImagenes[j]);
                        }
                    }
                }
            },
            getComodines() {
                axios({
                    method: "GET",
                    url: "/pregunta/showVcomodines"
                }).then(
                    result => {
                        this.valorComodines = result.data.vc[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
            getTemas() {
                ///Funcion para mostrar los temas
                /*axios({
                    method: "GET",
                    url: "/tema/all"
                }).then(
                    result => {
                        this.temas = result.data;
                    },
                    error => {
                        console.error(error);
                    }
                );*/
                axios({
                    method: "GET",
                    url: "/tema/all"
                }).then(
                    result => {
                        let temasApi = result.data[0];
                        for (let i = 0; i < temasApi.length; i++) {
                            this.temas.push({
                                id: temasApi[i].id,
                                text: temasApi[i].nombre_tema
                            })
                        }
                    },
                    error => {
                        console.error(error);
                    }
                );

            },
            limpiarCampos(id) {

                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputMargen = document.getElementById("msjInputMargen");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");


                if (id == "tema") {
                    msjSelectTema.innerHTML = "";
                }

                if (id == "pregunta") {
                    document.getElementById("pregunta").style.border = "1px solid #dee2e6";
                    msjInputPregunta.innerHTML = "";
                }

                if (id == "respuesta") {
                    document.getElementById("respuesta").style.border = "1px solid #dee2e6";
                    msjInputRespuesta.innerHTML = "";
                }

                if (id == "margen") {
                    document.getElementById("margen").style.border = "1px solid #dee2e6";
                    msjInputMargen.innerHTML = "";;
                }



            },

            btnGuardarPregunta(id) {
                var vacio = false;
                var comodinesCorrecto = true;
                var pregunta = document.getElementById("pregunta").value;
                var respuesta = document.getElementById("respuesta").value;
                var margen = document.getElementById("margen").value;
                //var tema = document.getElementById("id_tema").value;
                var tema = this.id_tema;
                var aplica_arriba = document.getElementById("arriba").checked ? 1 : 0;
                var aplica_abajo = document.getElementById("abajo").checked ? 1 : 0;


                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputMargen = document.getElementById("msjInputMargen");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");


                this.valorComodines = [];
                for (var i = 0; i < this.comodines.length; i++) {
                    var input = document.getElementById(i).value;
                    if (input == "")
                        vacio = true;
                }
                if (vacio == true || pregunta == "" || respuesta == "" || this.id_tema == "") {

                    if (this.id_tema == "") {
                        msjSelectTema.innerHTML = "Este dato es obligatorio";
                        msjSelectTema.style.color = "#ff6258";
                    }

                    if (pregunta == "") {
                        document.getElementById("pregunta").style.border = "1px solid #ff6258";
                        msjInputPregunta.innerHTML = "Este dato es obligatorio";
                        msjInputPregunta.style.color = "#ff6258";
                    }

                    if (respuesta == "") {
                        document.getElementById("respuesta").style.border = "1px solid #ff6258";
                        msjInputRespuesta.innerHTML = "Este dato es obligatorio";
                        msjInputRespuesta.style.color = "#ff6258";
                    }

                    if (margen == "") {
                        document.getElementById("margen").style.border = "1px solid #ff6258";
                        msjInputMargen.innerHTML = "Este dato es obligatorio";
                        msjInputMargen.style.color = "#ff6258";
                    }

                    /*this.$swal({
                        type: 'error',
                        title: '¡Datos incompletos!'
                    })*/

                } else {
                    for (var i = 0; i < this.comodines.length; i++) {
                        var vcomodin = document.getElementById(i).value;
                        this.valorComodines[i] = vcomodin;
                        var separada = vcomodin.trim().split("~");
                        var incorrecto = false;
                        var number = /^\-{0,1}(?:[0-9]+){0,1}(?:\.[0-9]+){0,1}$/i;
                        var regex = RegExp(number);
                        if (separada.length != 2)
                            incorrecto = true;
                        else {
                            if (!(regex.test(separada[0]) && separada[0].length > 0))
                                if (separada[0] >= separada[1])
                                    incorrecto = true;

                                else
                            if (!(regex.test(separada[1]) && separada[1].length > 0))
                                if (separada[0] >= separada[1])
                                    incorrecto = true;
                            if (!incorrecto)
                                if (parseInt(separada[0]) >= parseInt(separada[1]))
                                    incorrecto = true;

                        }
                        if (incorrecto) {
                            input = document.getElementById(i).value;
                            separada = input.split(",")
                            incorrecto = false;
                            for (var j = 0; j < separada.length; j++) {
                                if (!(regex.test(separada[j]) && separada[j].length > 0))
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
                    if (comodinesCorrecto) {
                        for (var i = 0; i < this.valorComodines.length; i++)
                            var ruta = "";
                        if (id == -1) {
                            ruta = '/preguntaCalculada/store';
                        } else {
                            ruta = '/preguntaCalculada/update'
                        }
                        var imagen;
                        axios.post(ruta, {
                                rectivo: pregunta,
                                respuesta: respuesta,
                                comodines: this.comodines,
                                valorComodines: this.valorComodines,
                                tema: tema,
                                decimales: this.decimales,
                                id: id,
                                margen: margen,
                                arriba: aplica_arriba,
                                abajo: aplica_abajo,
                                imagen: imagen,
                                imagenesAEliminar: this.subidor.imagenesAEliminar
                            })
                            .then(async (res) => {

                                this.$swal.fire({
                                    position: 'top-end',
                                    icon: 'success',
                                    title: 'Información almacenada con éxito',
                                    showConfirmButton: false,
                                    timer: 1500,
                                    toast: true
                                })
                                const modals = document.getElementsByClassName('modal');
                                this.getComodines();
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

                                if (id == -1) {
                                    await this.subirImagenes(res.data.ultimo_id);
                                } else {
                                    await this.subirImagenes(id);
                                }


                                this.getPreguntaNumerica();
                            })
                    }
                }
            },
            ExpresionCorrecta() {
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
                            "decbin (") != -1 || entrada.indexOf("decoct (") != -1 || entrada.indexOf("deg2rad (") != -
                        1 ||
                        entrada.indexOf("exp (") != -1 || entrada.indexOf("expm1 (") != -1 || entrada.indexOf(
                            "floor (") != -1 || entrada.indexOf("fmod (") != -1 || entrada.indexOf("is_finite (") != -
                        1 ||
                        entrada.indexOf("is_infinite (") != -1 || entrada.indexOf("is_nan (") != -1 || entrada.indexOf(
                            "log10 (") != -1 || entrada.indexOf("log1p (") != -1 || entrada.indexOf("log (") != -1 ||
                        entrada.indexOf("max (") != -1 || entrada.indexOf("min (") != -1 || entrada.indexOf(
                            "octdec (") != -1 || entrada.indexOf("pi (") != -1 || entrada.indexOf("pow (") != -1 ||
                        entrada
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
                var operacion = document.getElementById("respuesta").value.toLowerCase().trim(),
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
                                    errorEncontrado.innerHTML = "parentesis incorrectos";
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
                    //console.log(operacion)
                    //-------------
                    if (operacionIncorrecta == false && ReducirExpresion(operacion) != "dec" && ReducirExpresion(
                            operacion) != "bin" && ReducirExpresion(operacion) != "oct") {
                        errorEncontrado.innerHTML = "Error de sintaxis.";
                        operacionIncorrecta = true;
                    }
                } else {
                    operacionIncorrecta = true;
                }
                this.comodines = [];
                var table = document.getElementById("opciones");
                while (table.firstChild) {
                    table.removeChild(table.lastChild);
                }

                if (!operacionIncorrecta == true)
                    this.DetectarComodines()
            },
            DetectarComodines() {
                this.comodines = [];
                var expresion = document.getElementById("respuesta").value;
                var table = document.getElementById("opciones");
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
                        for (var j = 0; j < this.comodines.length; j++) {
                            if (this.comodines[j] == contenido)
                                encontrado = true;
                        }
                        if (!encontrado)
                            this.comodines.push(contenido);
                        else
                            encontrado = false;
                        contenido = "";
                    }
                }
                for (var i = 0; i < this.comodines.length; i++) {
                    var row = table.insertRow(-1);

                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    cell1.innerHTML = "" + this.comodines[i];
                    let entrada = document.createElement('input');
                    entrada.type = "text";
                    entrada.id = i;
                    cell2.appendChild(entrada);
                }
            },
            getMargen() {
                ///Funcion para mostrar los temas
                axios({
                    method: "GET",
                    url: "/configuracionCuestionario/margen"
                }).then(
                    result => {
                        this.margend = result.data.rango_por_defecto;

                    },
                    error => {
                        console.error(error);
                    }
                );
            },

            abrirModal: async function (id, imagenes) {


                this.subidor.imagenesVistaPrevia = [];
                this.subidor.imagenes = [];
                this.subidor.imagenesAEliminar = [];
                this.getMargen();

                var tituloModal = document.getElementById("exampleModalLabel");
                if (id == -1) {
                    tituloModal.innerHTML = "<b>Registrar pregunta</b>"
                } else {
                    tituloModal.innerHTML = "<b>Editar pregunta</b>"

                    let numeroMayorDeImagen = 0;
                    for (let i = 0; i < imagenes.length; i++) {
                        this.subidor.acomodarImagen("/imagenes/preguntas/" + imagenes[i].nombre, 1, imagenes[i]
                            .idImagen);
                        if (imagenes[i].alias.split("_")[3].split(".")[0] > numeroMayorDeImagen) {
                            numeroMayorDeImagen = imagenes[i].alias.split("_")[3].split(".")[0];
                        }
                    }

                    this.subidor.ultimaImagenEnPreguntaAEditar = numeroMayorDeImagen;


                }

                /*var x = document.getElementById("id_tema");

                var length = x.options.length;
                for (i = length - 1; i >= 0; i--) {
                    x.options[i] = null;
                }

                for (var i = 0; i < this.temas[0].length; i++) {
                    var option = document.createElement("option");
                    option.text = this.temas[0][i].nombre_tema;
                    option.value = this.temas[0][i].id;
                    option.id = "tema_" + this.temas[0][i].id;
                    x.add(option);
                }*/

                document.getElementById("errorEncontrado").innerHTML = "";

                //Limpiar el reactivo
                var pregunta = document.getElementById("pregunta");
                var respuesta = document.getElementById("respuesta");
                var margen = document.getElementById("margen");
                var aplica_arriba = document.getElementById("arriba");
                var aplica_abajo = document.getElementById("abajo");

                var table = document.getElementById("opciones");
                while (table.firstChild) {
                    table.removeChild(table.lastChild);
                }

                //se quitan los atributos selected de los select
                for (var i = 0; i < 10; i++)
                    document.getElementById(i + "_decimal").removeAttribute("selected");

                //for (var i = 0; i < this.preguntaNumerica.length; i++)
                //    document.getElementById("tema_" + this.preguntaNumerica[i].id_tema).removeAttribute("selected");

                if (id == -1) {
                    this.GuardarEditar = -1;
                    pregunta.value = "";
                    respuesta.value = "";

                    var opcionDecimal = document.getElementById("0_decimal")
                    opcionDecimal.setAttribute("selected", "");

                    aplica_arriba.checked = true;
                    aplica_abajo.checked = true;
                    margen.value = "0.1";
                } else {
                    this.GuardarEditar = id;

                    var id_opcion;
                    for (i = 0; i < this.preguntaNumerica.length; i++) {
                        if (this.preguntaNumerica[i].id_pregunta == id) {
                            pregunta.value = this.preguntaNumerica[i].pregunta;
                            respuesta.value = this.preguntaNumerica[i].opcion;
                            margen.value = this.preguntaNumerica[i].rango;
                            aplica_arriba.checked = this.preguntaNumerica[i].aplicableArriba;
                            aplica_abajo.checked = this.preguntaNumerica[i].aplicableAnbajo;
                            id_opcion = this.preguntaNumerica[i].id_opcion;

                            this.id_tema = this.preguntaNumerica[i].id_tema;
                            /*var opcionTema = document.getElementById("tema_" + this.preguntaNumerica[i].id_tema);
                            opcionTema.setAttribute("selected", "");*/

                            var opcionDecimal = document.getElementById(this.preguntaNumerica[i].decimales +
                                "_decimal")
                            opcionDecimal.setAttribute("selected", "");

                            i = this.preguntaNumerica.length;
                        }
                    }

                    this.comodines = [];
                    var indiceAux = 0;
                    for (var i = 0; i < this.valorComodines.length; i++) {
                        if (this.valorComodines[i].id_opcion == id_opcion) {
                            var row = table.insertRow(-1);
                            var cell1 = row.insertCell(0);
                            var cell2 = row.insertCell(1);
                            cell1.innerHTML = "" + this.valorComodines[i].comodin;
                            this.comodines.push(this.valorComodines[i].comodin);
                            let entrada = document.createElement('input');
                            entrada.type = "text";
                            entrada.id = indiceAux;
                            entrada.value = this.valorComodines[i].valor_comodin;
                            cell2.appendChild(entrada);
                            indiceAux++;
                        }
                    }
                }

            },

            guardarPregunta(pregunta, respuesta, margen, arriba, abajo, tipo, id_tema) {
                ///Funcion para guardar los temas
                axios
                    .post("/pregunta/addNumerica", {
                        pregunta: pregunta,
                        respuesta: respuesta,
                        margen: margen,
                        arriba: arriba,
                        abajo: abajo,
                        tipo: tipo,
                        id_tema: this.id_tema
                    })
                    .then(res => {
                        this.tipo = "";
                        this.respuesta = "";
                        this.pregunta = "";
                        this.margen = "";
                        this.id_tema = "";
                        this.getPreguntaNumerica();
                        //console.log(res);
                    })
                    .catch(err => {
                        console.log(err);
                    });
            },
            editar(id, pregunta, respuesta, tipo, id_tema) {
                axios
                    .post("/pregunta/updateSinOpciones", {
                        id: id,
                        pregunta: pregunta,
                        respuesta: respuesta,
                        tipo: tipo,
                        id_tema: this.id_tema
                    })
                    .then(res => {
                        this.id = "";
                        this.tipo = "";
                        this.respuesta = "";
                        this.pregunta = "";
                        this.id_tema = "";
                        this.getPreguntaNumerica();
                        //console.log(res);
                    })
                    .catch(err => {
                        console.log(err);
                    });
            },

            eliminarCalculadas(id, imagenes) {
                this.$swal.fire({
                    html: `<h3 style="color:#212529;">¿Realmente desea eliminar esta pregunta?</h3>`,
                    showCancelButton: true,
                    confirmButtonColor: '#dc3545',
                    cancelButtonColor: '#6C757D',
                    confirmButtonText: '<i class="fas fa-trash"></i> Eliminar',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                }).then((result) => {
                    if (result.value) {

                        axios
                            .post("/preguntaCalculada/delete", {
                                id: id,
                                imagenesAEliminar: imagenes
                            })
                            .then(res => {
                                this.id = "";
                                this.getPreguntaNumerica();
                                //console.log(res);
                                this.$swal.fire({
                                    position: 'top-end',
                                    icon: 'success',
                                    title: 'Información eliminada con éxito',
                                    showConfirmButton: false,
                                    timer: 1500,
                                    toast: true
                                })
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
        }
    };

</script>
