<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Preguntas</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"> </i> </span> <span style="color: #bdb9bd">  Preguntas <i class="fas fa-angle-right"> </i> </span> <b>Abiertas </b>
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
                                <h3 class="card-title mt-2"> <b> Preguntas abiertas </b> </h3>
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
                                      <!-- //////////////////////////////////////////////////////////-->
                                        <b> Termino de busqueda: </b>
                                        <input class="form-control" type="search" 
                                            placeholder="Término" 
                                            v-model="filters.pregunta.value" 
                                            style=" height: 38px;" />
                                        <!-- //////////////////////////////////////////////////////////--> 
                                    </div>
                                    <div class="col-6" >
                                       <!-- //////////////////////////////////////////////////////////-->
                                        <b>Campo de busqueda: </b>
                                        <select class="form-control" name="campoBusqueda" id="campoBusqueda" @change="cambiarCampoDeBusqueda">
                                        <option value="pregunta">Pregunta</option>
                                        <option value="tema">Tema</option>
                                        <option value="opcion">Respuesta</option>
                                        </select>
                                       <!-- //////////////////////////////////////////////////////////-->
                                    </div>
                                </div>
                               <!-- /////////////////////////////////////////////////////////////////////////////////////-->

                                <div class="table-responsive">

                                    <v-table :data="preguntaAbierta" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                        <thead slot="head" >
                                            <v-th sortKey="pregunta" defaultSort="desc" >Pregunta</v-th>
                                            <v-th sortKey="opcion" defaultSort="desc">Respuesta</v-th>
                                            <v-th sortKey="tema" defaultSort="desc">Tema</v-th>
                                            <th>Previsualizar</th>
                                            <th>Imagen </th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="preguntaAbierta in displayData" :key="preguntaAbierta.id">
                                                <td style="width:30%">
                                                    {{preguntaAbierta.pregunta}}
                                                </td>
                                                <td style="width:30%">
                                                    {{preguntaAbierta.opcion}}
                                                </td>
                                                <td style="width:25%">
                                                    {{preguntaAbierta.tema}}
                                                </td>
                                                <td style="width:5%">
                                                    <button type="button" class="btn btn-outline-success"  data-toggle="modal" data-target="#modalPrevisualizacion" @click="previsualizarPreguntaMetodo(preguntaAbierta)">
                                                        <i class="fas fa-eye"></i> 
                                                    </button> 
                                                </td>
                                                <td style="width:5%">
                                                    <a data-toggle="modal"
                                                        data-target="#modalParaVerImagenes"
                                                        @click="desplegarImagenesEnModal(preguntaAbierta.imagenes)" class="btn btn-outline-primary">
                                                        <i class="fas fa-image" style="color: #2196f3"></i> <span  style="color: #2196f3"></span>
                                                      
                                                    </a>
                                                </td>

                                                <td style="width:5%">
                                                    <a @click="btnEditar(preguntaAbierta.id_pregunta,preguntaAbierta.pregunta,preguntaAbierta.opcion,preguntaAbierta.tipo,preguntaAbierta.id_tema, preguntaAbierta.imagenes)"
                                                        data-toggle="modal" data-target="#registrarPregunta" class="btn btn-outline-warning">
                                                        <i class="fas fa-pen" style="color: #ffae00;"></i> <span style="color: #ffae00;"></span>
                                                    </a>
                                                </td>
                                                <td style="width:5%">
                                                    <a  @click="eliminar(preguntaAbierta.id_pregunta, preguntaAbierta.imagenes)" class="btn btn-outline-danger" >
                                                        <i class="fas fa-trash" style="color: #ff6258"></i>  <span style="color: #ff6258"></span>
                                                    </a>
                                                </td>
                                            </tr>
                                        
                                      </tbody>
                                    </v-table>
                                   <!-- ///////////////////////////////////////////////////////////////////////////////////////////-->
                                </div>
                            </div>
                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                      <!-- Total: 75 registros -->
                                        <label> <b> Total: {{ preguntaAbierta.length }} registros </b> </label>
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                          <!-- Paginas-->
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
                            
                                <h3 v-if="modoEdicion" class="modal-title" id="exampleModalLabel"> Actualizar pregunta </h3>
                                <h3 v-else class="modal-title" id="exampleModalLabel"> Registrar pregunta </h3>
                        
                                
                                <p class="text-left mt-0 mb-0"><b>Pregunta <span style="color:red">*</span>:</b></p>
                                <textarea rows="4" id="pregunta" type="text" class="form-control mt-0 mb-0" 
                                    placeholder="Pregunta" @focus="limpiarCampos('pregunta')" > </textarea>
                                <span id="msjInputPregunta"> </span>
              
                                
                                                                                                                            
                                <p class="text-left mt-0 mb-0"><b>Respuesta <span style="color:red">*</span>: </b></p>
                                <textarea rows="1" id="respuesta" type="text"  class="form-control mt-0 mb-0"
                                    placeholder="Respuesta" @focus="limpiarCampos('respuesta')"  ></textarea>
                                <span id="msjInputRespuesta"> </span>

                                <p class="text-left mt-0 mb-0"><b>Tema <span style="color:red">*</span>:</b> </p>
                                <Select2  :options="temas" v-model="id_tema" @select="cambioSelect($event)" id="id_tema"/>
                                <span id="msjSelectTema"> </span>
                            

                                <p class="text-left mt-0 mb-0"><b>Imagenes: </b></p>
                                <div @dragover="dragover" @dragleave="dragleave" @drop="drop"
                                    style="border: 0.5px dashed black; width: 100%;" >
                                    <input type="file" id="assetsFieldHandle" 
                                        class="w-px h-px opacity-0 overflow-hidden absolute"
                                        @change="onChange" ref="file" accept=".pdf,.jpg,.jpeg,.png"
                                        hidden />
                                    <div class="row">
                                        <div class="col-md-12">
                                            <label for="assetsFieldHandle" class="block cursor-pointer">
                                                <div>
                                                    <center>
                                                    <p id="mensajito" class="text-center">
                                                        <i class="fas fa-cloud-download-alt"></i> Arrastra la imagen
                                                        o da clic aquí para subir
                                                    </p>
                                                    </center>
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
                                            <a  @click="remove(imagen)" title="Eliminar la imagen"> <i class="fas fa-trash-alt" style="color: #ff6258"></i> </a>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                </div>
                                
                                
                                
                                
                                <p class="text-left mt-0 mb-0" style="font-size: 12px;"> <span style="color:red">*</span> Datos obligatorios </p>
                                


                                <button type="button" class="btn btn-secondary float-right btn-lg mt-4 " data-dismiss="modal" >  <i class="fas fa-ban"></i> Cerrar
                                </button>
                                <button v-if="modoEdicion" type="button" @click="editar" class="btn btn-primary float-right btn-lg mt-4 mr-2" >
                                    <i class="fas fa-save"></i>  Guardar</button>
                                <button v-else type="button" @click="btnGuardar" class="btn btn-primary float-right btn-lg mt-4 mr-2"> <i class="fas fa-save"></i> Guardar
                                </button>
                              
                              
                              
                              
                              
                              
                              
                            
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal animated animate__bounceIn" id="modalParaVerImagenes" tabindex="-1" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                            
                            <div class="modal-body">
                            
                            <h3 class="modal-title" id="exampleModalLabel"> Imagenes adjuntas en la pregunta
                                </h3>

                                <div style="width: 100%;">

                                    <table style="list-style-type: none; width:100%">
                                        <tr>
                                            <th >
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

                                    <span v-if="imagenesParaDesplegarEnModal.length == 0" class="text-center"> Esta
                                        pregunta no tiene imagenes adjuntas </span>


                                </div>
                                <button type="button" data-dismiss="modal" class="btn btn-secondary float-right btn-lg mt-4 "> <i class="fas fa-ban"></i> Cerrar
                                </button>
                            </div>

                        </div>
                    </div>
                </div>
              
              
              <!-- Modal para previsualizar pregunta -->
              
              <div class="modal animated" id="modalPrevisualizacion" tabindex="-1" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                            
                            <div class="modal-body">
                            
                            <h3 class="modal-title" id="exampleModalLabel"> Previsualización de Pregunta </h3>

                                <div style="width: 100%;">
                                  
                                    
                                  <visualizador :datosPregunta="preguntaPrevisualizar"></visualizador>
                                    

                                </div>
                                <button type="button" data-dismiss="modal" class="btn btn-secondary float-right btn-lg mt-4 "> <i class="fas fa-ban"></i> Cerrar
                                </button>
                            </div>

                        </div>
                    </div>
                </div>
              
              <!-- Fin modal para previsualizar pregunta -->

            </div>
        </section>   
    </div>
