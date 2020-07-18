<template>
  <footer v-if="message">
    <transition name="fade">
      <div class="marquee">
        <p>{{ message }}</p>
      </div>
    </transition>
  </footer>
</template>

<script>
const messageURL = "https://camp.cabotscouts.org.uk/wall/message"

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

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
    this.timer = setInterval(() => this.fetchMessage(), 60000)
  },

  methods: {
    fetchMessage: async function() {
      await fetch(messageURL).then(response => response.json()).then(data => {
        if(this.message != data.message) {
          this.message = false
          sleep(1500)
          this.message = data.message
        }
      })
    }
  }
}
</script>

<style lang="scss">
footer {
  padding: 1.2rem 0;
  font-family: 'Lato', sans-serif;
  font-weight: 700;
  font-size: 2.6rem;
  text-shadow: 1px 1px darken(#0583c7, 8%);

  p {
    margin: 0;
    text-align: center;
  }

  .marquee {
    white-space: nowrap;
    overflow: hidden;

    p {
      display: inline-block;
      padding-left: 100%;
      animation: marquee 45s linear infinite;
      text-align: left;
    }
  }

}

@keyframes marquee {
  from { transform: translate(0, 0); }
  to { transform: translate(-105%, 0); }
}
</style>
