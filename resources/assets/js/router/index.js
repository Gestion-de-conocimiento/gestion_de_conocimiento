// resources/assets/js/router/index.js
import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Profesores from '@/components/Profesores'
import Expertos from '@/components/Expertos'
import Alumnos from '@/components/Alumnos'
import Administrador from '@/components/Administrador'
import temas from '@/components/temas'
import PreguntasAbiertas from '@/components/PreguntasAbiertas'
import PreguntasNumericas from '@/components/PreguntasNumericas'
import PreguntasVerdaderoFalso from '@/components/PreguntasVerdaderoFalso'
import PreguntasOpcionMultiple from '@/components/PreguntasOpcionMultiple'
import Cuestionario from '@/components/Cuestionario'
import ConfiguracionCuestionario from '@/components/ConfiguracionCuestionario'
import AccesoRutas from '@/components/AccesoRutas'
import PreguntasCalculadas from '@/components/PreguntasCalculadas'
import PreguntasOpcionMultipleCalculadas from '@/components/PreguntasOpcionMultipleCalculadas'
import Perfil from '@/components/Perfil'
import NotFound from '@/components/NotFound.vue'
import Grafo from '@/components/grafo'
import Contacto from '@/components/Contacto'
import subirImagenes from '@/components/subir_Imagenes'
import GrafoAlumnos from '@/components/GrafoAlumnos'
import configuracionModulo from '@/components/configuracionModulo'
import Ejemplo from '@/components/Ejemplo'
import PreguntasExpresiones from '@/components/PreguntasExpresiones'
import Recursos from '@/components/Recursos'
import StatusGrafo from '@/components/StatusGrafo'
import ConfiguracionEvaluacion from '@/components/ConfiguracionEvaluacion'
import Aprender from '@/components/Aprender'
import VistaEspecial from '@/components/VistaEspecial.vue'; // La vista para ramas con grado 2
import VistaGeneral from '@/components/VistaGeneral.vue'; // La vista para ramas con otros grados
import VistaRama from '@/components/VistaRama.vue'
import Evaluacion from '@/components/Evaluacion'
import DashboardAlumno from '@/components/DashBoardAlumno'
Vue.use(Router)

export default new Router({
    mode: 'history',
   routes: [
	   
    {
        path:'/tablero',
        name:'Index',
        component:Index
    },
     
        
     
	{
        path:'/accesos/configuracion',
        name:'AccesoRutas',
        component: AccesoRutas
    },
    {
        path: '/usuariosAdministrador',
        name: 'Administrador',
        component: Administrador
    },
    {
        path: '/usuariosAlumno',
        name: 'Alumno',
        component: Alumnos
    },
    {
        path: '/usuariosExperto',
        name: 'Expertos',
        component: Expertos
    },
     {
        path: '/usuariosProfesor',
        name: 'Profesores',
        component: Profesores
    },
    {
	      path:'/configurarCuestionario',
	      name: 'ConfiguracionCuestionario',
	      component: ConfiguracionCuestionario
    },
     {
	      path:'/dashboardAlumno',
	      name: 'DashboardAlumno',
	      component: DashboardAlumno
    },
    {
       path:'/cuestionario',
       name: 'cuestionario',
       component: Cuestionario
    },
    {
        path: '/preguntasAbiertas',
        name: 'PreguntasAbiertas',
        component: PreguntasAbiertas
    },
    {
        path: '/preguntasNumericas',
        name: 'PreguntasNumericas',
        component: PreguntasNumericas
    },
	  {
        path: '/preguntasVerdaderoFalso',
        name: 'PregunasVerdaderoFalso',
        component: PreguntasVerdaderoFalso
    },
    {
        path: '/preguntasOpcionMultiple',
        name: 'PreguntasOpcionMultiple',
        component: PreguntasOpcionMultiple
    }, 
	{
		path: '/preguntasCalculadas',
        name: 'PreguntasCalculadas',
        component: PreguntasCalculadas
	},
    {
		path: '/PreguntasOpcionMultipleCalculadas',
        name: 'PreguntasOpcionMultipleCalculadas',
        component: PreguntasOpcionMultipleCalculadas
	},
  {
		path: '/PreguntasExpresiones',
        name: 'PreguntasExpresione',
        component: PreguntasExpresiones
	},
    {
         path:'/temas',
         name:'temas',
         component:temas
    },
    {
         path:'/experto/temas',
         name:'temasExperto',
         component:temas
    },
  
    {
        path: '/experto/preguntasAbiertas',
        name: 'PreguntasAbiertasExperto',
        component: PreguntasAbiertas
    },
    {
        path: '/experto/preguntasNumericas',
        name: 'PreguntasNumericasExperto',
        component: PreguntasNumericas
    },
	  {
        path: '/experto/preguntasVerdaderoFalso',
        name: 'PregunasVerdaderoFalsoExperto',
        component: PreguntasVerdaderoFalso
    },
    {
        path: '/experto/preguntasOpcionMultiple',
        name: 'PreguntasOpcionMultipleExperto',
        component: PreguntasOpcionMultiple
    }, 
          
	 {
       path:'/admins/app/Preguntanodo',
       name:'Preguntanodo',
       component:temas
    },
	   {
       path:'/perfil',
       name:'Perfil',
       component:Perfil
    },
    {
        path: '/grafo',
        name: 'grafo',
        component: Grafo
    },
    {
        path: '/contacto',
        name: 'contacto',
        component: Contacto
    },
    {
        path: '/subirImagenes',
        name: 'subirImagenes',
        component: subirImagenes
    },
     {
       path:'/grafoalumnos',
       name: 'grafoAlumnos',
       component: GrafoAlumnos
     },
     {
        path: '/statusGrafo',
        name: 'statusGrafo',
        component: StatusGrafo
     },
     {
       path:'/configuracion/modulo',
       name: 'configuracionModulo',
       component: configuracionModulo
     },
     {
       path:'/ejemplo',
       name:'componenteejemplo',
       component: Ejemplo
     },
	{
        path: '*',
        name: 'NotFound',
        component: NotFound,
    },
     {
       //Ruta del archivo
        path:'/recursos',
       //Nombre del Componente
        name:'recursos',
       //El componente se encuentra como
        component:Recursos
    },
     {
        path: '/configuracion/evaluacion',
        name: 'ConfiguracionEvaluacion',
        component: ConfiguracionEvaluacion
     },
     {
       //Ruta del archivo
        path:'/aprender',
       //Nombre del Componente
        name:'aprender',
       //El componente se encuentra como
        component:Aprender
    },
      { path: '/vista-especial/:rama',
       name: 'vista-especial', 
       component: VistaEspecial 
      },
     
    { path: '/vista-general/:rama', 
     name: 'vista-general', 
     component: VistaGeneral 
    },
     {
      path: '/rama/:rama',
      name: 'VistaRama',
      component: VistaRama,
      props: true
    },     
     {
      path: '/Evaluacion',
      name: 'Evaluacion',
      component: Evaluacion,
    },
     
],linkActiveClass:"active", linkExactActiveClass: "active",
})