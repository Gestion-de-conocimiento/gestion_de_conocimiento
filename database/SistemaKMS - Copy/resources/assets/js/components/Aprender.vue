<template>
  <div class="content-wrapper"> <!-- Elemento raíz -->
    <div class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="page-title m-0">Enseñanza-Aprendizaje</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <span style="color: #bdb9bd">
                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
              </span>
              <span style="color: #bdb9bd">
                Enseñanza-Aprendizaje <i class="fas fa-angle-right"></i>
              </span>
              <b> Contestar </b> 
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
                <h3 class="card-title mt-2"> <b> Ramas de matemáticas</b> </h3>
                <div class="card-tools">
                  <div class="" style="width: 150px;">
                    <button type="button" class="btn btn-primary float-right" data-toggle="modal" data-target="#exampleModal">
                      <i class="fas fa-calculator"></i>  
                    </button>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <div class="row">
                  <div class="col-12">
                    <!-- Botón de iniciar -->
                    <div class="row">
                      <button type="button" @click="Pickle" class="btn btn-primary float-right btn-lg mt-4 mr-2">
                        <i class="fas fa-rocket"></i>
                        Iniciar
                      </button>
                    </div>
                    <!-- Contenedor para los botones de las ramas -->
                    <div class="row mt-4">
                      <div v-for="(nombre, rama) in botonesRamas" :key="rama" class="col-md-4 mb-3">
                        <button
                          v-if="rama >= 2 && rama <= 9"
                          :class="['btn', 'btn-lg', 'btn-block', getButtonClass(rama)]"
                          @click="handleRamaClick(rama)">
                          {{ nombre }}
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
    </section>

    <!-- Modal calculadora -->
    <div class="modal animated animate__bounceIn" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel"> Calculadora </h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <input type="text" class="form-control" id="campo_calculadora" style="text-align:right;font-size:35px;">
            </div>
            <div class="form-group">
              <table style="table-layout: fixed; width: 100%;">
                <tr>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('ac')" style="width: 100%; height: 100%;">AC</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('(')" style="width: 100%; height: 100%;">(</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora(')')" style="width: 100%; height: 100%;">)</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('/')" style="width: 100%; height: 100%;">/</button></td>
                </tr>
                <tr>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('7')" style="width: 100%; height: 100%;">7</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('8')" style="width: 100%; height: 100%;">8</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('9')" style="width: 100%; height: 100%;">9</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('*')" style="width: 100%; height: 100%;">*</button></td>
                </tr>
                <tr>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('4')" style="width: 100%; height: 100%;">4</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('5')" style="width: 100%; height: 100%;">5</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('6')" style="width: 100%; height: 100%;">6</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('+')" style="width: 100%; height: 100%;">+</button></td>
                </tr>
                <tr>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('1')" style="width: 100%; height: 100%;">1</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('2')" style="width: 100%; height: 100%;">2</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('3')" style="width: 100%; height: 100%;">3</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('-')" style="width: 100%; height: 100%;">-</button></td>
                </tr>
                <tr>
                  <td><button class="btn btn-primary" data-toggle="modal" data-target="#funciones" style="width: 100%; height: 100%;">fun</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('0')" style="width: 100%; height: 100%;">0</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('.')" style="width: 100%; height: 100%;">.</button></td>
                  <td><button class="btn btn-primary" v-on:click="botonesCalculadora('=')" style="width: 100%; height: 100%;">=</button></td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal funciones -->
    <div class="modal fade bd-example-modal-lg" id="funciones" tabindex="-1" role="dialog" aria-labelledby="funcionesModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="funcionesModalLabel">Funciones</h5>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' abs (')">abs</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' acos (')">acos</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' acosh (')">acosh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' asin (')">asin</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' asinh (')">asinh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' atan (')">atan</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' atan2 (')">atan2</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' atanh (')">atanh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' bindec (')">bindec</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' ceil (')">ceil</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' cos (')">cos</button></div>
            </div>

            <div class="row">
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' cosh (')">cosh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' decbin (')">decbin</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' decoct (')">decoct</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' deg2rad (')">deg2rad</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' exp (')">exp</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' expm1 (')">expm1</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' floor (')">floor</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' log10 (')">log10</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' log1p (')">log1p</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' log (')">log</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' max (')">max</button></div>
            </div>

            <div class="row">
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' min (')">min</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' pi ( )')">pi</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' pow (')">pow</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' rad2deg (')">rad2deg</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' round (')">round</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' sin (')">sin</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' sinh (')">sinh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' sqrt (')">sqrt</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' tan (')">tan</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' tanh (')">tanh</button></div>
              <div class="col-1"><button class="btn btn-primary" v-on:click="botonesCalculadora(' ,')">,</button></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div> <!-- Cierre del contenedor raíz -->
</template>


