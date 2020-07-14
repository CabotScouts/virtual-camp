<template>
  <footer>
    <marquee scrollamount="4" v-bind="msg"></marquee>
  </footer>
</template>

<script>
export default {
  name: 'FooterMarquee',
  props: ['msg']
}
</script>

<style>
footer {
  padding: 1rem 0;
}

marquee {
  font-family: 'Lato', sans-serif;
  font-weight: 700;
  font-size: 3rem;

  text-shadow: 1px 1px darken(#0583c7, 8%);
}
</style>
