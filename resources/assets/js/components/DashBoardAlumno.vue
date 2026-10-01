<template>
  <div :style="{ marginLeft: sidebarWidth + 'px' }" class="p-6 min-h-screen transition-all duration-300">
    <h1 class="text-3xl font-bold text-gray-800 mb-6 flex items-center gap-2">
      📊 Desempeño Académico
    </h1>

    <div v-if="limpiando" class="text-gray-500 mb-6">🔄 Limpiando gráficas anteriores...</div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Distribución -->
      <div class="bg-white p-4 rounded-2xl shadow-md">
        <h2 class="text-lg font-semibold text-blue-700 mb-2">Distribución actual</h2>
        <div v-if="loadingDistribucion" class="text-gray-600">🔄 Cargando distribución...</div>
        <div v-if="errorDistribucion" class="text-red-600 font-semibold">❌ Error al cargar distribución</div>
        <iframe
          v-if="graficaDistribucion"
          :src="graficaDistribucion"
          width="100%"
          height="300px"
          class="rounded border"
        ></iframe>
      </div>

      <!-- Histórico -->
      <div class="bg-white p-4 rounded-2xl shadow-md">
        <h2 class="text-lg font-semibold text-green-700 mb-2">Histórico de evolución</h2>
        <div v-if="loadingHistorico" class="text-gray-600">🔄 Cargando histórico...</div>
        <div v-if="errorHistorico" class="text-red-600 font-semibold">❌ Error al cargar histórico</div>
        <iframe
          v-if="graficaHistorico"
          :src="graficaHistorico"
          width="100%"
          height="300px"
          class="rounded border"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      graficaDistribucion: "",
      graficaHistorico: "",
      loadingDistribucion: false,
      loadingHistorico: false,
      errorDistribucion: false,
      errorHistorico: false,
      limpiando: false,
      sidebarWidth: 256, // ancho inicial
    };
  },
  async mounted() {
    this.detectarSidebar();
    await this.limpiarGraficasAntiguas();
    this.cargarGraficaDistribucion(); // ✅ Se cargan al montar
    this.cargarGraficaHistorico();
  },
  methods: {
    async cargarGraficaDistribucion() {
      this.loadingDistribucion = true;
      this.errorDistribucion = false;
      try {
        const response = await fetch("/generar-grafica", { method: "POST" });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Error");
        this.graficaDistribucion = data.graphUrl;
      } catch (err) {
        console.error("❌ Error en distribución:", err);
        this.errorDistribucion = true;
      } finally {
        this.loadingDistribucion = false;
      }
    },
    async cargarGraficaHistorico() {
      this.loadingHistorico = true;
      this.errorHistorico = false;
      try {
        const response = await fetch("/generar-historico", { method: "POST" });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Error");
        this.graficaHistorico = data.graphUrl;
        console.log("✅ Histórico:", data.graphUrl);
      } catch (err) {
        console.error("❌ Error en histórico:", err);
        this.errorHistorico = true;
      } finally {
        this.loadingHistorico = false;
      }
    },
    async limpiarGraficasAntiguas() {
      this.limpiando = true;
      try {
        const response = await fetch("/limpiar-graficas", { method: "POST" });
        const data = await response.json();
        console.log("🧹 Limpieza:", data.message);
      } catch (error) {
        console.warn("⚠️ Limpieza fallida:", error);
      } finally {
        this.limpiando = false;
      }
    },
    detectarSidebar() {
      const sidebar = document.querySelector("#sidebar");
      if (!sidebar) return;

      const observer = new ResizeObserver(() => {
        this.sidebarWidth = sidebar.offsetWidth;
      });

      observer.observe(sidebar);
    },
  },
};
</script>
