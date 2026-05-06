<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">常見問題</div>
    </transition>
    <transition name="slide">
      <div class="box-outframe" v-if="showSlide">
        <div v-for="(question, index) in questionData" :key="index">
          <div class="box-frame">
            <div class="question-box">
              <div class="question">{{ question.question }}</div>
              <div class="icon" @click="HandleShowAnswer(index)">﹀</div>
            </div>
            <transition name="slide-down">
              <div class="answer-box" v-if="question.show">
                <div class="answer" v-html="question.answer"></div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </transition>
  </div>

  <i
    class="fa-regular fa-message"
    id="contact"
    @click="contactStore.showElePage = true"
  ></i>

  <i
    class="fa-regular fa-circle-question"
    id="help-btn"
    @click="showSitemap = true"
  ></i>

  <div
    class="overlay"
    v-show="contactStore.showElePage"
    @click="contactStore.showElePage = false"
  ></div>
  <transition name="slide-ele">
    <ContactEle class="ele-page" v-show="contactStore.showElePage" />
  </transition>

  <div class="overlay" v-show="showSitemap" @click="showSitemap = false"></div>
  <div class="overlay" v-if="showSitemap" @click="showSitemap = false"></div>
  <transition name="slide-sitemap">
    <ServerContactSitemap class="ele-page" v-if="showSitemap" />
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";

import { contactUiStore } from "@/store/contact";

import QuestionDataRaw from "../assets/data/questionData.json";

import ContactEle from "./pageElement/ContactEle.vue";
import ServerContactSitemap from "./sitemap/ServerContactSitemap.vue";

export default {
  name: "ProblemPage",
  components: {
    ContactEle,
    ServerContactSitemap,
  },
  setup() {
    const questionData = ref(QuestionDataRaw);
    const showSlide = ref(false);
    const showFade = ref(false);
    const showSitemap = ref(false);

    const contactStore = contactUiStore();

    const HandleShowAnswer = (index) => {
      questionData.value[index].show = !questionData.value[index].show;

      const queEle = document.querySelectorAll(".box-frame")[index];

      if (questionData.value[index].show) {
        if (window.innerWidth <= 500) {
          queEle.style.marginBottom = "140px";
        } else {
          queEle.style.marginBottom = "110px";
        }
      } else {
        queEle.style.marginBottom = "20px";
      }
    };

    onMounted(async () => {
      showSlide.value = true;
      showFade.value = true;
      showSitemap.value = true;
    });

    return {
      QuestionDataRaw,
      questionData,
      showSlide,
      showFade,
      showSitemap,
      contactStore,
      HandleShowAnswer,
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
.box-outframe {
  width: 85%;
}
.box-frame {
  width: 100%;
  margin-bottom: 20px;
  position: relative;
}
.question-box {
  width: 95%;
  color: #3b5131;
  background-color: #d3dcba;
  border-radius: 20px;
  text-align: start;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 1;
  transition: all 0.3s ease;
}
.question {
  font-size: 22px;
}
.icon {
  color: #849c7d;
  font-size: 26px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}
.icon:hover {
  color: #ffffff;
}
.answer-box {
  width: calc(95% - 2px);
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  text-align: start;
  padding: 20px;
  padding-top: 50px;
  position: absolute;
  top: 100px;
  transform: translate(0, -50%);
  z-index: 0;
}
.answer {
  font-size: 18px;
}

#contact {
  width: 60px;
  height: 60px;
  color: #ffffff;
  font-size: 26px;
  text-align: center;
  line-height: 60px;
  background-color: #849c7d;
  border-radius: 50%;
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 2;
  transition: all 0.3s ease;
}
#contact:hover {
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

.slide-enter-active,
.slide-leave-active {
  transition: all 1s ease;
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
.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.8s ease;
}
.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-20px) translate(0, -50%);
}
.slide-down-enter-to,
.slide-down-leave-from {
  opacity: 1;
  transform: translateY(0) translate(0, -50%);
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

@media (max-width: 500px) {
  .question-box {
    width: 90%;
  }
  .answer-box {
    width: calc(90% - 2px);
    top: 120px;
  }
}
</style>
