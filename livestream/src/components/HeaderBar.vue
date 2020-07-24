<template>
  <header>
    <div id="logo">Way Out West!</div>
    <div id="clock"><time>{{ hours }}<span class="sep">:</span>{{ minutes }}</time></div>
  </header>
</template>

<script>
const pad = (val) => val < 10 ? "0" + val : val
const date = () => new Date()
const theHour = () => pad(date().getHours())
const theMinute = () => pad(date().getMinutes())

export default {
  name: 'HeaderBar',

  data() {
    return {
      tick: null,
      hours: theHour(),
      minutes: theMinute()
    }
  },

  created() {
    this.tick = setInterval(() => {
      this.hours = theHour();
      this.minutes = theMinute();
    }, 1000)
  },

  destroyed() {
    clearInterval(this.tick)
  }
}
</script>

<style lang="scss">
header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;

  padding: 1rem 2rem;

  text-shadow: 1px 1px darken(#0583c7, 8%);
}

#logo {
  margin-top: -0.2rem;

  font-family: 'Sriracha', cursive;
  font-size: 2.2rem;

}

#clock {
  font-family: 'Lato', sans-serif;
  font-weight: 900;
  font-size: 3.5rem;

  .sep {
    padding: 0 5px;
  }
}
</style>
