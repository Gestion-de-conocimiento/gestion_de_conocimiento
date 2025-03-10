<template>
    <div class="content-wrapper">
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="page-title m-0">
                            Estatus de dominio
                        </h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <li class="breadcrumb-item"><a href="#"> Estatus de dominio </a></li>
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

                    <div id="contenedor" style="width: 100%; ">

                        <div>

                            <button type="button" class="btn btn-success float-right mb-3" data-toggle="modal"
                                data-target="#configuracionGrafo">

                                <i class="fas fa-cogs"></i>
                            </button>
                          
                            <br>
                          
                            <div class="row">
                              <div class="col-6">
                                
                                  <select name="cars" id="cars">
                                    <option value="grafo1">Grafo 1</option>
                                    <option value="grafo2">Grafo 2</option>
                                  </select>
                                
                              </div>
                              <div class="col-6">
                                  <button type="button" class="btn btn-success float-right mb-3" data-toggle="modal" data-target="#configuracionGrafo">
                                      <i class="fas fa-cogs"></i>
                                  </button>
                              </div>
                            </div>
                            
                            
                          

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

                                            <button type="button" class="btn btn-secondary float-right btn-lg mt-4 "
                                                data-dismiss="modal" style="border-radius: 4px"> <i
                                                    class="fas fa-ban"></i> Cerrar
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
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

        async mounted() {
            $('document').ready(function () {
                $("#horizontalVertical").change(function (e) {
                    horizontalVertical = !horizontalVertical;
                    outer_updateDos(tree_root);
                });
				        $("#moverNodosCheck").change(function (e) {
					          habilitarDesplazamiento();
                });
                $("#orienta").change(function (e) {
                    outer_updateDos(tree_root);
                });
                d3.json("arbol/tree.json'", draw_status_grafo);
                $('#modalDeCarga').modal('show');

            });

        },
      created(){
        
      },
      methods: {

      }
    }

</script>
