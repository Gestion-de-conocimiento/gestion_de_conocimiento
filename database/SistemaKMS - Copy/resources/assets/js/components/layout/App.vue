<template>
    <div>
      <MyNavBar></MyNavBar>
      <MyHeader></MyHeader>
      <router-view ></router-view>
      <Footer></Footer>
    </div>
    
</template>

<script>
import MyHeader from "./menu.vue";
import MyNavBar from "./navbar.vue";
import Footer from "./footer.vue";
export default {
  components: {
    MyNavBar,
    MyHeader,
    Footer
  },
  name: 'App'
}
</script>
