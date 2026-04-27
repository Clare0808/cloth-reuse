<template>
  <div class="page">
    <transition name="fade">
      <div class="title-frame">
        <transition-group name="fade">
          <div class="title" v-if="showEle">舊衣回收平台</div>
          <div class="slogan" v-if="showEle">讓每件衣服再走一段路</div>
        </transition-group>
        <transition name="slide">
          <div class="btn" v-if="showEle">開始</div>
        </transition>
      </div>
    </transition>
  </div>
  <div class="sub-page-info">
    <div class="page-title">服飾預覽</div>
    <div class="info-outframe" id="slide">
      <div class="last-cloth-page" @click="ChangeClothPage(-1)">〈</div>
      <div class="info-frame">
        <img :src="clothData.image" />
        <div class="text-frame">
          <div class="name">{{ clothData.name }}</div>
          <div class="info-box">
            <div class="info-title">類型 :</div>
            <div class="info-content">{{ type }}</div>
          </div>
          <div class="info-box">
            <div class="info-title">尺寸 :</div>
            <div class="info-content">{{ clothData.size }}</div>
          </div>
          <div class="info-box">
            <div class="info-title">服飾狀況 :</div>
            <div class="info-content">{{ clothData.description }}</div>
          </div>
          <div class="info-box">
            <div class="info-title">取衣地點 :</div>
            <div class="info-content">{{ clothData.place }}</div>
          </div>
          <div class="info-box">
            <div class="info-title">取衣時間 :</div>
            <div class="info-content">{{ clothData.time }}</div>
          </div>
        </div>
      </div>
      <div class="next-cloth-page" @click="ChangeClothPage(1)">〉</div>
    </div>
  </div>
  <div class="sub-page">
    <div class="page-title">選擇我們!</div>
    <div class="special-outframe" id="slide">
      <div class="special-box">
        <div class="special-title">衣物再利用資訊</div>
        <i class="fa-solid fa-recycle"></i>
        <div class="special">
          提供舊衣捐贈、回收、再利用的資訊，幫助使用者更了解衣物循環。
        </div>
      </div>
      <div class="special-box">
        <div class="special-title">舊衣回收地點查詢</div>
        <i class="fa-solid fa-location-dot"></i>
        <div class="special">
          提供回收箱或回收據點地圖，讓使用者可以快速找到最近的舊衣回收地點，減少衣物被丟棄的情況。
        </div>
      </div>
    </div>
    <div class="special-outframe" id="slide">
      <div class="special-box">
        <div class="special-title">回收影響力統計</div>
        <i class="fa-solid fa-chart-line"></i>
        <div class="special">
          網站顯示平台累積的回收成果，讓使用者看到自己對環境的貢獻。
        </div>
      </div>
      <div class="special-box">
        <div class="special-title">支持 SDGs 永續發展目標</div>
        <i class="fa-solid fa-earth-americas"></i>
        <div class="special">
          本平台呼應 SDGs，透過舊衣回收與再利用，減少資源浪費並促進永續生活。
        </div>
      </div>
    </div>
  </div>

  <div class="sub-page">
    <div class="page-title">使用者給我們的回饋!</div>
    <div class="review-outframe" id="slide">
      <div class="last-review-page" @click="ChangeReviewPage(-1)">〈</div>
      <div class="review-box">
        <div class="review-stars">
          <div v-for="i in reviewData.star" :key="i">
            <i class="fa-solid fa-star"></i>
          </div>
        </div>
        <div class="review-content">{{ reviewData.content }}</div>
        <div class="review-author-info">
          <i class="fa-solid fa-user"></i>
          <div class="review-text-frame">
            <div class="review-author-name">{{ reviewData.name }}</div>
            <div class="review-author-date">{{ reviewData.data }}</div>
          </div>
        </div>
      </div>
      <div class="next-review-page" @click="ChangeReviewPage(1)">〉</div>
    </div>
    <div class="contact-frame">
      <div class="contact-title">有任何問題歡迎聯絡我們！</div>
      <div class="contact-info">
        <i class="fa-solid fa-envelope"></i>
        123456@gmail.com
      </div>
      <div class="contact-info">
        <i class="fa-solid fa-phone"></i>
        0987654321
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { reviewUiStore } from "@/store/review";

