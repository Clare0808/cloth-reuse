<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">給我們的回饋</div>
    </transition>
    <transition name="slide">
      <div class="review-box-frame" v-if="showSlide">
        <div v-for="i in 7" :key="i">
          <div class="review-box">
            <div class="review-stars">
              <div v-for="s in 5" :key="s">
                <i class="fa-solid fa-star"></i>
              </div>
            </div>
            <div class="review-content">
              以前不知道舊衣要丟哪裡，現在用這個網站就能快速找到回收點，讓衣服有第二次生命。
            </div>
            <div class="review-author-info">
              <i class="fa-solid fa-user"></i>
              <div class="review-text-frame">
                <div class="review-author-name">王小明</div>
                <div class="review-author-date">2026-03-12</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <div class="add-btn" @click="showWriteWebReview = true" v-if="showFade">
        +
      </div>
    </transition>
  </div>

  <div
    class="overlay"
    v-show="showWriteWebReview"
    @click="showWriteWebReview = false"
  ></div>
  <transition name="slide-ele">
    <WriteWebReview class="ele-page" v-show="showWriteWebReview" />
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";

import WriteWebReview from "./pageElement/WriteWebReview.vue";

import { showWriteWebReview } from "./pageElement/WriteWebReview.vue";

export default {
  name: "ReviewPage",
  components: {
    WriteWebReview,
  },
  setup() {
    const showSlide = ref(false);
    const showFade = ref(false);

    onMounted(() => {
      showSlide.value = true;
      showFade.value = true;
    });

    return {
      showWriteWebReview,
      showSlide,
      showFade,
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
.review-author-info i {
  font-size: 30px;
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
</style>
