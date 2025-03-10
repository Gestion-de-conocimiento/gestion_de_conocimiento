<template>

  <div id="container">
    <div id="div1">
      
          <div>
    </div>
       <!--div id="input2"></div> entrada de la expresión -->
       <div id="mathquill-editor"></div>
      <div ref="mathField" id="input2" @input="handleInput"></div>
       
      <div v-for="buttonClass in buttonClasses" :key="buttonClass" :class="['menu-buttons', { active: buttonClass === activeButton }]">
     
      </div>    
      </div>
  </div>
</template>

<script>

  
  export default {
  name: 'ToolBarPregunta',
  props: ['dato','banderaParaEdicion'], // variable recibida desde el padre
 
  created() {
  
  },
  data() {
    return {

      selectedOption: 'basic', // opción inicial del menú desplegable
      activeButton: 'basic-buttons', // valor inicial para activeButton
      buttonClasses: ['basic-buttons', 'functions-buttons','logic-buttons','symbols-buttons'],// clases adicionales de los botones 
      inputValue: '', // nueva variable para manejar el valor del input
      showEtiqueta: false,
      mensaje: "Hola desde el hijo",
      banderaLocal: true,
      datorecibido:'',
    };
  },
  mounted(){

      const MQ = MathQuill.getInterface(2);
      this.mathField = MQ.MathField(this.$refs.mathField);
    
      this.handleInput();
    
    // Obtener la referencia al campo de mathquill
    const mathquillInput = this.$refs.mathField;

    // Agregar un evento de teclado al campo de matquill
    mathquillInput.addEventListener('keydown', (event) => {
      // Obtener el código de la tecla presionada
      const keyCode = event.keyCode || event.which;
      console.log("keycode:"+keyCode);
            // Permitir solo teclas de letras y números, el enter
      if (!((keyCode >= 48 && keyCode <= 57) || (keyCode >= 65 && keyCode<=90) || (keyCode >= 96 && keyCode<=105) || keyCode===13 || keyCode===110 || keyCode===190 || ( keyCode === 17 && keyCode === 18 && keyCode===222 && keyCode===50))) { 
            event.preventDefault(); // Evitar que la tecla se ingrese
            console.log("tecla bloqueada");
      }
    });
    this.datorecibido = this.dato;
    this.mathField.write(this.dato);
    
  },
  watch: {
      //console.log("dato anteriorrrr "+ this.oldVal)
  },
  methods: {
    
    
    TraducirLatex(){
     
     this.mathField.latex(''); // Limpia el contenido del campo MathQuill
      
    },
    handleInput(){
      const mathquillText = this.mathField.latex();
      console.log(mathquillText);
      this.$emit('mathquill-updated', mathquillText);
      
    },
     editarCampoMathquill() {
    // Utiliza un temporizador para escribir el valor en MathQuill después de un breve retraso
    setTimeout(() => {
      this.mathField.write(this.dato);
    }, 0);
  }, 
    limpiarCampoMathquill(){
      
       this.mathField.latex(''); // Limpia el contenido del campo MathQuill
      
    },
  },
};
</script>


<style>
    body {
      font-family: Arial, sans-serif;
    }
    #container {
      width: 600px;
      height: 300px;
      overflow: hidden;

    }
    #input2 {
      width: 400px;
      height: 90px;
      margin: 20px;
      padding: 10px;
      font-size: 24px;
      border: 1px solid #000000da;
    }

    .menu {
      margin-bottom: 10px;
    }

    .menu select {
      font-size: 18px;
      padding: 5px;
    }

    .menu-buttons {
      display: none;
    }

    .menu-buttons.active {
      display: flex;
      flex-wrap: wrap;
    }

    menu-buttons .button-image {
      width: 50px;
      height: 50px;
      padding: 5px;
      background-color: #f1f1f1;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
      transition: background-color 0.3s;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .menu-buttons .button-image img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .menu-buttons button:hover {
      background-color: #e0e0e0;
    }

    .tooltip {
      position: relative;
      display: inline-block;
      cursor: pointer;
    }

    .tooltip .tooltiptext {
      visibility: hidden;
      width: 120px;
      background-color: #1485c9;
      color: #fff;
      text-align: center;
      border-radius: 6px;
      padding: 5px;
      position: absolute;
      z-index: 1;
      bottom: 125%;
      left: 50%;
      margin-left: -60px;
      opacity: 0;
      transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }

    #translate {
      margin-top: 10px;
      padding: 10px;
      font-size: 18px;
      background-color: #1485c9;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
      transition: background-color 0.3s;
    }

    #translate:hover {
      background-color: #1173a6;
    }

    .texto-emergente {
      display: none;
      position: absolute;
      background-color: rgba(71, 180, 215, 0.56);
      padding: 10px;
      border-radius: 5px;
      font-size: 12px;
    }

    .menu-buttons button img {
      max-width: 140%;
      max-height: 100%;
    }
  .menu-buttons.active {
  display: grid;
  grid-template-columns: repeat(8, 40px); 
  gap: 10px; 
  }

.menu-buttons button {
  width: 40px;
  height: 40px;
  font-size: 16px; 
}
.tooltip {
  position: relative;
}

</style>
