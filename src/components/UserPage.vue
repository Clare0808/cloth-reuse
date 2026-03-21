<template>
  <div class="page">
    <transition name="fade">
      <div class="title" v-if="showFade">使用者中心</div>
    </transition>
    <transition name="slide">
      <div class="info-frame" v-if="showSlide">
        <div class="text-frame">
          <div class="func-outframe">
            <div class="user-info-frame">
              <div class="img-frame">
                <img src="../assets/img/user.jpg" />
                <i class="fa-solid fa-pencil" id="pencil"></i>
              </div>
              <div class="user-info">
                {{ userName }} 您好!
                <i class="fa-solid fa-pencil" @click="ClickModify()"></i>
              </div>
              <div class="user-info">
                {{ userPhone }}
                <i class="fa-solid fa-pencil" @click="ClickModify()"></i>
              </div>
              <div class="btn" @click="ClickBack">進入後台</div>
            </div>
            <div class="func-frame">
              <div class="sec-title">取衣紀錄</div>
              <div class="no-item" v-if="showNone">這裡是空的!</div>
              <div class="order-outframe">
                <div v-for="(finish, index) in dataList" :key="index">
                  <div class="order-frame">
                    <div class="cloth-info">
                      <div class="cloth-info">{{ finish.code }}</div>
                      <div class="cloth-info">{{ finish.name }}</div>
                    </div>
                    <div class="cloth-date">{{ finish.time }}</div>
                    <div class="cloth-info">
                      <div class="cloth-info">{{ finish.type }}</div>
                      <div class="cloth-info">尺寸: {{ finish.size }}</div>
                      <div class="cloth-info">提供者: {{ finish.pName }}</div>
                      <div class="cloth-info">{{ finish.place }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { useRouter } from "vue-router";

import { loginUiStore } from "@/store/login";
import { finishUiStore } from "@/store/finish";

export default {
  name: "UserPage",
  setup() {
    const showFade = ref(false);
    const showSlide = ref(false);
    const userName = ref("");
    const userPhone = ref("");
    const dataList = ref([]);
    const showNone = ref(false);

    const router = useRouter();

    const loginStore = loginUiStore();
    const finishStore = finishUiStore();

    const GetUserInfo = async () => {
      userName.value = localStorage.getItem("userName");

      const data = await loginStore.getUserInfo();

      const filteredData = data.find((item) => {
        return item.name === userName.value;
      });

      userPhone.value = filteredData.phone;
    };

    const ClickBack = () => {
      router.push("/back-home");
    };

    onMounted(async () => {
      showFade.value = true;
      showSlide.value = true;

      await GetUserInfo();

      dataList.value = await finishStore.GetFinishData();

      if (dataList.value.length === 0) {
        showNone.value = true;
      }
    });

    return {
      showFade,
      showSlide,
      userName,
      userPhone,
      dataList,
      showNone,
      GetUserInfo,
      ClickBack,
    };
  },
};
</script>

<style scoped>
.page {
  height: 80vh;
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
.info-frame {
  width: 80%;
  text-align: start;
  display: flex;
  justify-content: center;
  align-items: center;
}
.img-frame {
  position: relative;
}
img {
  width: 200px;
  height: 200px;
  border-bottom: 1px solid #3b5131;
  margin-bottom: 10px;
  padding-bottom: 10px;
}
#pencil {
  width: 30px;
  height: 30px;
  color: #3b5131;
  font-size: 16px;
  background-color: #ffffff;
  border-radius: 50%;
  text-align: center;
  line-height: 30px;
  position: absolute;
  bottom: 50px;
  right: 10px;
}
#pencil:hover {
  color: #ffffff;
  background-color: #849c7d;
  cursor: pointer;
}
.user-info-frame {
  font-size: 22px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.user-info {
  width: 100%;
  margin: 10px 0;
  text-align: center;
}
.user-info i {
  color: #3b5131;
  font-size: 18px;
  margin-left: 20px;
}
.user-info i:hover {
  color: #849c7d;
  cursor: pointer;
}
.btn {
  width: 150px;
  height: 40px;
  color: #ffffff;
  background-color: #849c7d;
  font-size: 20px;
  border-radius: 20px;
  line-height: 40px;
  text-align: center;
  margin-top: 10px;
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.text-frame {
  width: 100%;
  background-color: #ffffff;
  border: 2px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.func-outframe {
  width: 100%;
  display: grid;
  grid-template-columns: 30% 70%;
  gap: 20px;
  justify-content: center;
  align-items: start;
}
.sec-title {
  color: #3b5131;
  font-size: 22px;
  margin-bottom: 10px;
}
.no-item {
  color: #adadad;
  font-size: 26px;
  text-align: center;
  margin-top: 30px;
}
.order-outframe {
  max-height: 370px;
  overflow-y: auto;
}
.order-frame {
  margin-top: 10px;
  padding: 10px;
}
.cloth-date {
  color: #9d9d9d;
}
.cloth-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 1;
}
.modify-page {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
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
