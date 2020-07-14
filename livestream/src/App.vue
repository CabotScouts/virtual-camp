<template>
  <div id="app">
    <HeaderBar />
    <!-- <Wall /> -->
    <FooterMarquee />
  </div>
</template>

<script>
import HeaderBar from './components/HeaderBar.vue'
import FooterMarquee from './components/FooterMarquee.vue'

export default {
  name: 'App',

  components: {
    HeaderBar,
    FooterMarquee
  },

}
</script>

<style lang="scss">
body {
  height: 100vh;
  margin: 0;
  overflow: hidden;

  // background-color: #f8f9fa;
  background-color: darken(#0583c7, 4%);
  // background-color: #2b2d42;
  color: #ffffff;
  font-family: 'Source Sans Pro', sans-serif;

  #app {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-flow: column nowrap;
    justify-content: space-between;

    header {
    }
  }
}
</style>
