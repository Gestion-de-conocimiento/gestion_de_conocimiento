<template>
  <div class="container mt-4 espaciado-sidebar">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3 class="mb-0">Tus alumnos</h3>
      <button class="btn btn-outline-primary" @click="cargarAlumnos">
        <i class="fas fa-sync-alt"></i> Recargar
      </button>
    </div>

    <div v-if="cargando" class="text-center my-4">
      <i class="fas fa-spinner fa-spin fa-2x"></i>
      <p class="mt-2">Cargando alumnos...</p>
    </div>

    <div v-else>
      <div v-if="alumnosFiltrados.length === 0" class="alert alert-info">
        No hay alumnos encontrados.
      </div>

      <table v-else class="table table-bordered table-hover table-sm text-center">
        <thead class="thead-dark">
          <tr>
            <th>ID</th>
            <th>Foto</th>
            <th>Nombre completo</th>
            <th>Matrícula</th>
            <th>Periodo</th>
            <th>Estado</th>
            <th>Cambiar estado</th>
            <th>Desempeño</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="alumno in alumnosFiltrados" :key="alumno.id">
            <td>{{ alumno.id }}</td>
            <td>
              <img
                :src="'/imagenes/fotosperfil/' + alumno.foto"
                alt="Foto"
                class="rounded-circle"
                width="40"
                height="40"
              />
            </td>
            <td>{{ alumno.nombre }} {{ alumno.apellido_paterno }} {{ alumno.apellido_materno }}</td>
            <td>{{ alumno.matricula }}</td>
            <td>{{ alumno.periodo }}</td>
            <td>
              <span :class="badgeClase(alumno.estado_alumno)">
                {{ alumno.estado_alumno }}
              </span>
            </td>
            <td>
              <select class="form-control" v-model="alumno.estado_alumno" @change="cambiarEstado(alumno)">
                <option value="pendiente">Pendiente</option>
                <option value="aprendiendo">Aprendiendo</option>
                <option value="evaluando">Evaluando</option>
                <option value="terminado">Terminado</option>
              </select>
            </td>
            <td>
              <button class="btn btn-sm btn-info mb-1" @click="verDesempeno(alumno, 'distribucion')">
                DGC
              </button>
              <button class="btn btn-sm btn-secondary" @click="verDesempeno(alumno, 'historico')">
                DHA
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal animado -->
    <transition name="fade-modal">
      <div v-if="mostrarModal" class="modal-overlay" @click.self="cerrarModal">
        <div class="modal-content">
          <button class="btn btn-sm btn-danger float-right mb-2" @click="cerrarModal">Cerrar</button>
          <div v-if="cargandoGrafica" class="text-center p-4">
            <i class="fas fa-spinner fa-spin fa-3x"></i>
            <p class="mt-3">Generando gráfica...</p>
          </div>
          <div v-else>
            <iframe
              v-if="graficaUrl"
              :src="graficaUrl"
              width="100%"
              height="500px"
              frameborder="0"
            ></iframe>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      alumnos: [],
      filtro: '',
      cargando: false,
      mostrarModal: false,
      graficaUrl: '',
      cargandoGrafica: false,
    };
  },
  computed: {
    alumnosFiltrados() {
      return this.alumnos.filter(a =>
        (a.nombre + ' ' + a.apellido_paterno + ' ' + a.apellido_materno)
          .toLowerCase()
          .includes(this.filtro.toLowerCase()) ||
        a.matricula?.toString().includes(this.filtro)
      );
    }
  },
  mounted() {
    this.cargarAlumnos();
  },
  methods: {
    cargarAlumnos() {
      this.cargando = true;
      axios.get('/tus-alumnos/listar')
        .then(res => {
          this.alumnos = res.data;
        })
        .catch(err => {
          console.error('Error al cargar alumnos', err);
          Swal.fire('Error', 'No se pudo cargar la lista', 'error');
        })
        .finally(() => {
          this.cargando = false;
        });
    },
    cambiarEstado(alumno) {
      axios.post('/tus-alumnos/cambiar', {
        id_alumno: alumno.id,
        estado: alumno.estado_alumno
      })
      .then(res => {
        Swal.fire({
          toast: true,
          position: 'top-end',
          icon: 'success',
          title: res.data.message,
          showConfirmButton: false,
          timer: 2000
        });
      })
      .catch(err => {
        Swal.fire('Error', 'No se pudo cambiar el estado', 'error');
        console.error(err);
      });
    },
    verDesempeno(alumno, tipo) {
      this.mostrarModal = true;
      this.cargandoGrafica = true;
      this.graficaUrl = '';

axios.post('/graficas/desempeno', {
        matricula: alumno.matricula,
        tipo: tipo
      })
      .then(res => {
        this.graficaUrl = res.data.graphUrl;
      })
      .catch(err => {
        Swal.fire('Error', 'No se pudo generar la gráfica', 'error');
        console.error(err);
      })
      .finally(() => {
        this.cargandoGrafica = false;
      });
    },
    cerrarModal() {
      this.mostrarModal = false;
      this.graficaUrl = '';
    },
    badgeClase(estado) {
      switch (estado) {
        case 'pendiente': return 'badge badge-danger';
        case 'aprendiendo': return 'badge badge-warning';
        case 'evaluando': return 'badge badge-primary';
        case 'terminado': return 'badge badge-success';
        default: return 'badge badge-secondary';
      }
    }
  }
};
</script>

<style scoped>
.espaciado-sidebar {
  margin-left: 250px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 90%;
  max-width: 1000px;
  max-height: 90%;
  overflow-y: auto;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* Transición suave para el modal */
.fade-modal-enter-active,
.fade-modal-leave-active {
  transition: opacity 0.4s ease;
}
.fade-modal-enter,
.fade-modal-leave-to {
  opacity: 0;
}
</style>