import OptionData from "@/assets/data/optionsData.json";

export default {
  name: "HomePage",
  setup() {
    const showEle = ref(false);
    const clothList = ref([]);
    const clothData = ref({});
    const pageCloth = ref(0);
    const type = ref("");
    const reviewList = ref([]);
    const reviewData = ref({});
    const pageReview = ref(0);

    const reviewStore = reviewUiStore();

    const GetClothData = async () => {
      const response = await fetch("/data/clothData.json");
      const data = await response.json();

      clothList.value = data.filter((item) => {
        return !item.lock;
      });
    };

    const TransformType = (list) => {
      type.value = OptionData.find((item) => {
        return item.label === list.category;
      }).name;
    };

    const ChangeClothPage = (num) => {
      const listLen = clothList.value.length;

      pageCloth.value = pageCloth.value + num;

      const nextEle = document.querySelector(".next-cloth-page");
      const lastEle = document.querySelector(".last-cloth-page");

      if (pageCloth.value >= listLen) {
        pageCloth.value = listLen - 1;

        nextEle.classList.add("noChange");
      } else if (pageCloth.value < 0) {
        pageCloth.value = 0;

        lastEle.classList.add("noChange");
      } else {
        nextEle.classList.remove("noChange");
        lastEle.classList.remove("noChange");
      }

      clothData.value = clothList.value[pageCloth.value];
      TransformType(clothData.value);
    };

    const ChangeReviewPage = (num) => {
      const listLen = reviewList.value.length;

      pageReview.value = pageReview.value + num;

      const nextEle = document.querySelector(".next-review-page");
      const lastEle = document.querySelector(".last-review-page");

      if (pageReview.value >= listLen) {
        pageReview.value = listLen - 1;

        nextEle.classList.add("noChange");
      } else if (pageReview.value < 0) {
        pageReview.value = 0;

        lastEle.classList.add("noChange");
      } else {
        nextEle.classList.remove("noChange");
        lastEle.classList.remove("noChange");
      }

      reviewData.value = reviewList.value[pageReview.value];
    };

    // 元素進入視窗後顯示動畫
    const CheckFadeIn = () => {
      document.querySelectorAll("#slide").forEach((el) => {
        // 判斷元素是否進入視窗
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight) {
          el.classList.add("visible"); // 如果進入就觸發動畫
        }
      });
    };

    window.addEventListener("scroll", CheckFadeIn); // 滾動畫面時進行檢查

    onMounted(async () => {
      showEle.value = true;

      await GetClothData();

      clothData.value = clothList.value[pageCloth.value];
      TransformType(clothData.value);

      reviewList.value = await reviewStore.GetReviewData();
      reviewData.value = reviewList.value[pageReview.value];
    });

    return {
      showEle,
      clothList,
      clothData,
      pageCloth,
      type,
      reviewList,
      reviewData,
      pageReview,
      GetClothData,
      CheckFadeIn,
      TransformType,
      ChangeClothPage,
      ChangeReviewPage,
    };
  },
};
</script>

<style scoped>
.page,
.sub-page-info,
.sub-page {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: top;
  align-items: center;
}
.title-frame {
  width: calc(100% - 60px);
  height: calc(80% - 20px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background: url("@/assets/img/background5.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;

  border-radius: 12px;
  padding: 20px;
}
.title {
  color: #ffffff;
  font-size: 90px;
  font-weight: bold;
}
.slogan {
  color: #ffffff;
  font-size: 26px;
  margin-top: 20px;
}
.btn {
  color: #3b5131;
  font-size: 22px;
  background-color: #ffffff;
  border-radius: 12px;
  margin-top: 30px;
  padding: 10px 20px;
  transition: all 0.3s ease;
}
.btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.2);
}

