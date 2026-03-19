<template>
  <div class="check-ele">
    <div class="title">是否確定完成取衣流程?</div>
    <div class="btn-frame">
      <div class="no-btn" @click="finishStore.showElePage = false">取消</div>
      <div class="yes-btn" @click="ClickYes">確定</div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

import { errorUiStore } from "@/store/error";
import { pickupUiStore } from "@/store/pickup";
import { finishUiStore } from "@/store/finish";

import { showLogoutCheck } from "@/App.vue";

export default {
  setup() {
    const codeData = ref("");
    const timeData = ref("");

    const errorStore = errorUiStore();
    const pickupStore = pickupUiStore();
    const finishStore = finishUiStore();

    const ClickYes = async () => {
      const userEmail = localStorage.getItem("userEmail");
      const userName = localStorage.getItem("userName");

      CreateDate();

      await finishStore.SendFinishData({
        rEmail: userEmail,
        rName: userName,
        name: finishStore.dataList.name,
        code: codeData.value,
        type: finishStore.dataList.type,
        size: finishStore.dataList.size,
        time: timeData.value,
        place: finishStore.dataList.place,
        pEmail: finishStore.dataList.pEmail,
        pName: finishStore.dataList.pName,
      });

      await pickupStore.DeletePickupNotRewrite(finishStore.dataList.name);

      finishStore.showElePage = false;

      errorStore.LoadSuccess("取衣完成!");

      await errorStore.CloseLoadEle();
      window.location.reload();
    };

    const CreateDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      const hour = String(date.getHours()).padStart(2, "0");
      const min = String(date.getMinutes()).padStart(2, "0");

      codeData.value = "CR" + String(year - 2000) + month + day + hour + min;
      timeData.value =
        String(year) + "-" + month + "-" + day + " " + hour + ":" + min;
    };

    return {
      showLogoutCheck,
      finishStore,
      codeData,
      timeData,
      ClickYes,
      CreateDate,
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