<script>
  import axios from "axios";
  import { useRouter } from 'vue-router'; // Importar el hook para la navegación
  export default {
    data() {
      return {
        botonesRamas: {}, // Objeto para almacenar las ramas y sus nombres
        gradosPorRama: {}, // Almacena los grados de conocimiento por rama
        temasPorRama: {}, // Almacena los temas por rama para el orden de enseñanza
        //branchLabels: [],
        //resultadoArray: [], // Array que contendrá el resultado de la API
        //ramasUnicas: [], // Array para almacenar las ramas únicas
        //temasPorRama: [],
       /* ramas:[],//utilizado actualmente
        mostrarRamas: false,
         ramasMap: {
        2: 'Aritmética',
        3: 'Álgebra',
        4: 'Geometría',
        5: 'Álgebra Lineal',
        6: 'Trigonometría',
        7: 'Funciones Matemáticas',
        8: 'Cálculo Diferencial',
        9: 'Cálculo Integral',
      },*/
        
        pregunta: [],
        pCalculadas: [],
        pCalculadasMultiples: [],
        opciones: [],
        comodines: [],
        configuracion: [],
        topic: [],
        numero_tema: 0,
        imagenesPregunta: [],
        imagenActual: '',
        imagenActualNombre: '',
        salidaModulo: '',
        ordenEvaluacion: [],
        ponderacion: 0,
        estatus: [],
        ultimoTema: 0,
        datosEvaluacion: {},
        temasAEvaluar: [96, 26, 44, 91],
        temaAEvaluarActual: 0,
      };
    },
    /*computed: {
    // Computed property para filtrar las ramas que estén entre 2 y 9
    ramasFiltradas() {
      return this.ramas.filter(rama => rama >= 2 && rama <= 9);
    }
  },*/
    async created() {

      
      await this.Pickle();
      
      
      
    },
    methods: {
      
      /* Pickle(){
        //console.log("Hola")
         
      },*/
       Pickle: async function() {
    try {
      console.log("Hola");
      const result = await axios({
        method: 'get',
        url: "/obtenerMatricula/" + matricula
      });
      this.botonesRamas = this.mapearRamas(result.data.temas_por_rama);
      this.gradosPorRama = this.mapearGrados(result.data.temas_por_rama);
      this.temasPorRama = result.data.temas_por_rama;
    } catch (error) {
      console.error("Ocurrió un error en la solicitud:", error);
    }
  },
    mapearRamas(temasPorRama) {
      const nombresRamas = {
      2: 'Aritmética',         // Añadida la tilde en la 'e'
      3: 'Álgebra',            // Correcto
      4: 'Geometría',         // Correcto
      5: 'Álgebra lineal',    // Correcto
      6: 'Trigonometría',     // Correcto
      7: 'Funciones matemáticas', // Correcto
      8: 'Cálculo diferencial',  // Correcto
      9: 'Cálculo integral'      // Correcto
    };

      let botones = {};
      for (const [rama, temas] of Object.entries(temasPorRama)) {
        const ramaNum = parseInt(rama);
        if (ramaNum >= 2 && ramaNum <= 9) {
          botones[ramaNum] = nombresRamas[ramaNum] || 'Rama Desconocida';
        }
      }
      return botones;
    },
    mapearGrados(temasPorRama) {
      let grados = {};
      for (const [rama, temas] of Object.entries(temasPorRama)) {
        grados[rama] = temas.every(tema => tema.grado_de_conocimiento === 2);
      }
      return grados;
    },
    getButtonClass(rama) {
      return this.gradosPorRama[rama] ? 'btn-primary' : 'btn-secondary';
    },
    handleRamaClick(rama) {
        console.log(`Botón de la rama ${rama} clickeado`);
        const nombreRama = this.botonesRamas[rama];
        if (this.gradosPorRama[rama]) {
          this.$router.push({ name: 'vista-especial', params: { rama }, query: { nombre: nombreRama } });
        } else {
          this.$router.push({ name: 'vista-general', params: { rama }, query: { nombre: nombreRama } });
        }
      },
      
      getopic: async function() {
        await axios({
          method: 'get',
          url: 'topic/getopic/'+this.ultimoTema
        }).then(
          result => {
            this.topic = result.data[0];
          }, error => {
            console.error(error)
          }
        )
      },  /*-------------------------------------------------------configuración del número de preguntas-----------------------------*/
      
      
     
      cargarCuestionario: async function(topic, prguntass) {
        
        //console.log("Se va a cargar el cuestionario con el tema " + topic);
        
        var questions = [];
        for (var i = 0; i < prguntass.length; i++) {
          var pregunta = prguntass[i].pregunta
          var tipo = Number(prguntass[i].tipo);
          var id = prguntass[i].id_pregunta;
          var up = 0;
          var down = 0;
          var value = 0;
          var decimales = 0;
          let imagenesPregunta = prguntass[i].imagenes;

          if (prguntass[i].tipo == 2 || prguntass[i].tipo == 5 || prguntass[i].tipo == 6) {
            up = prguntass[i].aplicableArriba;
            down = prguntass[i].aplicableAnbajo;
            value = prguntass[i].rango;
          }
          if (prguntass[i].tipo == 5 || prguntass[i].tipo == 6) {
            decimales = prguntass[i].decimales;
          }

          questions.push(new Question(id, pregunta, [], [], tipo, up, down, value, decimales,
            imagenesPregunta));

        }


        /* ESTA ES LA PARTE DEL CUESTIONARIO */
        function Quiz(questions) {
          this.score = 0;
          this.questions = questions;
          this.questionIndex = 0;
        }
        Quiz.prototype.getQuestionIndex = function() {
          return this.questions[this.questionIndex];
        }
        Quiz.prototype.guess = function(answer) {
          return this.getQuestionIndex().isCorrectAnswer(answer);
        }
        Quiz.prototype.isEnded = function() {
          return this.questionIndex === this.questions.length;
        }
        Quiz.prototype.nextQuestion = function() {
          this.questionIndex++;
        }
        Quiz.prototype.getImages = function() {
          return this.getQuestionIndex().imagenes;
        }
        function Question(id, text, choices, answer, type, up, down, value, decimales, imagenes) {
          this.id = id;
          this.text = text;
          this.choices = choices;
          this.answer = answer;
          this.type = type;
          this.up = up;
          this.down = down;
          this.value = value;
          this.decimales = decimales;
          this.imagenes = imagenes;
        }
        Question.prototype.isCorrectAnswer = function(choice) {
          var correcta = false;

          switch (this.type) {
            case 1:
              if (choice == this.answer[0].toString().toLowerCase())
                correcta = true;
              break;
            case 2:
              //validar que si entra una fracción tomarla como texto 
              var isfraccion = this.answer[0].search('/');
              console.log("SI ES FRACCION "+isfraccion)
                
              if(isfraccion >= 0){
                if(choice == this.answer[0].toString()){
                  correcta = true;
                }
                
              }else{
              
              
              this.answer[0] = Number(this.answer[0]);
              var arriba = this.answer[0] + Math.abs(Number(this.answer[0] * this.value * this
                .up))
              var abajo = this.answer[0] - Math.abs(Number(this.answer[0] * this.value * this
                .down))

              if (choice >= abajo && choice <= arriba) {
                correcta = true;

              }}


              break;
            case 3:
              if (choice == this.answer[0])
                correcta = true;
              break;
            case 4:
              for (var i = 0; i < this.answer.length; i++) {
                if (choice == this.answer[i]) {
                  correcta = true;
                }
              }
              break;

            case 5:
              this.answer[0] = Number(this.answer[0]);
              var arriba = this.answer[0] + Math.abs(Number(this.answer[0] * this.value * this
                .up))
              var abajo = this.answer[0] - Math.abs(Number(this.answer[0] * this.value * this
                .down))

              if (choice >= abajo && choice <= arriba) {
                correcta = true;
              }
              break;

            case 6:
              for (var i = 0; i < this.answer.length; i++)
                if (choice == this.answer[i])
                  correcta = true;
              break;
          }
          return correcta;
        }
        var tipo = this.configuracion.ponde_estricta; //
        var cuestionarioTema = new Quiz(questions);
        
        console.log(questions);
       
        //Boton de siguiente pregunta
        
        document.getElementById("next").addEventListener("click", async function() {

          console.log("Quizz");
          console.log(cuestionarioTema);
          
          //AQUI SE OBTIENE LA RESPUESTA A LA PREGUNTA
          await axios({
            method: 'get',
            url: '/pregunta/respuestas/' + cuestionarioTema.getQuestionIndex().id
          }).then(
            result => {
              var res = [];
              var id_opcion_correcta = [];
              for (var i = 0; i < result.data.length; i++) {
                res.push(result.data[i].opcion);
                id_opcion_correcta.push(result.data[i].id_opcion);
              }

              if (cuestionarioTema.getQuestionIndex().type == 5 || cuestionarioTema.getQuestionIndex().type ==
                6) {
                var power = Math.pow(10, cuestionarioTema.getQuestionIndex().decimales);
                //console.log("Respuesta antes de la funcion "+res[0]);
                res = [Math.round(_this.generarRespuesta(cuestionarioTema.getQuestionIndex().id,
                  res[0], id_opcion_correcta[0]) * power) / power];
                //label.innerHTML = Math.round(_this.generarRespuesta(cuestionarioTema.getQuestionIndex().id,choices[i], opcionesAux[i].id_opcion) * power) / power;
              }

              cuestionarioTema.getQuestionIndex().answer = res;
            }, error => {
              console.error(error)
            }
          )

          var respuestas_correctas = 0;
          var respuestas_incorretas = 0;

          switch (cuestionarioTema.getQuestionIndex().type) {

            case 1:

              var opc = document.getElementById("input_respuesta");
              var resp = opc.value.toString().toLowerCase();
              resp = resp.trim();
              resp = resp.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,
                "");

              if (resp == "") {
                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Por favor ingresa una respuesta válida',
                  showConfirmButton: false,
                  timer: 1500
                })
                return;
              }

              if (cuestionarioTema.guess(resp))
                respuestas_correctas++;
              else
                respuestas_incorretas++;
              break;
/* Validación para la pregunta númerica */
            case 2:
              var opc = document.getElementById("input_respuesta");

              if (opc.value == "") {
                //_this.$swal.fire("Por favor ingresa una respuesta valida");

                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Por favor ingresa una respuesta válida',
                  showConfirmButton: false,
                  timer: 1500
                })

                return;
              }

              if (cuestionarioTema.guess(opc.value))
                respuestas_correctas++;
              else
                respuestas_incorretas++;

              break;
            case 3:

              var input_verdadero = document.getElementById("input_verdadero");
              var input_falso = document.getElementById("input_falso");
              var resp = "";

              if (input_verdadero.checked && !input_falso.checked)
                resp = "verdadero";

              if (input_falso.checked && !input_verdadero.checked)
                resp = "falso";

              if (input_verdadero.checked === false && input_falso.checked === false) {
                //_this.$swal.fire("Por favor selecciona una respuesta");

                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Selecciona una respuesta',
                  showConfirmButton: false,
                  timer: 1500
                })

                return;
              }

              if (cuestionarioTema.guess(resp))
                respuestas_correctas++;
              else
                respuestas_incorretas++;
              break;

            case 4:
              var chequeada = false;
              for (var i = 0; i < cuestionarioTema.getQuestionIndex().choices.length; i++) {
                var opc = document.getElementById("opc_" + i);
                if (opc.checked) {
                  chequeada = true;
                }
              }

              if (!chequeada) {
                //_this.$swal.fire("Por favor selecciona una respuesta");
                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Selecciona una respuesta',
                  showConfirmButton: false,
                  timer: 1500
                })

                return;
              }


              for (var i = 0; i < cuestionarioTema.getQuestionIndex().choices.length; i++) {
                var opc = document.getElementById("opc_" + i);
                if (opc.checked) {
                  var lbl = document.getElementById("opcl_" + i);
                  var opcion_text = lbl.innerHTML.split("<")[
                    0]; //Obtener el texto del check
                  if (cuestionarioTema.guess(opcion_text)) {
                    respuestas_correctas++;
                  } else {
                    respuestas_incorretas++;
                  }
                }
              }

              break;

            case 5:
              var opc = document.getElementById("input_respuesta");
              var resp = opc.value.toString().toLowerCase();
              resp = resp.trim();
              resp = resp.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ /g,
                "");

              if (resp == "") {
                //_this.$swal.fire("Por favor ingresa una respuesta valida");
                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Por favor ingresa una respuesta válida',
                  showConfirmButton: false,
                  timer: 1500
                })
                return;
              }

              if (cuestionarioTema.guess(opc.value))
                respuestas_correctas++;
              else
                respuestas_incorretas++;
              break;

            case 6:

              var chequeada = false;
              for (var i = 0; i < cuestionarioTema.getQuestionIndex().choices.length; i++) {
                var opc = document.getElementById("opc_" + i);
                if (opc.checked) {
                  chequeada = true;
                }
              }

              if (!chequeada) {
                _this.$swal.fire({
                  position: 'center',
                  icon: 'warning',
                  title: 'Selecciona una respuesta',
                  showConfirmButton: false,
                  timer: 1500
                })

                return;
              }

              for (var i = 0; i < cuestionarioTema.getQuestionIndex().choices.length; i++) {
                var opc = document.getElementById("opc_" + i);
                if (opc.checked) {
                  var lbl = document.getElementById("opcl_" + i);
                  var opcion_text = lbl.innerHTML.split("<")[0];
                  if (cuestionarioTema.guess(opcion_text)) {
                    respuestas_correctas++;
                  } else {
                    respuestas_incorretas++;
                  }
                }
              }

              break;

          }
          if (respuestas_correctas == cuestionarioTema.getQuestionIndex().answer.length &&
            respuestas_incorretas == 0) {
            cuestionarioTema.score = cuestionarioTema.score + 1;
            //_this.$swal.fire('Correcta');
            _this.$swal.fire({
              position: 'top-end',
              icon: 'success',
              title: 'Respuesta correcta',
              showConfirmButton: false,
              timer: 1500
            })
          } else if (respuestas_correctas > 0 && respuestas_incorretas == 0 && tipo == 0) {
            cuestionarioTema.score = cuestionarioTema.score + (respuestas_correctas / cuestionarioTema.getQuestionIndex().answer
              .length);
            //_this.$swal.fire("Parcialmente correcta");
            _this.$swal.fire({
              position: 'top-end',
              icon: 'success',
              title: 'Respuesta parcialmente correcta',
              showConfirmButton: false,
              timer: 1500
            })
          } else {
            //_this.$swal.fire('Incorrecta');

            _this.$swal.fire({
              position: 'top-end',
              icon: 'warning',
              title: 'Respuesta incorrecta',
              showConfirmButton: false,
              timer: 1500
            })
          }

          cuestionarioTema.nextQuestion();
          populate();
        });
        let _this = this
        async function populate() {
          
          if (cuestionarioTema.isEnded()) {
            if (cuestionarioTema.questions.length > 0) {
              var total = Math.round((cuestionarioTema.score / cuestionarioTema.questions.length) * 100);
              
              if ( ! _this.datosEvaluacion.detenerse ) {
                cuestionarioTema = "";
                questions = [];
                
                 _this.ponderacion = total;
                 _this.enviarPonderacion();
                 //_this.getpreguntas();
                
              } else {
                showScores();
              }
            }
          } else {

            document.getElementById("buttons").innerHTML = "";
            var element = document.getElementById("question").innerHTML = cuestionarioTema.getQuestionIndex()
              .text;

            let imgstr = "";
            _this.imagenesPregunta = [];
            for (let ii = 0; ii < cuestionarioTema.getQuestionIndex().imagenes.length; ii++) {
              imgstr = "/imagenes/preguntas/" + cuestionarioTema.getQuestionIndex().imagenes[ii].nombre;
              _this.imagenesPregunta.push(imgstr);
              console.log(_this.imagenesPregunta);
            }
            console.log(cuestionarioTema.getQuestionIndex().imagenes);
            var tema = document.getElementById("tag_topic");
            tema.innerHTML = " <b> Tema: </b> " + _this.topic[0].nombre_tema;


            if (cuestionarioTema.getQuestionIndex().type == 4) {
              await axios({
                method: 'get',
                url: '/pregunta/opciones/' + cuestionarioTema.getQuestionIndex().id
              }).then(
                result => {
                  var ops = [];
                  for (var i = 0; i < result.data.length; i++) {
                    ops.push(result.data[i].opcion);
                  }
                  cuestionarioTema.getQuestionIndex().choices = ops;

                }, error => {
                  console.error(error)
                }
              )
            }

            var opcionesAux = [];
            if (cuestionarioTema.getQuestionIndex().type == 6) {
              await axios({
                method: 'get',
                url: '/pregunta/opcionescalculadasmultiples/' + cuestionarioTema.getQuestionIndex()
                  .id
              }).then(
                result => {
                  var ops = [];
                  for (var i = 0; i < result.data.length; i++) {
                    ops.push(result.data[i].opcion);
                    opcionesAux.push(result.data[i]);
                  }
                  cuestionarioTema.getQuestionIndex().choices = ops;
                }, error => {
                  console.error(error)
                }
              )
            }

            var choices = cuestionarioTema.getQuestionIndex().choices;


            switch (cuestionarioTema.getQuestionIndex().type) {

              case 1:
                var input_respuesta = document.createElement("input");
                input_respuesta.type = "text";
                input_respuesta.id = "input_respuesta";
                var zona_botones = document.getElementById("buttons");
                zona_botones.innerHTML = " <b> Respuesta: </b> <br>";
                zona_botones.appendChild(input_respuesta);
                break;
              case 2:
                var input_respuesta = document.createElement("input");
                input_respuesta.type = "text"; // se cambió de number a text para que acepte fracciones
                input_respuesta.id = "input_respuesta";
                var zona_botones = document.getElementById("buttons");
                zona_botones.innerHTML = "<b> Respuesta: </b> <br>";
                zona_botones.appendChild(input_respuesta);
                break;
              case 3:
                var div_verdadero = document.createElement("div");
                var div_falso = document.createElement("div");
                var label_verdadero = document.createElement("label");
                label_verdadero.innerHTML = " Verdadero";
                var label_falso = document.createElement("label");
                label_falso.innerHTML = " Falso";
                var input_verdadero = document.createElement("input");
                input_verdadero.type = "radio";
                input_verdadero.name = "truefalse";
                input_verdadero.id = "input_verdadero";
                var input_falso = document.createElement("input");
                input_falso.type = "radio";
                input_falso.name = "truefalse";
                input_falso.id = "input_falso";
                div_verdadero.appendChild(input_verdadero);
                div_verdadero.appendChild(label_verdadero);
                div_falso.appendChild(input_falso);
                div_falso.appendChild(label_falso);
                var zona_botones = document.getElementById("buttons");
                zona_botones.innerHTML = " <b> Respuesta: </b> <br>";
                zona_botones.appendChild(div_verdadero);
                zona_botones.appendChild(div_falso);
                break;
              case 4:
                var zona_botones = document.getElementById("buttons");
                zona_botones.innerHTML = " <b> Respuesta: </b> <br>";
                for (var i = 0; i < choices.length; i++) {
                  var label = document.createElement("label");
                  label.innerHTML = choices[i];
                  label.className = "container";
                  label.id = "opcl_" + i;
                  var span = document.createElement("checkmark");
                  span.className = "checkmark";
                  var button = document.createElement("input");
                  button.type = "checkbox"
                  button.text = choices[i];
                  button.id = "opc_" + i;
                  label.appendChild(button);
                  label.appendChild(span);

                  //zona_botones.innerHTML = "Respuesta: <br>";
                  zona_botones.appendChild(label);
                }
                break;
              case 5:
                var input_respuesta = document.createElement("input");
                input_respuesta.type = "number";
                input_respuesta.id = "input_respuesta";
                var zona_botones = document.getElementById("buttons");
                zona_botones.innerHTML = "<b> Respuesta: </b> <br>";
                zona_botones.appendChild(input_respuesta);
                break;
              case 6:
                for (var i = 0; i < choices.length; i++) {
                  var label = document.createElement("label");
                  //label.innerHTML = choices[i];
                  var power = Math.pow(10, opcionesAux[i].decimales);
                  label.innerHTML = Math.round(_this.generarRespuesta(cuestionarioTema.getQuestionIndex()
                    .id, choices[i], opcionesAux[i].id_opcion) * power) / power;
                  label.className = "container";
                  label.id = "opcl_" + i;
                  var span = document.createElement("checkmark");
                  span.className = "checkmark";
                  var button = document.createElement("input");
                  button.type = "checkbox"
                  //button.text = choices[i];
                  button.text = Math.round(_this.generarRespuesta(cuestionarioTema.getQuestionIndex().id,
                    choices[i], opcionesAux[i].id_opcion) * power) / power;
                  button.id = "opc_" + i;
                  label.appendChild(button);
                  label.appendChild(span);
                  var zona_botones = document.getElementById("buttons");
                  zona_botones.innerHTML = " <b> Respuesta: </b> <br>";
                  zona_botones.appendChild(label);
                }
                break;
            }
            //showProgress();
          }
        };
        //Asegurar que solo sean checkeados las posibles respuestas
        function guess() {
          var answers = cuestionarioTema.getQuestionIndex().answer;
          var choices = cuestionarioTema.getQuestionIndex().choices;
          opc_check = 0;

          for (var i = 0; i < choices.length; i++) {
            var opc = document.getElementById("opc_" + i);
            if (opc.checked == true) {
              if (opc_check == answers.length) {
                opc.checked = false;
              } else {
                opc.checked = true;
              }
              opc_check++;
            }
          }

        };
        /*function showProgress() {
          var currentQuestionNumber = cuestionarioTema.questionIndex + 1;
          var element = document.getElementById("progress");
          element.innerHTML = "<b> Progreso: </b>" + currentQuestionNumber + " de " + questionIndex.questions
            .length;
        };*/
        async function showScores() {

          var gameOverHTML = "<h1>Resultados</h1>";
          gameOverHTML += "<center> <h4>Estos son tus resultados</h4> </center>";

          gameOverHTML += "<center> <table><tr><th>Tema</th><th>Dominio</th></tr>";

          await axios.get('/arbol/obtenerResultados').then((res) => {


              for (var i = 0; i < res.data.length; i++) {

                if (res.data[i].clasificacion == 1) {
                  gameOverHTML += "<tr style='background-color: rgb(0,195,255);' >";
                } else {
                  gameOverHTML += "<tr>";
                }

                gameOverHTML += "<td> " + res.data[i].nombre + "</td>";
                gameOverHTML += "<td> " + res.data[i].ponderacion + " % </td>";
                gameOverHTML += "</tr>";
              }

              gameOverHTML += "</table> </center>";

              gameOverHTML +=
                " <center> <h4> Los temas <b style='color: rgb(0,195,255);'> azules</b> son los temas evaluados en el cuestionario </h4> </center>";

              gameOverHTML +=
                " <br> <center> <h6> Muchas gracias por participar. </h6> </center>";
              gameOverHTML += "<center> <h6> Ya puedes cerrar esta ventana </h6> </center>";

            })
            .catch((err) => {
              console.log(err)
            })


          var element = document.getElementById("quiz");
          element.innerHTML = gameOverHTML;


        };
        populate();
      },
      generarRespuesta(id, res, id_opcion_actual) {
        res = res.trim();
        var count = 0;

        function deg2rad(valor) {
          return (valor / 180) * Math.PI;
        }

        function binTodecimal(binstr) {
          return binstr.split('').reverse().reduce(function(x, y, i) {
            return (y === '1') ? x + Math.pow(2, i) : x;
          }, 0);
        }

        function roundTo(value, places) {
          var power = Math.pow(10, places);
          return Math.round(value * power) / power;
        }

        function operacion(nombreOperacion, valor) {
          valor = valor + "";
          valor = valor.split(",")
          switch (nombreOperacion) {
            case "abs":
              return Math.abs(valor[0]);
              break;
            case "acos":
              return Math.acos(valor[0]);
              break;
            case "acosh":
              return Math.acosh(valor[0]);
              break;
            case "asin":
              return Math.asin(valor[0]);
              break;
            case "asinh":
              return Math.asinh(valor[0]);
              break;
            case "atan2":
              return Math.atan2(valor[0], valor[1]);
              break;
            case "atan":
              return Math.atan(valor[0]);
              break;
            case "atanh":
              return Math.atan(valor[0]);
              break;
            case "bindec":
              return binTodecimal(valor[0]);
              break;
            case "ceil":
              return Math.ceil(valor[0]);
              break;
            case "cos":
              return Math.cos(valor[0]);
              break;
            case "cosh":
              return Math.cosh(valor[0]);
              break;
            case "decbin":
              return valor[0].toString(2);
              break;
            case "decoct":
              return valor[0].toString(8);
              break;
            case "deg2rad":
              return deg2rad(valor[0]);
              break;
            case "exp":
              return Math.exp(valor[0]);
              break;
            case "expm1":
              return Math.expm1(valor[0]);
              break;
            case "floor":
              return Math.floor(valor[0]);
              break;
            case "is_finite":
              return isFinite(valor[0]);
              break;
            case "is_infinite":
              return !isFinite(valor[0]);
              break;
            case "is_nan":
              return isNaN(valor[0]);
              break;
            case "log10":
              return Math.log10(valor[0]);
              break;
            case "log1p":
              return Math.log1p(valor[0]);
              break;
            case "log":
              return Math.log(valor[0]);
              break;
            case "max":
              return Math.max.apply(null, valor);
              break;
            case "min":
              return Math.min.apply(null, valor);
              break;
            case "pi":
              return Math.PI;
              break;
            case "pow":
              return Math.pow(valor[0], valor[1])
            case "rad2deg":
              return valor[0] * (180 / Math.PI);
              break;
            case "round":
              return roundTo(valor[0], valor[1]);
              break;
            case "sin":
              return Math.sin(valor[0]);
              break;
            case "sinh":
              return Math.sinh(valor[0]);
              break;
            case "sqrt":
              return Math.sqrt(valor[0]);
              break;
            case "tan":
              return Math.tan(valor[0]);
              break;
            case "tanh":
              return Math.tanh(valor[0]);
              break;

          }

        }
        class Pila {
          constructor() {
            this.items = [];
          }

          incluir(element) {
            this.items.push(element);
            return this.items;
          }
          extraer() {
            return this.items.pop();
          }

          tamano() {
            return this.items.length;
          }

          estaVacia() {
            if (this.items.length == 0)
              return true;
            else
              return false;

          }

          inspeccionar() {
            return this.items[this.items.length - 1];
          }

          print() {
            //console.log(this.items);
          }
        }

        function infija_a_sufija(expresionInfija) {
          var precedencia = {};
          precedencia["*"] = 3;
          precedencia["/"] = 3;
          precedencia["+"] = 2;
          precedencia["-"] = 2;
          precedencia["("] = 1;
          var pilaOperadores = new Pila();
          var listaSufija = [];
          var listaSimbolos = expresionInfija.split(" ");
          for (var simbolo in listaSimbolos) {
            if ('+-*/()'.indexOf(listaSimbolos[simbolo]) == -1)
              listaSufija.push(listaSimbolos[simbolo]); //AÑADE ELEMENTO A LA LISTA
            else if (listaSimbolos[simbolo] == '(')
              pilaOperadores.incluir(listaSimbolos[simbolo]);
            else if (listaSimbolos[simbolo] == ')') {
              var simboloTope = pilaOperadores.extraer();
              while (simboloTope != '(') {
                listaSufija.push(simboloTope);
                simboloTope = pilaOperadores.extraer();
              }
            } else {
              while (!pilaOperadores.estaVacia() && precedencia[pilaOperadores.inspeccionar()] >=
                precedencia[listaSimbolos[simbolo]]) {
                listaSufija.push(pilaOperadores.extraer())
              }
              pilaOperadores.incluir(listaSimbolos[simbolo]);
            }
          }
          while (!pilaOperadores.estaVacia()) {
            listaSufija.push(pilaOperadores.extraer());
          }
          return listaSufija.join(" ");
        }

        function evaluacionNotacionSufija(expresionSufija) {
          var pilaOperandos = new Pila()
          var listaSimbolos = expresionSufija.split(" ");
          var operando2;
          var operando1;
          var resultado;
          for (var simbolo in listaSimbolos) {
            if ("+-*/()".indexOf(listaSimbolos[simbolo]) == -1)
              pilaOperandos.incluir(parseFloat(listaSimbolos[simbolo]))
            else {
              operando2 = pilaOperandos.extraer()
              operando1 = pilaOperandos.extraer()
              resultado = hacerAritmetica(listaSimbolos[simbolo], operando1, operando2)
              pilaOperandos.incluir(resultado)
            }
          }
          return pilaOperandos.extraer()
        }

        function hacerAritmetica(operador, operandoIzquierda, operandoDerecha) {
          if (operador == "*")
            return operandoIzquierda * operandoDerecha
          else if (operador == "/")
            return operandoIzquierda / operandoDerecha
          else if (operador == "+")
            return operandoIzquierda + operandoDerecha
          else
            return operandoIzquierda - operandoDerecha
        }

        function evaluar(expresion) {
          var separado = expresion.split(",")
          if (separado.length > 1) {
            var sufija = infija_a_sufija(separado[0].trim());
            resultado = evaluacionNotacionSufija(sufija) + " , ";
            for (var i = 1; i < separado.length; i++) {
              sufija = infija_a_sufija(separado[i].trim());
              if (i < separado.length - 1)
                resultado += evaluacionNotacionSufija(sufija) + " , ";
              else
                resultado += evaluacionNotacionSufija(sufija);
            }

          } else {
            var sufija = infija_a_sufija(expresion);
            var resultado = evaluacionNotacionSufija(sufija.trim());
          }
          return resultado;
        }

        function analizar(expresion) {
          expresion.trim();
          var estracto = "";
          var abiertos = 0;
          var cerrados = 0;
          var interior = "";
          var reemplazar = "";
          var activado = false;
          var analizandoInterior = false;
          var expresionNueva = expresion;
          for (var i = 0; i < expresion.length; i++) {
            if (expresion[i].charCodeAt() >= 97 && expresion[i].charCodeAt() <= 122)
              activado = true;
            if (activado && expresion[i] != "(" && analizandoInterior == false)
              estracto += expresion[i]
            if (activado && expresion[i] == "(" && analizandoInterior == false) {
              analizandoInterior = true;
              reemplazar = estracto;
            }
            if (analizandoInterior) {
              reemplazar += expresion[i];
              if (expresion[i] == "(")
                abiertos++;
              if (expresion[i] == ")")
                cerrados++;
              if (abiertos == cerrados) {
                abiertos = 0;
                cerrados = 0;
                activado = false;
                analizandoInterior = false;
                interior = interior.substr(2, interior.length - 3);
                interior = analizar(interior.trim());
                var interiorEvaluado = evaluar(interior.trim());
                if (!isNaN(interiorEvaluado))
                  expresionNueva = expresionNueva.replace(interior, interiorEvaluado);
                if (!isNaN(interiorEvaluado))
                  reemplazar = reemplazar.replace(interior, interiorEvaluado);
                var resultado = operacion(estracto.trim(), interiorEvaluado);
                if (!isNaN(resultado))
                  expresionNueva = expresionNueva.replace(reemplazar, resultado);
                interior = "";
                estracto = "";
                reemplazar = "";
              } else
                interior += expresion[i];
            }
          }
          return expresionNueva;
        }
        //console.log("res antes "+res)
        if (id != -1) {
          var comodinesPregunta = [];
          for (var j = 0; j < this.comodines.length; j++)
            if (id == this.comodines[j].id_pregunta && id_opcion_actual === this.comodines[j].id_opcion)
              comodinesPregunta.push(this.comodines[j]);
          for (var k = 0; k < comodinesPregunta.length; k++)
            while (res.indexOf(comodinesPregunta[k].comodin) != -1)
              res = res.replace(comodinesPregunta[k].comodin, comodinesPregunta[k].valor);
          //console.log("res despues "+res)
        }
        var resultado = analizar(res.replace(/\s+/g, ' '));
        return (evaluar(resultado));
      },
      botonesCalculadora: function(boton) {
        var campo_calculadora = document.getElementById("campo_calculadora");

        function esNumero(entrada) {
          var salida = false;
          if (entrada == "1" || entrada == "2" || entrada == "3" || entrada == "4" || entrada == "5" ||
            entrada == "6" || entrada == "7" || entrada == "8" || entrada == "9" || entrada == "0" ||
            entrada == ".") {

            salida = true;
          }
          return salida;
        }

        if (esNumero(boton)) {
          //campo_calculadora.value = campo_calculadora.value + boton;
          if (campo_calculadora.value.length == 0) {
            campo_calculadora.value = boton;
          } else {
            if (esNumero(campo_calculadora.value.substr(campo_calculadora.value.length - 1,
                campo_calculadora.value.length))) {
              campo_calculadora.value = campo_calculadora.value + boton;
            } else {
              campo_calculadora.value = campo_calculadora.value + " " + boton;
            }
          }
        } else {
          //campo_calculadora.value = campo_calculadora.value + " " + boton;
          if (boton == "ac") {
            campo_calculadora.value = "";
          } else if (boton != "fun" && boton != "=") {
            campo_calculadora.value = campo_calculadora.value + " " + boton;
          } else if (boton = "=") {
            campo_calculadora.value = this.generarRespuesta(-1, campo_calculadora.value, 0);
          }

        }


      }
    }
  };
