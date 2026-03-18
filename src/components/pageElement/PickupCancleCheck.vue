<template>
  <div class="check-ele">
    <div class="title">是否要取消取衣申請?</div>
    <div class="btn-frame">
      <div class="no-btn" @click="pickupStore.showElePage = false">取消</div>
      <div class="yes-btn" @click="ClickYes">確定</div>
    </div>
  </div>
</template>

<script>
import { errorUiStore } from "@/store/error";
import { pickupUiStore } from "@/store/pickup";

import { showLogoutCheck } from "@/App.vue";

export default {
  setup() {
    const errorStore = errorUiStore();
    const pickupStore = pickupUiStore();

    const ClickYes = async (data) => {
      await pickupStore.DeletePickup(data);

      pickupStore.showElePage = false;

      errorStore.LoadSuccess("成功取消申請!");

      await errorStore.CloseLoadEle();
      window.location.reload();
    };
    return {
      showLogoutCheck,
      pickupStore,
      ClickYes,
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
