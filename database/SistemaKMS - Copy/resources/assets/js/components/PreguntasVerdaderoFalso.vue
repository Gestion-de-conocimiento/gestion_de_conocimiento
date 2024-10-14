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
                            <span style="color: #bdb9bd"> <i class="fas fa-home"></i> <i class="fas fa-angle-right">
                                </i> </span> <span style="color: #bdb9bd"> Preguntas <i class="fas fa-angle-right"> </i>
                            </span> <b>Verdadero / Falso </b>
                        </ol>
                    </div><!-- /.col -->
                </div><!-- /.row -->
            </div><!-- /.container-fluid -->
        </div>

        <section class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12 ">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b> Preguntas verdadero / Falso </b> </h3>
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
                                    <v-table :data="pregunta" :filters="filters" :currentPage.sync="currentPage" :pageSize="5"
                                        @totalPagesChanged="totalPages = $event" style="width:100%" class="table table-hover">
                                        <thead slot="head">
                                            <v-th sortKey="pregunta" defaultSort="desc">Pregunta</v-th>
                                            <v-th sortKey="tema" defaultSort="desc">Tema</v-th>
                                            <v-th sortKey="opcion" defaultSort="desc">Respuesta</v-th>
                                            <th>Imagenes </th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="pregunta in displayData" :key="pregunta.id">
                                                <td v-html="espaciarTexto(pregunta.pregunta)"> </td>
                                                <td class="text-left">{{pregunta.tema}}</td>
                                                <td> {{pregunta.opcion}} </td>
                                                <td>
                                                    <a data-toggle="modal" data-target="#modalParaVerImagenes"
                                                        @click="desplegarImagenesEnModal(pregunta.imagenes)" class="btn btn-outline-primary">
                                                        <i class="fas fa-eye" style="color: #2196f3"></i>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a
                                                        @click="editarPregunta({id:pregunta.id_pregunta, pregunta: pregunta.pregunta, respuesta: pregunta.opcion, tipo: 3, tema:pregunta.id_tema}, pregunta.imagenes)" class="btn btn-outline-warning">
                                                        <i class="fas fa-pen" style="color: #ffae00;"></i>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="eliminarPregunta(pregunta.id_pregunta, pregunta.imagenes )" class="btn btn-outline-danger">
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
                        </div>
                    </div>
                </div>


                <div class="modal animated animate__bounceIn" id="registrarPregunta" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true" data-focus="false">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content" >

                            <div class="modal-body">
                                <h3 v-if="modoEdicion" class="modal-title" id="exampleModalLabel"> Actualizar
                                    pregunta </h3>
                                <h3 v-else class="modal-title" id="exampleModalLabel"> Registrar pregunta </h3>


                                <p class="text-left mb-0"> <b> Pregunta: </b> </p>
                                <textarea rows="4" v-model="form.pregunta" id="inpPregunta" type="text"
                                    class="form-control mt-0 mb-0" placeholder="Pregunta"
                                    @focus="limpiarCampo('pregunta')"
                                    style="margin:0px; font-size: 15px; line-height: 20px;"></textarea>

                                <span id="msjInputPregunta" style="color: #ff6258;"> </span>

                                <p class="text-left mt-2 mb-0"> <b> Respuesta: </b> </p>
                                <select v-model="form.respuesta" id="selRespuesta" class="form-control mt-0 mb-0"
                                    @focus="limpiarCampo('respuesta')">
                                    <option value="">Respuesta</option>
                                    <option value="verdadero">Verdadero</option>
                                    <option value="falso">Falso</option>
                                </select>
                                <span id="msjInputRespuesta" style="color: #ff6258;"> </span>

                                <p class="text-left mt-2 mb-0"> <b> Tema: </b> </p>
                                <Select2 :options="this.temas" v-model="id_tema" @select="cambioSelect($event)"
                                    id="id_tema" />

                                <span id="msjSelectTema" style="color: #ff6258;"> </span>

                                <p class="text-left mt-2 mb-0"> <b> Imagenes: </b> </p>
                                <div @dragover="dragover" @dragleave="dragleave" @drop="drop"
                                    style="border: 0.5px solid #dee2e6; width: 100%;">
                                    <input type="file" id="assetsFieldHandle" class="w-px h-px opacity-0 overflow-hidden absolute" @change="onChange"
                                        ref="file" accept=".pdf,.jpg,.jpeg,.png" hidden />
                                    <div class="row">
                                        <div class="col-md-12 text-center">
                                            <label for="assetsFieldHandle" id="mensajito" class="block cursor-pointer">
                                                <i class="fas fa-cloud-download-alt"></i>
                                                Arrastra la imagen o da clic aquí para subir
                                            </label>
                                        </div>
                                    </div>
                                    <table class="table table-hover" v-if="this.subidor.imagenesVistaPrevia.length" v-cloak>
                                        <tr>
                                            <th class="text-center">Imagen</th>
                                            <th class="text-center">Acción</th>
                                        </tr>
                                        <tr v-for="imagen in subidor.imagenesVistaPrevia">
                                            <td class="d-flex justify-content-center"> 
                                                <img :src="imagen.imagen"style=" width: 15em;"> 
                                            </td>
                                            <td>
                                                <a @click="remove(imagen)" title="Eliminar la imagen" class="btn btn-outline-danger"> 
                                                    <i class="fas fa-trash-alt" style="color: #ff6258"></i> 
                                                </a>
                                            </td>
                                        </tr>
                                    </table>
                                </div>



                                <button type="button" class="btn btn-secondary float-right btn-lg mt-4 " data-dismiss="modal">
                                    <i class="fas fa-ban"></i> Cancelar
                                </button>
                                <button v-if="modoEdicion" type="button" @click="actualizarPregunta" class="btn btn-primary float-right btn-lg mt-4 mr-2" >
                                    <i class="fas fa-save"></i> Editar
                                </button>
                                <button v-else type="button" @click="registrarPregunta" class="btn btn-primary float-right btn-lg mt-4 mr-2">
                                    <i class="fas fa-save"></i> Guardar
                                </button>


                            </div>

                        </div>
                    </div>
                </div>

                <div class="modal animated animate__bounceIn" id="modalParaVerImagenes" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">

                            <div class="modal-body">

                                <h3 class="modal-title" id="exampleModalLabel">
                                    Imagenes adjuntas en la pregunta
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
        </section>

    </div>
