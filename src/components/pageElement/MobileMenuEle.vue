<template>
  <div class="ele">
    <div class="title-frame">
      <img src="@/assets/img/logo.png" />
      <div class="title">舊衣回收平台</div>
    </div>
    <div class="func-text">
      <router-link to="/">主頁</router-link>
      <router-link to="/cloth">服飾專區</router-link>
      <router-link to="/map">再生地圖</router-link>
      <router-link to="/web-review">網站回饋</router-link>
      <router-link to="/problem">疑問中心</router-link>
    </div>
    <div class="mobile-func-icon">
      <router-link to="/pickup">
        <i class="fa-solid fa-shirt" v-if="loginStore.isAuthenticated"></i>
      </router-link>
      <router-link to="/like">
        <i class="fa-solid fa-heart" v-if="loginStore.isAuthenticated"></i>
      </router-link>
      <router-link to="/user">
        <i class="fa-solid fa-user" v-if="loginStore.isAuthenticated"></i>
      </router-link>
      <i
        class="fa-solid fa-arrow-right-from-bracket"
        id="logout"
        v-if="loginStore.isAuthenticated"
        @click="HandleLogout"
      ></i>
      <router-link
        to="/login"
        class="login-sign-btn"
        v-if="!loginStore.isAuthenticated"
        >登入/註冊
      </router-link>
    </div>
  </div>
</template>

<script>
import { onMounted } from "vue";

import { useRoute, useRouter } from "vue-router";

import { loginUiStore } from "@/store/login";
import { errorUiStore } from "@/store/error";

import { showLogoutCheck, showMobileMenu } from "@/App.vue";

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();

    const loginStore = loginUiStore();
    const errorStore = errorUiStore();

    const HandleLogout = () => {
      showLogoutCheck.value = true;
      showMobileMenu.value = false;
    };

    onMounted(async () => {
      if (!loginStore.isAuthenticated) {
        try {
          await loginStore.googleLogin();

          errorStore.LoadSuccess("登入成功!");

          localStorage.setItem("userEmail", loginStore.user.email);
          localStorage.setItem("userName", loginStore.user.name);
          localStorage.setItem("inAdmin", loginStore.isAdmin);
        } catch (err) {
          errorStore.SetError(err.message);

          router.push("/login");
        }
      }

      await errorStore.CloseLoadEle();
    });

    return {
      showLogoutCheck,
      showMobileMenu,
      route,
      loginStore,
      errorStore,
      HandleLogout,
    };
  },
};
</script>

<style scoped>
.ele {
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
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
.func-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.func-text a {
  color: #3b5131;
  font-size: 22px;
  margin: 10px 0;
  text-decoration: none;
}
.mobile-func-icon i {
  color: #3b5131;
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
  display: block;
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
