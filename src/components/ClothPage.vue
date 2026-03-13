<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showText">服飾專區</div>
    </transition>
    <div class="container">
      <transition name="slide">
        <div class="options-frame" v-if="showElement">
          <div v-for="(opt, index) in OptionsData" :key="index">
            <div
              class="option"
              @click="ClickOption(opt)"
              :class="{ active: opt.click }"
            >
              {{ opt.name }}
            </div>
          </div>
        </div>
      </transition>
      <transition name="slide">
        <div class="cloth-box-frame" v-if="showElement">
          <div
            class="cloth-frame"
            v-for="(cloth, index) in filteredList"
            :key="index"
            @click="ClickCloth(cloth)"
          >
            <img :src="cloth.image" />
            <div class="cloth-info-frame">
              <div class="cloth-name">{{ cloth.name }}</div>
              <div class="cloth-size">{{ cloth.size }}</div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>

  <div class="overlay" v-show="showElePage" @click="showElePage = false"></div>
  <transition name="slide-ele">
    <CheckClothInfo class="ele-page" v-show="showElePage" />
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";

import OptionsDataRaw from "@/assets/data/optionsData.json";

import CheckClothInfo from "./pageElement/CheckClothInfo.vue";

export const selectedCloth = ref({});
export const showElePage = ref(false);

export default {
  name: "ClothPage",
  components: {
    CheckClothInfo,
  },
  setup() {
    const showText = ref(false);
    const showElement = ref(false);
    const dataList = ref([]);
    const filteredList = ref([]);

    const OptionsData = ref(OptionsDataRaw); // 修正成 reactive 狀態

    const GetDishData = async () => {
      const response = await fetch("/data/clothData.json");
      const data = await response.json();

      dataList.value = data;
    };

    const ClickOption = (opt) => {
      filteredList.value = dataList.value.filter((data) => {
        return data.category === opt.label;
      });

      opt.click = true;

      OptionsData.value.forEach((data) => {
        if (data.label !== opt.label) {
          data.click = false;
        }
      });

      if (opt.label === "all") {
        filteredList.value = dataList.value;
        opt.click = true;

        OptionsData.value.forEach((data) => {
          if (data.label !== "all") {
            data.click = false;
          }
        });
      }
    };

    const ClickCloth = (cloth) => {
      selectedCloth.value = cloth;
      showElePage.value = true;
    };

    onMounted(async () => {
      showText.value = true;
      showElement.value = true;

      await GetDishData();

      filteredList.value = dataList.value;

      OptionsData.value.forEach((data) => {
        if (data.label === "all") {
          data.click = true;
        }
      });
    });

    return {
      showElePage,
      showText,
      showElement,
      dataList,
      filteredList,
      OptionsData,
      GetDishData,
      ClickOption,
      ClickCloth,
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
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.options-frame {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.option {
  width: 80px;
  color: #3b5131;
  font-size: 20px;
  background-color: #ffffff;
  border: 1px solid #849c7d;
  border-radius: 20px;
  margin: 10px;
  padding: 10px;
  transition: all 0.3s ease;
}
.option:hover {
  color: #ffffff;
  background-color: #849c7d;
  cursor: pointer;
}
.active {
  color: #ffffff;
  background-color: #849c7d;
}
.cloth-box-frame {
  width: 90%;
  display: grid;
  grid-template-columns: repeat(3, 30%);
  grid-template-rows: auto;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.cloth-box-frame img {
  width: 300px;
  height: 300px;
}
.cloth-frame {
  width: 300px;
  background-color: #ffffff;
  border: 1px solid #849c7d;
  border-radius: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}
.cloth-frame:hover {
  cursor: pointer;
  transform: scale(1.05);
}
.cloth-frame img {
  width: 250px;
}
.cloth-info-frame {
  width: 95%;
  font-size: 24px;
  margin-top: 10px;
  padding-top: 15px;
  border-top: 1px solid #849c7d;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.cloth-size {
  color: #849c7d;
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
