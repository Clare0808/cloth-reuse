<template>
  <div class="back-ele">
    <div class="cloth-box-outframe">
      <div
        class="cloth-box-frame"
        v-for="(cloth, index) in dataList"
        :key="index"
      >
        <div class="cloth-box">
          <img :src="cloth.image" />
          <div class="info-frame">
            <div class="text-outframe">
              <div class="text-frame">
                <div class="cloth-info">{{ cloth.name }}</div>
                <div class="cloth-info">{{ cloth.pName }}</div>
                <div class="cloth-info">{{ cloth.email }}</div>
              </div>
              <div class="text-sec-frame">
                <div class="cloth-info"></div>
                <div class="cloth-info">{{ cloth.place }}</div>
                <div class="cloth-info">{{ cloth.time }}</div>
              </div>
              <div class="text-sec-frame">
                <div class="cloth-info"></div>
                <div class="cloth-info">類型: {{ cloth.category }}</div>
                <div class="cloth-info">尺寸: {{ cloth.size }}</div>
              </div>
            </div>
            <div class="btn-frame">
              <i
                class="fa-solid fa-lock"
                :class="{ lock: cloth.lock, unlock: !cloth.lock }"
                @click="ClickLock(cloth)"
              ></i>
              <i class="fa-solid fa-pencil" @click="ClickModify(cloth)"></i>
              <i class="fa-solid fa-trash-can" @click="ClickDelete(cloth)"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="add-btn" @click="clothStore.showElePage = true">
        新增服飾 +
      </div>
    </div>

    <div
      class="overlay"
      v-show="clothStore.showElePage"
      @click="clothStore.showElePage = false"
    ></div>
    <transition name="slide-ele">
      <UploadCloth class="ele-page" v-show="clothStore.showElePage" />
    </transition>

    <div
      class="overlay"
      v-show="clothStore.showModifyPage"
      @click="clothStore.showModifyPage = false"
    ></div>
    <transition name="slide-ele">
      <ModifyCloth class="ele-page" v-show="clothStore.showModifyPage" />
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { deleteUiStore } from "@/store/delete";
import { clothUiStore } from "@/store/cloth";
import { errorUiStore } from "@/store/error";

import UploadCloth from "../pageElement/UploadCloth.vue";
import ModifyCloth from "../pageElement/ModifyCloth.vue";

import OptionsDataRaw from "@/assets/data/optionsData.json";

export default {
  name: "BackClothPage",
  components: {
    UploadCloth,
    ModifyCloth,
  },
  setup() {
    const dataList = ref([]);

    const deleteStore = deleteUiStore();
    const clothStore = clothUiStore();
    const errorStore = errorUiStore();

    const OptionsData = ref(OptionsDataRaw);

    const GetDishData = async () => {
      const response = await fetch("/data/clothData.json");
      const data = await response.json();

      dataList.value = data;

      dataList.value.forEach((item) => {
        const type = OptionsData.value.find((op) => op.label === item.category);

        item.category = type.name;
      });
    };

    const ClickDelete = async (data) => {
      deleteStore.open("cloth", data.id);
    };

    const ClickModify = (data) => {
      clothStore.modifyList = data;
      clothStore.showModifyPage = true;
    };

    const ClickLock = async (data) => {
      await clothStore.ModifyCloth({
        id: data.id,
        lock: !data.lock,
      });

      clothStore.showModifyPage = false;

      errorStore.LoadSuccess("修改成功!");
    };

    onMounted(async () => {
      await GetDishData();
    });

    return {
      dataList,
      clothStore,
      OptionsData,
      GetDishData,
      ClickDelete,
      ClickModify,
      ClickLock,
    };
  },
};
</script>

<style scoped>
.back-ele {
  width: calc(100% - 290px);
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
}
.cloth-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.cloth-box-frame {
  width: 100%;
}
.cloth-box {
  width: 100%;
  margin: 20px 0;
  display: grid;
  grid-template-columns: 12% 88%;
  justify-content: center;
  align-items: center;
}
img {
  width: 100px;
  height: 100px;
}
.info-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-outframe {
  width: 100%;
  font-size: 20px;
  text-align: start;
  margin: 0 20px;
  border-right: 1px solid #3b5131;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.text-frame,
.text-sec-frame {
  width: 100%;
  margin-bottom: 10px;
  text-align: left;
  display: grid;
  grid-template-columns: 30% 30% 35%;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
.text-sec-frame {
  color: #4f4f4f;
  font-size: 16px;
}
.cloth-sec-info {
  font-size: 18px;
}
.btn-frame {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
i {
  color: #3b5131;
  margin: 10px 0;
}
i:hover {
  color: #849c7d;
  cursor: pointer;
}
.unlock {
  color: #d3dcba;
}
.unlock:hover {
  color: #3b5131;
}
.lock {
  color: #3b5131;
}
.add-btn {
  color: #3b5131;
  font-size: 24px;
  margin: 20px;
}
.add-btn:hover {
  color: #849c7d;
  cursor: pointer;
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
