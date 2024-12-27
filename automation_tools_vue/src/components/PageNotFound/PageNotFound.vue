
<template>
  <div class="PageNotFound">
    <div class="w-full">
      <img
        :src="imageSrc"
        @error="loadFallbackImage"
        alt="Page Not Found"
        class="img-fluid h-full w-full"
      />
    </div>
  </div>
</template>
<script>
// import fallbackImage from '../../Images/Page_Not_Found/404.jpg';

export default {
  name: 'PageNotFound',
  data() {
    return {
      // الرابط الأساسي للصورة من الإنترنت
      imageSrc:
        'https://raw.githubusercontent.com/LearnCodingEasy/Images/refs/heads/main/images/Page_Not_Found/404.jpg',

      // الصورة المحلية
      fallbackImage: '../../assets/Images/Page_Not_Found/404.jpg',
    }
  },
  methods: {
    loadFallbackImage() {
      // في حالة الخطأ، تغيير الصورة إلى المسار المحلي
      console.error('Error loading image, switching to fallback.')
      this.imageSrc = this.fallbackImage
    },
  },
  mounted() {
    document.title = 'Page Not Found'
    setTimeout(() => {
      this.$router.go(-1)
    }, 15000)
  },
}
</script>

<style lang="scss">
.PageNotFound {
  > div {
    height: calc(100vh - 70px);
  }
  /* For Scrollbar */
  ::-webkit-scrollbar {
    width: 1rem;
    background-color: #333;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #bbbbbb;
    border-radius: 0.25rem;
  }
}
</style>

