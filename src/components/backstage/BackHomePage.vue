<template>
  <div class="back-page">
    <transition name="slide">
      <div class="btn-outframe" v-if="showSlide">
        <div class="text-frame">
          <img src="../../assets/img/logo.png" />
          <div class="sec-title">後台管理系統</div>
        </div>
        <div class="btn-frame">
          <router-link to="/back-cloth">上架服飾</router-link>
          <router-link to="/back-pickup">取衣紀錄</router-link>
          <router-link to="/back-user">用戶資訊</router-link>
          <router-link to="/back-web-review">網站回饋</router-link>
          <router-link to="/back-chart">數據統計</router-link>
          <router-link to="/back-contact">客服聯絡</router-link>
        </div>
        <router-link to="/user" class="store-btn">返回</router-link>
      </div>
    </transition>

    <transition name="slide">
      <router-view class="child-page" v-if="showSlide" />
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "BackHomePage",
  setup() {
    const showSlide = ref(false);

    onMounted(() => {
      showSlide.value = true;
    });

    return {
      showSlide,
    };
  },
};
</script>

<style scoped>
.back-page {
  width: 100vw;
  height: 100vh;
  background-color: #d3dcba;
  display: flex;
  justify-content: start;
  align-items: center;
  position: absolute;
  top: 0;
  left: 0;
}
.btn-outframe {
  width: 120px;
  height: 80%;
  background-color: #ffffff;
  border-radius: 20px;
  margin-left: 30px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
img {
  width: 50px;
  height: 50px;
}
.sec-title {
  margin-top: 10px;
}
a {
  color: #bebebe;
  font-size: 22px;
  text-decoration: none;
  margin: 20px 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s ease;
}
a:hover {
  color: #849c7d;
}
a:focus {
  color: #849c7d;
}
.store-btn {
  font-size: 18px;
  margin: 0;
}

.child-page {
  width: calc(100% - 290px);
  height: 80%;
  position: absolute;
  right: 30px;
  border-radius: 20px;
  background-color: #ffffff;
  padding: 20px;
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
