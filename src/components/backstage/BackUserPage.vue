<template>
  <div class="back-ele">
    <div class="user-box-outframe">
      <div
        class="user-box-frame"
        v-for="(user, index) in userData"
        :key="index"
      >
        <div class="user-box">
          <div class="text-outframe">
            <div class="text-frame">
              <div class="user-info">{{ user.name }}</div>
              <div class="user-info">{{ user.email }}</div>
              <div class="user-info">{{ user.phone }}</div>
              <div class="user-info">{{ user.role }}</div>
            </div>
          </div>
          <div class="btn-frame">
            <i class="fa-solid fa-pencil" @click="ClickModify(user)"></i>
            <i class="fa-solid fa-trash-can" @click="ClickDelete(user)"></i>
          </div>
        </div>
      </div>
    </div>

    <div
      class="overlay"
      v-show="modifyStore.showBackEle"
      @click="modifyStore.showBackEle = false"
    ></div>
    <transition name="slide-ele">
      <ModifyUser class="ele-page" v-show="modifyStore.showBackEle" />
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { loginUiStore } from "@/store/login";
import { deleteUiStore } from "@/store/delete";
import { modifyUiStore } from "@/store/modify";

import ModifyUser from "../pageElement/ModifyUser.vue";

export default {
  name: "BackUserPage",
  components: {
    ModifyUser,
  },
  setup() {
    const userData = ref([]);

    const loginStore = loginUiStore();
    const deleteStore = deleteUiStore();
    const modifyStore = modifyUiStore();

    const GetData = async () => {
      userData.value = await loginStore.getUserInfo();

      userData.value.forEach((item) => {
        if (item.role === "user") {
          item.role = "使用者";
        } else if (item.role === "admin") {
          item.role = "管理者";
        }
      });
    };

    const ClickDelete = async (data) => {
      deleteStore.open("user", data.id);
    };

    const ClickModify = (data) => {
      modifyStore.showBackEle = true;
      modifyStore.backDataList = data;
    };

    onMounted(async () => {
      await GetData();
    });

    return {
      userData,
      modifyStore,
      GetData,
      ClickDelete,
      ClickModify,
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
.user-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.user-box-frame {
  width: 100%;
}
.user-box {
  width: 100%;
  margin: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-outframe {
  width: 100%;
  font-size: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.text-frame {
  width: 100%;
  font-size: 18px;
  margin-bottom: 10px;
  text-align: start;
  display: grid;
  grid-template-columns: 25% 40% 25% 10%;
  justify-content: center;
  align-items: center;
}
.user-info-box-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}
.user-info-box-frame {
  width: 98%;
}
.btn-frame {
  margin-left: 20px;
  border-left: 1px solid #3b5131;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.btn-frame i {
  color: #3b5131;
  margin: 10px 0;
}
.btn-frame i:hover {
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
