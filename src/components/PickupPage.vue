<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">取衣專區</div>
    </transition>
    <transition name="fade">
      <div class="no-item" v-if="showNone">這裡是空的!</div>
    </transition>
    <transition name="slide">
      <div class="pickup-outframe" v-if="showSlide">
        <div
          class="pickup-frame"
          v-for="(pickup, index) in dataList"
          :key="index"
        >
          <div class="pickup-box">
            <img :src="pickup.image" />
            <div class="cloth-info-frame">
              <div class="title-frame">
                <div class="cloth-title-info">{{ pickup.name }}</div>
                <div class="cloth-title-info">{{ pickup.place }}</div>
                <div class="cloth-title-info">{{ pickup.time }}</div>
                <div class="icon-box">
                  <i class="fa-solid fa-map"></i>
                  <i
                    class="fa-solid fa-trash"
                    @click="DeleteData(pickup.name)"
                  ></i>
                </div>
              </div>
              <div class="cloth-info">類型: {{ pickup.type }}</div>
              <div class="cloth-info">尺寸: {{ pickup.size }}</div>
              <div class="cloth-info">服飾狀況: {{ pickup.description }}</div>
            </div>
            <div class="btn" @click="ClickFinish(pickup)">取衣完成</div>
          </div>
        </div>
      </div>
    </transition>
  </div>

  <div
    class="overlay"
    v-show="pickupStore.showElePage"
    @click="pickupStore.showElePage = false"
  ></div>
  <transition name="slide-ele">
    <PickupCancleCheck class="ele-page" v-show="pickupStore.showElePage" />
  </transition>

  <div
    class="overlay"
    v-show="finishStore.showElePage"
    @click="finishStore.showElePage = false"
  ></div>
  <transition name="slide-ele">
    <FinishCheck class="ele-page" v-show="finishStore.showElePage" />
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";

import { pickupUiStore } from "@/store/pickup";
import { finishUiStore } from "@/store/finish";

import PickupCancleCheck from "./pageElement/PickupCancleCheck.vue";
import FinishCheck from "./pageElement/FinishCheck.vue";

export default {
  name: "PickupPage",
  components: {
    PickupCancleCheck,
    FinishCheck,
  },
  setup() {
    const showFade = ref(false);
    const showSlide = ref(true);
    const dataList = ref([]);
    const showNone = ref(false);

    const pickupStore = pickupUiStore();
    const finishStore = finishUiStore();

    const DeleteData = async (data) => {
      pickupStore.dataList = data;

      pickupStore.showElePage = true;
    };

    const ClickFinish = async (data) => {
      finishStore.dataList = data;

      finishStore.showElePage = true;
    };

    onMounted(async () => {
      showFade.value = true;
      showSlide.value = true;

      dataList.value = await pickupStore.GetPickupData();

      if (dataList.value.length === 0) {
        showNone.value = true;
      }
    });

    return {
      showFade,
      showSlide,
      dataList,
      showNone,
      pickupStore,
      finishStore,
      DeleteData,
      ClickFinish,
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
.no-item {
  color: #adadad;
  font-size: 26px;
  margin-top: 30px;
}
.pickup-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.pickup-frame {
  width: 80%;
}
.pickup-box {
  width: 100%;
  border: 2px solid #3b5131;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  text-align: left;
  display: grid;
  grid-template-columns: 15% 85%;
  justify-content: center;
  align-items: center;
  position: relative;
  transition: all 0.3s ease;
}
img {
  width: 120px;
  margin-right: 50px;
}
.title-frame {
  width: 100%;
  border-bottom: 1px solid #3b5131;
  margin-bottom: 10px;
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
  color: #d3dcba;
  cursor: pointer;
  transform: scale(1.1);
}
.cloth-title-info {
  font-size: 24px;
  margin-bottom: 10px;
}
.icon-box i {
  margin: 0 10px;
}
.cloth-info {
  font-size: 18px;
  margin-bottom: 10px;
}
.btn {
  width: 150px;
  height: 40px;
  color: #ffffff;
  font-size: 20px;
  background-color: #849c7d;
  border-radius: 12px;
  line-height: 40px;
  text-align: center;
  margin-top: 30px;
  position: absolute;
  right: 20px;
  bottom: 20px;
  transition: all 0.3s ease;
}
.btn:hover {
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
