<template>
  <div>     
    <input ref ="wolfi" v-model="query" @keyup.enter="fetchWolframData" value="Valor por defecto"/>
    <button @click="fetchWolframData">Search</button>    <button id="colcaD" @click="colocarDato">Transferir dato</button>
 <p hidden>{{ mensaje }}</p> <p hidden>{{ unvalo }}</p>
    <div v-if="result">
      <h3>Result:</h3>
      <p>{{ result }}</p>


  </div>
    </div>
</template>

<script>
import axios from 'axios'
import ButtonComponent from './Cuestionario.vue';
var alo;
  alo = false;
  
export default {
    components: {
    ButtonComponent
  },
   updated(){
     console.log("algo hay");
             
          //btnRes.click();
  },
  data() {
    return {
      query: '',
      result: null
    }
  },
  methods: {

 colocarDato: async function() {
                 //if(this.$refs.wolfi.value == '' || this.$refs.wolfi.value == this.mensaje){
        this.$refs.wolfi.value = this.mensaje;
    console.log('Comecioo 2', this.mensaje);
   if(this.unvalo){
     this.fetchWolframData(); 
      }
   //
 },
    async fetchWolframData() {
              

      try {
          // }
      
        //this.$refs.wolfi.value = '2+2';// = this.mensaje;
    console.log("asa" + this.$refs.wolfi.value);

        const response = await axios.post('/wolfram-query', { query:  this.$refs.wolfi.value})
            console.log('Comecioo 23');
        this.result = response.data.result
        console.log('Result:', this.result)
         this.$emit('mensajeEnviado', this.result);
        console.log('Query:', this.query)
      } catch (error) {
        console.error('Error retrieving data:', error)
        this.result = 'Error retrieving data'
      }
    },
  },
    props: {
    name: {
      type: String,
      default: ''
    },
    mensaje: {
      type: String,
      default: ''
    },unvalo: {
      type: Boolean,
      default: false
    },
      buttonText: {
      type: String,
      default: 'Clic aquí'
    }
  }
}
</script>

<style scoped>
input {
  margin-right: 10px;
}
</style>
