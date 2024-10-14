import Vue from 'vue'
import router from './router'
import App from '@/components/layout/App'
import VueSweetalert2 from 'vue-sweetalert2'
import 'select2';
import ToggleButton from 'vue-js-toggle-button'
import SmartTable from 'vuejs-smart-table'
import VueViewer from 'v-viewer'
import vueselect2 from 'vue-select2'
import Select2 from 'v-select2-component';

import { Form } from 'vform';
window.Form = Form;
Vue.component('Select2', Select2);
Vue.use(SmartTable)
Vue.use(ToggleButton)
Vue.use(VueSweetalert2)
Vue.use(VueViewer)
Vue.use(vueselect2)
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  menu:0,
  components: { App},
  template: '<App/>'
})