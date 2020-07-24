<template>
<main>
  <transition name="fade">
    <div id="share" v-if="current" v-bind:data="current">
      <div class="media" :class="current.type" v-if="current.file">
        <img v-if="current.type == 'image'" :src="current.file" />
        <div v-if="current.type == 'video'" class="video">
          <video ref="video" :src="current.file" autoplay />
        </div>
      </div>
      <div class="caption" v-if="current.caption">
        <p>
          {{ current.caption }}
        </p>
      </div>
    </div>
  </transition>
</main>
</template>

<script type="text/javascript">
const sharesURL = "https://camp.cabotscouts.org.uk/wall/shares/60"

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export default {
  name: 'Wall',

  data() {
    return {
      fetchTimer: null,
      changeTimer: null,
      media: [],
      current: {},
      currentIdx: -1,
      error: false
    }
  },

  mounted() {
    this.fetchMedia().then(() => {
      this.currentIdx = -1
      if(!this.changeTimer) this.changeMedia()
      this.fetchTimer = setInterval(()  => this.fetchMedia(), 180000)
    })
  },

  methods: {
    fetchMedia: async function() {
      return await fetch(sharesURL).then(response => response.json()).then(data => {
        const l = data.media.length
        if(this.media.length > 0 && data.media[l-1].file != this.media[l-1].file) this.currentIdx = -1
        this.media = data.media
      })
    },

    changeMedia: async function() {
      clearInterval(this.changeTimer)
      this.current = false
      await sleep(2000)
      this.currentIdx = ((this.currentIdx + 1) >= this.media.length) ? 0 : this.currentIdx + 1
      this.current = this.media[this.currentIdx]

      var timer = 18000;
      if(this.current.type == "video") {
        this.$nextTick(() => {
          this.$refs.video.addEventListener('loadedmetadata', () => {
            timer = (this.$refs["video"].duration * 1000) + 5000
            this.$refs["video"].play()
          })
        })
      }

      if(this.media.length > 1) {
        this.changeTimer = setInterval(() => this.changeMedia(), timer)
      }
      else {
        this.changeTimer = false
      }
    },
  }
}
</script>

<style lang="scss">
main {
  display: flex;
  justify-content: center;
  padding: 20px 30px;

  #share {
    display: flex;
    justify-content: center;

    .media {
      border-radius: 8px;

      img, .video, video {
        border-radius: 6px;
      }

      img, video {
        display: block;
        max-height: 70vh;
        margin: 0;
        padding: 0;
      }

      img {
        image-orientation: from-image;
      }
    }

    .media.video {
      border-radius: 8px;
      padding: 6px;

      video {
        min-width: 50%;
        border-radius: 8px;
      }
    }

    .caption {
      display: flex;
      flex-flow: column nowrap;
      justify-content: center;
      max-width: 40%;
      padding: 30px;

      p {
        margin: 0;
        max-height: 60vh;
        font-size: 2.5rem;
        font-weight: 500;
        line-height: 1.5;
      }
    }
  }
}
</style>
