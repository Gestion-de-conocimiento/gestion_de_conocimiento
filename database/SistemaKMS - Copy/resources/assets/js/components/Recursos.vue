<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                 
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Recursos</h1>
                     
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"> </i> </span> <span style="color: #bdb9bd"> Recursos <i class="fas fa-angle-right"> </i> </span> <b> registrados </b>
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
                                <h3 class="card-title mt-2"> <b> Recursos registrados </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                        <button type="button" class="btn btn-primary float-right"  data-toggle="modal"
                                            data-target="#registrarRecurso" @click="cambiarModo">
                                            <i class="fas fa-edit"></i>Registrar
                                        </button> 
                                    
                                  </div>
                                </div>
                            </div>
                          
                            <div class="card-body">
                            
                                <div class="row mb-2">
                                    <div class="col-6" >
                                        <b> Término de búsqueda</b>
                                        <input class="form-control" type="search" 
                                            placeholder="Ingresar el término de búsqueda"
                                           v-model="filters.pregunta.value"
                                            style=" height: 38px;" />
                                        
                                    </div>
                                   <div class="col-6" >
                                        <b>Campo de busqueda: </b>
                                       <select class="form-control" name="campoBusqueda" id="campoBusqueda" @change="cambiarCampoDeBusqueda">
                                          <option value="0">Seleccionar...</option>
                                         <option value="tema">Orden de enseñanza</option>
                                        <option value="tema">Tema</option>
                                        <option value="opcion">Url</option>
                                        </select>
                                    </div>
                                </div>
                              <!-- ------------------------------------------------------------Tabla---------------------------------------- -->
                               <div class="table-responsive">
                                
                                 <v-table :data="temasOrdenEnsenanza" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">
                                   <!-- --------------------------------------------Encabezado de la tabla-------------------------- -->

                                 <thead slot="head" >
                                          
                                            <v-th sortKey="orden_ensenanza" >Orden de enseñanza</v-th>
                                            <v-th sortKey="nombre_tema_ordenado"> Tema</v-th>
                                            <v-th sortKey="url">Url</v-th>
                                           <!-- <th>Editar</th>
                                            <th>Eliminar</th>-->
                                             
                                         
                                 </thead>
                                   <!-- ---------------------------------------------------------------------------------------------------------------------- -->
                                             <tbody slot="body" slot-scope="{displayData}">

                                                <tr v-for="temasOrdenEnsenanza in displayData" :key="temasOrdenEnsenanza.id">
                                                   <td style="width:30%">
                                                              {{temasOrdenEnsenanza.orden_ensenanza}}
                                                          </td>
                                                   <td style="width:30%">
                                                              {{temasOrdenEnsenanza.nombre_tema_ordenado}}
                                                          </td>
                                                          <td style="width:30%">
                                                            <a :href="temasOrdenEnsenanza.url" target="_blank">{{ temasOrdenEnsenanza.url }}</a>
                                                          </td>
                                                           <!-- <td style="width:5%">
                                                                <a @click="btnEditar(temasOrdenEnsenanza.nombre_tema_ordenado, temasOrdenEnsenanza.url)"
                                                                    data-toggle="modal" data-target="#registrarRecurso" class="btn btn-outline-warning">
                                                                    <i class="fas fa-pen" style="color: #ffae00;"></i> <span style="color: #ffae00;"></span>
                                                                </a>
                                                             
                                                          </td>-->
                                                  </tr>

                                                </tbody>
                                  </v-table>
                                              
                                </div> 
                            <!-- ----------------------------------------------------------------------------------------------------- -->
                            </div>
                          <!-- ----------------------------------Paginado de la tabla---------------------------------------------------------------- -->
                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-6">
                                        <label> <b> Total: {{ temasOrdenEnsenanza.length }} registros </b> </label> 
                                    </div>
                                    <div class="col-6">
                                        <div class="float-right">
                                            <smart-pagination :currentPage.sync="currentPage" :totalPages="totalPages" :maxPageLinks="5" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                          <!-- ----------------------------------------------------------------------------------------------------- -->
                        </div>
                    </div>
                </div>


                <div class="modal animated animate__bounceIn" id="registrarRecurso" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true" data-focus="false">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content" >
                            <div class="modal-body">
                            
                                <h3 v-if="modoEdicion" class="modal-title" id="exampleModalLabel"> Actualizar recurso </h3>
                             
                                <h3 v-else class="modal-title" id="exampleModalLabel"> Registrar recurso </h3>
                              
                             
                              
                              <!-- Utiliza la directiva de enlace (v-model) para vincular el valor seleccionado del componente de selección a la propiedad id_tema en el modelo de datos de Vue.js. -->
                              <!-- Utiliza la directiva :options para proporcionar las opciones del componente de selección, que probablemente se obtienen de la variable temas en el modelo de datos de Vue.js. -->
                              <!-- Escucha el evento select para realizar una acción cuando se selecciona un valor en el componente de selección. La función cambioSelect($event) se llama cuando se produce este evento. -->
                              <!-- Tiene un atributo id con el valor "id_tema", que proporciona un identificador único para el componente de selección. Esto puede ser útil para seleccionar y manipular el elemento mediante JavaScript o CSS. -->
                              
                              
                              <p class="text-left mt-0 mb-0"><b>Tema <span style="color:red">*</span>:</b> </p>
                                <select2 :options="temas" v-model="nombre_tema_ordenado" @select="cambioSelect($event)" id="nombre_tema_ordenado"/>
                                <span id="msjSelectTema"> </span>
                              
                              
                               
                              
                              <p class="text-left mt-0 mb-0"><b>Url <span style="color:red">*</span>: </b></p>
                                <textarea rows="1" id="url" type="text"  class="form-control mt-0 mb-0"
                                    placeholder="url" @focus="limpiarCampos('url')"  ></textarea>
                                <span id="msjInputUrl"> </span>
                                
                                <p class="text-left mt-0 mb-0" style="font-size: 12px;"> <span style="color:red">*</span> Datos obligatorios </p>
                                


                                <button type="button" class="btn btn-secondary float-right btn-lg mt-4 " data-dismiss="modal" >  <i class="fas fa-ban"></i> Cerrar
                                </button>
                              
                                
                              
                               <button v-if="modoEdicion" type="button" @click="" class="btn btn-primary float-right btn-lg mt-4 mr-2" ><i class="fas fa-save"></i>
                                 Actualizar
                              </button>
                              
                                <button  type="button" @click="editar" class="btn btn-primary float-right btn-lg mt-4 mr-2"> <i class="fas fa-save"></i>
                                  Guardar
                                </button>
                              
                              
                            </div>
                        </div>
                    </div>
                </div>
                
              
              
              <!-- Modal para previsualizar pregunta -->
             
              
              <!-- Fin modal para previsualizar pregunta -->

            </div>
        </section>   
    </div>