</template>

<script>
    import axios from 'axios';
    import Cargador from '@/components/subirImagenes';
    import Select2 from 'v-select2-component';

    export default {
        components: {
            Select2
        },
        data() {
            return {
                modoEdicion: 0,
                todasLasImagenes: [],
                totalImagenesEnPregunta: 0,
                imagenesParaDesplegarEnModal: [],
                subidor: {},
                pregunta: [],
                
                currentPage: 1,
                totalPages: 0,
                temas: [],
                id_tema:'' ,
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta', 'tema']
                    }
                },
                form: new Form({
                    id: '',
                    tipo: 3,
                    pregunta: '',
                    respuesta: '',
                    tema: ''
                }),
                myValue: '',
                myOptions: ['opc1', 'opc2', 'opc3'] // or [{id: key, text: value}, {id: key, text: value}]
            }
        },
        created() {
            this.subidor = new Cargador();

        },
        mounted() {
            this.obtenerPreguntasVerdaderoFalso();
            this.obtenerTemas();
            let uri = window.location.href;
            if (uri.includes("?")) {
                uri = window.location.href.split('?');
                var fil = uri[1].split('=')[1];
                this.filters.pregunta.value = fil.replace(/%20/g, " ");

            }
        },
        methods: {
            cambioSelect(val) {
                this.limpiarMensajeYAlerta("id_tema", "msjSelectTema");
            },

            myChangeEvent(val) {
                console.log(val);
            },
            mySelectEvent({
                id,
                text
            }) {
                console.log({
                    id,
                    text
                })
            },

            cambiarCampoDeBusqueda() {
                let x = document.getElementById("campoBusqueda").value;
                this.filters.pregunta.keys[0] = x;
            },
            espaciarTexto(str) {
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
            resetearDatos() {
                this.limpiarMensajeYAlerta("id_tema", "msjSelectTema");
                this.limpiarMensajeYAlerta("inpPregunta", "msjInputPregunta");
                this.limpiarMensajeYAlerta("selRespuesta", "msjInputRespuesta");
                this.form.reset();
                this.id_tema = "";
                this.subidor.imagenesVistaPrevia = [];
                this.subidor.imagenes = [];
                this.subidor.imagenesAEliminar = [];
            },
            cambiarModo() {
                this.resetearDatos();
                this.modoEdicion = 0;
            },
            async obtenerPreguntasVerdaderoFalso() {

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
                    url: "/pregunta/show"
                }).then(
                    result => {
                        this.pregunta = result.data[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
                for (let i = 0; i < this.pregunta.length; i++) {
                    this.pregunta[i].imagenes = [];
                    for (let j = 0; j < this.todasLasImagenes.length; j++) {
                        if (this.pregunta[i].id_pregunta == this.todasLasImagenes[j].idpregunta) {
                            this.pregunta[i].imagenes.push(this.todasLasImagenes[j]);
                        }
                    }
                }


            },
            obtenerTemas() { ///Funcion para mostrar los temas
                axios({
                    method: 'GET',
                    url: '/tema/all'
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
                        console.error(error)
                    }
                )
            },
            mostrarMensajeYAlerta(idInput, idMensaje, mensajeADesplegar) {
                document.getElementById(idInput).style.border = "1px solid #ff6258";
                document.getElementById(idMensaje).innerHTML = mensajeADesplegar;
            },
            limpiarMensajeYAlerta(idInput, idMensaje) {
                document.getElementById(idInput).style.border = "1px solid #dee2e6";
                document.getElementById(idMensaje).innerHTML = "";
            },
            limpiarCampo(id) {
                //if (id === "tema") this.limpiarMensajeYAlerta("selTema", "msjSelectTema");
                if (id === "pregunta") this.limpiarMensajeYAlerta("inpPregunta", "msjInputPregunta")
                if (id === "respuesta") this.limpiarMensajeYAlerta("selRespuesta", "msjInputRespuesta")
            },
            comprobarCampos() {
                let existeError = false;
                if (this.id_tema === "") {
                    this.mostrarMensajeYAlerta("id_tema", "msjSelectTema", "Este dato es obligatorio");
                    existeError = true;
                }
                if (this.form.pregunta === "") {
                    this.mostrarMensajeYAlerta("inpPregunta", "msjInputPregunta", "Este dato es obligatorio");
                    existeError = true;
                }
                if (this.form.respuesta === "") {
                    this.mostrarMensajeYAlerta("selRespuesta", "msjInputRespuesta", "Este dato es obligatorio");
                    existeError = true;
                }
                return existeError;
            },
            async registrarPregunta() {
                let existeError = await this.comprobarCampos();
                if (!existeError) {
                    axios.post('/pregunta/add', {
                            pregunta: this.form.pregunta,
                            respuesta: this.form.respuesta,
                            tipo: this.form.tipo,
                            id_tema: this.id_tema
                        })
                        .then(async (res) => {
                            this.form.reset();
                            this.id_tema = "";

                            $('#registrarPregunta').modal('hide');
                            await this.subidor.subirImagenes(res.data.ultimo_id);
                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Pregunta almacenada con éxito',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })

                            this.obtenerPreguntasVerdaderoFalso();

                        })
                        .catch((err) => {
                            console.log(err)
                        })
                }
            },
            editarPregunta(pregunta, imagenes) {
                this.resetearDatos();
                this.modoEdicion = 1;
                this.id_tema = pregunta.tema;
                this.form.fill(pregunta);
                this.totalImagenesEnPregunta = (imagenes.length + 1);
                let numeroMayorDeImagen = 0;
                for (let i = 0; i < imagenes.length; i++) {
                    this.subidor.acomodarImagen("/imagenes/preguntas/" + imagenes[i].nombre, 1, imagenes[i].idImagen);
                    if (imagenes[i].alias.split("_")[3].split(".")[0] > numeroMayorDeImagen) {
                        numeroMayorDeImagen = imagenes[i].alias.split("_")[3].split(".")[0];
                    }
                }
                this.subidor.ultimaImagenEnPreguntaAEditar = numeroMayorDeImagen;
                $('#registrarPregunta').modal('show');
                console.log(pregunta);
            },
            async actualizarPregunta() {
                let existeError = await this.comprobarCampos();
                if (!existeError) {
                    axios.post('/pregunta/update', {
                            id: this.form.id,
                            pregunta: this.form.pregunta,
                            respuesta: this.form.respuesta,
                            tipo: this.form.tipo,
                            id_tema: this.id_tema,
                            imagenesAEliminar: this.subidor.imagenesAEliminar,
                        })
                        .then(async (res) => {
                            await this.subidor.subirImagenes(this.form.id);

                            this.resetearDatos();
                            this.form.reset();
                            $('#registrarPregunta').modal('hide');
                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Pregunta actualizada con éxito',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })
                            this.obtenerPreguntasVerdaderoFalso();
                        })
                        .catch((err) => {
                            console.log(err)
                        })
                }
            },
            eliminarPregunta(id,imagenes) {
                this.$swal.fire({
                    
                    html: `<h3 style="color:#212529;">¿Realmente desea eliminar esta pregunta?</h3>`,
                    showCancelButton: true,
                    confirmButtonColor: '#dc3545',
                    cancelButtonColor: '#6C757D',
                    confirmButtonText: '<i class="fas fa-trash"></i> Eliminar',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                }).then((result) => {
                          //console.log("soy pregunta:" + id);
                    if (result.value) {
                        axios.post('pregunta/delete', {
                                id: id,
                                imagenesAEliminar: imagenes
                        }).then((res) => {      
                                
                            //    console.log("entre");
                                this.id = "";
                                
                                this.obtenerPreguntasVerdaderoFalso();
                                this.$swal.fire({
                                    position: 'top-end',
                                    icon: 'success',
                                    title: 'Pregunta eliminada con éxito',
                                    showConfirmButton: false,
                                    timer: 1500,
                                    toast: true
                                })

                            })
                            .catch((err) => {
                                console.log(err);
                                this.$swal({
                                    icon: 'info',
                                    title: 'Error al eliminar',
                                })
                            })
                    }
                })
            }
        }
    }

</script>