.sub-page-info {
  border-radius: 12px;
  box-shadow: inset 0px 0px 20px 20px #d3dcba;
  justify-content: center;
}
.page-title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}
.info-outframe,
.review-outframe {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.info-frame {
  width: 80%;
  border: 2px solid #3b5131;
  border-radius: 12px;
  padding: 20px;
  text-align: left;
  display: grid;
  grid-template-columns: 35% 65%;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}
.info-frame:hover {
  cursor: pointer;
  transform: translateY(-10px);
}
.info-frame img {
  width: 300px;
  height: 300px;
}
.name {
  font-size: 30px;
  border-bottom: 1px solid #3b5131;
  margin-bottom: 20px;
  padding-bottom: 10px;
}
.info-box {
  width: 100%;
  font-size: 22px;
  margin: 10px;
  display: grid;
  grid-template-columns: 30% 70%;
  align-items: center;
}
.last-cloth-page,
.next-cloth-page,
.last-review-page,
.next-review-page {
  width: 50px;
  height: 50px;
  font-size: 30px;
  font-weight: bold;
  line-height: 50px;
  color: #ffffff;
  background-color: #d3dcba;
  border-radius: 50%;
  box-shadow: 0px 0px 5px 5px #d3dcba;
  margin: 30px;
  transition: all 0.3s ease;
}
.last-cloth-page:hover,
.next-cloth-page:hover,
.last-review-page:hover,
.next-review-page:hover {
  cursor: pointer;
  background-color: #3b5131;
  box-shadow: 0px 0px 5px 5px #3b5131;
  transform: scale(1.05);
}
.noChange {
  background-color: #adadad;
  box-shadow: 0px 0px 5px 5px #adadad;
}
.noChange:hover {
  cursor: not-allowed;
  background-color: #adadad;
  box-shadow: 0px 0px 5px 5px #adadad;
}

.sub-page {
  justify-content: center;
}
.special-outframe {
  width: 90%;
  margin: 10px 0;
  display: grid;
  grid-template-columns: repeat(2, 45%);
  gap: 40px;
  justify-content: center;
  align-items: center;
}
.special-box {
  width: 95%;
  height: 200px;
  background-color: #d3dcba;
  color: #3b5131;
  font-size: 22px;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}
.special-box:hover {
  color: #d3dcba;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.05);
}
.special-title {
  font-size: 30px;
  margin-bottom: 20px;
}
.special-box i {
  color: #849c7d;
  font-size: 40px;
  margin-bottom: 20px;
}

.sub-page {
  overflow-x: hidden;
  position: relative;
}
.review-outframe {
  margin-bottom: 120px;
}
.review-box {
  width: 60%;
  background-color: #ffffff;
  border: 2px solid #3b5131;
  border-radius: 20px;
  margin: 0 30px;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  transition: all 0.3s ease;
}
.review-box:hover {
  transform: translateY(-10px);
}
.review-stars {
  color: #f0c42d;
  font-size: 24px;
  display: flex;
  justify-content: start;
}
.review-stars i {
  margin: 0 3px;
}
.review-content {
  font-size: 22px;
  margin: 20px 0;
  text-align: start;
}
.review-author-info {
  text-align: start;
  display: flex;
  align-items: center;
}
.review-author-info i {
  font-size: 40px;
  margin-right: 20px;
}
.review-text-frame {
  font-size: 20px;
}
.contact-frame {
  width: 100%;
  height: calc(20% - 20px);
  color: #849c7d;
  font-size: 22px;
  text-align: start;
  background-color: #d3dcba;
  padding: 20px;
  position: absolute;
  bottom: 0;
}
.contact-title {
  margin-left: 30px;
}
.contact-info {
  margin-left: 50px;
  margin-top: 10px;
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

#slide {
  transition: all 2s ease;
  opacity: 0;
  transform: translateY(20px);
}
#slide.visible {
  opacity: 1;
  transform: translateY(0);
}
</style>
