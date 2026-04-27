<template>
  <div class="modify-user">
    <div class="title">修改身份</div>
    <div class="modify-box">
      <div class="info-box">
        <div class="sec-title">用戶名稱</div>
        <div class="user-info">{{ modifyUser.name }}</div>
      </div>
      <div class="info-box-role">
        <div class="sec-title">身份選擇</div>
        <div class="selector" @click="showOption = !showOption">
          {{ selectedOption }}
        </div>
        <div class="role-select" v-show="showOption">
          <div class="role-option" @click="ClickOption('admin')">管理者</div>
          <div class="role-option" @click="ClickOption('user')">使用者</div>
        </div>
      </div>
    </div>
    <div class="btn-frame">
      <div class="no-btn" @click="ClickCancel">取消</div>
      <div class="yes-btn" @click="HandleModify">確定</div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";

import { errorUiStore } from "@/store/error";
import { modifyUiStore } from "@/store/modify";

export default {
  setup() {
    const showOption = ref(false);
    const selectedOption = ref("");
    const modifyUser = ref({});

    const errorStore = errorUiStore();
    const modifyStore = modifyUiStore();

    const HandleModify = async () => {
      let roleType = selectedOption.value;

      if (roleType === modifyUser.value.role) {
        errorStore.SetError("資料未修改!");
        errorStore.CloseEle();
      } else {
        if (roleType === "管理者") {
          roleType = "admin";
        } else if (roleType === "使用者") {
          roleType = "user";
        }

        await modifyStore.ModifyUserRole({
          id: modifyUser.value.id,
          role: roleType,
        });

        modifyStore.showBackEle = false;

        errorStore.LoadSuccess("資料修改成功!");

        await errorStore.CloseLoadEle();
        window.location.reload();
      }
    };

    const ClickOption = (role) => {
      if (role === "admin") {
        selectedOption.value = "管理者";
      } else if (role === "user") {
        selectedOption.value = "使用者";
      }

      showOption.value = false;

      const roleEle = document.querySelector(".selector");
      roleEle.style.backgroundColor = "#849c7d";
      roleEle.style.color = "#ffffff";
      roleEle.style.border = "1px solid #849c7d";
    };

    const ClickCancel = () => {
      modifyStore.showBackEle = false;
    };

    watch(
      () => modifyStore.backDataList,
      (newVal) => {
        modifyUser.value = newVal;
        selectedOption.value = newVal.role;
      }
    );

    return {
      showOption,
      selectedOption,
      modifyUser,
      HandleModify,
      ClickOption,
      ClickCancel,
    };
  },
};
</script>

<style scoped>
.modify-user {
  width: 65%;
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.modify-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.info-box,
.info-box-role {
  width: 95%;
  font-size: 20px;
  margin: 20px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.info-box-role {
  position: relative;
}
.selector {
  width: 120px;
  height: 40px;
  font-size: 18px;
  font-family: "Brush Script MT", cursive;
  border: 1px solid #3b5131;
  border-radius: 20px;
  line-height: 40px;
  text-align: center;
}
.selector:hover {
  cursor: pointer;
}
.role-select {
  width: 120px;
  border: 1px solid #3b5131;
  border-top: none;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  padding-top: 10px;
  position: absolute;
  top: 65px;
  right: calc(0% - 60px);
  transform: translate(-50%, -50%);
}
.role-option {
  font-size: 18px;
  margin: 5px 0;
}
.role-option:hover {
  color: #ffffff;
  background-color: #849c7d;
  border-radius: 20px;
  cursor: pointer;
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
