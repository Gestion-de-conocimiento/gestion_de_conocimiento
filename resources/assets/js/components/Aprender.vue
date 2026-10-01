<template>
  <div class="content-wrapper">
    <div class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="page-title m-0">Enseñanza</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <span style="color: #bdb9bd">
                <i class="fas fa-home"></i> <i class="fas fa-angle-right"></i>
              </span>
              <span style="color: #bdb9bd">
                Enseñanza<i class="fas fa-angle-right"></i>
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
              </div>
              <div class="card-body">
                <div class="row">
                  <div class="col-12">
                    <div class="row">
                      <button type="button" @click="Pickle" class="btn btn-primary float-right btn-lg mt-4 mr-2" style="width: 200px; height: 60px;">
                        <i class="fas fa-rocket"></i>
                        Iniciar
                      </button>
                    </div>
                    <div class="row mt-4">
                      <div v-for="(nombre, rama, index) in botonesRamas" :key="rama" class="col-md-4 mb-3">
                        <button
                          class="btn btn-lg btn-block"
                          @click="handleRamaClick(rama)"
                          :style="{ backgroundColor: gradosPorRama[rama] ? '#6c757d' : '#007bff', color: 'white' }"
                          :class="{ 'animate-button': firstBlueButtonIndex === index }"
                          :disabled="!gradosPorRama[rama] && firstBlueButtonIndex !== index"
                        >
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      botonesRamas: {},
      gradosPorRama: {},
      temasPorRama: {},
      firstBlueButtonIndex: null,
      areButtonsDisabled: false,
    };
  },
  async created() {
    await this.startHighlighting();
  },
  methods: {
    async Pickle() {
      this.firstBlueButtonIndex = null;
      this.areButtonsDisabled = false; // Resetea el estado de los botones
      try {
        const result = await axios.get("/obtenerMatricula/" + matricula);
        console.log("La matrícual es:",result);
        this.botonesRamas = this.mapearRamas(result.data.temas_por_rama);
        this.gradosPorRama = this.mapearGrados(result.data.temas_por_rama);
        this.temasPorRama = result.data.temas_por_rama;

        // Determinar el primer botón no dominado
        this.firstBlueButtonIndex = Object.keys(this.botonesRamas).findIndex(rama => !this.gradosPorRama[rama]);
      } catch (error) {
        console.error("Ocurrió un error en la solicitud:", error);
      }
    },
    mapearRamas(temasPorRama) {
      const nombresRamas = {
        2: '1. Aritmética',
        3: '2. Álgebra',
        4: '3. Geometría',
        5: '4. Álgebra lineal',
        6: '5. Trigonometría',
        7: '6. Funciones matemáticas',
        8: '7. Cálculo diferencial',
        9: '8. Cálculo integral',
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
    handleRamaClick(rama) {
      const nombreRama = this.botonesRamas[rama];
      const temasString = JSON.stringify(this.temasPorRama[rama]);

      // Verifica si el botón es gris (rama dominada)
      if (this.gradosPorRama[rama]) {
        // Redirige a la vista especial
        this.$router.push({ 
          name: 'vista-especial', 
          params: { rama }, 
          query: { nombre: nombreRama, temas: temasString } 
        });
      } else {
        // Redirige a la vista general
        this.$router.push({ 
          name: 'vista-general', 
          params: { rama }, 
          query: { nombre: nombreRama, temas: temasString } 
        });
      }
    },
    startHighlighting() {
      this.isHighlighting = true;
      setTimeout(() => {
        this.isHighlighting = false;
        this.startHighlighting();
      }, 2000);
    }
  }
};
</script>

<style>
.svg-wrapper {
  margin: 10px;
}

.pulse {
  --color: #007bff; /* Color del botón */
  position: relative;
  display: inline-block;
  font-size: 16px;
  color: white;
  background-color: var(--color);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.pulse:hover,
.pulse:focus {
  animation: pulse 1s infinite; /* Animación constante */
  box-shadow: 0 0 0 2em rgba(255, 165, 0, 0.5); /* Sombra naranja */
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 165, 0, 0.7); /* Sombra inicial */
  }
  100% {
    box-shadow: 0 0 0 20px rgba(255, 165, 0, 0); /* Sombra expandida y desvanecida */
  }
}

.animate-button {
  animation: pulse 1s infinite; /* Animación pulsante */
}
</style>


