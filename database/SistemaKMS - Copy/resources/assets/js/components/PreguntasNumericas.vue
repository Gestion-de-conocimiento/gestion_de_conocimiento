<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Preguntas</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd"> <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
                            </span> <span style="color: #bdb9bd"> Preguntas <i class="fas fa-angle-right"></i> </span>
                            <b>Numéricas </b>

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
                                <h3 class="card-title mt-2"> <b> Preguntas Numericas </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                        <button type="button" class="btn btn-primary float-right"  data-toggle="modal"
                                            data-target="#registrarPregunta" @click="cambiarModo">
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
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                        <thead slot="head">
                                            <v-th sortKey="pregunta" defaultSort="desc" style="width:10%">Pregunta
                                            </v-th>
                                            <v-th sortKey="tema" defaultSort="desc">Tema</v-th>
                                            <v-th sortKey="opcion" defaultSort="desc">Respuesta</v-th>
                                            <th>Margen</th>
                                            <th>Margen arriba</th>
                                            <th>Margen abajo</th>
                                            <th>Imagenes</th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="preguntaNumerica in displayData" :key="preguntaNumerica.id">
                                                <td>{{preguntaNumerica.pregunta}} </td>
                                                <td>{{preguntaNumerica.tema}}</td>
                                                <td>{{preguntaNumerica.opcion}} </td>
                                                <td>{{preguntaNumerica.rango}}</td>
                                                <td v-if="preguntaNumerica.aplicableArriba == true"> <i
                                                        class="far fa-check-circle" style="color: #3bd949;"></i> Si <span
                                                        style="color: #3bd949;"></span> </td>
                                                <td v-else> <i class="fas fa-ban" style="color: #ff6258"></i> No <span
                                                        style="color: #ff6258"></span> </td>
                                                <td v-if="preguntaNumerica.aplicableAnbajo == true"> <i
                                                        class="far fa-check-circle" style="color: #3bd949;"></i> Si <span
                                                        style="color: #3bd949;"></span> </td>
                                                <td v-else> <i class="fas fa-ban" style="color: #ff6258"> </i> No <span
                                                        style="color: #ff6258"></span> </td>
                                                <td>
                                                    <a data-toggle="modal" data-target="#modalParaVerImagenes"
                                                        @click="desplegarImagenesEnModal(preguntaNumerica.imagenes)" class="btn btn-outline-primary">
                                                        <i class="fas fa-eye" style="color: #2196f3"
                                                            title="Ver imagenes adjuntas a la pregunta"></i> <span
                                                            style="color: #2196f3"></span>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="btnEditar(preguntaNumerica.id_pregunta,preguntaNumerica.pregunta,preguntaNumerica.opcion,preguntaNumerica.tipo,preguntaNumerica.id_tema, preguntaNumerica.rango ,preguntaNumerica.imagenes)"
                                                        data-toggle="modal" data-target="#registrarPregunta" class="btn btn-outline-warning"><i
                                                            class="fas fa-pen" style="color: #ffae00;"
                                                            title="Editar la pregunta"></i> <span
                                                            style="color: #ffae00;"></span>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="eliminar(preguntaNumerica.id_pregunta, preguntaNumerica.imagenes)" class="btn btn-outline-danger"><i
                                                            class="fas fa-trash" style="color: #ff6258"
                                                            title="Eliminar la pregunta"></i> <span
                                                            style="color: #ff6258"></span>
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

                <div class="row">
                    <div class="modal animated animate__bounceIn" id="registrarPregunta" role="dialog"
                        aria-labelledby="exampleModalLabel" aria-hidden="true" data-focus="false">
                        <div class="modal-dialog modal-dialog-centered" role="document">
                            <div class="modal-content">
                                <div class="modal-body">
                                    <h3 v-if="modoEdicion" class="modal-title" id="exampleModalLabel">
                                        Actualizar pregunta </h3>
                                    <h3 v-else class="modal-title" id="exampleModalLabel"> Registrar
                                        pregunta </h3>

                                    <p class="text-left mt-0 mb-0"> <b>Pregunta <span
                                                style="color:red">*</span>:</b> </p>
                                    <textarea rows="4" id="pregunta" type="text"
                                        class="form-control mt-0 mb-0" placeholder="Pregunta"
                                        @focus="limpiarCampos('pregunta')"></textarea>
                                    <span id="msjInputPregunta"> </span>

                                    <p class="text-left mt-0 mb-0"><b>Respuesta: <span
                                                style="color:red">*</span>:</b></p>
                                    <textarea rows="1" id="respuesta" type="text"
                                        class="form-control mt-0 mb-0" placeholder="Respuesta"
                                        @focus="limpiarCampos('respuesta')"></textarea>
                                    <span id="msjInputRespuesta"> </span>

                                    <p class="text-left mt-0 mb-0"><b>Margen de error: <span
                                                style="color:red">*</span>:</b></p>
                                    <input id="margen" placeholder="margen" type="number"
                                        @focus="limpiarCampos('margen')" class="form-control mt-0 mb-0">
                                    <span id="msjInputMargen"> </span>

                                    <p class="text-left mt-0 mb-0"> <b>Aplicar el margen:</b> </p>

                                    <table style="width: 100%; margin: 0px 0px 10px;">
                                        <tr>
                                            <th>
                                                <div class="checkbox">
                                                    <label>
                                                        <input
                                                            style="width:20px; height:20px; border:2px solid #555;"
                                                            type="checkbox" id="arriba" name="arriba"
                                                            value="si" checked>&nbsp;&nbsp;Aplicar hacia
                                                        arriba
                                                    </label>
                                                </div>

                                            </th>
                                            <th>
                                                <div class="checkbox">
                                                    <label><input
                                                            style="width:20px; height:20px; border:2px solid #555;"
                                                            type="checkbox" id="abajo" name="abajo"
                                                            value="si" checked>
                                                        &nbsp;&nbsp;Aplicar hacia abajo
                                                    </label>
                                                </div>
                                            </th>
                                        </tr>
                                    </table>

                                    <p class="text-left mt-0 mb-0"><b>Tema: <span
                                                style="color:red">*</span>: </b></p>
                                    <Select2 :options="temas" v-model="id_tema"
                                        @select="cambioSelect($event)" id="id_tema" />

                                    <span id="msjSelectTema"> </span>

                                    <p class="text-left mt-0 mb-0" style="margin-top: 8px;"> <b>
                                            Imagenes:</b> </p>
                                    <div @dragover="dragover" @dragleave="dragleave" @drop="drop"
                                        style="border: 0.5px dashed black; width: 100%;">
                                        <input type="file" id="assetsFieldHandle"
                                            class="w-px h-px opacity-0 overflow-hidden absolute"
                                            @change="onChange" ref="file" accept=".pdf,.jpg,.jpeg,.png"
                                            hidden />
                                        <div class="row">
                                            <div class="col-md-12">
                                                <label for="assetsFieldHandle" class="block cursor-pointer">
                                                    <p id="mensajito" class="text-center">
                                                        <i class="fas fa-cloud-download-alt"></i> Arrastra
                                                        la imagen
                                                        o da clic aquí para subir
                                                    </p>
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
                                                <td class="d-flex justify-content-center"> <img
                                                        :src="imagen.imagen" style=" width: 15em;"> </td>
                                                <td>
                                                    <a @click="remove(imagen)" title="Eliminar la imagen">
                                                        <i class="fas fa-trash-alt"
                                                            style="color: #ff6258"></i> </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                    <p class="text-left mt-0 mb-0" style="font-size: 12px;"> <span
                                            style="color:red">*</span> Datos obligatorios </p>

                                    <button type="button" class="btn btn-secondary float-right btn-lg mt-4 "
                                        data-dismiss="modal"> <i
                                            class="fas fa-ban"></i> Cerrar
                                    </button>
                                    <button v-if="modoEdicion" type="button" @click="editar" class="btn btn-primary float-right btn-lg mt-4 mr-2" >
                                        <i class="fas fa-save"></i> Guardar 
                                    </button>
                                    <button v-else type="button" @click="btnGuardar" class="btn btn-primary float-right btn-lg mt-4 mr-2" > 
                                        <i class="fas fa-save"></i> Guardar
                                    </button>
                                </div>

                            </div>
                        </div>
                    </div>

                    <div class="modal animated animate__bounceIn" id="modalParaVerImagenes" tabindex="-1"
                        role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered" role="document">
                            <div class="modal-content">
                                <div class="modal-body">
                                    <h3 class="modal-title" id="exampleModalLabel"> Imagenes adjuntas en la
                                        pregunta
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
                                        <span v-if="imagenesParaDesplegarEnModal.length == 0"
                                            class="text-center"> <b> Esta pregunta no tiene imagenes
                                                adjuntas </b> </span>
                                    </div>

                                    <button type="button" data-dismiss="modal"
                                        class="btn btn-secondary float-right btn-lg mt-4 "> <i
                                            class="fas fa-ban"></i> Cerrar
                                    </button>

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
    import Cargador from '@/components/subirImagenes';
    export default {
        data() {
            return {
                subidor: {},
                pregunta: [],
                preguntaNumerica: [],
                id: "",
                id_tema: "",
                respuesta: "",
                pregunta: "",
                margen: "",
                margend: "",
                arriba: null,
                abajo: null,
                tipo: 2,
                temas: [],
                id: "",
                nombre_tema: "",
                nivel: "",
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta', 'tema']
                    }
                },
                currentPage: 1,
                totalPages: 0,
                modoEdicion: 0,
                todasLasImagenes: [],
                totalImagenesEnPregunta: 0,
                imagenesParaDesplegarEnModal: []
            };
        },
        created() {
            this.subidor = new Cargador();
        },
        mounted() {
            this.getPreguntaNumerica();
            this.getTemas();
            this.getMargen();
            let uri = window.location.href;
            if (uri.includes("?")) {
                uri = window.location.href.split('?');
                var fil = uri[1].split('=')[1];
                this.filters.pregunta.value = fil.replace(/%20/g, " ");
            }
        },
        methods: {
            cambioSelect(val) {
                this.limpiarCampos("tema");
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
            async acomodarImagen(imagen, vaAEliminarse, idImagen) {
                this.subidor.acomodarImagen(imagen, vaAEliminarse, idImagen);
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
                    url: "/pregunta/showPN"
                }).then(
                    result => {
                        this.preguntaNumerica = result.data[0];
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
            getTemas() {
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
            getMargen() {
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
            async guardarPregunta(pregunta, respuesta, margen, arriba, abajo, tipo, id_tema) {
                await axios
                    .post("/pregunta/addNumerica", {
                        pregunta: pregunta,
                        respuesta: respuesta,
                        margen: margen,
                        arriba: arriba,
                        abajo: abajo,
                        tipo: tipo,
                        id_tema: id_tema
                    })
                    .then(async res => {
                        this.respuesta = "";
                        this.pregunta = "";
                        this.margen = "";
                        this.id_tema = "";
                        await this.subidor.subirImagenes(res.data.ultimo_id);
                        $('#registrarPregunta').modal('toggle');
                        this.getPreguntaNumerica();
                    })
                    .catch(err => {
                        console.log(err);
                    });
            },
            btnGuardar() {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let inputMargen = document.getElementById("margen");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputMargen = document.getElementById("msjInputMargen");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                this.margen = document.getElementById("margen").value;
                this.arriba = document.getElementById("arriba").checked;
                this.abajo = document.getElementById("abajo").checked;
                this.pregunta = inputPregunta.value;
                this.respuesta = inputRespuesta.value.toString().toLowerCase().normalize("NFD").replace(
                    /[\u0300-\u036f]/g, "").replace(/ /g, "")
                if (this.id_tema == "" || this.pregunta == "" || this.respuesta == "" || this.margen == "") {
                    if (this.id_tema == "") {
                        selectTema.style.border = "1px solid #ff6258";
                        msjSelectTema.innerHTML = "Este dato es obligatorio";
                        msjSelectTema.style.color = "#ff6258";
                    }
                    if (this.pregunta == "") {
                        inputPregunta.style.border = "1px solid #ff6258";
                        msjInputPregunta.innerHTML = "Este dato es obligatorio";
                        msjInputPregunta.style.color = "#ff6258";
                    }
                    if (this.respuesta == "") {
                        inputRespuesta.style.border = "1px solid #ff6258";
                        msjInputRespuesta.innerHTML = "Este dato es obligatorio";
                        msjInputRespuesta.style.color = "#ff6258";
                    }

                    if (this.margen == "") {
                        inputMargen.style.border = "1px solid #ff6258";
                        msjInputMargen.innerHTML = "Este dato es obligatorio";
                        msjInputMargen.style.color = "#ff6258";
                    }
                } else {
                    this.guardarPregunta(
                        this.pregunta,
                        this.respuesta,
                        this.margen,
                        this.arriba,
                        this.abajo,
                        this.tipo,
                        this.id_tema
                    );
                }
            },
            limpiarCampos(id) {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let inputMargen = document.getElementById("margen");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                let msjInputMargen = document.getElementById("msjInputMargen");
                if (id == "tema") {
                    selectTema.style.border = "1px solid #dee2e6";
                    msjSelectTema.innerHTML = "";
                }
                if (id == "pregunta") {
                    inputPregunta.style.border = "1px solid #dee2e6";
                    msjInputPregunta.innerHTML = "";
                }
                if (id == "respuesta") {
                    inputRespuesta.style.border = "1px solid #dee2e6";
                    msjInputRespuesta.innerHTML = "";
                }
                if (id == "margen") {
                    inputMargen.style.border = "1px solid #dee2e6";
                    msjInputMargen.innerHTML = "";

                }
            },
            btnEditar(id, pregunta, respuesta, tipo, id_tema, margen, imagenes) {
                this.totalImagenesEnPregunta = (imagenes.length + 1);
                this.subidor.imagenesVistaPrevia = [];
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let inputMargen = document.getElementById("margen");
                this.modoEdicion = 1;
                this.id = id;
                inputRespuesta.value = respuesta;
                inputPregunta.value = pregunta;
                this.id_tema = id_tema;
                inputMargen.value = margen;

                let numeroMayorDeImagen = 0;
                for (let i = 0; i < imagenes.length; i++) {
                    this.subidor.acomodarImagen("/imagenes/preguntas/" + imagenes[i].nombre, 1, imagenes[i].idImagen);
                    if (imagenes[i].alias.split("_")[3].split(".")[0] > numeroMayorDeImagen) {
                        numeroMayorDeImagen = imagenes[i].alias.split("_")[3].split(".")[0];
                    }
                }
                this.subidor.ultimaImagenEnPreguntaAEditar = numeroMayorDeImagen;
                this.limpiarCampos("tema");
                this.limpiarCampos("pregunta");
                this.limpiarCampos("respuesta");
            },
            cambiarModo() {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let inputMargen = document.getElementById("margen");
                inputMargen.value = this.margend;
                inputRespuesta.value = "";
                inputPregunta.value = "";
                this.id_tema = "";
                this.subidor.imagenesVistaPrevia = [];
                this.subidor.imagenes = [];
                this.subidor.imagenesAEliminar = [];
                this.modoEdicion = 0;

                this.limpiarCampos("tema");
                this.limpiarCampos("pregunta");
                this.limpiarCampos("respuesta");
                this.limpiarCampos("margen");
            },
            editar() {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                this.margen = document.getElementById("margen").value;
                this.arriba = document.getElementById("arriba").checked;
                this.abajo = document.getElementById("abajo").checked;
                this.pregunta = inputPregunta.value;
                this.respuesta = inputRespuesta.value.toString().toLowerCase().normalize("NFD").replace(
                    /[\u0300-\u036f]/g, "").replace(/ /g, "")
                if (this.id_tema == "" || this.pregunta == "" || this.respuesta == "" || this.margen == "") {
                    if (this.id_tema == "") {
                        selectTema.style.border = "1px solid #ff6258";
                        msjSelectTema.innerHTML = "Este dato es obligatorio";
                        msjSelectTema.style.color = "#ff6258";
                    }
                    if (this.pregunta == "") {
                        inputPregunta.style.border = "1px solid #ff6258";
                        msjInputPregunta.innerHTML = "Este dato es obligatorio";
                        msjInputPregunta.style.color = "#ff6258";
                    }
                    if (this.respuesta == "") {
                        inputRespuesta.style.border = "1px solid #ff6258";
                        msjInputRespuesta.innerHTML = "Este dato es obligatorio";
                        msjInputRespuesta.style.color = "#ff6258";
                    }
                    if (this.margen == "") {
                        inputMargen.style.border = "1px solid #ff6258";
                        msjInputMargen.innerHTML = "Este dato es obligatorio";
                        msjInputMargen.style.color = "#ff6258";
                    }

                } else {
                    axios.post("/pregunta/updateAbierta", {
                        id: this.id,
                        pregunta: this.pregunta,
                        respuesta: this.respuesta,
                        tipo: this.tipo,
                        id_tema: this.id_tema,
                        imagenesAEliminar: this.subidor.imagenesAEliminar,
                        mArriba: this.arriba,
                        mAbajo: this.abajo,
                        margen: this.margen
                    }).then(async () => {
                        await this.subidor.subirImagenes(this.id);
                        await this.getPreguntaNumerica();
                        this.id = "";
                        this.respuesta = "";
                        this.pregunta = "";
                        this.id_tema = "";
                        this.arriba = "";
                        this.abajo = "";

                        this.$swal.fire({
                            position: 'top-end',
                            icon: 'success',
                            title: 'Pregunta actualizada con éxito',
                            showConfirmButton: false,
                            timer: 1500,
                            toast: true
                        })

                        $('#registrarPregunta').modal('toggle');
                    })
                    .catch(err => {
                        console.error(err);
                    });
                }
            },
            eliminar(id, imagenes) {
                this.$swal.fire({
                    html: `<h3 style="color:#212529;">¿Realmente desea eliminar esta pregunta?</h3>`,
                    showCancelButton: true,
                    confirmButtonColor: '#dc3545',
                    cancelButtonColor: '#6C757D',
                    confirmButtonText: '<i class="fas fa-trash"></i> Eliminar',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                }).then((result) => {
      //              console.log(result.value);
                    if (result.value) {
                        axios.post("/pregunta/delete", {
                            id: id,
                            imagenesAEliminar: imagenes
                            
                        })
                        .then(() => {
                            console.log("entre "+id);
                            this.id = "";
                            this.getPreguntaNumerica();
                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Pregunta eliminada con éxito',
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
            }
        }
    };

</script>
