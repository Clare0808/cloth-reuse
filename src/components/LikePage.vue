<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">我的收藏</div>
    </transition>
    <transition name="slide">
      <div class="like-outframe" v-if="showSlide">
        <div class="like-frame" v-for="i in 8" :key="i">
          <div class="like-box">
            <img src="../assets/img/cloth1.jpg" />
            <div class="cloth-info-frame">
              <div class="title-frame">
                <div class="cloth-name">白色上衣</div>
                <i class="fa-solid fa-heart"></i>
              </div>
              <div class="text-inframe">
                <div class="cloth-info">類型: 上衣</div>
                <div class="cloth-info">尺寸: L</div>
              </div>
              <div class="cloth-info">服飾狀況: 稍微有汙漬沾染</div>
              <div class="cloth-info">取衣地點: 台北市信義區xx路</div>
              <div class="cloth-info">取衣時間: 9:00~11:00 AM</div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "LikePage",
  setup() {
    const showFade = ref(false);
    const showSlide = ref(false);

    onMounted(() => {
      showFade.value = true;
      showSlide.value = true;
    });

    return {
      showFade,
      showSlide,
    };
  },
};
</script>

<style scoped>
.page {
  padding-bottom: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.like-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.like-frame {
  width: 80%;
}
.like-box {
  width: 100%;
  border: 2px solid #3b5131;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  text-align: left;
  display: grid;
  grid-template-columns: 35% 65%;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}
img {
  width: 300px;
  margin-right: 50px;
}
.title-frame {
  width: 95%;
  border-bottom: 1px solid #3b5131;
  padding: 10px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title-frame i {
  color: #3b5131;
  font-size: 22px;
  transition: all 0.3s ease;
}
.title-frame i:hover {
  color: #849c7d;
  cursor: pointer;
  transform: scale(1.1);
}
.cloth-name {
  font-size: 30px;
}
.text-inframe {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 50%);
  align-items: center;
}
.cloth-info {
  font-size: 20px;
  margin-bottom: 10px;
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
</style>
