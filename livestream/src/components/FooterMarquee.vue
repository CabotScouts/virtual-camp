<template>
  <footer>
    <marquee scrollamount="5">{{ message }}</marquee>
  </footer>
</template>

<script>
const messageURL = "http://camp.cabotscouts.org.uk/wall/message"

export default {
  name: 'FooterMarquee',

  data() {
    return {
      message: "",
      timer: null
    }
  },

  mounted() {
    this.fetchMessage()
    this.timer = setInterval(() => this.fetchMessage(), 120000)
  },

  methods: {
    fetchMessage: function() {
      fetch(messageURL).then(response => response.json()).then(data => {
        this.message = data.message
      })
    }
  }
}
</script>

<style lang="scss">
footer {
  padding: 1.2rem 0;
}

marquee {
  font-family: 'Lato', sans-serif;
  font-weight: 700;
  font-size: 2.6rem;

  text-shadow: 1px 1px darken(#0583c7, 8%);
}
</style>
