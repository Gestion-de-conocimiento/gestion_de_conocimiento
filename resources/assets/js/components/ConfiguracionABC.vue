<template>
  <div class="abc-container">
    <!-- Panel izquierdo: Configuración -->
    <div class="config-panel">
      <h2>Configuración de Actualización</h2>

      <!-- Selección del modo de actualización -->
      <div class="form-group">
        <label>Modo de actualización:</label>
        <select v-model="modo">
          <option value="cantidad">Por cantidad de pickles</option>
          <option value="tiempo">Por tiempo</option>
          <option value="ambos">Lo que ocurra primero</option>
        </select>
      </div>

      <!-- Configuración específica según modo -->
      <div class="form-group" v-if="modo !== 'tiempo'">
        <label>Cantidad mínima de pickles aptos:</label>
        <input type="number" v-model.number="cantidadMinima" min="1" />
      </div>

      <div class="form-group" v-if="modo !== 'cantidad'">
        <label>Tiempo (en días):</label>
        <input type="number" v-model.number="dias" min="1" />
      </div>

      <div class="form-group">
        <label>Peso de los datos reales (%):</label>
        <input type="number" v-model.number="peso" min="0" max="100" />
      </div>

      <div class="form-group">
        <label>Temas dominados mínimos por pickle:</label>
        <input type="number" v-model.number="temasDominados" min="1" />
      </div>

      <!-- Botón para guardar configuración -->
      <button @click="guardarConfiguracion">Guardar configuración</button>

      <!-- Progreso de actualización automática -->
      <div class="avance-container">
        <h3>Progreso hacia la actualización</h3>
        <div class="circle" :style="{ background: `conic-gradient(#007bff ${porcentaje}%, #e0e0e0 0%)` }">
          <div class="circle-inner">{{ porcentaje }}%</div>
        </div>
        <!-- Pickles aptos y total -->
        <p>{{ picklesAptos }} pickles aptos</p>
        <p>Total de pickles: {{ totalPickles }}</p>
        <!-- Cuenta regresiva basada en la configuración -->
        <p v-if="modo !== 'cantidad'">Cuenta regresiva: {{ countdown }}</p>
      </div>
    </div>

    <!-- Panel derecho: Visualización de red bayesiana -->
    <div class="red-panel">
      <h2>Red Bayesiana Actual</h2>

      <!-- Selector de red disponible -->
      <select v-if="listaRedes.length" v-model="redSeleccionada" @change="graficarRed">
        <option v-for="red in listaRedes" :key="red" :value="red">{{ red }}</option>
      </select>

      <!-- Iframe que muestra la red generada -->
      <iframe v-if="iframeUrl" :src="iframeUrl" width="100%" height="600" frameborder="0"></iframe>

      <!-- Historial de actualizaciones -->
      <div v-if="historial.length" class="historial-panel">
        <h3>Historial de actualizaciones</h3>
        <table>
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Motivo</th>
              <th>Pickles aptos</th>
              <th>Total</th>
              <th>Observaciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="registro in historial" :key="registro.id">
              <td>{{ formatearFecha(registro.fecha) }}</td>
              <td>{{ registro.motivo }}</td>
              <td>{{ registro.pickles_aptos }}</td>
              <td>{{ registro.total_pickles }}</td>
              <td>{{ registro.observaciones }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      modo: 'ambos',
      cantidadMinima: 50,
      dias: 14,
      peso: 20,
      temasDominados: 30,
      picklesAptos: 0,
      totalPickles: 0,
      countdown: '--:--:--:--',
      nextUpdateTimestamp: null,
      iframeUrl: '',
      listaRedes: [],
      redSeleccionada: null,
      historial: [],
      estadoTimer: null,
      countdownTimer: null,
    };
  },
  computed: {
    porcentaje() {
      if (!this.cantidadMinima) return 0;
      return Math.min(Math.round((this.picklesAptos / this.cantidadMinima) * 100), 100);
    },
  },
  methods: {
    async guardarConfiguracion() {
      try {
        const payload = {
          modo: this.modo,
          minimo_pickles: this.cantidadMinima,
          tiempo_en_dias: this.dias,
          peso_real: this.peso / 100,
          minimo_temas_dominados: this.temasDominados,
        };
        await axios.post('/api/configuracion-actualizacion', payload);
        alert('Configuración guardada exitosamente');
        this.setNextUpdate();
        this.cargarEstado();
      } catch (err) {
        alert('Error al guardar la configuración');
        console.error(err);
      }
    },
    async cargarConfiguracion() {
      try {
        const res = await axios.get('/api/configuracion-actualizacion');
        const config = res.data;
        this.modo = config.modo;
        this.cantidadMinima = config.minimo_pickles;
        this.temasDominados = config.minimo_temas_dominados;
        this.dias = config.tiempo_en_dias;
        this.peso = config.peso_real * 100;
        this.setNextUpdate();
      } catch (err) {
        console.error('Error al cargar configuración:', err);
      }
    },
    setNextUpdate() {
      if (this.modo !== 'cantidad') {
        this.nextUpdateTimestamp = Date.now() + this.dias * 24 * 3600 * 1000;
      } else {
        this.nextUpdateTimestamp = null;
        this.countdown = '--:--:--:--';
      }
    },
    async cargarEstado() {
      try {
        const res = await axios.get('/api/estado-actualizacion');
        this.picklesAptos = res.data.picklesAptos;
        this.totalPickles = res.data.totalPickles;
      } catch (err) {
        console.error('Error al cargar estado:', err);
      }
    },
    updateCountdown() {
      if (!this.nextUpdateTimestamp) return;
      const diff = this.nextUpdateTimestamp - Date.now();
      if (diff <= 0) {
        this.countdown = '00:00:00:00';
        return;
      }
      const days = Math.floor(diff / (24 * 3600 * 1000));
      const hours = Math.floor((diff % (24 * 3600 * 1000)) / (3600 * 1000));
      const mins = Math.floor((diff % (3600 * 1000)) / (60 * 1000));
      const secs = Math.floor((diff % (60 * 1000)) / 1000);
      this.countdown =
        String(days).padStart(2, '0') + ':' +
        String(hours).padStart(2, '0') + ':' +
        String(mins).padStart(2, '0') + ':' +
        String(secs).padStart(2, '0');
    },
    async cargarRedes() {
      try {
        const res = await axios.get('/api/redes-bayesianas');
        this.listaRedes = res.data.sort((a, b) => {
          const na = parseInt(a.replace(/\D/g, ''), 10);
          const nb = parseInt(b.replace(/\D/g, ''), 10);
          return na - nb;
        });
        if (this.listaRedes.length) {
          this.redSeleccionada = this.listaRedes[this.listaRedes.length - 1];
          this.graficarRed();
        }
      } catch (err) {
        console.error('Error al cargar redes:', err);
      }
    },
    async graficarRed() {
      if (!this.redSeleccionada) return;
      try {
        const res = await axios.post('/api/graficar-bifxml', { red: this.redSeleccionada });
        if (res.data.graphUrl) {
          this.iframeUrl = `${res.data.graphUrl}?t=${Date.now()}`;
        }
      } catch (err) {
        console.error('Error al graficar red:', err);
      }
    },
    async cargarHistorial() {
      try {
        const res = await axios.get('/api/historial-actualizaciones');
        this.historial = res.data;
      } catch (err) {
        console.error('Error al cargar historial:', err);
      }
    },
    formatearFecha(fechaIso) {
      return new Date(fechaIso).toLocaleString();
    }
  },
  mounted() {
    this.cargarConfiguracion();
    this.cargarEstado();
    this.cargarRedes();
    this.cargarHistorial();
    this.estadoTimer = setInterval(this.cargarEstado, 5000);
    this.countdownTimer = setInterval(this.updateCountdown, 1000);
  },
  beforeDestroy() {
    clearInterval(this.estadoTimer);
    clearInterval(this.countdownTimer);
  }
};
</script>

<style scoped>
.abc-container { display: flex; flex-direction: row; gap: 20px; padding: 20px; margin-left: 270px; }
.config-panel, .red-panel { background: #fff; padding: 20px; border-radius: 16px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
.config-panel { flex: 1; max-width: 400px; }
.red-panel { flex: 2; }
.form-group { margin-bottom: 16px; }
input, select { width:100%; padding:8px; border-radius:8px; border:1px solid #ccc; }
button { padding:10px 20px; border:none; background:#007bff; color:#fff; border-radius:8px; cursor:pointer; margin-top:10px; }
button:hover { background:#0056b3; }
.avance-container { margin-top:30px; text-align:center; }
.circle { width:120px; height:120px; border-radius:50%; margin:0 auto 10px; display:flex; align-items:center; justify-content:center; }
.circle-inner { font-weight:bold; font-size:20px; }
.historial-panel { margin-top:40px; }
table { width:100%; border-collapse:collapse; margin-top:10px; }
th, td { border:1px solid #ccc; padding:8px; font-size:14px; text-align:center; }
th { background:#f2f2f2; }
</style>
