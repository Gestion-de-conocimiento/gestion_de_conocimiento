<template>
  <!--head>
    <title>MathQuill Editor</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mathquill/0.10.1/mathquill.css">
  </head-->   
    <div id="container">
      <div id="div1">
        <!-- menu desplegable para los botones  -->
        <div class="menu">
          <select id="menu-options" @change="toggleButtons" v-model="selectedOption">
            <option value="basic">Matemáticas Básicas</option>
            <option value="logic">Cálculo y Sumas</option>
            <option value="functions">Trigonometria</option>
            <option value="symbols">Símbolos</option>
          </select>
        </div>
            <div>
        <!--input
          v-model="inputValue"
          v-mathquill
          type="text"
          id="input2"
          class="mathquill-input"
        -->
      </div>
         <!--div id="input2"></div> <!-- entrada de la expresión -->
         <div id="mathquill-editor"></div>
        <div ref="mathField" id="input2" @input="handleInput"></div>
        <!--p>Dato recibido del padre: {{ dato }}</p>
        <!--p>Dato recibido del padre: {{ banderaParaEdicion}}</p>
        <p>Mensaje desde el hijo: {{ mensaje }}</p-->
  
        <!--h1>
          {{aboutname}}
        </h1-->
        <!--script src="https://cdnjs.cloudflare.com/ajax/libs/mathquill/0.10.1/mathquill.js"></script-->
  
        
        
      
        
        <div v-for="buttonClass in buttonClasses" :key="buttonClass" :class="['menu-buttons', { active: buttonClass === activeButton }]">
  
          <!-- Los botones para Matemáticas Básicas -->
          
            <button
              v-if="buttonClass === 'basic-buttons'"
              id="left-p"
              @click="insertLeftP"
              @mouseover="showEtiqueta = true"
              @mouseleave="showEtiqueta = false"
              title="paréntesis izquierdo"
            >(</button>
                       
          <button 
              v-if="buttonClass === 'basic-buttons'" 
              id="right-p" 
              @click="insertRightP"
              @mouseover="showEtiqueta = true"
              @mouseleave="showEtiqueta = false"
              title="paréntesis derecho"
          >)</button>
          
          <button 
              v-if="buttonClass === 'basic-buttons'" 
              id="xexp" 
              @click="insertXExp"
              @mouseover="showEtiqueta = true"
              @mouseleave="showEtiqueta = false"
              title="potencia"    >
              <img src="/imagenes/toolbar-buttons/^.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="xsub" 
               @click="insertXSub"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="subíndice"   >
               <img src="/imagenes/toolbar-buttons/_.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="sqrt" 
               @click="insertSqrt"            
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="raíz cuadrada">
               <img src="/imagenes/toolbar-buttons/sqrt.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="sqrt3" 
               @click="insertNThroot"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="n-ésima raíz">
               <img src="/imagenes/toolbar-buttons/sqrt3.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="frac" 
               @click="insertFrac"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="fracción">
               <img src="/imagenes/toolbar-buttons/frac.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="suma" 
               @click="insertSuma"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="suma"
           >+</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="resta" 
               @click="insertResta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="resta"
          >-</button>
                  
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="times" 
               @click="insertTimes"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="multiplicación"
          >×</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="div" 
               @click="insertDiv"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="división"
          >÷</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="ln" 
               @click="insertLn"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="logaritmo natural">
               <img src="/imagenes/toolbar-buttons/log.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="exp" 
               @click="insertExp"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="función exponencial">
               <img src="/imagenes/toolbar-buttons/exp.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="leq" 
               @click="insertLeq"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="menor o igual que"
          >≤</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="geq" 
               @click="insertGeq"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="mayor o igual que"
          >≥</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="equal" 
               @click="insertEqual"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="igual"
           >=</button>
          
          <button 
               v-if="buttonClass === 'basic-buttons'" 
               id="puntoYcoma" 
               @click="insertPyC"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="punto y coma"
           >;</button>
          
          <!-- Los botones para Cálculo y Sumas -->
          
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadasimple"
               @click="insertderivadasimple"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="derivada simple">
               <img src="/imagenes/toolbar-buttons/derivada.png" />
          </button>
          
           <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadaY"
               @click="insertderivadaY"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Derivada Y">
               <img src="/imagenes/toolbar-buttons/derivadaY.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadasegundoorden"
               @click="insertderivadasegundoorden"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="derivada segundo orden">
               <img src="/imagenes/toolbar-buttons/derivada2orden.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadaparcialsimple"
               @click="insertderivadaparcialsimple"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="derivada parcial simple">
               <img src="/imagenes/toolbar-buttons/parcial.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadaparcialsegundoorden"
               @click="insertderivadaparcialsegundoorden"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="derivada parcial segundo orden">
               <img src="/imagenes/toolbar-buttons/parcial2orden.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="derivadaparcialmixta"
               @click="insertderivadaparcialmixta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="derivada parcial mixta">
               <img src="/imagenes/toolbar-buttons/derivadamixta.png" />
          </button>
          
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="intindeff"
               @click="insertintindeff"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral indefinida">
               <img src="/imagenes/toolbar-buttons/indefinida.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="intintindef"
               @click="insertintintindef"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral doble indefinida">
               <img src="/imagenes/toolbar-buttons/indefinidadoble.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="intintintindef"
               @click="insertintintintindef"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral triple indefinida">
               <img src="/imagenes/toolbar-buttons/indefinidatriple.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="limite"
               @click="insertlimite"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="limite">
               <img src="/imagenes/toolbar-buttons/lim.png" />
          </button>
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="limiteizq"
               @click="insertlimiteizq"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="limite por la izquierda">
               <img src="/imagenes/toolbar-buttons/limizq.png" />
          </button>
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="limiteder"
               @click="insertlimiteder"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="limite por la derecha">
               <img src="/imagenes/toolbar-buttons/limder.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="pasounitario"
               @click="insertpasounitario"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="paso unitario">
               <img src="/imagenes/toolbar-buttons/pasounit.png" />
          </button>
           <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="int"
               @click="insertint"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral definida">
               <img src="/imagenes/toolbar-buttons/definida.png" />
          </button>
           <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="int2"
               @click="insertint2"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral definida doble">
               <img src="/imagenes/toolbar-buttons/definidadoble.png" />
          </button>
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="int3"
               @click="insertint3"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="integral definida triple">
               <img src="/imagenes/toolbar-buttons/definidatriple.png" />
          </button>
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="sigma"
               @click="insertsigma"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="suma">
               <img src="/imagenes/toolbar-buttons/sigma.png" />
          </button>
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="prod"
               @click="insertprod"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="prod">
               <img src="/imagenes/toolbar-buttons/prod.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="laplace"
               @click="insertlaplace"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="transformada de laplace">
               <img src="/imagenes/toolbar-buttons/laplace.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="laplaceinv"
               @click="insertlaplaceinv"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="transformada de laplace inversa">
               <img src="/imagenes/toolbar-buttons/laplaceinv.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="fourier"
               @click="insertfourier"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="transformada de fourier">
               <img src="/imagenes/toolbar-buttons/fourier.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'logic-buttons'" 
               id="fourierinv"
               @click="insertfourierinv"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="transformada de fourier inverisa">
               <img src="/imagenes/toolbar-buttons/fourierinv.png" />
          </button>
          
          
          
          <!-- Los botones para Trigonometría -->
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="pi"@click="insertpi"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="pi">
               <img src="/imagenes/toolbar-buttons/pi.png" />
          </button>
          
  
                       
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="circ" 
               @click="insertcirc"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="grados"
          >°</button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="sin"
               @click="insertsin"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="seno">
               <img src="/imagenes/toolbar-buttons/sin.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="cos"
               @click="insertcos"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cos">
               <img src="/imagenes/toolbar-buttons/cos.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="tan"
               @click="inserttan"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="tangente">
               <img src="/imagenes/toolbar-buttons/tan.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="sec"
                @click="insertsec"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="secante">
               <img src="/imagenes/toolbar-buttons/sec.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="csc"
               @click="insertcsc"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cosecante">
               <img src="/imagenes/toolbar-buttons/csc.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="cot"
               @click="insertcot"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cotangente">
               <img src="/imagenes/toolbar-buttons/cot.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="arcsin"
               @click="insertarcsin"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcoseno">
                  
               <img src="/imagenes/toolbar-buttons/arcsin.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="arccos"
               @click="insertarccos"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcocoseno">
          
               <img src="/imagenes/toolbar-buttons/arccos.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="arctan"
               @click="insertarctan"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcotangente">
               <img src="/imagenes/toolbar-buttons/arctan.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="sinh"
               @click="insertsinh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="seno hiperbólico">
               <img src="/imagenes/toolbar-buttons/sinh.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="cosh"
               @click="insertcosh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="coseno hiperbólico">
               <img src="/imagenes/toolbar-buttons/cosh.png" />
          </button>
          
                  <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="tanh"
               @click="inserttanh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="tangente hiperbólico">
               <img src="/imagenes/toolbar-buttons/tanh.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="sech"
               @click="insertsech"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="secante hiperbólico">
               <img src="/imagenes/toolbar-buttons/sech.png" />
          </button>
                  <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="csch"
               @click="insertcsch"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cosecante hiperbólico">
               <img src="/imagenes/toolbar-buttons/csch.png" />
          </button>
                  <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertcoth"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cotangente hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
                   <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarcsinh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcoseno hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
          
                   <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarccosh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcocoseno hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
                   <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarctanh"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcotangente hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
          
                   <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarcsech"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="arcosecante hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
          
                   <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarccsch"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="cosecante hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
          
          <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="coth"
               @click="insertarccoth"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="contangente hiperbólico">
               <img src="/imagenes/toolbar-buttons/coth.png" />
          </button>
           <!-- Los botones para Símbolos-->
         <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="theta"
               @click="inserttheta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="theta"
         >θ</button>
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="infinito"
               @click="insertinfinito"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="infinito"
         >∞</button>
                  <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="pm"
               @click="insertpm"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="pm"
         >±</button>
                   <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="pi2"
               @click="insertpi"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="pi"
         >π</button>
                          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="alpha"
               @click="insertalpha"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="alpha"
         >α</button>
                         <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="beta"
               @click="insertbeta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="beta"
         >β</button>
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="gamma"
               @click="insertgamma"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="gamma"
         >γ</button>
          
                  <button 
               v-if="buttonClass === 'functions-buttons'" 
               id="circ" 
               @click="insertcirc"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="grados"
          >°</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="deltaMay"
               @click="insertdeltaMay"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="delta Mayúscula"
         >Δ</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="delta"
               @click="insertdelta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="delta"
         >δ</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="in"
               @click="insertin"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="in"
         >∈</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="notin"
               @click="insertnotin"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="notin"
         >∉</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="lambda"
               @click="insertlambda"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="lambda"
         >λ</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="sigma"
               @click="insertsigma2"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="sigma"
         >σ</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="ipsilon"
               @click="insertipsilon"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="ipsilon"
         >ϒ</button>
  
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="thetaMay"
               @click="insertthetaMay"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="thetaMay"
         >Θ</button>
          
           <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="paraTodo"
               @click="insertParatodo"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Para todo"
         >∀</button>
          
         <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="exist"
               @click="insertExist"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Existe"
         >∃</button>
          
          
           <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="union"
               @click="insertUnion"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Unión"
         >∪</button>
          
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="interseccion"
               @click="insertIntersec"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Intersección"
         >∩</button>
          
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="zeta"
               @click="insertZeta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Zeta"
         >ζ</button>
          
          
          <button 
               v-if="buttonClass === 'symbols-buttons'" 
               id="eta"
               @click="insertEta"
               @mouseover="showEtiqueta = true"
               @mouseleave="showEtiqueta = false"
               title="Eta"
         >η</button>
          
          
         
         <button id="latex" @click="TraducirLatex">Borrar</button>
        
        
        </div>    
        </div>
    </div>
  </template>
  
  <script>
  //import MathQuill from 'mathquill';
  //import MathQuillDirective from './directives/MathQuillDirective';
  // import MathQuill from 'https://cdn.jsdelivr.net/npm/mathquill@0.10.1-a/build/mathquill.css';
  // importa el archivo CSS de MathQuill desde la carpeta local
  //import '@/components/mathquill/mathquill.css';
  //importa el archivo JS de MathQuill desde la carpeta local
  //import MathQuill from '@/components/mathquill/mathquill.js';
    
  
  //import "https://cdnjs.cloudflare.com/ajax/libs/mathquill/0.10.1/mathquill.css";
  
  //import MathQuill from "https://cdnjs.cloudflare.com/ajax/libs/mathquill/0.10.1/mathquill.js";
  
    
    export default {
    name: 'ToolBar',
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
        banderaLocal: '',
        datorecibido:'',
      };
    },
    mounted(){
  //      this.initMathQuill();
        //const MQ = MathQuill.getInterface(2); 
        //const mathField = MQ.MathField(this.$refs.mathField); 
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
      
    },
    watch: {
   /* dato(newVal,oldVal) {
        if(newVal){
        this.mathField.write(newVal); //newVal
        //console.log("dato nuevo: " + newVal + "dato anterior "+oldVal);
        this.banderaLocal=true;
        console.log("soy bandera en watch "+this.banderaLocal)
  
        }
        this.datorecibido=oldVal;
        console.log("soy datorecibido"+this.datorecibido);
        
    }*/
        //console.log("dato anteriorrrr "+ this.oldVal)
    },
  //},
  //},
    methods: {
      
      toggleButtons() {
        this.activeButton = this.selectedOption + '-buttons'; 
       },
      insertLeftP(){
        this.mathField.cmd('(');
      },
      insertRightP(){
        this.mathField.cmd(')');
      },
      insertFrac(){
        this.mathField.cmd('\\frac')
        //this.mathField.write('\\frac{}{}');
      },
      insertXExp(){
        this.mathField.cmd('^');
      },
      insertXSub(){
        this.mathField.cmd('_')
      },
      insertSqrt(){
        this.mathField.cmd('\\sqrt')
      },
      insertNThroot(){
        this.mathField.cmd('\\nthroot')
      },
      insertSuma(){
        this.mathField.cmd('+')
      },
      insertResta(){
        this.mathField.cmd('-')
      },
      insertTimes(){
        this.mathField.cmd('\\times')
      },
      insertDiv(){
        this.mathField.cmd('\\div')
      },
      insertLn(){
        this.mathField.write("\\ln\\left(\\right)")
      },
      insertExp(){
        this.mathField.write("\\exp\\left(\\right)")
      },
      insertLeq(){
        this.mathField.write("\\left(\\right)\\leq\\left(\\right)")   
      },
      insertGeq(){
        this.mathField.write("\\left(\\right)\\geq\\left(\\right)")
      },
      insertEqual(){
        //this.mathField.cmd('\\equal')
        this.mathField.write("\\left(\\right)\\=\\left(\\right)")
      },
      insertderivadaY(){
        this.mathField.write("y'")
      },
      insertderivadasimple(){
        this.mathField.write("(d/d)()")
      },
      insertderivadasegundoorden(){
        this.mathField.write("((d^2/d^2)()")
      },
      insertderivadaparcialsimple(){
        this.mathField.write("(∂/∂)()")
      },
      insertderivadaparcialsegundoorden(){
        this.mathField.write("(∂^2/∂^2)()")
      },
      insertderivadaparcialmixta(){
        this.mathField.write("(∂^2/∂∂)()")
      },
      insertintindeff(){
        this.mathField.write("\\int()")
      },
     insertintintindef(){
        this.mathField.write("\\int\\int()")
      },
      insertintintintindef(){
        this.mathField.write("\\int\\int\\int()")
      },
      insertlimite(){
        this.mathField.write("lim_{() -> ()}()")
      },
     insertlimiteizq(){
       this.mathField.write("lim_{() -> ()^-} ()")
     },
      
     insertlimiteder(){
       this.mathField.write("lim_{()->()^+}()")
     },
     insertpasounitario(){
       this.mathField.write("UnitStep[]")
     },
     insertint(){
       this.mathField.write("\\int_{ }^{ } ()")
     },
     insertint2(){
       this.mathField.write("\\int_{ }^{ }\\int_{ }^{ } () ")
     },
     insertint3(){
       this.mathField.write("\\int_{ }^{ }\\int_{ }^{ }\\int_{ }^{ } ()")
     },
      
     insertsigma(){
       this.mathField.write("\\sum_{ }^{ }")
     },
      
     insertprod(){
       this.mathField.write("\\prod")
     },
     insertlaplace(){
       this.mathField.write("LaplaceTransform[,,]")
     },
     insertlaplaceinv(){
       this.mathField.write("InverseLaplaceTransform[,,]")
     },
     insertfourier(){
       this.mathField.write("FourierTransform[,,]")
     },
     insertfourierinv(){
       this.mathField.write("InverseFourierTransform[,,]")
     },    
     insertpi(){
        this.mathField.write("\\pi")
      },
      insertcirc(){
        this.mathField.write("°")
      },
      insertsin(){
        this.mathField.write("\\sin\\left(\\right)")
      },
      insertsec(){
        this.mathField.write("\\sin\\left(\\right)")
      },
      insertcos(){
        this.mathField.write("\\cos\\left(\\right)")
      },
      inserttan(){
        this.mathField.write("\\tan\\left(\\right)")
      },
      insertcos(){
        this.mathField.write("\\cos\\left(\\right)")
      },
      insertcsc(){
        this.mathField.write("\\csc\\left(\\right)")
      },
      insertcot(){
        this.mathField.write("\\cot\\left(\\right)")
      },
      insertarcsin(){
        this.mathField.write("\\arcsin\\left(\\right)")
      },
      insertarccos(){
        this.mathField.write("\\arccos\\left(\\right)")
      },
      insertarctan(){
        this.mathField.write("\\arctan\\left(\\right)")
      },
      insertsinh(){
        this.mathField.write("\\sinh\\left(\\right)")
      },
      insertcosh(){
        this.mathField.write("\\cosh\\left(\\right)")
      },
      inserttanh(){
        this.mathField.write("\\sin\\left(\\right)")
      },
      insertsech(){
        this.mathField.write("\\sech\\left(\\right)")
      },
      insertcsch(){
        this.mathField.write("\\csch\\left(\\right)")
      },
      insertcoth(){
        this.mathField.write("\\coth\\left(\\right)")
      },
      insertarcsinh(){
        this.mathField.write("\\arcsinh\\left(\\right)")
      },
      insertarccosh(){
        this.mathField.write("\\arccosh\\left(\\right)")
      },
      insertarctanh(){
        this.mathField.write("\\arctanh\\left(\\right)")
      },
      insertarcsech(){
        this.mathField.write("\\arcsech\\left(\\right)")
      },
      insertarccsch(){
        this.mathField.write("\\arccsch\\left(\\right)")
      },
      insertarccoth(){
        this.mathField.write("\\arccoth\\left(\\right)")
      },
      inserttheta(){
        this.mathField.write("\\theta")
      },
      insertinfinito(){
        this.mathField.write("\\infty")
      },
      insertpm(){
        this.mathField.write("\\pm")
      },
      insertalpha(){
        this.mathField.write("\\alpha")
      },
      insertpm(){
        this.mathField.write("\\pm")
      },
      insertbeta(){
        this.mathField.write("\\beta")
      },
      insertgamma(){
        this.mathField.write("\\gamma")
      },
      insertdeltaMay(){
        this.mathField.write("\\Delta")
      },
      insertin(){
        this.mathField.write("\\in")
      },
      insertnotin(){
        this.mathField.write("\\notin")
      },
      insertdelta(){
        this.mathField.write("\\delta")
      },
      insertlambda(){
       this.mathField.write("\\lambda")
      },
      insertsigma2(){    
       this.mathField.write("\\sigma")
      },
      insertipsilon(){
      this.mathField.write("\\Upsilon")
      },
      insertthetaMay(){
      this.mathField.write("\\Theta")
      },
      insertParatodo(){
      this.mathField.write("\\forall")
      },
      insertExist(){
      this.mathField.write("\\exists")
      },
      insertUnion(){
      this.mathField.write("\\union")
      },
      insertIntersec(){
      this.mathField.write("\\intersection")
      },
      insertZeta(){
      this.mathField.write("\\zeta")
      },
      insertEta(){
      this.mathField.write("\\eta")
      },
      insertPyC(){
      this.mathField.write(";")
      },
      
      
      
      TraducirLatex(){
        //console.log(this.mathField.latex());
        //const latexContent = this.mathField.latex();
        //console.log('hola??');
       this.mathField.latex('');
        // Limpia el contenido del campo MathQuill
        
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
  