</template>
<script>
    import axios from "axios";
    import Cargador from '@/components/subirImagenes';
    import visualizador from '@/components/PrevisualizarPregunta'
  
    export default {
        components: {
          visualizador
        },
        data() {
            return {
                preguntaPrevisualizar: {
                  id: 1,
                  id_tema: 1,
                  tipo: '',
                },
                totalRegistros: "6",
                subidor: {},
                pregunta: [],
                preguntaAbierta: [],
                id: "",
                id_tema: "",
                respuesta: "",
                pregunta: "",
                tipo: 1,
                temas: [],
                id: "",
                nombre_tema: "",
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta']
                    }
                },
                currentPage: 1,
                totalPages: 0,
                modoEdicion: 0,
                todasLasImagenes: [],
                totalImagenesEnPregunta: 0,
                ultimaImagenEnPreguntaAEditar: 0,
                imagenesParaDesplegarEnModal: []
            };
        },
        created() {
            this.subidor = new Cargador();
        },
        async mounted() {
            await this.getPreguntaAbierta();
            this.getTemas();
          
        },
        methods: {
            previsualizarPreguntaMetodo(pregunta){
              console.log("Pregunta a previsualizar");
              console.log( pregunta );
              this.preguntaPrevisualizar = {
                id: pregunta.id_pregunta,
                id_tema: pregunta.id_tema,
                tipo: pregunta.tipo
              }
            },
            cambioSelect(val){
              this.limpiarCampos("tema");
            },
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
          // -------------------------------GetPreguntaAbierta------------------------------------------
            async getPreguntaAbierta() {
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
                    url: "/pregunta/showPAB"
                }).then(
                    result => {
                        this.preguntaAbierta = result.data[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
                for (let i = 0; i < this.preguntaAbierta.length; i++) {
                    this.preguntaAbierta[i].imagenes = [];
                    for (let j = 0; j < this.todasLasImagenes.length; j++) {
                        if (this.preguntaAbierta[i].id_pregunta == this.todasLasImagenes[j].idpregunta) {
                            this.preguntaAbierta[i].imagenes.push(this.todasLasImagenes[j]);
                        }
                    }
                }
            },
          //-------------------------------Termina GetPreguntaAbierta-----------------------------------------
            getTemas() {
                axios({
                    method: "GET",
                    url: "/tema/all"
                }).then(
                    result => {
                        let temasApi = result.data[0];
                        for( let i = 0; i <  temasApi.length; i++ ){
                          this.temas.push({id: temasApi[i].id, text: temasApi[i].nombre_tema })
                        }
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
            async guardarPregunta(pregunta, respuesta, tipo, id_tema) {
                await axios.post("/pregunta/add", {
                    pregunta: pregunta,
                    respuesta: respuesta,
                    tipo: tipo,
                    id_tema: id_tema
                }).then(async res => {
                    this.tipo = "";
                    this.respuesta = "";
                    this.pregunta = "";
                    this.id_tema = "";
                    await this.subirImagenes(res.data.ultimo_id);
                    await this.getPreguntaAbierta();
                    $('#registrarPregunta').modal('toggle');
                    //this.$swal.fire({type: "success",title: res.data.mensaje});

                    this.$swal.fire({
                        position: 'top-end',
                        icon: 'success',
                        title: 'Información guardada con éxito',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })

                    await this.getPreguntaAbierta();
                })
                .catch(err => {
                    console.log(err);
                });
            },
            btnGuardar() {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                // Pasar los valores del formuario a las propiedades del objeto de vue.
                this.pregunta = inputPregunta.value;
                this.respuesta = inputRespuesta.value.toString().toLowerCase().normalize("NFD").replace(
                    /[\u0300-\u036f]/g, "").replace(/ /g, "")
                //this.id_tema = selectTema.value;
                if (this.id_tema == "" || this.pregunta == "" || this.respuesta == "" ) {
                    // Alertar al usuario sobre campos vacios
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
                } else {
                    this.guardarPregunta(
                        this.pregunta,
                        this.respuesta,
                        this.tipo,
                        this.id_tema
                    );
                }
            },
            limpiarCampos(id) {
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
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
            },
            btnEditar(id, pregunta, respuesta, tipo, id_tema, imagenes) {
                this.totalImagenesEnPregunta = (imagenes.length + 1);
                this.subidor.imagenesVistaPrevia = [];
                //this.subidor.imagenes = [];
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let selectTema = document.getElementById("id_tema");
                this.modoEdicion = 1;
                this.id = id;
                this.id_tema = id_tema;
                inputRespuesta.value = respuesta;
                inputPregunta.value = pregunta;
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
                let selectTema = document.getElementById("id_tema");
                inputRespuesta.value = "";
                inputPregunta.value = "";
                this.subidor.imagenesVistaPrevia = [];
                this.subidor.imagenes = [];
                this.subidor.contadorImagen = 0;
                this.subidor.form_data = {};
                this.subidor.ultimaImagenEnPreguntaAEditar = 0;
                this.subidor.imagenesAEliminar = [];
                this.modoEdicion = 0;
                this.id_tema = "";
              
                this.limpiarCampos("tema");
                this.limpiarCampos("pregunta");
                this.limpiarCampos("respuesta");
            },
            editar() {
                // Referencia de los elementos del formulario.
                let inputPregunta = document.getElementById("pregunta");
                let inputRespuesta = document.getElementById("respuesta");
                let selectTema = document.getElementById("id_tema");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputRespuesta = document.getElementById("msjInputRespuesta");
                let msjInputPregunta = document.getElementById("msjInputPregunta");
                // Pasar los valores del formuario a las propiedades del objeto de vue.
                this.pregunta = inputPregunta.value;
                this.respuesta = inputRespuesta.value.toString().toLowerCase().normalize("NFD").replace(
                    /[\u0300-\u036f]/g, "").replace(/ /g, "")
                //this.id_tema = selectTema.value;
                if (this.id_tema == "" || this.pregunta == "" || this.respuesta == "") {
                    // Alertar al usuario sobre campos vacios
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
                } else {
                    axios.post("/pregunta/update", {
                            id: this.id,
                            pregunta: this.pregunta,
                            respuesta: this.respuesta,
                            tipo: this.tipo,
                            id_tema: this.id_tema,
                            imagenesAEliminar: this.subidor.imagenesAEliminar
                        }).then(async res => {
                            await this.subirImagenes(this.id);
                            await this.getPreguntaAbierta();
                            this.id = "";
                            this.respuesta = "";
                            this.pregunta = "";
                            this.id_tema = "";
                            this.subidor.imagenesAEliminar = [];
                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Información almacenada con éxito',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })
                        
                            $('#registrarPregunta').modal('toggle');
                            await this.getPreguntaAbierta();
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
                    if (result.value) {
                        axios.post("/pregunta/delete", {
                                id: id,
                                imagenesAEliminar: imagenes
                            })
                            .then(() => {
                                this.id = "";
                                this.getPreguntaAbierta();
                                const Toast = this.$swal.mixin({
                                    toast: true,
                                    position: "top-end",
                                    showConfirmButton: false,
                                    timer: 3000
                                });
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
            }
        }
    };
</script>