<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Perfil</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <span style="color: #bdb9bd">  <i class="fas fa-home"></i> <i class="fas fa-angle-right"> </i> </span> <b> Perfil </b>
                        </ol>
                    </div>
                </div>
            </div>
        </div>

		<section class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12 col-md-4">
						<div class="card shadow">
							<div class="card-header">
								<h3 class="card-title mt-2"> <b> Cambiar foto de perfil </b> </h3>
								<div class="card-tools">
									<div class="" style="width: 150px;">
									</div>
								</div>
							</div>
							<div class="card-body">
								<div class="row">
									<form method="POST" action="/subirfotoperfil" enctype="multipart/form-data">
										<div class="form-group">
											<img class="img-circle elevation-2 mt-2" :src="'/imagenes/fotosperfil/'+datos.foto" alt="Profile image" style="width: 150px; ">
										</div>
										<div class="form-group">
											<input type="file" name="profile_pic" required />
										</div>
										<div class="form-group">
											<button type="submit" class="btn btn-primary">  <i class="fas fa-save"></i> Guardar </button>
										</div>
									</form>
								</div>
							</div>
							<div class="card-footer">
								<div class="row">
								</div>
							</div>
						</div>
					</div>
                
             
					<div class="col-12 col-md-8">
						<div class="card shadow">
							<div class="card-header">
								<h3 class="card-title mt-2"> <b> Datos del perfil de usuario </b> </h3>
								<div class="card-tools">
									<div class="" style="width: 150px;">
									</div>
								</div>
							</div>
							<div class="card-body">
								<form method="POST" action="/editardatos" enctype="multipart/form-data">
									<div class="form-group">
										<label for="exampleInputEmail1">Nombre:</label>
										<input type="text" class="form-control" id="nombre" name="nombre" placeholder="Nombre"
											:value="datos.nombre">
									</div>
									<div class="form-group">
										<label for="exampleInputEmail1">Apellido Paterno:</label>
										<input type="text" class="form-control" id="apellidopaterno" name="apellidopaterno"
											placeholder="Apellido Paterno" :value="datos.apellido_paterno">
									</div>
									<div class="form-group">
										<label for="exampleInputEmail1">Apellido Materno:</label>
										<input type="text" class="form-control" id="apellidomaterno" name="apellidomaterno"
											placeholder="Apellido materno" :value="datos.apellido_materno">
									</div>
									<div class="form-group">
										<label for="exampleInputEmail1">Correo:</label>
										<input type="email" class="form-control" id="coreo" name="correo" placeholder="Correo"
											:value="datos.matricula+'@upv.edu.com'" disabled>
									</div>
									<div class="form-group">
										<label for="exampleInputPassword1">Contraseña:</label>
										<input type="password" class="form-control" id="contrasena" name="contrasena">
									</div>
									<div class="form-group">
										<label for="exampleInputPassword1">Repetir contraseña:</label>
										<input type="password" class="form-control" id="contrasena2" name="contrasena2">
									</div>
									<button type="submit" class="btn btn-primary"> <i class="fas fa-save"></i> Guardar</button>
								</form>
							</div>
							<div class="card-footer">
								<div class="row">
								</div>
							</div>
						</div>
					</div>
                
               <div class="col-12 col-md-12">
						<div class="card shadow">
							<div class="card-header">
								<h3 class="card-title mt-2"> <b> Historial de cambios </b> </h3>
								<div class="card-tools">
									<div class="" style="width: 150px;">
									</div>
								</div>
							</div>
							<div class="card-body">
								<div class="row">
									<form method="POST" action="/subirfotoperfil" enctype="multipart/form-data">
										<div class="form-group">
											
										</div>
										<div class="form-group">
										
										</div>
										<div class="form-group">
										</div>
									</form>
								</div>
							</div>
							<div class="card-footer">
								<div class="row">
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
                datos: {}
            }
        },
        mounted() {
            this.obtenerdatos();

            var uri = window.location.href.split('?');
            var fil = uri[1].split('=')[1];
            console.log(fil);

            if (fil == 1) {
                this.$swal({
                    type: 'success',
                    title: 'Datos guardados correctamente'
                })
            } else if (fil == 2) {
                this.$swal({
                    type: 'error',
                    title: 'Error al guardar los datos'
                })
            }
        },
        methods: {
            obtenerdatos() {
                axios({
                    method: 'GET',
                    url: '/obtenerDatos'
                }).then(
                    result => {
                        this.datos = result.data[0][0]
                    },
                    error => {
                        console.error(error)
                    }
                )
            }


        }
    }

</script>
