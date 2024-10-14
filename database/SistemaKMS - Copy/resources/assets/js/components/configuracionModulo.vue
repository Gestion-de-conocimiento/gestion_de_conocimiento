<template>
    <div class="content-wrapper">

      <div class="content-header">
          <div class="container-fluid">
              <div class="row mb-2">
                  <div class="col-sm-6">
                      <h1 class="page-title m-0">Configurar módulo de Rutas de Evaluación </h1>
                  </div>
                  <div class="col-sm-6">
                      <ol class="breadcrumb float-sm-right">
                          <span style="color: #bdb9bd">  
                              <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i> 
                          </span> 
                          <span style="color: #bdb9bd">  
                              Cuestionario <i class="fas fa-angle-right"></i> 
                          </span> 
                          <b> Configuración módulo </b>
                      </ol>
                  </div>
              </div>
          </div>
      </div>

		  <section class="content">
            <div class="container-fluid">
				        <div class="row">
					        <div class="col-12 ">
						<div class="card shadow">
							<div class="card-header">
								<h3 class="card-title mt-2"> <b> Configurar módulo de la Red Bayesiana </b> </h3>
								<div class="card-tools">
									<div class="" style="width: 150px;">
									</div>
								</div>
							</div>
              
							<div class="card-body">
								
                
								<div class="form-group">
									<label class="mb-2" for="exampleFormControlSelect1">Error estandar: </label>
									<input type="number" @keyup="validarInpErrorEstandar" v-model="configuraciones.errorEstandar"
										id="numeroPreguntasNumericas" class="form-control">

                                    <label style="color: red;">{{ mensajes.errorEstandar }}</label>
								</div>
                
                                <div class="form-group">
									<label class="mb-2" for="exampleFormControlSelect1">No. Máximo de temas: </label>
									<input @keyup="validarInpMaxTemas" v-model="configuraciones.numeroMaxTemas"
										id="numeroPreguntasNumericas" class="form-control">
                                  
                                  <label style="color: red;">{{ mensajes.numeroMaxTemas }}</label>
                                  
								</div>

								<div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect2">Ponderación de dominio:</label>
                                    <input @keyup="validarInpPonderacionDominio" v-model="configuraciones.ponderacionDominio"
                                        id="numeroPreguntasBreves" class="form-control">
                  
                        <label style="color: red;">{{ mensajes.ponderacionDominio }}</label>
								</div>

								<div class="form-group">
									<label class="mb-2" for="exampleFormControlSelect2">Cantidad de saltos:</label>
									<input @keyup="validarInpCanitdadSaltos" v-model="configuraciones.numeroSaltos"
										id="numeroPreguntasCalculadas" class="form-control">
                  
                  <label style="color: red;">{{ mensajes.numeroSaltos }}</label>
                  
								</div>
                
                                
                                <div class="form-group">
                                    <label class="mb-2" for="exampleFormControlSelect1">Versión de Red Bayesiana Maestra:</label>	
                                    <select class="form-control" v-model="configuraciones.versionRbm">
                                      <option v-for="rb in rbs" :value="rb.id">{{rb.nombre}}</option>
                                    </select>           
                                </div>

                                <div class="form-group">
                                  <button type="button" class="btn btn-primary" data-toggle="modal"
                                      data-target="#registrarPregunta" @click="btnGuardarCambios" :disabled="deshabilitarBoton">
                                      <i class="fas fa-save"></i> Guardar cambios
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
    export default {
        data() {
            return {
                rbs: [],
                configuraciones: {
                    errorEstandar: 0,
                    ponderacionDominio: 0,
                    numeroSaltos: 0,
                    versionRbm: '',
                    numeroMaxTemas: 0
                },
                mensajes: {
                    errorEstandar: '',
                    ponderacionDominio: '',
                    numeroSaltos: '',
                    numeroMaxTemas: ''
                },
                deshabilitarBoton: false
            };
        },
        mounted() {
            this.obtenerRbs();
            this.obtenerConfiguracion();
        },
        methods: {
            
            obtenerRbs(){
                // Obtiene toda la información de la tabla donde se almacenan las versiones de la red bayesiana
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
            
            obtenerConfiguracion: async function() {
              
                await axios({
                    method: 'get',
                    url: "/obtenerConfiguracionRedBayesiana "
                }).then(result => {
                    
                    let configuracionServer = result.data[0][0];
                    console.log(configuracionServer);
                  
                    this.configuraciones.errorEstandar = configuracionServer.error_estandar;
                    this.configuraciones.ponderacionDominio = configuracionServer.ponderacion_dominio;
                    this.configuraciones.numeroSaltos = configuracionServer.cantidad_saltos;
                    this.configuraciones.versionRbm = configuracionServer.version_red_bayesiana;
                    this.configuraciones.numeroMaxTemas = configuracionServer.max_temas;
                  
                }, error => {
                    console.error(error)
                })
              
              
            },
          
            btnGuardarCambios(){              
                axios.post('/guardarConfiguracionRB', {
                    errorEstandar: this.configuraciones.errorEstandar,
                    ponderacionDominio: this.configuraciones.ponderacionDominio,
                    numeroSaltos: this.configuraciones.numeroSaltos,
                    versionRbm: this.configuraciones.versionRbm,
                    numeroMaxTemas: this.configuracionesl.numeroMaxTemas
                })
                .then((res) => {
                    this.$swal.fire({
                        icon: 'success',
                        title: 'Configuracion guardada',
                        text: 'Configuracion guardada con exito',
                    })

                    this.obtenerConfiguracion();
                })
                .catch((err) => {
                    console.log(err)
                })
              
            },
            
            validarInpErrorEstandar(){
                if( this.configuraciones.errorEstandar < 0 || this.configuraciones.errorEstandar > 1 ){
                    this.mensajes.errorEstandar = "El error estandar debe estar en un rango entre 0 y 1"
                }else{
                    this.mensajes.errorEstandar = ""
                }
              
                this.validarBoton();
            },
            
            validarInpMaxTemas(){
                if( this.configuraciones.numeroMaxTemas < 0 || this.configuraciones.numeroMaxTemas > 50 ){
                  this.mensajes.numeroMaxTemas = "El numero máximo de temas debe ser menor a 50";
                }else{
                    this.mensajes.numeroMaxTemas = "";
                }
              
                this.validarBoton();
            },
            
            validarInpPonderacionDominio(){
              
                if( this.configuraciones.ponderacionDominio < 0 || this.configuraciones.ponderacionDominio > 100){
                  this.mensajes.ponderacionDominio = "La ponderación debe estar en un rango de 0 a 100"
                }else{
                  this.mensajes.ponderacionDominio = "";

                }
              
              
                if( this.configuraciones.ponderacionDominio < 0){
                    this.configuraciones.ponderacionDominio = 0;
                }
                
                if( this.configuraciones.ponderacionDominio > 100 ){
                   this.configuraciones.ponderacionDominio = 100;
                }
                
                this.validarBoton();
            },
            
            validarInpCanitdadSaltos(){
                if( this.configuraciones.numeroSaltos < 0 || this.configuraciones.numeroSaltos > 10 ){
                  this.mensajes.numeroSaltos = "El numero de saltos debe estar en un rango de 0 a 10";
                }else{
                  this.mensajes.numeroSaltos = "";
                }
                this.validarBoton();
            },
            
          
            validarBoton(){
              
              
              if( this.mensajes.errorEstandar == "" && this.mensajes.ponderacionDominio == "" && this.mensajes.numeroSaltos == "" && this.mensajes.numeroMaxTemas == ""){
                this.deshabilitarBoton = false;
                console.log("Validar botón true")
              }else{
                this.deshabilitarBoton = true;
                console.log("Validar botón false");
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
