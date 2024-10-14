<template>
    <div class="content-wrapper">

        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">Grafo de conocimiento</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <li class="breadcrumb-item"><a href="#"> Grafo de conocimiento</a></li>
                        </ol>
                    </div><!-- /.col -->
                </div><!-- /.row -->
            </div><!-- /.container-fluid -->
        </div>

        <div class="col-md-12 ">
            <div class="card" id="tarjeta_arbol">
                <div class="card-body">

                    <input id="x_input" type="text" value="0" hidden>
                    <input id="y_input" type="text" value="0" hidden>
                    <input id="e_input" type="text" value="0" hidden>

                    <div id="tree-container" style="width: 100%; ">

                        <div>

                            <button type="button" class="btn btn-success float-right mb-3" data-toggle="modal"
                                data-target="#configuracionGrafo">

                                <i class="fas fa-cogs"></i>
                            </button>

                            <div class="modal animate__bounceIn" id="configuracionGrafo" role="dialog"
                                aria-labelledby="configuracionGrafo" aria-hidden="true" data-focus="false">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="configuracionGrafo">Configuración del grafo</h5>
                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">

                                            <div class="form-group row">
                                                <label for="staticEmail" class="col-sm-6 col-form-label">Vista:</label>
                                                <div class="col-sm-6">
                                                    <input type="checkbox" class="form-check-label"
                                                        id="horizontalVertical">
                                                    <label> Horizontal </label>
                                                </div>
                                            </div>


											<div class="form-group row">
                                                <label class="col-sm-6 col-form-label">
													Mover nodos:
												</label>
                                                <div class="col-sm-6">
                                                    <input type="checkbox" class="form-check-label" id="moverNodosCheck">
                                                    <label> Activado </label>
                                                </div>
                                            </div>


                                            <div class="form-group row">
                                                <label for="staticEmail" class="col-sm-6 col-form-label">Tamaño del
                                                    nodo:</label>
                                                <div class="col-sm-6">
                                                    <select id="slider" onchange="updateSizeNode()"
                                                        class="form-control">
                                                        <option value="10"> 10 % </option>
                                                        <option value="20"> 20 % </option>
                                                        <option value="30"> 30 % </option>
                                                        <option value="40"> 40 % </option>
                                                        <option value="50"> 50 % </option>
                                                        <option value="60"> 60 % </option>
                                                        <option value="70"> 70 % </option>
                                                        <option value="80"> 80 % </option>
                                                        <option value="90"> 90 % </option>
                                                        <option value="100"> 100 % </option>
                                                    </select>
                                                </div>
                                            </div>



                                            <h4>Evidencia de expertos</h4>



                                            <div class="form-group row">
                                                <label for="staticEmail" class="col-sm-6 col-form-label">Nodos
                                                    ponderados:</label>
                                                <div class="col-sm-6">
                                                    <span id="total_evaluados"> </span> de <span
                                                        id="total_nodos_por_ponderar"> </span>
                                                </div>
                                            </div>

                                            <div class="form-group row">
                                                <label for="staticEmail" class="col-sm-6 col-form-label">Registro de
                                                    evidencia:</label>
                                                <div class="col-sm-6">
                                                    <button type="button" class="d-block btn btn-primary"
                                                        onclick="resetearConteo()" id="btn_empezar_evidencia">
                                                        <i class="fas fa-edit"></i> Comenzar
                                                    </button>
                                                </div>
                                            </div>




                                            <!-- <table class="table">
											<tr>
												<td> 
													Vista 
												</td>
												<td>
													<center>
														<input type="checkbox" class="form-check-label" id="horizontalVertical">
														<label> Horizontal </label>
													</center>
												</td>
											</tr>

											<tr>
												<td>
													Tamaño del nodo
												</td>
												<td>
													<select  id="slider" onchange="updateSizeNode()" class="form-control"> 
														<option value="10"> 10 % </option>
														<option value="20"> 20 % </option>
														<option value="30"> 30 % </option>
														<option value="40"> 40 % </option>
														<option value="50"> 50 % </option>
														<option value="60"> 60 % </option>
														<option value="70"> 70 % </option>
														<option value="80"> 80 % </option>
														<option value="90"> 90 % </option>
														<option value="100"> 100 % </option>
													</select>
												</td>
											</tr>
											

											<tr>
												<td> 
													Nodos ponderados:
												</td>
												<td> 
													<center>  
														<span id="total_evaluados"> </span> de  <span id="total_nodos_por_ponderar"> </span> 
													</center> 
												</td>
											</tr>
											<tr>
												<td>
													Registro de evaluación
												</td>
												<td>
													<center>
														<button type="button" class="btn btn-primary"  onclick="resetearConteo()" id="btn_empezar_evidencia">
															<i class="fas fa-edit"></i> Comenzar
														</button>
													</center>
												</td>
												
											</tr>
										</table> -->

                                            <button type="button" class="btn btn-secondary float-right btn-lg mt-4 "
                                                data-dismiss="modal" style="border-radius: 4px"> <i
                                                    class="fas fa-ban"></i> Cerrar
                                            </button>
                                        </div>

                                    </div>
                                </div>
                            </div>

                            <!-- <table class="table">
								<tr>
									<td> 
										Vista 
									</td>
									<td>
										<center>
											<input type="checkbox" class="form-check-label" id="horizontalVertical">
											<label> Horizontal </label>
										</center>
									</td>
								</tr>

								<tr>
									<td>
										Tamaño del nodo
									</td>
									<td>
										<select  id="slider" onchange="updateSizeNode()" class="form-control"> 
											<option value="10"> 10 % </option>
											<option value="20"> 20 % </option>
											<option value="30"> 30 % </option>
											<option value="40"> 40 % </option>
											<option value="50"> 50 % </option>
											<option value="60"> 60 % </option>
											<option value="70"> 70 % </option>
											<option value="80"> 80 % </option>
											<option value="90"> 90 % </option>
											<option value="100"> 100 % </option>
										</select>
									</td>
								</tr>
								

								<tr>
									<td> 
										Nodos ponderados:
									</td>
									<td> 
										<center>  
											<span id="total_evaluados"> </span> de  <span id="total_nodos_por_ponderar"> </span> 
										</center> 
									</td>
								</tr>
								<tr>
									<td>
										Registro de evaluación
									</td>
									<td>
										<center>
											<button type="button" class="btn btn-primary"  onclick="resetearConteo()" id="btn_empezar_evidencia">
												<i class="fas fa-edit"></i> Comenzar
											</button>
										</center>
									</td>
									
								</tr>
							</table> -->
                        </div>
                    </div>



                    <div class="row">
                        <div class="col-md-12">


                            <div class="modal animated animate__bounceIn" id="RenameNodeModal" tabindex="-1"
                                role="dialog" aria-labelledby="RenameNodeModal" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <h2 id="modalTitle">Renombrar Nodo</h2>

                                            <form id="RenameNodeForm">

                                                <div class="form-group">
                                                    <label>Nombre del nodo</label>
                                                    <input type="text" class="form-control" id='RenameNodeName'
                                                        placeholder="nombre del nodo" />
                                                    <p id="mensaje_3" style="color: red;"></p>
                                                </div>



                                            </form>



                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>

                                            <button type="button" onclick="rename_node()"
                                                class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>


                                        </div>
                                    </div>
                                </div>
                            </div>


                            <div class="modal animated animate__bounceIn" id="CreateNodeModal" tabindex="-1"
                                role="dialog" aria-labelledby="CreateNodeModal" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">
                                            <h2 id="modalTitle">Crear Nodo</h2>
                                            <form id="CreateNodeForm">
                                                <div class="form-group">
                                                    <label>Nombre del nodo</label>
                                                    <input type="text" class="form-control" id='CreateNodeName'
                                                        placeholder="nombre del nodo" />
                                                    <p id="mensaje_4" style="color: red;"></p>
                                                </div>
                                                <div class="form-group">
                                                    <span>Seleccione el color de la conexión: </span>
                                                    <input type="color" id="colorNuevaConexion"
                                                        class="form-control form-control-color">
                                                </div>
                                            </form>
                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>
                                            <button type="button" onclick="create_node()"
                                                class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>



                            <div class="modal animated animate__bounceIn" id="NewParentModal" role="dialog"
                                aria-labelledby="NewParentModal" aria-hidden="true" data-focus="false">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <h2 id="modalTitle">Crear conexión parental</h2>

                                            <div class="form-group">
                                                <span>Seleccione el padre: </span>
                                                <select id="nodesSelect" class="form-control" style="width:100%">
                                                </select>
                                                <span id="mensaje_1" style="color: red;"></span>
                                            </div>

                                            <div class="form-group">
                                                <span>Seleccione el color de la conexión: </span>
                                                <input type="color" id="colorConexion"
                                                    class="form-control form-control-color">
                                            </div>


                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>
                                            <button type="button" onclick="createParentConection()"
                                                class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>





                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--MODAL PARA BORRAR UN  PADRE AL NODO-->

                            <div class="modal animated animate__bounceIn" id="DeleteParentModal" tabindex="-1"
                                role="dialog" aria-labelledby="DeleteParentModal" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <h2 id="modalTitle">Eliminar un padre del nodo</h2>

                                            <div class="form-group">
                                                <span>Selecciona el nodo: </span>
                                                <select id="deleteParentSelect" class="js-example-basic-multiple"
                                                    style="width:50%">
                                                </select>
                                                <span id="mensaje_2" style="color: red;"></span>
                                            </div>

                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>
                                            <button type="button" onclick="deleteParent()"
                                                class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Eliminar
                                            </button>



                                        </div>
                                    </div>
                                </div>
                            </div>


                            <div class="modal animated animate__bounceIn" id="DeleteNodeModal" tabindex="-1"
                                role="dialog" aria-labelledby="DeleteNodeModal" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <div class="form-group">
                                                <label>Elija una opción:</label>
                                                <select id="optionsDelete" class="js-example-basic-multiple"
                                                    style="width:50%">
                                                    <option value="1">Borrar Todos</option>
                                                    <option value="2">Hacer padre al abuelo</option>
                                                    <option value="3">Cambiar de padre a un hijo</option>
                                                    <option value="4">Cambiar de padre</option>
                                                </select>
                                            </div>

                                            <div class="form-group">
                                                <select id="nodesSelectAllDelete" name="selectName" class="form-control"
                                                    style="width:50%">
                                                </select>
                                            </div>

                                            <div class="form-group">
                                                <select id="nodesSelectChildNewParent" name="selectName"
                                                    class="form-control" style="width:50%">
                                                </select>
                                            </div>

                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>

                                            <button class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                onclick="delete_node(node_to_delete)" style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>


                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="modal animated animate__bounceIn" id="QuestionModal" tabindex="-1" role="dialog"
                                aria-labelledby="QuestionModal" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">


                                            <h3 id="modalTitle"> <b> Estimación del experto sobre el grado de
                                                    conocimiento de sus alumnos. </b> </h3>



                                            <p style="font-size:1.5rem;">
                                                Considerando todos los alumnos a los cuales ha impartido la clase de
                                                matemáticas. Realice una estimación de una distribución de porcentajes
                                                en los siguientes rangos.
                                            </p>

                                            <div>
                                                <ol id="questionList">
                                                </ol>
                                            </div>

                                            
											<div clas="row mb-2">
                                                <div class="col-12">
                                                    <button href="#" class="btn btn-secondary float-right"
                                                        id="btn_siguiente_tema" onclick="siguienteRegistroEvidencia()">
                                                        <i class="fas fa-arrow-right"></i>
                                                    </button>

                                                    <button href="#" class="btn btn-secondary float-right"
                                                        id="btn_anterior_tema" onclick="anteriorRegistroEvidencia()">
                                                        <i class="fas fa-arrow-left"></i>
                                                    </button>

                                                </div>
                                            </div>

                                            <table class="table table-striped">
                                                <thead>
                                                    <tr>
                                                        <th scope="col" style="font-size:20px;">Tipo</th>
                                                        <th scope="col" style="font-size:20px;">Descripción</th>
                                                        <th scope="col" style="font-size:20px;">Porcentaje</th>
                                                    </tr>
                                                </thead>
                                                <tbody>

                                                    <tr>
                                                        <td style="font-size:20px;">Bueno</td>
                                                        <td style="font-size:20px;">Mayor a 83 - Menor o igual a 100
                                                        </td>
                                                        <td style="font-size:20px;"> <input onkeyup="cambioInput(id)"
                                                                onchange="cambioInput(id)" type="number" min="0"
                                                                max="100" class="form-control" id="inp_bueno"> </td>
                                                    </tr>

                                                    <tr>
                                                        <td style="font-size:20px;">Regular</td>
                                                        <td style="font-size:20px;"> Mayor a 66 - Menor o igual a 83
                                                        </td>
                                                        <td style="font-size:20px;"> <input onkeyup="cambioInput(id)"
                                                                onchange="cambioInput(id)" type="number" min="0"
                                                                max="100" class="form-control" id="inp_regular"> </td>
                                                    </tr>

                                                    <tr>
                                                        <td style="font-size:20px;">Bajo</td>
                                                        <td style="font-size:20px;"> Mayor a 0 - Menor o igual a 66 </td>
                                                        <td style="font-size:20px;"> <input onkeyup="cambioInput(id)"
                                                                onchange="cambioInput(id)" type="number" min="0"
                                                                max="100" class="form-control" id="inp_bajo"> </td>
                                                    </tr>

                                                    <tr>
                                                        <td></td>
                                                        <td style="font-size:20px;">Total:</td>
                                                        <td style="font-size:20px;">
                                                            <h3> <b> <label id="lbl_total_porcentaje"> x </label> </b>
                                                            </h3>
                                                        </td>
                                                    </tr>


                                                </tbody>
                                            </table>

                                            <label id="msg_porcentaje"></label><br>
                                            <label id="msg_cero"></label>



											



                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>

                                            <button class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                id="btn_guardar_porcentajes" onclick="guardarPorcentajes()"
                                                style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>


                                        </div>
                                    </div>
                                </div>
                            </div>


                            <!-- Modal -->
                            <div class="modal animated animate__bounceIn" id="modalDeCarga" role="dialog"
                                aria-labelledby="modalDeCarga" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <center>


                                                <div class="spinner-border text-primary" role="status">
                                                    <span class="sr-only">Loading...</span>
                                                </div>
                                                Cargando

                                            </center>


                                        </div>
                                    </div>
                                </div>
                            </div>




                            <!--MODAL PARA CAMBIAR DE COLOR AL NODO-->

                            <div class="modal animated animate__bounceIn" id="CambiarColorConexion" tabindex="-1"
                                role="dialog" aria-labelledby="CambiarColorConexion" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <h2 id="modalTitle">Cambiar color de conexión</h2>

                                            <div class="form-group">
                                                <input id="idConexion" value="" hidden />
                                                <span>Seleccione el nuevo color de la conexión: </span>
                                                <input type="color" id="colorConexionNvo"
                                                    class="form-control form-control-color">
                                            </div>

                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>

                                            <button class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                onclick="guardarNuevoColor()" style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Guardar
                                            </button>



                                        </div>
                                    </div>
                                </div>
                            </div>



                            <div class="modal animated animate__bounceIn" id="CambiarConexionPadre" role="dialog"
                                aria-labelledby="CambiarConexionPadre" aria-hidden="true" data-focus="false">
                                <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-body">

                                            <h2 id="modalTitle"> Cambiar conexión parental </h2>

                                            <div class="form-group">
                                                <span>Nodo seleccionado:</span>
                                                <select id="childrenSelect" class="js-example-basic-multiple"
                                                    style="width:100%" disabled></select>
                                            </div>

                                            <div class="form-group">
                                                <span>Elija el nodo padre a cambiar:</span>
                                                <select id="oldParentSelect" class="js-example-basic-multiple"
                                                    style="width:100%"></select>
                                                <span id="mensaje_1" style="color: red;"></span>
                                            </div>

                                            <div class="form-group">
                                                <span>Elija el nuevo padre:</span>
                                                <select id="newParentSelect" class="js-example-basic-multiple"
                                                    style="width:100%"></select>

                                            </div>

                                            <div class="form-group">
                                                <span>Seleccione el color de la conexión: </span>
                                                <input type="color" id="colorParentConnection"
                                                    class="form-control form-control-color">
                                            </div>


                                            <button type="button" data-dismiss="modal"
                                                class="btn btn-secondary float-right btn-lg mt-4 "
                                                style="border-radius: 4px">
                                                <i class="fas fa-ban"></i> Cerrar
                                            </button>

                                            <button class="btn btn-primary float-right btn-lg mt-4 mr-2"
                                                onclick="changeParent()" style="border-radius: 4px">
                                                <i class="fas fa-save"></i> Crear conexión
                                            </button>

                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {

            }
        },
        mounted() {
          
            let dndTree = document.createElement('script')
            dndTree.setAttribute('src', 'arbol/experto/dndTree.js')
            document.head.appendChild(dndTree)
          
          


            $('document').ready(function () {
                $('.js-example-basic-multiple').select2();
                $('#nodesSelect').select2();
                $('#nodesSelectAllDelete').select2();
                $('#nodesSelectChildNewParent').select2();
                $('#nodesSelectAllDelete').next(".select2-container").hide();
                $('#nodesSelectChildNewParent').next(".select2-container").hide();

                $("#horizontalVertical").change(function (e) {
                    horizontalVertical = !horizontalVertical;
                    outer_update(tree_root);
                });

				

				$("#moverNodosCheck").change(function (e) {
                    
					habilitarDesplazamiento();
                    //outer_update(tree_root);
                });



                $("#textPosition").change(function (e) {
                    textPosition = !textPosition;
                });

                $("#textPositionRename").change(function (e) {
                    textPosition = !textPosition;
                });

                $("#orienta").change(function (e) {
                    outer_update(tree_root);

                });

                $("#showNames").change(function (e) {
                    showNames = !showNames;
                    outer_update(tree_root);

                });

                $("#showNumber").change(function (e) {
                    showNumber = !showNumber;
                    outer_update(tree_root);
                });



                var $optionsDelete = $("#optionsDelete").select2().on("change", function (e) {
                    var optionsS = $('#optionsDelete').select2('data')
                    let deleteOption = optionsS[0]['id'];
                    if (deleteOption == 4) {
                        $('#nodesSelectAllDelete').next(".select2-container").show();
                        $('#nodesSelectChildNewParent').next(".select2-container").hide();
                    } else if (deleteOption == 3) {
                        $('#nodesSelectChildNewParent').next(".select2-container").show();
                        $('#nodesSelectAllDelete').next(".select2-container").hide();
                    } else {
                        $('#nodesSelectAllDelete').next(".select2-container").hide();
                        $('#nodesSelectChildNewParent').next(".select2-container").hide();
                    }

                });


                //$(document).foundation();
                $(document).on('opened', '[data-reveal]', function () {
                    var element = $(".inputName:visible").first();
                    element.focus(function () {
                        this.selectionStart = this.selectionEnd = this.value.length;
                    });
                    element.focus();
                });
                $('#RenameNodeForm').submit(function (e) {
                    rename_node();
                    return false;
                });
                $('#CreateNodeForm').submit(function (e) {
                    create_node();
                    return false;
                });

                //$(document).foundation();

                /*$(document).on('opened', '[data-reveal]', function () {
                    var element = $(".inputName:visible").first();
                    element.focus(function(){
                        this.selectionStart = this.selectionEnd = this.value.length;
                    });
                    element.focus();
                });
                $('#RenameNodeForm').submit(function(e){});
                $('#CreateNodeForm').submit(function(e){});*/


                d3.json("arbol/tree.json'", draw_tree);

                $('#modalDeCarga').modal('show');

            });

        },
        methods: {

        }
    }

</script>
