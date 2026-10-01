<template>
  <div class="main-container">
    <div class="title-container">
      <p>Actualizar Base de Conocimiento</p>
    </div>

    <div class="element-container">
      <div class="element-subtitle">
        <p>Redes Bayesianas</p>
        <select v-model="selectedRedGraficar" @change="generarGrafica">
          <option v-for="red in listaRedes" :key="red" :value="red">
            {{ red }}
          </option>
        </select>
      </div>

      <div class="bayesianas-container">
        <div v-if="cargando" class="spinner-container">
          <div class="spinner"></div>
          <p>Cargando gráfica...</p>
        </div>
        <iframe
          v-if="iframeSrc"
          :src="iframeSrc"
          width="100%"
          height="100%"
          @load="iframeCargado"
        ></iframe>
      </div>

      <div class="element-subtitle" style="padding: 0px; padding-left: 20px;">
        <p>Actualizar Base de Conocimiento</p>
      </div>

      <div class="input-container">
        <label for="dato">Ingrese el peso (0 a 100):</label>
        <div class="input-label-select">
          <input
            id="dato"
            type="number"
            min="0"
            max="100"
            v-model.number="peso"
            placeholder="Eg. 0, 50, 100"
          />
          <select v-model="selectedRedActualizar">
            <option v-for="red in listaRedes" :key="red" :value="red">
              {{ red }}
            </option>
          </select>
        </div>
        <button @click="actualizarBC">Actualizar</button>
        <label v-if="errorMsg" id="errorMsg" style="color:red; margin-top:10px;">{{ errorMsg }}</label>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      peso: null,
      selectedRedGraficar: null,
      selectedRedActualizar: null,
      listaRedes: [],
      iframeSrc: '',
      cargando: false,
      errorMsg: ''  // <-- AÑADIDO
    };
  },
  mounted() {
    this.cargarRedes();
  },
  methods: {
    async cargarRedes() {
      try {
        const response = await fetch('/api/redes-bayesianas');
        this.listaRedes = await response.json();
        if (this.listaRedes.length > 0) {
          this.selectedRedGraficar = this.listaRedes[0];
          this.selectedRedActualizar = this.listaRedes[0];
          this.generarGrafica();
        }
      } catch (e) {
        console.error("Error al cargar redes", e);
      }
    },
 async generarGrafica() {
  if (!this.selectedRedGraficar) return;
  this.cargando = true;
  this.iframeSrc = '';
  try {
    const res = await fetch('/api/graficar-bifxml', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ red: this.selectedRedGraficar })
    });
    const data = await res.json();
    if (res.ok) {
      // Agregar timestamp para evitar cache
      this.iframeSrc = `${data.graphUrl}?t=${Date.now()}`;
    } else {
      alert(data.error || "Error al generar la gráfica");
    }
  } catch (e) {
    console.error(e);
    alert("Error en la petición de gráfica");
  } finally {
    this.cargando = false;
  }
},

    iframeCargado() {  // <-- AÑADIDO
      this.cargando = false;
    },
    async actualizarBC() {
      this.errorMsg = '';

      if (this.peso === null || this.peso < 0 || this.peso > 100) {
        this.errorMsg = "El peso debe ser un valor entre 0 y 100";
        return;
      }

      const pesoNormalizado = this.peso / 100;
      try {
        const res = await fetch('/api/actualizar-bc', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            red: this.selectedRedActualizar,
            peso: pesoNormalizado
          })
        });
        const data = await res.json();
        if (res.ok) {
          alert(data.mensaje);
          this.cargarRedes();
        } else {
          alert(data.error || "Error en la actualización");
        }
      } catch (e) {
        console.error(e);
        alert("Error en la petición de actualización");
      }
    }
  }
};
</script>



<style>
.spinner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.spinner {
  border: 8px solid #f3f3f3;
  border-top: 8px solid #007BFF;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin-bottom: 10px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes wrongAnimation {
  0% { transform: translateX(3px); }
  20% { transform: translateX(-3px); }
  40% { transform: translateX(3px); }
  60% { transform: translateX(-3px); }
  80% { transform: translateX(3px); }
  100% { transform: translateX(-3px); }
}

.loader {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 1.2em;
  color: #555;
}


body {
  background-color: #F4F6F9;
}
.main-container {
  margin-top: 10px;
  width: 82%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-flow: column wrap;
  margin-left: 270px;
  height: 100%;
}
.title-container {
  width: 100%;
  height: 3rem;
  font-size: 30px;
}
.element-container {
  width: 100%;
  margin-top: 20px;
  display: flex;
  justify-content: flex-start;
  margin-bottom: 20px;
  align-items: flex-start;
  flex-flow: column wrap;
  height: 100%;
  background-color: white;
  border-radius: 5px;
  box-shadow: 2px 2px 10px gray;
}
label {
  margin-right: 10px;
}
select {
  padding: 5px;
  background: white;
  border: 1px solid gray;
  border-radius: 0px;
  cursor: pointer;
  margin-bottom: 20px;
  margin-left: 20px;
}
.input-label-select {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  flex-flow: row wrap;
}
input {
  width: 10rem;
  margin-bottom: 20px;
}
button {
  padding: 10px;
  background-color: #007BFF;
  border-radius: 5px;
  outline: none;
  border: none;
  color: white;
  transition: all 0.3s;
  text-transform: capitalize;
  cursor: pointer;
}
button:hover {
  opacity: 0.7;
}
.element-subtitle {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-flow: row wrap;
  height: fit-content;
  padding: 20px;
  padding-bottom: 0px;
  font-size: 18px;
  font-weight: 600;
  border-bottom: 2px solid #DFDFDF;
}
.bayesianas-container {
  width: 100%;
  height: 20rem;
  margin-top: 20px;
  margin-bottom: 20px;
  border-bottom: 2px solid #DFDFDF;
}
.input-container {
  width: 100%;
  height: 100%;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-left: 20px;
  flex-flow: column wrap;
  margin-bottom: 20px;
}
@keyframes wrongAnimation {
  0% { transform: translateX(3px); }
  20% { transform: translateX(-3px); }
  40% { transform: translateX(3px); }
  60% { transform: translateX(-3px); }
  80% { transform: translateX(3px); }
  100% { transform: translateX(-3px); }
}
@keyframes reloadAnimation {
  0% { transform: scale(1); }
  100% { transform: scale(0.5); }
}
</style>
