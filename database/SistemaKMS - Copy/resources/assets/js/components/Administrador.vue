<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Administradores</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">
                                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
                            </span>
                            <span style="color: #bdb9bd"> Usuarios <i class="fas fa-angle-right"></i>
                            </span>
                            <b> Administradores </b>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
        <section class="content">
            <div class="container-fluid">
                <div class="row ">
                    <div class="col-12">
                        <div class="card shadow">
                            <div class="card-header">
                                <h3 class="card-title mt-2"> <b> Lista de administradores </b> </h3>
                                <div class="card-tools">
                                    <div class="" style="width: 150px;">
                                        <button type="button" class="btn btn-primary float-right" data-toggle="modal"
                                            data-target="#registrarPregunta" @click="btnGuardar">
                                            <i class="fas fa-plus"></i> Nuevo
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <div class="card-body">
                                <div class="row mb-2">
                                    <div class="col-6">
                                        <b> Término de busqueda: </b>
                                        <input class="form-control" type="search" placeholder="Término"
                                            v-model="filters.nombre.value" style="height: 2.35rem;" />
                                    </div>
                                    <div class="col-6">
                                        <b>Campo de busqueda: </b>
                                        <select class="form-control" name="campoBusqueda" id="campoBusqueda"
                                            @change="cambiarCampoDeBusqueda">
                                            <option value="nombre">Nombre</option>
                                            <option value="apellido_paterno">Apellido parterno</option>
                                            <option value="apellido_materno">Apellido materno</option>
                                            <option value="matricula">Correo</option>
                                        </select>
                                    </div>
                                </div>


                                <div class="table-responsive">

                                    <v-table :data="admin" :filters="filters" :currentPage.sync="currentPage"
                                        :pageSize="5" @totalPagesChanged="totalPages = $event" style="width:100%"
                                        class="table table-hover">

                                        <thead slot="head">
                                            <v-th sortKey="nombre" defaultSort="desc">Nombre</v-th>
                                            <v-th sortKey="apellido_paterno" defaultSort="desc">Apellido Paterno</v-th>
                                            <v-th sortKey="apellido_materno" defaultSort="desc">Apellido Materno</v-th>
                                            <v-th sortKey="matricula" defaultSort="desc">Correo</v-th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </thead>
                                        <tbody slot="body" slot-scope="{displayData}">
                                            <tr v-for="admin in displayData" :key="admin.id">
                                                <td>{{ admin.nombre }}</td>
                                                <td>{{ admin.apellido_paterno }}</td>
                                                <td>{{ admin.apellido_materno }}</td>
                                                <td>{{ admin.matricula }} </td>
                                                <td>
                                                    <a @click="btnEditar(admin.id,admin.nombre,admin.apellido_paterno, admin.apellido_materno,admin.matricula)"
                                                        class="btn btn-outline-warning">
                                                        <i class="fas fa-pen " style="color: #ffae00;"></i>
                                                    </a>
                                                </td>
                                                <td>
                                                    <a @click="eliminar(admin.id)" class="btn btn-outline-danger">
                                                        <i class="fas fa-trash " style="color: #ff6258"></i>
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
                                        <label> <b> Total: {{ admin.length }} registros </b> </label>
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
                admin: [],
                id: '',
                nombre: '',
                apellido_paterno: '',
                apellido_materno: '',
                apellidos: '',
                matricula: '',
                password: '',
                id_rol: '',
                filters: {
                    nombre: {
                        value: '',
                        keys: ['nombre']
                    }
                },
                currentPage: 1,
                totalPages: 0
            }
        },
        mounted() {
            this.getAdmin();
        },
        methods: {
            cambiarCampoDeBusqueda() {
                let x = document.getElementById("campoBusqueda").value;
                this.filters.nombre.keys[0] = x;
            },
            getAdmin() {
                axios({
                    method: 'GET',
                    url: 'admin/show'
                }).then(
                    result => {
                        this.admin = result.data
                    },
                    error => {
                        console.error(error)
                    }
                )
            },

            guardarAdmin(nombre, apellido_materno, apellido_paterno, matricula,
                password) { ///Funcion para guardar los usuarios
                axios.post('registrar', {
                        nombre: nombre,
                        nivel_academico: "",
                        id_rol: 1,
                        apellido_materno: apellido_materno,
                        apellido_paterno: apellido_paterno,
                        password: password,
                        matricula: matricula
                    })
                    .then((res) => {
                        this.nombre = ''
                        this.id_rol = ''
                        this.apellido_materno = ''
                        this.apellido_paterno = ''
                        this.matricula = ''
                        this.password = ''
                        this.getAdmin()
                    })
                    .catch((err) => {
                        console.log(err)
                    })
            },
            btnGuardar: async function () {
                const valores = await this.$swal({
                    html: `
                <h3 class="text-left" style="color:#212529;"> Registrar administrador </h3>
                <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nombre<span style="color:red">*</span>: </b> </p>
                <input id="nombre" type="text" class="form-control" placeholder="Juan">
                <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido paterno<span style="color:red">*</span>: </b> </p>
                <input id="apellido_paterno" type="text" class="form-control" placeholder="Martinez">
                <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido materno: </b> </p> 
                <input id="apellido_materno" type="text" class="form-control" placeholder="Perez">
                <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Correo<span style="color:red">*</span>: <b> </p> 
                <input id="matricula" type="text" class="form-control" placeholder="ejemplo@ejemplo.com">
                <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Contraseña<span style="color:red">*</span>: </b> </p>
                <input id="password" type="password" type="password" class="form-control" placeholder="contraseña"> 
                <div id="div_error_matricula" style="display: none;" class="alert alert-danger" role="alert">
                  <span class="text-left" id="msjError">  </span>
                </div>
                <p class="text-left" style="font-size: 12px;"> <b> <span style="color:red">*</span> Datos obligatorios </b> </p>
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
                        this.apellido_paterno = document.getElementById('apellido_paterno').value;
                        this.apellido_materno = document.getElementById('apellido_materno').value;
                        this.nombre = document.getElementById('nombre').value;
                        this.matricula = document.getElementById('matricula').value;
                        this.password = document.getElementById('password').value;

                        let mensajeError = document.getElementById('msjError');

                        if (this.nombre == "" || this.apellido_paterno == "" || this.password == "" ||
                            this.matricula == "") {
                            error = 2;
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
                                "El Correo ya esta siendo usado, por favor elija otro";
                            document.getElementById('msjError').innerHTML = "El correo está en uso";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else if (error === 2) {
                            mensajeError.innerHTML = "Por favor, complete todos los campos requeridos";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else {
                            return [
                                this.apellido_paterno = document.getElementById('apellido_paterno')
                                .value,
                                this.apellido_materno = document.getElementById('apellido_materno')
                                .value,
                                this.nombre = document.getElementById('nombre').value,
                                this.matricula = document.getElementById('matricula').value,
                                this.password = document.getElementById('password').value,
                                error
                            ]
                        }

                    }
                })

                if (valores.hasOwnProperty('value')) {
                    this.guardarAdmin(this.nombre, this.apellido_materno, this.apellido_paterno, this.matricula,
                        this.password); //funcion guardarAdmin
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
                    this.matricula = "";
                    this.password = "";
                }
            },


            btnEditar: async function (id, nombre, apellido_paterno, apellido_materno, matricula) {
                const valores = await this.$swal({
                    html: `
            <h3 class="text-left" style="color:#212529;"> Actualizar administrador </h3>
			      <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Nombre<span style="color:red">*</span>: </b> </p>
            <input id="nombre" type="text" class="form-control" placeholder="Nombre" value="` + nombre + `">
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido paterno<span style="color:red">*</span>: </b> </p>
            <input id="apellido_paterno" type="text" class="form-control" placeholder="Apellido Paterno" value="` +
                        apellido_paterno + `">
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Apellido materno<span style="color:red">*</span>: </b> </p>
            <input id="apellido_materno" type="text" class="form-control" placeholder="Apellido Materno" value="` +
                        apellido_materno + `">
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Correo<span style="color:red">*</span>: </b> </p>
            <input id="matricula" type="text" class="form-control" placeholder="ejemplo@ejemplo.com" value="` +
                        matricula + `">
            <p class="text-left mt-0 mb-0" style="color:#212529; font-size:16px;"> <b> Contraseña <span style="color:red">**</span> : </b> </p> 
            <input id="password" type="password" class="form-control" placeholder="Contraseña" >  
            <div id="div_error_matricula" style="display: none;" class="alert alert-danger" role="alert">
              <span class="text-left" id="msjError">  </span>
            </div>
            <p class="text-left mt-0 mb-0" style="font-size: 12px;color:#212529;"> <b> <span style="color:red">*</span> Datos obligatorios </b> </p>
            <p class="text-left mt-0 mb-0" style="font-size: 12px;color:#212529;"> <b> <span style="color:red">**</span> Deje en blanco si no desea actualizar </b> </p>

            
            `,
                    focusConfirm: false,
                    showCancelButton: true,

                    confirmButtonText: '<i class="fas fa-save"></i> Guardar',
                    confirmButtonColor: '#007BFF',
                    cancelButtonColor: '#6C757D',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                    allowOutsideClick: false,
                    allowEscapeKey: false,
                    preConfirm: async () => {

                        let error = 0;
                        this.apellido_paterno = document.getElementById('apellido_paterno').value;
                        this.apellido_materno = document.getElementById('apellido_materno').value;
                        this.nombre = document.getElementById('nombre').value;
                        this.matricula = document.getElementById('matricula').value;
                        this.password = "";
                        let mensajeError = document.getElementById('msjError');

                        if (this.nombre == "" || this.apellido_paterno == "" || this.matricula == "") {
                            error = 2;
                        } else {

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
                                "El Correo ya esta siendo usado, por favor elija otro";
                            document.getElementById('msjError').innerHTML = "El correo está en uso";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else if (error === 2) {
                            mensajeError.innerHTML = "Por favor, complete todos los campos requeridos";
                            document.getElementById('div_error_matricula').style.display = "block";
                            return false;
                        } else {
                            return [
                                this.apellido_paterno = document.getElementById('apellido_paterno')
                                .value,
                                this.apellido_materno = document.getElementById('apellido_materno')
                                .value,
                                this.nombre = document.getElementById('nombre').value,
                                this.matricula = document.getElementById('matricula').value,
                                this.password = document.getElementById('password').value,
                                error
                            ]
                        }

                    }
                })

                if (valores.hasOwnProperty('value')) {


                    axios.post('user/actualizar', {
                            id: id,
                            nombre: this.nombre,
                            nivel_academico: "",
                            id_rol: 1,
                            apellido_materno: this.apellido_materno,
                            apellido_paterno: this.apellido_paterno,
                            password: this.password,
                            matricula: this.matricula
                        })
                        .then((res) => {
                            this.nombre = ''
                            this.id_rol = ''
                            this.apellido_materno = ''
                            this.apellido_paterno = ''
                            this.matricula = ''
                            this.password = ''
                            this.id = ''
                            this.getAdmin()
                        })
                        .catch((err) => {
                            console.log(err)
                        })

                    this.$swal.fire({
                        position: 'top-end',
                        icon: 'success',
                        title: 'Información actualizada',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })

                    console.log(this.id, this.nombre, this.apellido_materno, this.apellido_paterno, this.matricula,
                        this.password);
                    this.apellido_paterno = "";
                    this.apellido_materno = "";
                    this.nombre = "";
                    this.matricula = "";
                    this.password = "";
                }

            },



            editar(id, nombre, apellido_materno, apellido_paterno, matricula, password) {
                axios.post('user/actualizar', {
                        id: id,
                        nombre: nombre,
                        nivel_academico: "",
                        id_rol: 1,
                        apellido_materno: apellido_materno,
                        apellido_paterno: apellido_paterno,
                        password: password,
                        matricula: matricula
                    })
                    .then((res) => {
                        this.nombre = ''
                        this.id_rol = ''
                        this.apellido_materno = ''
                        this.apellido_paterno = ''
                        this.matricula = ''
                        this.password = ''
                        this.id = ''
                        this.getAdmin()
                    })
                    .catch((err) => {
                        console.log(err)
                    })
            },



            eliminar(id) {

                this.$swal.fire({
                    html: `
                        <h3 style="color:#212529;">¿Realmente desea eliminar este registro?</h3>
			        `,
                    showCancelButton: true,
                    confirmButtonColor: '#DC3545',
                    cancelButtonColor: '#6C757D',
                    confirmButtonText: '<i class="fas fa-trash"></i> Aceptar',
                    cancelButtonText: '<i class="fas fa-ban"></i> Cancelar',
                }).then((result) => {
                    if (result.value) {
                        axios.post('user/delete', {
                                id: id
                            }).then((res) => {
                                this.nombre = ''
                                this.id_rol = ''
                                this.apellido_materno = ''
                                this.apellido_paterno = ''
                                this.matricula = ''
                                this.password = ''
                                this.id = ''
                                this.getAdmin();

                                this.$swal.fire({
                                    position: 'top-end',
                                    icon: 'success',
                                    title: 'Datos eliminados con éxito',
                                    showConfirmButton: false,
                                    timer: 1500,
                                    toast: true
                                })
                            })
                            .catch((err) => {
                                console.log(err)

                            })
                    }
                })
            }
        }
    }

</script>
