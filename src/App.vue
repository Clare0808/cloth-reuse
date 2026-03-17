<template>
  <nav>
    <div class="title-frame">
      <img src="./assets/img/logo.png" />
      <div class="title">舊衣回收平台</div>
    </div>
    <div class="func-text">
      <router-link to="/">主頁</router-link>
      <router-link to="/cloth">服飾專區</router-link>
      <router-link to="/map">再生地圖</router-link>
      <router-link to="/web-review">網站回饋</router-link>
      <router-link to="/problem">問題回報</router-link>
    </div>
    <div class="func-icon">
      <router-link to="/like">
        <i class="fa-solid fa-heart"></i>
      </router-link>
      <router-link to="/user">
        <i class="fa-solid fa-user"></i>
      </router-link>
      <i
        class="fa-solid fa-arrow-right-from-bracket"
        id="logout"
        v-if="loginStore.isAuthenticated"
        @click="showLogoutCheck = true"
      ></i>
      <router-link
        to="/login"
        class="login-sign-btn"
        v-if="!loginStore.isAuthenticated"
        >登入/註冊
      </router-link>
    </div>
  </nav>
  <router-view />

  <transition name="slide-x">
    <StatusEle class="status-msg" v-show="errorStore.showErrorMsg" />
  </transition>

  <transition name="slide-ele">
    <LoadingEle v-if="errorStore.showLoader" />
  </transition>

  <div
    class="overlay"
    v-show="showLogoutCheck"
    @click="showLogoutCheck = false"
  ></div>
  <transition name="slide-ele">
    <LogoutCheck class="logout-check" v-if="showLogoutCheck" />
  </transition>
</template>

<script>
import { ref } from "vue";

import { useRoute } from "vue-router";

import { loginUiStore } from "./store/login";
import { errorUiStore } from "./store/error";

import StatusEle from "../src/components/pageElement/StatusEle.vue";
import LoadingEle from "../src/components/pageElement/LoadingEle.vue";
import LogoutCheck from "../src/components/pageElement/LogoutCheck.vue";

export const showLogoutCheck = ref(false);

export default {
  components: {
    StatusEle,
    LoadingEle,
    LogoutCheck,
  },
  setup() {
    const route = useRoute();

    const loginStore = loginUiStore();
    const errorStore = errorUiStore();

    return {
      showLogoutCheck,
      route,
      loginStore,
      errorStore,
    };
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Pacifico", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  margin: 0;
  padding: 0;
}

nav {
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
nav a {
  color: #3b5131;
  font-size: 22px;
  text-decoration: none;
  margin: 20px;
  display: inline-block; // 讓動畫生效
  transition: all 0.3s ease;
}
nav a:hover {
  color: #849c7d;
  transform: scale(1.1);
}
.title-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.title-frame img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
.title {
  color: #3b5131;
  font-size: 28px;
}
.func-icon a {
  font-size: 20px;
  margin: 10px;
}
#logout {
  color: #3b5131;
  font-size: 20px;
  margin: 10px;
}
#logout:hover {
  cursor: pointer;
}
.login-sign-btn {
  width: 120px;
  height: 40px;
  color: #ffffff;
  font-size: 20px;
  text-align: center;
  line-height: 40px;
  background-color: #849c7d;
  border-radius: 20px;
  text-decoration: none;
  transition: all 0.3s ease;
}
.login-sign-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}

.status-msg {
  position: fixed;
  top: 90px;
  right: 20px;
  z-index: 3;
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
.logout-check {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 99;
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
.slide-x-enter-active,
.slide-x-leave-active {
  transition: all 1s ease;
}
.slide-x-enter-from,
.slide-x-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
.slide-x-enter-to,
.slide-x-leave-from {
  opacity: 1;
  transform: translateX(0);
}
</style>
