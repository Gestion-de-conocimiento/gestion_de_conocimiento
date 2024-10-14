<template>
    <div class="content-wrapper">

		<div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0"> Accesos</h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i> </span> <span style="color: #bdb9bd">  Accesos  </span>
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
                                <h3 class="card-title mt-2"> <b> Configurar accesos al sistema </b> </h3>
                            </div>
							<div class="card-body">
								<label for="roles">Tipo de usuario: </label>
								<select v-model="rol_sel" @change="cambioRol" name="roles" id="roles" class="form-control">
									<option value="2">Experto</option>
									<option value="3">Profesor</option>
									<option value="4">Alumno</option>
								</select>
								<label >Tabla de accesos: </label>
								<div class="table-responsive">
									<table style="width:100%" class="table table-hover">
										<tr>
											<th>Acción</th>
											<th>Descripción</th>
											<th>Estado</th>
										</tr>
										<tr v-for="acceso in accesos">
											<td v-if="acceso.descripcion != '' " > <span style="padding-left: 30px;"> {{ acceso.nombre }}
												</span> </td>
											<td v-else> <b> {{ (acceso.nombre).toUpperCase() }} </b> </td>
											<td> {{ acceso.descripcion }} </td>
											<td v-if="acceso.descripcion != '' ">
												<toggle-button :name="acceso.id.toString()" :value="acceso.estado" color="#82C7EB"
													:labels="true" @change="cambiarEstado" />
											</td>
											<td v-else></td>
										</tr>

									</table>
								</div>
							</div>
                            <div class="card-footer">
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
                rol_sel: 3,
                accesos: [],
                variable: false,
                gruposaccesos: []
            }
        },
        mounted() {


            this.cambioRol();
        },
        methods: {

            abrirModal() {
                console.log("Se ha abierto el modal");
            },

            cambiarEstado(e) {
                let id_nodo = e.srcEvent.target.name;
                let valor = e.value;
                let valor_entero = 0;
                if (valor) {
                    valor_entero = 1;
                }

                axios.post('/guardarAccesoRutas', {
                        idruta: id_nodo,
                        valorruta: valor_entero,
                        idrol: this.rol_sel
                    })
                    .then((res) => {

                        Swal.fire({
                            toast: true,
                            title: 'Configuracion guardada',
                            position: 'top-end',
                            showConfirmButton: false,
                            icon: 'success',
                            timer: 3000
                        })
                        //this.cambioRol();
                    })
                    .catch((err) => {
                        console.log(err)
                    })



            },

            cambioRol() {

                this.accesos = [];

                axios({
                    method: 'GET',
                    url: '/accesos/' + this.rol_sel
                }).then(
                    result => {
                        this.accesos = result.data;

                        let grupo = "";
                        for (var i = 0; i < this.accesos.length; i++) {


                            if (this.accesos[i].grupo != grupo) {
                                grupo = this.accesos[i].grupo;

                                this.accesos.splice(i, 0, {
                                    descripcion: '',
                                    estado: 0,
                                    grupo: 0,
                                    id: 'g' + this.accesos[i].id_grupo,
                                    id_grupo: this.accesos[i].id_grupo,
                                    nombre: '' + grupo,
                                    rol: ''
                                });
                            }
                        }

                        for (var i = 0; i < this.accesos.length; i++) {
                            if (this.accesos[i].estado == 1) {
                                this.accesos[i].estado = true;
                            } else {
                                this.accesos[i].estado = false;
                            }
                        }
                    },
                    error => {
                        console.error(error)
                    }
                )

            }


        }
    }

</script>
