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
    </div>
  </nav>
  <router-view />
</template>

<script>
import { useRoute } from "vue-router";

export default {
  setup() {
    const route = useRoute();

    return {
      route,
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
  /* background-color: #e7e9e6; */
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
nav a {
  color: #3b5131;
  font-size: 22px;
  text-decoration: none;
  margin: 20px;
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
</style>
