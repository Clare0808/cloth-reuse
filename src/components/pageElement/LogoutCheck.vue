<template>
  <div class="check-ele">
    <div class="title">是否確定登出?</div>
    <div class="btn-frame">
      <div class="no-btn" @click="showLogoutCheck = false">取消</div>
      <div class="yes-btn" @click="ClickLogout">確定</div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

import { loginUiStore } from "@/store/login";
import { errorUiStore } from "@/store/error";

import { showLogoutCheck } from "@/App.vue";

export default {
  setup() {
    const router = useRouter();
    const loginStore = loginUiStore();
    const errorStore = errorUiStore();

    const ClickLogout = async () => {
      errorStore.LoadSuccess("登出成功!");
      showLogoutCheck.value = false;

      loginStore.logout();

      await errorStore.CloseLoadEle();
      router.push("/login");
    };
    return {
      showLogoutCheck,
      ClickLogout,
    };
  },
};
</script>

<style scoped>
.check-ele {
  width: 65%;
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.title {
  font-size: 26px;
  margin-bottom: 10px;
}
.btn-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.no-btn,
.yes-btn {
  width: 150px;
  height: 40px;
  font-size: 20px;
  border-radius: 20px;
  line-height: 40px;
  text-align: center;
  margin: 20px 20px 0px 20px;
  transition: all 0.3s ease;
}
.no-btn {
  color: #3b5131;
  background-color: #ffffff;
  border: 1px solid #849c7d;
}
.no-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  border: 1px solid #3b5131;
  cursor: pointer;
}
.yes-btn {
  color: #ffffff;
  background-color: #849c7d;
}
.yes-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
}
</style>
