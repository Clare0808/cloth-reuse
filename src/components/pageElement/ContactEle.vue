<template>
  <div class="ele">
    <div class="title">聯絡客服</div>
    <div class="contact-content">
      <div class="sec-title">有任何問題請聯絡客服中心!</div>
      <textarea type="text" v-model.trim="content"></textarea>
    </div>
    <div class="btn-frame">
      <div class="cancel-btn" @click="contactStore.showElePage = false">
        取消
      </div>
      <div class="submit-btn" @click="SendContent">提交</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { errorUiStore } from "@/store/error";
import { contactUiStore } from "@/store/contact";

export default {
  setup() {
    const content = ref("");
    const userMail = ref("");
    const userName = ref("");
    const contentDate = ref("");

    const errorStore = errorUiStore();
    const contactStore = contactUiStore();

    const SendContent = async () => {
      const userEmail = localStorage.getItem("userEmail");
      const userName = localStorage.getItem("userName");

      CreateDate();

      await contactStore.SendContact({
        email: userEmail,
        name: userName,
        content: content.value,
        time: contentDate.value,
      });

      contactStore.showElePage = false;

      errorStore.LoadSuccess("成功送出線上客服表單!");

      await errorStore.CloseLoadEle();
      window.location.reload();
    };

    const CreateDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");

      contentDate.value = year + "-" + month + "-" + day;
    };

    onMounted(async () => {
      content.value = "";
    });

    return {
      content,
      userMail,
      userName,
      contentDate,
      contactStore,
      SendContent,
      CreateDate,
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
.contact-content {
  width: 100%;
  margin: 10px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.sec-title {
  font-size: 22px;
}
textarea {
  width: calc(100% - 20px);
  font-size: 20px;
  font-family: "Pacifico", cursive;
  margin-top: 10px;
  height: 150px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #adadad;
}
textarea:focus {
  outline: none;
  border: 1px solid #849c7d;
}
.btn-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.submit-btn,
.cancel-btn {
  width: 150px;
  height: 40px;
  font-size: 20px;
  border-radius: 20px;
  line-height: 40px;
  text-align: center;
  margin: 20px 20px 0px 20px;
  transition: all 0.3s ease;
}
.submit-btn {
  color: #ffffff;
  background-color: #849c7d;
}
.cancel-btn {
  background-color: #ffffff;
  border: 1px solid #3b5131;
}
.submit-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.cancel-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  border: 1px solid #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}

@media (max-width: 540px) {
  .title {
    font-size: 30px;
  }
  .submit-btn,
  .cancel-btn {
    width: 100px;
    height: 30px;
    font-size: 16px;
    line-height: 30px;
  }
}
</style>
