<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">給我們的回饋</div>
    </transition>
    <transition name="fade">
      <div class="no-item" v-if="showNone">這裡是空的!</div>
    </transition>
    <transition name="slide">
      <div class="review-box-frame" v-if="showSlide">
        <div v-for="(review, index) in dataList" :key="index">
          <div class="review-box">
            <div class="review-stars">
              <div v-for="indexS in review.star" :key="indexS">
                <i class="fa-solid fa-star"></i>
              </div>
            </div>
            <div class="review-content">{{ review.content }}</div>
            <div class="review-author-info">
              <img :src="review.image" />
              <div class="review-text-frame">
                <div class="review-author-name">{{ review.name }}</div>
                <div class="review-author-date">{{ review.data }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <i
      class="fa-regular fa-circle-question"
      id="help-btn"
      @click="showSitemap = true"
    ></i>

    <transition name="fade">
      <div
        class="add-btn"
        @click="reviewStore.showElePage = true"
        v-if="showFade"
      >
        +
      </div>
    </transition>
  </div>

  <div
    class="overlay"
    v-show="reviewStore.showElePage"
    @click="reviewStore.showElePage = false"
  ></div>
  <transition name="slide-ele">
    <WriteWebReview class="ele-page" v-show="reviewStore.showElePage" />
  </transition>

  <div class="overlay" v-show="showSitemap" @click="showSitemap = false"></div>
  <div class="overlay" v-if="showSitemap" @click="showSitemap = false"></div>
  <transition name="slide-sitemap">
    <WebReviewSitemap class="ele-page" v-if="showSitemap" />
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";

import { reviewUiStore } from "@/store/review";

import WriteWebReview from "./pageElement/WriteWebReview.vue";
import WebReviewSitemap from "./sitemap/WebReviewSitemap.vue";

export default {
  name: "ReviewPage",
  components: {
    WriteWebReview,
    WebReviewSitemap,
  },
  setup() {
    const showSlide = ref(false);
    const showFade = ref(false);
    const dataList = ref([]);
    const showNone = ref(false);
    const showSitemap = ref(false);

    const reviewStore = reviewUiStore();

    onMounted(async () => {
      showSlide.value = true;
      showFade.value = true;
      showSitemap.value = true;

      dataList.value = await reviewStore.GetReviewData();

      if (dataList.value.length === 0) {
        showNone.value = true;
      }
    });

    return {
      showSlide,
      showFade,
      dataList,
      showNone,
      showSitemap,
      reviewStore,
    };
  },
};
</script>

<style scoped>
.page {
  padding-bottom: 50px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  position: relative;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.no-item {
  color: #adadad;
  font-size: 26px;
  margin-top: 30px;
}
.review-box-frame {
  display: grid;
  grid-template-columns: repeat(3, 350px);
  grid-template-rows: auto;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.review-box {
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.review-stars {
  color: #f0c42d;
  font-size: 24px;
  display: flex;
  justify-content: start;
  align-items: center;
}
.review-content {
  font-size: 22px;
  margin: 20px 0;
  text-align: start;
}
.review-author-info {
  display: flex;
  justify-content: start;
  align-items: center;
}
.review-author-info img {
  width: 30px;
  height: 30px;
  margin-right: 20px;
}
.review-text-frame {
  font-size: 20px;
  text-align: start;
}
.non-content {
  font-size: 30px;
  margin-top: 100px;
}
.add-btn {
  width: 60px;
  height: 60px;
  color: #ffffff;
  font-size: 40px;
  text-align: center;
  line-height: 60px;
  background-color: #849c7d;
  border-radius: 50%;
  position: fixed;
  bottom: 30px;
  right: 30px;
  transition: all 0.3s ease;
}
.add-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
#help-btn {
  font-size: 26px;
  color: #849c7d;
  position: fixed;
  bottom: 20px;
  left: 20px;
  z-index: 2;
  cursor: pointer;
}

.ele-page {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 99;
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 98;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
.slide-enter-active,
.slide-leave-active {
  transition: all 2s ease;
}
.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.slide-ele-enter-active,
.slide-ele-leave-active {
  transition: all 1s ease;
}
.slide-ele-enter-from,
.slide-ele-leave-to {
  opacity: 0;
  transform: translate(-50%, -50%) translateY(20px);
}
.slide-ele-enter-to,
.slide-ele-leave-from {
  opacity: 1;
  transform: translate(-50%, -50%) translateY(0);
}
.slide-sitemap-enter-active,
.slide-sitemap-leave-active {
  transition: all 1s ease;
}
.slide-sitemap-enter-from,
.slide-sitemap-leave-to {
  opacity: 0;
  transform: translateX(-100%) translate(-50%, -50%);
}
.slide-sitemap-enter-to,
.slide-sitemap-leave-from {
  opacity: 1;
  transform: translateX(0) translate(-50%, -50%);
}
</style>
