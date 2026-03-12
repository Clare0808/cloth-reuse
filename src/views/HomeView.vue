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
      <div class="last-page">〈</div>
      <div class="info-frame">
        <img src="../assets/img/cloth1.jpg" />
        <div class="text-frame">
          <div class="name">白色T-shirt</div>
          <div class="info-box">
            <div class="info-title">類型 :</div>
            <div class="info-content">上衣</div>
          </div>
          <div class="info-box">
            <div class="info-title">尺寸 :</div>
            <div class="info-content">M</div>
          </div>
          <div class="info-box">
            <div class="info-title">服飾狀況 :</div>
            <div class="info-content">稍微有汙漬沾染</div>
          </div>
          <div class="info-box">
            <div class="info-title">取衣地點 :</div>
            <div class="info-content">台北市信義區xx路</div>
          </div>
          <div class="info-box">
            <div class="info-title">取衣時間 :</div>
            <div class="info-content">9:00~11:00 AM</div>
          </div>
        </div>
      </div>
      <div class="next-page">〉</div>
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
      <div class="last-page">〈</div>
      <div class="review-box">
        <div class="review-stars">
          <div v-for="i in 5" :key="i">
            <i class="fa-solid fa-star"></i>
          </div>
        </div>
        <div class="review-content">
          以前不知道舊衣要丟哪裡，現在用這個網站就能快速找到回收點，讓衣服有第二次生命。
        </div>
        <div class="review-author-info">
          <i class="fa-solid fa-user"></i>
          <div class="review-text-frame">
            <div class="review-author-name">張小姐</div>
            <div class="review-author-date">2026-03-12</div>
          </div>
        </div>
      </div>
      <div class="next-page">〉</div>
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

export default {
  name: "HomePage",
  setup() {
    const showEle = ref(false);

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

    onMounted(() => {
      showEle.value = true;
    });

    return {
      showEle,
      CheckFadeIn,
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
.last-page,
.next-page {
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
.last-page:hover,
.next-page:hover {
  cursor: pointer;
  background-color: #3b5131;
  box-shadow: 0px 0px 5px 5px #3b5131;
  transform: scale(1.05);
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
