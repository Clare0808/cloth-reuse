<template>
  <div class="box-frame">
    <div class="last-page" @click="ChangePage('prev')">〈</div>
    <transition name="dish-slide">
      <ClothDetailSiteMap class="guide" v-if="showDetail" />
    </transition>
    <transition name="cart-slide">
      <ClothStoreSitemap class="guide" v-if="showStore" />
    </transition>
    <div class="next-page" @click="ChangePage('next')">〉</div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import ClothDetailSiteMap from "./ClothDetailSiteMap.vue";
import ClothStoreSitemap from "./ClothStoreSitemap.vue";

export default {
  components: {
    ClothDetailSiteMap,
    ClothStoreSitemap,
  },
  setup() {
    const showDetail = ref(false);
    const showStore = ref(false);

    const ChangePage = (direc) => {
      const nextEle = document.querySelector(".next-page");
      const lastEle = document.querySelector(".last-page");

      if (direc === "next") {
        showDetail.value = false;
        showStore.value = true;

        nextEle.classList.add("nonActive");
        lastEle.classList.remove("nonActive");
      } else {
        showStore.value = false;
        showDetail.value = true;

        nextEle.classList.remove("nonActive");
        lastEle.classList.add("nonActive");
      }
    };

    onMounted(() => {
      showDetail.value = true;

      const lastEle = document.querySelector(".last-page");
      lastEle.classList.add("nonActive");
    });

    return {
      showDetail,
      showStore,
      ChangePage,
    };
  },
};
</script>

<style scoped>
.box-frame {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.guide {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 98;
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
  transition: all 0.5s ease;
}
.last-page {
  position: fixed;
  top: 50%;
  left: 5%;
  z-index: 100;
}
.next-page {
  position: fixed;
  top: 50%;
  right: 5%;
  z-index: 100;
}
.last-page:hover,
.next-page:hover {
  cursor: pointer;
  background-color: #3b5131;
  box-shadow: 0px 0px 5px 5px #3b5131;
  transform: scale(1.05);
}
.nonActive {
  background-color: #d0d0d0;
  box-shadow: 0px 0px 5px 5px #d0d0d0;
}
.nonActive:hover {
  cursor: not-allowed;
  background-color: #d0d0d0;
  box-shadow: 0px 0px 5px 5px #d0d0d0;
}

.dish-slide-enter-active,
.dish-slide-leave-active {
  transition: all 1s ease;
}
.dish-slide-enter-from,
.dish-slide-leave-to {
  opacity: 0;
  transform: translateX(-100%) translate(-50%, -50%);
}
.dish-slide-enter-to,
.dish-slide-leave-from {
  opacity: 1;
  transform: translateX(0) translate(-50%, -50%);
}
.cart-slide-enter-active,
.cart-slide-leave-active {
  transition: all 1s ease;
}
.cart-slide-enter-from,
.cart-slide-leave-to {
  opacity: 0;
  transform: translateX(100%) translate(-50%, -50%);
}
.cart-slide-enter-to,
.cart-slide-leave-from {
  opacity: 1;
  transform: translateX(0) translate(-50%, -50%);
}
</style>