</template>
<script>
  
  //axios es una biblioteca para hacer solicitudes HTTP desde el navegador o desde Node.js.  
  import axios from "axios";
  //Se importan los módulos que son dos archivos (subir_Imagenes.vue y PrevisualizarPreguntas.vue)
    import Cargador from '@/components/subirImagenes';
    import visualizador from '@/components/PrevisualizarPregunta'
  
    export default {
     // Se define el componente Vue.js y se especifica que está utilizando el componente visualizador.
        components: {
          visualizador
        },
      //Se define un objeto de datos con varias propiedades, como preguntaPrevisualizar, totalRegistros, subidor, pregunta, preguntaAbierta, id, id_tema, etc.
        data() {
            return {
                

                totalRegistros: "5",
                currentPage: 1,
                totalPages: 0,
                temasOrdenEnsenanza: [],
                nombre_tema_ordenado: "",
                url:"",
               //nombre_tema_ordenado: nombre_tema_ordenado.nombre_tema_ordenado,
             
                temas: [],
                respuesta: "",
               
                tipo: 1,
               
                temasParaTabla: [],
                id: "",
            
                filters: {
                    pregunta: {
                        value: '',
                        keys: ['pregunta']
                    }
                },
                
                modoEdicion: 0,
                todasLasImagenes: [],
                totalImagenesEnPregunta: 0,
                ultimaImagenEnPreguntaAEditar: 0,
                imagenesParaDesplegarEnModal: [],
                id_tema_add_enlace_ejercicio: '',
                enlaceEjercicio:'',
            };
        },
      //Se ejecuta cuando se crea el componente. 
      //Aquí se instancia el objeto subidor utilizando el componente Cargador.
        created() {
            this.subidor = new Cargador();
        },
      //Se ejecuta después de que el componente ha sido montado en el DOM. 
      //Aquí se llaman a los métodos getPreguntaAbierta() y getTemas(). 
      //Probablemente estas funciones hagan solicitudes al servidor para obtener datos
        async mounted() {
            //this.llenarTabla()
            //await this.getPreguntaAbierta();
            this.getTemas();
            this.getRecurso();
          
          
        },
      // Se definen varios métodos que realizan acciones específicas, como previsualizarPreguntaMetodo(),
      //cambioSelect(), cambiarCampoDeBusqueda(), wrapText(), desplegarImagenesEnModal(), onChange(),
      //remove(), dragover(), dragleave(), drop(), y subirImagenes().
        methods: {
           
            cambioSelect(val){
              //temas
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
           
          // -- ---------------------------Inicio getPreguntasAbiertas---------------------------------------------- --
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
          //-------------------------------Get Recurso------------------------------------------------------------
          
          async getRecurso() {
                
                await axios({
                    method: "GET",
                    url: "/recurso/mostrarrecurso"
                }).then(
                    result => {
                        this.temasOrdenEnsenanza= result.data[0];
                    },
                    error => {
                        console.error(error);
                    }
                );
               
            },
       
          
           getTemas() {
                axios({
                    method: "GET",
                  url: "/tema/temas"
                }).then(
                    result => {
                        let temasApi = result.data[0];
                        for( let i = 0; i <  temasApi.length; i++ ){
                          this.temas.push({id: temasApi[i].orden_ensenanza, text: temasApi[i].nombre_tema_ordenado})
                          console.log('temasApi');
                        }
                    },
                    error => {
                        console.error(error);
                    }
                );
            },
          // --    --------------------------------Get temas----------------------------------------------------------------------- --
            
           /* llenarTabla() {
                axios({
                    method: "GET",
                    url: "tema/Ejercicios/ordenEnsenanza"
                }).then(
                    result => {
                        let temasApi = result.data[0];
                        console.log(temasApi)
                        for( let i = 0; i <  temasApi.length; i++ ){
                          $("#responsive-data-table").append("<tr> <td>"+temasApi[i].orden_ensenanza+"</td><td>"+temasApi[i].nombre_tema_ordenado+"</td> <td>"+temasApi[i].url+"</td> </tr>")
                          this.temasParaTabla.push({id: temasApi[i].id_tema, text: temasApi[i].nombre_tema_ordenado })
                        }
                    },
                    error => {
                        console.error(error);
                    }
                );
            },*/
          //AGREGAR ENLACE DE EJERCICIO
             async addNewUrlEjercicio () {
                console.log(this.enlaceEjercicio)
                console.log(this.id_tema_add_enlace_ejercicio)
                await axios.post("/ejercicio/anadir", {
                   id_tema: this.id_tema_add_enlace_ejercicio,
                  enlace: this.enlaceEjercicio,
                }).then(async res => {
                  console.log(res)
                })
                .catch(err => {
                    console.log(err);
                });
              },
          
          // -- -----------------------Inicio post-------------------------------------------- --
           
           /*----------------------- Intento 1----------------------------------------------------
           async guardarRecurso() {
                await axios.post("/recurso/anadirRecurso", {
                    nombre_tema_ordenado: this.nombre_tema_ordenado,
                    url: this.url  
                }).then(async res => {
                    this.nombre_tema_ordenado = "";
                    this.url = "";
                    await this.getRecurso();
                    $('#registrarRecurso').modal('toggle');
                    //this.$swal.fire({type: "success",title: res.data.mensaje});

                    this.$swal.fire({
                        position: 'top-end',
                        icon: 'success',
                        title: 'Información guardada con éxito',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })

                    await this.getRecurso();
                })
                .catch(err => {
                    console.log(err);
                });
            },*/
          
         
          /* ----------------------------Intento 1-------------------------------------
          btnGuardar() {
                let selectTema = document.getElementById("nombre_tema_ordenado");
                let inputUrl = document.getElementById("url");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputUrl = document.getElementById("msjInputUrl");
               
                this.url = inputUrl.value;
                
                if (this.nombre_tema_ordenado == "" || this.url == "") {
                    // Alertar al usuario sobre campos vacios
                    if (this.nombre_tema_ordenado == "") {
                        selectTema.style.border = "1px solid #ff6258";
                        msjSelectTema.innerHTML = "Este dato es obligatorio";
                        msjSelectTema.style.color = "#ff6258";
                    }
                    if (this.url == "") {
                        inputUrl.style.border = "1px solid #ff6258";
                        msjInputUrl.innerHTML = "Este dato es obligatorio";
                        msjInputUrl.style.color = "#ff6258";
                    }
                    
                } else {
                    this.guardarRecurso(
                        this.nombre_tema_ordenado,
                        this.url
                    );
                }
            },*/
          
         
          
         
            limpiarCampos(id) {
              // @focus="limpiarCampos('enlace')"
                let selectTema = document.getElementById("nombre_tema_ordenado");
                let inputUrl = document.getElementById("url");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputUrl = document.getElementById("msjInputUrl");
                //temas
              if (id == "tema") {
                    selectTema.style.border = "1px solid #dee2e6";
                    msjSelectTema.innerHTML = "";
                } 
                if (id == "url") {
                    inputUrl.style.border = "1px solid #dee2e6";
                    msjInputUrl.innerHTML = "";
                }
                
            },
            btnEditar() {
                //this.subidor.imagenes = [];
                let selectTema = document.getElementById("nombre_tema_ordenado");
                let inputUrl = document.getElementById("url");
                this.modoEdicion = 1;
                this.id=id;
                this.nombre_tema_ordenado = nombre_tema_ordenado;
                inputUrl.value = url;
                this.limpiarCampos("nombre_tema_ordenado");
                this.limpiarCampos("url");
       
            },
            cambiarModo() {
                let selectTema = document.getElementById("nombre_tema_ordenado");
                let inputUrl = document.getElementById("url");
                inputUrl.value = "";
                this.modoEdicion = 0;
                this.nombre_tema_ordenado = "";
                //this.id_tema = "";
                
                this.limpiarCampos("url");
                this.limpiarCampos("nombre_tema_ordenado");
                
            },
            editar() {
                // Referencia de los elementos del formulario.
                let selectTema = document.getElementById("nombre_tema_ordenado");
                let inputUrl = document.getElementById("url");
                let msjSelectTema = document.getElementById("msjSelectTema");
                let msjInputUrl = document.getElementById("msjInputUrl");
                // Pasar los valores del formuario a las propiedades del objeto de vue.
               // let id_tema = this.nombre_tema_ordenado;
                this.url = inputUrl.value;
              
                console.log('Datos a enviar:');
                //console.log('id:', this.id_tema);
                console.log('nombre_tema_ordenado:', this.nombre_tema_ordenado);
                console.log('url:', this.url);
              
                //this.id_tema = selectTema.value;
                if (this.nombre_tema_ordenado == "" || this.url == "") {
                    // Alertar al usuario sobre campos vacios
                    if (this.nombre_tema_ordenado == "") {
                        selectTema.style.border = "1px solid #ff6258";
                        msjSelectTema.innerHTML = "Este dato es obligatorio";
                        msjSelectTema.style.color = "#ff6258";
                    }
                    if (this.url == "") {
                        inputUrl.style.border = "1px solid #ff6258";
                        msjInputUrl.innerHTML = "Este dato es obligatorio";
                        msjInputUrl.style.color = "#ff6258";
                    }
                   
                } else {
                    axios.post("/recurso/actualizarRecurso", {
                           // id: this.id,
                            nombre_tema_ordenado: this.nombre_tema_ordenado,
                            url: this.url
                        }).then(async res => {
                            await this.getRecurso();
                           // this.id = "";
                            this.nombre_tema_ordenado = "";
                            this.url = "";
                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Información almacenada con éxito',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })
                        
                            $('#registrarRecurso').modal('toggle');
                            await this.getRecurso();
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
