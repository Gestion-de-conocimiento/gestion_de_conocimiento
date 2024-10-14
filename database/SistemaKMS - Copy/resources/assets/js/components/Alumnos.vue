<template>
    <div class="content-wrapper">
		<div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Alumnos</h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  
                                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i> 
                            </span> 
                            <span style="color: #bdb9bd">  
                                Usuarios <i class="fas fa-angle-right"></i> 
                            </span> 
                            <b> Alumnos </b>
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
								<h3 class="card-title mt-2"> <b> Lista de alumnos </b> </h3>
								<div class="card-tools">
									<div class="" style="width: 150px;">
										<button type="button" class="btn btn-primary float-right"  data-toggle="modal"
											data-target="#registrarPregunta" @click="btnGuardar">
											<i class="fas fa-plus"></i> Nuevo
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
                                            v-model="filters.nombre.value" 
                                            style=" height: 38px;" />
                                    </div>
                                    <div class="col-6" >
                                        <b>Campo de busqueda: </b>
                                        <select class="form-control" name="campoBusqueda" id="campoBusqueda" @change="cambiarCampoDeBusqueda">
                                        	<option value="nombre_alumno">Nombre</option>
											<option value="apellido_paterno">Apellido</option>
											<option value="matricula">Matricula</option>
											<option value="nivel_academico">Nivel academico</option>
											<option value="nombre_profesor">Profesor</option>
                                        </select>
                                    </div>
                                </div>


								<div class="table-responsive">
									<v-table :data="alumnos" :filters="filters" :currentPage.sync="currentPage" :pageSize="5"
										@totalPagesChanged="totalPages = $event" style="width:100%" class="table table-hover">
										<thead slot="head">
											<v-th sortKey="nombre_alumno" defaultSort="desc">Nombre</v-th>
											<v-th sortKey="apellido_paterno" defaultSort="desc">Apellido</v-th>
											<v-th sortKey="edad" defaultSort="desc">Edad</v-th>											

                      <v-th sortKey="matricula" defaultSort="desc">Matricula</v-th>
                      <v-th sortKey="genero" defaultSort="desc">Género</v-th>											

											<v-th sortKey="nivel_academico" defaultSort="desc">Nivel academico</v-th>
											<v-th sortKey="periodo" defaultSort="desc">Período</v-th>

                      <th>Profesor</th>
											<th>Editar</th>
											<th>Eliminar</th>
										</thead>
										<tbody slot="body" slot-scope="{displayData}">
											<tr v-for="alumnos in displayData" :key="alumnos.id">
												<td class="text-left">{{alumnos.nombre_alumno}}</td>
												<td class="text-left">{{alumnos.apellido_paterno}} {{alumnos.apellido_materno}} </td>
												<td class="text-left">{{alumnos.edad}}</td>

                        <td class="text-left">{{alumnos.matricula}}</td>

												<td class="text-left">{{alumnos.genero}}</td>
                        <td class="text-left">{{alumnos.nivel_academico}}</td>
                        <td class="text-left">{{alumnos.periodo}}</td>

                        <td class="text-left">{{alumnos.nombre_profesor + ' ' + alumnos.apellido_profesor }} </td>
												<td>
													<a @click="btnEditar(alumnos.id_alumnos,alumnos.nombre_alumno,alumnos.apellido_paterno,alumnos.apellido_materno,alumnos.edad,alumnos.matricula,alumnos.genero,alumnos.nivel_academico,alumnos.periodo,alumnos.id_profesor)" class="btn btn-outline-warning">
														<i class="fas fa-pen" style="color: #ffae00;"></i> </a>
												</td>
												<td>
													<a v-if="alumnos.eliminado=='0'"
														@click="eliminar(alumnos.id_alumnos, alumnos.eliminado)" class="btn btn-outline-danger">
														<i class="fas fa-user-lock" style="color: #ff6258;"></i>
													</a>
													<a v-else @click="eliminar(alumnos.id_alumnos, alumnos.eliminado)"  class="btn btn-outline-success">
														<i class="fas fa-unlock" style="color: green;"></i>
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
                                        <label> <b> Total: {{ alumnos.length }} registros </b> </label>
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
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                alumnos: [],
                id: '',
                nombre_alumno: '',
                apellido_paterno: '',
                apellido_materno: '',
                apellidos: '',
                edad: '',
                nivel_academico: '',
                periodo: '',
                id_profesor: '',
                matricula: '',
                genero: '',
                password: '',
                id_rol: '',
                filters: {
                    nombre: {
                        value: '',
                        keys: ['nombre_alumno']
                    }
                },
                currentPage: 1,
                totalPages: 0
            }

        },

        mounted() {
            this.getAlumnos();
            this.getprofesor();
        },
        methods: {
            cambiarCampoDeBusqueda() {
                let x = document.getElementById("campoBusqueda").value;
                this.filters.nombre.keys[0] = x;
            },
            getAlumnos() {
                axios({
                    method: 'GET',
                    url: '/alumno/show'
                }).then(
                    result => {
                        console.log(result.data)
                        this.alumnos = result.data[0]
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
            getprofesor() {
                axios({
                    method: 'GET',
                    url: '/show/profesor'
                }).then(
                    result => {
                        this.profesor = result.data
                    },
                    error => {
                        console.error(error)
                    }
                )
            },
          
            guardarAlumno(nombre, apellido_paterno, apellido_materno, edad,matricula, genero, password, nivel_academico, periodo,id_profesor, id_rol) { ///Funcion para guardar los usuarios
                axios.post('/alumno/add', {
                        nombre: nombre,
                        apellido_paterno: apellido_paterno,
                        apellido_materno: apellido_materno,
                        edad: edad,
                        matricula: matricula,
                        genero: genero,
                        password: password,
                        nivel_academico: nivel_academico,
                        periodo: periodo,
                        id_profesor: id_profesor,
                        id_rol: id_rol
                    })
                    .then(() => {
                        this.nombre = '';
                        this.apellido_materno = '';
                        this.apellido_paterno = '';
                        this.edad='';
                        this.matricula = '';
                        this.genero='';
                        this.password = '';
                        this.id_profesor = '';
                        this.id_rol = '';
                        this.nivel_academico = '';
                        this.periodo = '';
                        this.getAlumnos();
                    })
                    .catch((err) => {
                        console.log(err);
                    })
            },
            btnGuardar: async function () {
                const valores = await this.$swal({
                    html: `
                    <h3 class="text-left" style="color:#212529;"> Registrar alumno </h3>
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nombre<span style="color:red">*</span>:  </b> </p>
                    <input id="nombre" type="text" class="form-control" placeholder="Juan">
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido paterno<span style="color:red">*</span>:  </b> </p>
                    <input id="apellido_paterno" type="text" class="form-control" placeholder="Martínez">
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido materno: </b> </p>
                    <input id="apellido_materno" type="text" class="form-control" placeholder="Peréz">
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Edad<span style="color:red">*</span>:  </b> </p>
                    <input type="number" class="form-control" id="edad" name="edad" min="10" max="85" placeholder="10~85" >                    
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Matricula<span style="color:red">*</span>:  </b> </p>
                    <input id="matricula" type="text" class="form-control" placeholder="1234567">
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Género: </b> </p>
                    <select id="genero" value="" name="genero" class="form-control">
                          <option value="Femenino">Femenino</option>
                          <option value="Masculino">Masculino</option>

                    </select>

                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Contraseña<span style="color:red">*</span>:  </b> </p>
                    <input id="password" type="password" class="form-control" placeholder="Contraseña">

                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nivel academico<span style="color:red">*</span>: </b> </p>
                    <input id="nivel_academico" type="text" class="form-control" placeholder="Superior">
               
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b>Período<span style="color:red">*</span>: </b> </p>
                    <select id="periodo" value="" name="periodo" class="form-control">
                          <option value="1">1</option>
                          <option value="2">2</option>
                          <option value="3">3</option>
                          <option value="4">4</option>
                          <option value="5">5</option>
                          <option value="6">6</option>
                          <option value="7">7</option>
                          <option value="8">8</option>
                          <option value="9">9</option>
                          <option value="10">10</option>
                          <option value="11">11</option>
                          <option value="12">12</option>
                          <option value="13">13</option>
                          <option value="14">14</option>
                          <option value="15">15</option>
                    </select>
                    <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Profesor: </b> </p>
                    <select id="id_profesor" value="${this.profesor}" name="profesor" class="form-control">
                        ${this.profesor.map(
                        cat => `<option value="${cat.id}">${cat.nombre}</option>`
                        )}
                    </select>   
                    



                    <div id="div_error_matricula" style="display: none;" class="alert alert-danger" role="alert">
                        <span class="text-left" id="msjError">  </span>
                    </div>
                    <p class="text-left mt-0 mb-0" style="font-size: 12px;"> <span style="color:red">*</span> Datos obligatorios </p>
                    `,
                    focusConfirm: false,
                    showCancelButton: true,
                    confirmButtonText: '<i class="fas fa-save"></i> Guardar',
                    confirmButtonColor: '#007BFF',
                    cancelButtonColor: '#6C757D',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',
                    allowOutsideClick: false,
                    allowEscapeKey: false,
                    
                    
                    preConfirm: async () => {
                        let error = 0;


                        this.nombre = document.getElementById('nombre').value;
                        this.apellido_paterno = document.getElementById('apellido_paterno').value;
                        this.apellido_materno = document.getElementById('apellido_materno').value;
                        this.edad = document.getElementById('edad').value;

                        this.matricula = document.getElementById('matricula').value;
                        this.genero = document.getElementById('genero').value;
                        this.password = document.getElementById('password').value;
                        this.nivel_academico = document.getElementById('nivel_academico').value;
                        this.periodo = document.getElementById('periodo').value;
                        this.id_profesor = document.getElementById('id_profesor').value;

                        let mensajeError = document.getElementById('msjError');

                        if (this.nombre == "" || this.apellido_paterno == "" ||  this.edad == "" || this.password == "" ||
                            this.matricula == "" || this.genero == "" || this.nivel_academico == "" || this.id_profesor == ""
                            ) {
                            error = 2;
                        }  else if(this.edad <10 || this.edad>85){
                            error=3;
                        } else {
                            await axios.post('/verificarExistencia', {
                                    correo: this.matricula
                                })
                                .then((res) => {
                                    if (res.data[0].length !== 0) {
                                        error = 1;
                                    }
                                })
                                .catch((err) => {
                                    console.log(err)
                                })
                        }

                        if (error === 1) {
                            mensajeError.innerHTML =
                                "La matricula ya esta siendo usada, por favor elija otra";
                            document.getElementById('msjError').innerHTML = "El correo está en uso";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else if (error === 2) {
                            mensajeError.innerHTML = "Por favor complete todos los campos requeridos";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        }else if(error===3){
                            mensajeError.innerHTML = "Por favor, ingrese una edad dentro del rango de 10 a 85 años";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else {
                            return [
                                this.nombre,
                                this.apellido_paterno,
                                this.apellido_materno,
                                this.edad,
                                this.matricula,
                                this.genero,
                                this.password,
                                this.nivel_academico,
                                this.periodo,
                                this.id_profesor,
                                error
                            ]
                        }


                    }
                })

                if (valores.hasOwnProperty('value')) {
                    this.guardarAlumno(this.nombre, this.apellido_paterno, this.apellido_materno, this.edad,this.matricula, this.genero,
                        this.password, this.nivel_academico, this.periodo,this.id_profesor, 4);
                    this.$swal.fire({
                        position: 'top-end',
                        icon: 'success',
                        title: 'Información almacenada con éxito',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })
                    this.apellido_paterno = "";
                    this.apellido_materno = "";
                    this.nombre = "";
                    this.edad="";
                    this.matricula = "";
                    this.genero = "";
                    this.password = "";
                    this.id_profesor = "";
                    this.nivel_academico = "";
                    this.periodo = "";

                }

            },
            btnEditar: async function (id, nombre_alumno, apellido_paterno, apellido_materno,edad, matricula,genero,
                nivel_academico, periodo, idProfesor) {
                const valores = await this.$swal({
                    confirmButtonText: '<i class="fa fa-thumbs-o-up"></i> Text',
                    html: `<h3 class="text-left" style="color:#212529;"> Actualizar alumno </h3>
						<p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nombre<span style="color:red">*</span>: </b> </p>
						<input id="nombre" type="text" class="form-control" placeholder="Nombre" value="` + nombre_alumno + `">
						<p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido paterno<span style="color:red">*</span>: </b> </p>
						<input id="apellido_paterno" type="text" class="form-control" placeholder="Apellido Paterno" value="` +
                        apellido_paterno + `">
						<p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido materno: </b> </p>
						<input id="apellido_materno" type="text" class="form-control" placeholder="Apellido Materno" value="` +
                        apellido_materno + `">

						<p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Edad<span style="color:red">*</span>: </b> </p>
						<input id="edad" type="number" class="form-control" placeholder="10~85" value="` + edad + `">
			   
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Matricula<span style="color:red">*</span>: </b> </p>
						<input id="matricula" type="text" class="form-control" placeholder="Matricula" value="` + matricula + `">

            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Género<span style="color:red">*</span>: </b> </p>
            
            <select id="genero" value="` + genero + `" name="genero" class="form-control">
              <option value="` + genero + `">` + genero + `</option>
              <option value="Masculino">Masculino</option>
              <option value="Femenino">Femenino</option>

            </select>

     
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Contraseña<span style="color:red">*</span>: </b> </p>
						<input id="password" type="password" class="form-control" placeholder="Contraseña" value="secret">
						<p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nivel academico<span style="color:red">*</span>: </b> </p>
						<input id="nivel_academico" type="text" class="form-control" placeholder="Superior" value="` +
                        nivel_academico + `" >
						
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b>Período<span style="color:red">*</span>: </b> </p>
                    <select id="periodo" value="" name="periodo" class="form-control">
                         <option value="` + periodo + `">` + periodo + `</option>
                   
                          <option value="1">1</option>
                          <option value="2">2</option>
                          <option value="3">3</option>
                          <option value="4">4</option>
                          <option value="5">5</option>
                          <option value="6">6</option>
                          <option value="7">7</option>
                          <option value="8">8</option>
                          <option value="9">9</option>
                          <option value="10">10</option>
                          <option value="11">11</option>
                          <option value="12">12</option>
                          <option value="13">13</option>
                          <option value="14">14</option>
                          <option value="15">15</option>
                    </select>
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Profesor<span style="color:red">*</span>: </b> </p>
						<select id="id_profesor" value="${
							this.profesor
						}" name="profesor" class="form-control">
							
              ${this.profesor.map(
							cat => `<option value="${cat.id}">${cat.nombre}</option>`
							)}
						</select>

            <div id="div_error_matricula" style="display: none;" class="alert alert-danger" role="alert">
              <span class="text-left" id="msjError">  </span>
            </div>
						<p class="text-left mt-0 mb-0" style="font-size: 12px; color:#212529;"> <span style="color:red">*</span> Datos obligatorios </p>
            <p class="text-left mt-0 mb-0" style="font-size: 12px; color:#212529;"> <span style="color:red">**</span> Deje en blanco si no desea actualizar </p>


							`,
                    focusConfirm: false,
                    showCancelButton: true,
                    confirmButtonText: '<i class="fas fa-save"></i> Guardar',
                    confirmButtonColor: '#007BFF',
                    cancelButtonColor: '#6C757D',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cerrar',
                    allowOutsideClick: false,
                    allowEscapeKey: false,
                    preConfirm: async () => {

                        let error = 0;

                        this.apellido_paterno = document.getElementById('apellido_paterno').value,
                            this.apellido_materno = document.getElementById('apellido_materno').value,
                            this.nombre = document.getElementById('nombre').value,
                            this.edad = document.getElementById('edad').value,

                            this.matricula = document.getElementById('matricula').value,
                            this.genero = document.getElementById('genero').value,
                            this.password = document.getElementById('password').value,
                            this.nivel_academico = document.getElementById('nivel_academico').value,
                            this.periodo = document.getElementById('periodo').value,

                            this.id_profesor = document.getElementById('id_profesor').value,
                            this.id = id

                        let mensajeError = document.getElementById('msjError');

                        if (this.nombre == "" || this.apellido_paterno == "" || this.edad == "" || this.password == "" ||
                            this.matricula == "" || this.genero == "" || this.nivel_academico == "" || this.id_profesor == ""
                            ) {
                            error = 2;
                        }  else if(this.edad <10 || this.edad>85){
                            error=3;
                        }else {

                            if (matricula !== this.matricula) {
                                await axios.post('/verificarExistencia', {
                                        correo: this.matricula
                                    })
                                    .then((res) => {
                                        if (res.data[0].length !== 0) {
                                            error = 1;
                                        }
                                    })
                                    .catch((err) => {
                                        console.log(err)
                                    })

                            }

                        }

                        if (error === 1) {
                            mensajeError.innerHTML =
                                "La matricula ya esta siendo usada, por favor elija otra";
                            document.getElementById('msjError').innerHTML = "El correo está en uso";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else if (error === 2) {
                            mensajeError.innerHTML = "Por favor, complete todos los campos requeridos";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        }else if(error===3){
                            mensajeError.innerHTML = "Por favor, ingrese una edad dentro del rango de 10 a 85 años";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        }
                        else {
                            return [
                                this.apellido_paterno = document.getElementById('apellido_paterno')
                                .value,
                                this.apellido_materno = document.getElementById('apellido_materno')
                                .value,
                                this.nombre = document.getElementById('nombre').value,
                                this.edad = document.getElementById('edad').value,
  
                                this.matricula = document.getElementById('matricula').value,
                                this.genero = document.getElementById('genero').value,
                                this.password = document.getElementById('password').value,
                                this.nivel_academico = document.getElementById('nivel_academico').value,
                                this.periodo = document.getElementById('periodo').value,

                                this.id_profesor = document.getElementById('id_profesor').value,
                                this.id = id,
                                error

                            ]
                        }
                       
                     



                    }
                })

                if (valores.hasOwnProperty('value')) {
                    this.editar(this.id, this.nombre, this.apellido_paterno, this.apellido_materno, this.edad,this.password,
                        this.matricula, this.genero,this.nivel_academico, this.periodo, this.id_profesor);
                }

            },



            editar(id, nombre, apellido_paterno, apellido_materno, edad,password, matricula, genero, nivel_academico, periodo,id_profesor) {
                axios.post('/alumno/actualizar', {
                        id: id,
                        nombre: nombre,
                        apellido_paterno: apellido_paterno,
                        apellido_materno: apellido_materno,
                        edad:edad,
                        password: password,
                        matricula: matricula,
                        genero:genero,
                        nivel_academico: nivel_academico,
                        periodo:periodo,
                        id_profesor: id_profesor
                    })
                    .then((res) => {
                        this.nombre = ''
                        this.nivel_academico = ''
                        this.apellido_materno = ''
                        this.apellido_paterno = ''
                        this.edad=''
                        this.matricula = ''
                        this.genero = ''
                        this.periodo=''
                        this.password = ''
                        this.id = ''
                        this.id_profesor = ''


                        this.$swal.fire({
                            position: 'top-end',
                            icon: 'success',
                            title: 'Información actualizada',
                            showConfirmButton: false,
                            timer: 1500,
                            toast: true
                        })

                        this.getAlumnos()
                    })
                    .catch((err) => {
                        console.log(err)
                    })
            },



            eliminar(id, estado) {

                if (estado == null) {
                    estado = 0;
                }

                console.log("Id " + id + " Estado " + estado);
                this.$swal.fire({
                    html: `
                        <h3 style="color:#212529;">¿Realmente desea eliminar este registro?</h3>
			        `,
                    //icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#DC3545',
                    cancelButtonColor: '#6C757D',
                    confirmButtonText: '<i class="fas fa-trash"></i> Aceptar',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                }).then((result) => {

                    if (result.value) {

                        axios.post('user/delete2', {
                            id: id,
                            estado: estado
                        }).then((res) => {
                            this.id = ''
                            this.getAlumnos()
                            /*const Toast = this.$swal.mixin({
                                toast: true,
                                position: 'top-end',
                                showConfirmButton: false,
                                timer: 3000
                            });
                            this.$swal.fire({
                                type: 'success',
                                title: '¡Tarea realizada con exito!'
                            })*/

                            this.$swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Tarea realizada con éxito',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })

                        }).catch((err) => {
                            console.log(err)

                        })
                    }
                })
            }
        }
    }

</script>
