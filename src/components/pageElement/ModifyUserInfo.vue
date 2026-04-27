<template>
  <div class="ele">
    <div class="title">更改資料</div>
    <div class="modify-outframe">
      <div class="modify-frame">
        <div class="sec-title">原始</div>
        <div class="original-info">{{ modifyData }}</div>
      </div>
      <div class="modify-frame">
        <div class="sec-title">修改後</div>
        <input type="text" v-model.trim="inputData" />
      </div>
    </div>
    <div class="btn" @click="ClickModify">確認送出</div>
  </div>
</template>

<script>
import { ref, watch } from "vue";

import { errorUiStore } from "@/store/error";
import { modifyUiStore } from "@/store/modify";
import { loginUiStore } from "@/store/login";

export default {
  setup() {
    const modifyData = ref("");
    const modifyType = ref("");
    const inputData = ref("");
    const userId = ref("");

    const errorStore = errorUiStore();
    const modifyStore = modifyUiStore();
    const loginStore = loginUiStore();

    const ClickModify = async () => {
      if (inputData.value === "") {
        errorStore.SetError("資料未修改!");
        errorStore.CloseEle();
      } else {
        await FindUserId();

        await modifyStore.ModifyUserRole({
          id: userId.value,
          [modifyType.value]: inputData.value,
        });

        modifyStore.showModifyEle = false;

        errorStore.LoadSuccess("資料修改成功!");

        await errorStore.CloseLoadEle();
        window.location.reload();
      }
    };

    const FindUserId = async () => {
      const data = await loginStore.getUserInfo();

      const userEmail = localStorage.getItem("userEmail");

      userId.value = data.find((item) => {
        return item.email === userEmail;
      }).id;
    };

    watch(
      () => [modifyStore.modifyType, modifyStore.modifyData],
      ([newType, newData]) => {
        modifyType.value = newType;
        modifyData.value = newData;
      }
    );

    return {
      modifyType,
      modifyData,
      inputData,
      userId,
      ClickModify,
      FindUserId,
    };
  },
};
</script>

<style scoped>
.ele {
  width: 65%;
  background-color: #ffffff;
  border-radius: 20px;
  border: 1px solid #3b5131;
  margin-bottom: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.modify-outframe {
  width: 90%;
  display: grid;
  grid-template-columns: repeat(2, calc(50% - 20px));
  gap: 40px;
}
.modify-frame {
  width: 100%;
}
.sec-title {
  font-size: 22px;
  text-align: start;
  margin: 5px 0;
}
.original-info,
input {
  width: 100%;
  height: 30px;
  font-size: 20px;
  font-family: "Brush Script MT", cursive;
  border: 1px solid #ffffff;
  border-bottom: 1px solid #849c7d;
  text-align: center;
}
input:focus {
  outline: none;
  border-bottom: 2px solid #3b5131;
}
.btn {
  width: 120px;
  height: 40px;
  color: #ffffff;
  font-size: 20px;
  text-align: center;
  line-height: 40px;
  background-color: #849c7d;
  border-radius: 20px;
  margin-top: 40px;
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
</style>
