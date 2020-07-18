<template>
  <div id="app">
    <HeaderBar />
    <Wall />
    <FooterMarquee/>
  </div>
</template>

<script>
import HeaderBar from './components/HeaderBar.vue'
import Wall from './components/Wall.vue'
import FooterMarquee from './components/FooterMarquee.vue'

export default {
  name: 'App',

  components: {
    HeaderBar,
    Wall,
    FooterMarquee
  }
}
</script>

<style lang="scss">
body {
  height: 100vh;
  margin: 0;
  overflow: hidden;
  background-color: darken(#0583c7, 4%);
  color: #ffffff;
  font-family: 'Source Sans Pro', sans-serif;

  #app {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-flow: column nowrap;
    justify-content: space-between;
  }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .8s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