</script>
<style>
  .pregresp {
    border: 2px solid #7da5e0;
    margin: 5px;
    font-family: Arial, Verdana, Helvetica, sans-serif;
    font-size: 15px;
    font-weight: bold;
  }
  
  .fixed-size-button {
  width: 100%;
  height: 100px;
}

  .pregunta {
    color: #7da5e0;
  }

  .respuestas {
    color: #000000;
  }

  .grid {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    background-color: #fff;
    padding: 10px 50px 50px 50px;
  }

  .grid h1 {
    text-align: center;
    color: #000000;
    padding: 2px 0px;
    border-radius: 50px;
  }

  #score {
    color: #5A6772;
    text-align: center;
    font-size: 30px;
  }

  .buttons {
    margin-top: 30px;
  }

  #btn0,
  #btn1,
  #btn2,
  #btn3,
  #next {
    width: 250px;
    font-size: 20px;
    margin: 10px 40px 10px 0px;
    padding: 10px 10px;
  }

  .container {
    display: block;
    position: relative;
    padding-left: 35px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  .container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
  }

  .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
  }

  .container:hover input~.checkmark {
    background-color: #ccc;
  }

  .container input:checked~.checkmark {
    background-color: #2196F3;
  }

  .checkmark:after {
    content: "";
    position: absolute;
    display: none;
  }

  .container input:checked~.checkmark:after {
    display: block;
  }

  .container .checkmark:after {
    left: 9px;
    top: 5px;
    width: 5px;
    height: 10px;
    border: solid white;
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
  }

  #carouselExampleIndicators {
    margin-left: 200px;
    margin-right: 200px;
  }

  .item img {
    margin-left: auto;
    margin-right: auto;
  }

  .selected img {
    opacity: 0.5;
  }

  .carousel-caption {
    position: relative;
    left: auto;
    right: auto;
  }

  .carousel-control.left,
  .carousel-control.right {
    background: none;
    border: none;
  }

  .carousel-control.left {
    margin-left: -300px;
  }

  .carousel-control.right {
    margin-right: -300px;
  }

  .carousel-control {
    width: 0%;
  }
  
  .fixed-size-button {
  font-size: 14px; /* Reduce el tamaño de la fuente */
 height: 40px; /* Reduce la altura para hacer los botones delgados */
  width: 100%;   /* Ocupa todo el ancho del contenedor */
  max-width: 150px; /* Limita el ancho máximo del botón */
  white-space: nowrap; /* Evita que el texto se divida en varias líneas */
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
   
}
</style>