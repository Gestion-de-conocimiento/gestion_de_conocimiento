<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mr-2 ml-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Inicio</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <li class="breadcrumb-item"><a href="#">Inicio</a></li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-md-12">
            <div class="card shadow m-2">
                <div class="card-body">
                  
                    {{ saludo }}

                    <!--<div v-if="this.id_rol==4">
                        <h1>Bienvenido alumno: {{this.nombre + ' ' + this.apellidoPaterno + ' ' + this.apellidoMaterno }} </h1>
                    </div>

                    <div v-if="this.id_rol==3">
                        <h1>Bienvenido profesor: {{this.nombre + ' ' + this.apellidoPaterno + ' ' + this.apellidoMaterno }} </h1>
                    </div>

                    <div v-if="this.id_rol==2">
                        <h1>Bienvenido experto: {{this.nombre + ' ' + this.apellidoPaterno + ' ' + this.apellidoMaterno }} </h1>
                    </div>

                    <div v-if="this.id_rol==1">
                        <h1>Bienvenido administrador: {{this.nombre + ' ' + this.apellidoPaterno + ' ' + this.apellidoMaterno }} </h1>
                    </div>

                    <div class="row" v-if="this.id_rol==1">
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-success">
                                <div class="inner">
                                    <h3>{{admins}}</h3>
                                    <p>Administradores</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-user-shield"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información <i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-warning">
                                <div class="inner">
                                    <h3>{{experto}}</h3>
                                    <p>Expertos</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-user-tie"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información <i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>
                        
                    </div>
                    
                    <div class="row" v-if="this.id_rol==1 || this.id_rol==3 ">
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-primary">
                                <div class="inner">
                                    <h3>{{alumnos}}</h3>
                                    <p>Alumnos</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-graduation-cap"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información <i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-info">
                                <div class="inner">
                                    <h3>{{pregunta}}</h3>
                                    <p>Preguntas</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-question"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información<i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>


                     <div class="row" v-if="this.id_rol==1">
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-secondary">
                                <div class="inner">
                                    <h3>{{temas}}</h3>
                                    <p>Temas del area disciplinar</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-calculator"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información <i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>
                        
                        <div class="col-md-6">
                            <div class="small-box bg-gradient-primary">
                                <div class="inner">
                                    <h3>{{profesor}}</h3>
                                  
                                  
                                    <p>Docentes</p>
                                </div>
                                <div class="icon">
                                    <i class="fas fa-chalkboard-teacher"></i>
                                </div>
                                <a href="#" class="small-box-footer">
                                    Más Información <i class="fas fa-arrow-circle-right"></i>
                                </a>
                            </div>
                        </div>

                    </div>  -->
					

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                pregunta: '',
                experto: '',
                profesor: '',
                alumnos: '',
                temas: '',
                admins: '',
                id_rol: '',
                rol: '',
                nombre: '',
                apellidoPaterno: '',
                apellidoMaterno: '',
                matricula: '',
                foto: '',
                id_rol: '',
                rol: '',
              
                saludo: ''
            }
        },
        mounted() {

           /* this.getpregunta();
            this.getTemas();
            this.getadmins();
            this.getprofesor();
            this.getalumnos();
            this.getexperto();

            this.id = window.idUsuario;
            this.id_rol = window.rol;

			this.nombre = window.nombre;
			this.apellidoPaterno = window.apellido_paterno;
			this.apellidoMaterno = window.apellido_materno;
			this.matricula = window.matricula;
			this.foto = window.foto;

            if (this.id_rol === '1') {
                this.rol = "Administrador"
            }

            if (this.id_rol === '2') {
                this.rol = "Experto"
            }

            if (this.id_rol === '3') {
                this.rol = "Profesor"
            }

            if (this.id_rol === '4') {
                this.rol = "Alumno"
            }*/
            this.obtenerSaludo();
        },
        methods: {
          
          
            obtenerSaludo(){
              axios({method:'get', url:'saludar'})
                .then(result=>{
                  console.log(result.data.saludo);
                  //this.saludo = result.data;
                },
                error => {
                    console.error(error)
                }
                )
            },
          
          
          
          
            
            getpregunta() {
                axios({
                    method: 'GET',
                    url: '/pregunta/count'
                }).then(
                    result => {
                        this.pregunta = result.data[0][0].totalPreguntas
                    },
                    error => {
                        console.error(error)
                    }
                )
              
            },
            getTemas() {
                axios({
                    method: 'GET',
                    url: '/temascount'
                }).then(
                    result => {
                        this.temas = result.data[0][0].totalTemas
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            getadmins() {
                axios({
                    method: 'GET',
                    url: '/admin/count'
                }).then(
                    result => {
                        this.admins = result.data[0][0].totalAdministradores
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            getalumnos() {
                axios({
                    method: 'GET',
                    url: '/alumno/count'
                }).then(
                    result => {
                        this.alumnos = result.data[0][0].totalAlumnos
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            getprofesor() {
                axios({
                    method: 'GET',
                    url: '/profesor/count'
                }).then(
                    result => {
                        this.profesor = result.data[0][0].totalDocentes
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            getexperto() {
                axios({
                    method: 'GET',
                    url: '/experto/count'
                }).then(
                    result => {
                        this.experto = result.data[0][0].totalExpertos
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
        }
    }
</script>
