<template>
  <div class="page">
    <div class="title">回饋填寫</div>
    <div class="write-content">
      <div class="sec-title">評分：</div>
      <div class="stars-frame">
        <div v-for="i in 5" :key="i">
          <i
            class="fa-solid fa-star"
            @mouseenter="HandleStarTouch(i)"
            @mouseleave="HandleStarLeave()"
            @click="ClickStart(i)"
            :class="{ starTouch: starTouch[i - 1] }"
          ></i>
        </div>
      </div>
    </div>
    <div class="write-content">
      <div class="sec-title">寫下你的評論吧!</div>
      <textarea type="text" v-model.trim="reviewContent"></textarea>
    </div>
    <div class="btn-frame">
      <div class="cancel-btn" @click="showWriteWebReview = false">取消</div>
      <div class="submit-btn" @click="ClickSend">提交</div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

import { errorUiStore } from "@/store/error";
import { reviewUiStore } from "@/store/review";

export const showWriteWebReview = ref(false);

export default {
  setup() {
    const starTouch = ref(Array(5).fill(false));
    const starClick = ref(0);
    const reviewContent = ref("");
    const reviewDate = ref("");

    const errorStore = errorUiStore();
    const reviewStore = reviewUiStore();

    const HandleStarTouch = (index) => {
      for (let i = 0; i < 5; i++) {
        starTouch.value[i] = i < index;
      }
    };

    const HandleStarLeave = () => {
      for (let i = 0; i < 5; i++) {
        starTouch.value[i] = i < starClick.value;
      }
    };

    const ClickStart = (index) => {
      starClick.value = index;

      for (let i = 0; i < 5; i++) {
        starTouch.value[i] = i < index;
      }
    };

    const ClickSend = async () => {
      ExamInput();

      if (!errorStore.errorType) {
        const userEmail = localStorage.getItem("userEmail");
        const userName = localStorage.getItem("userName");

        CreateDate();

        await reviewStore.SendReview({
          email: userEmail,
          name: userName,
          content: reviewContent.value,
          star: starClick.value,
          date: reviewDate.value,
          image: "/img/user.jpg",
        });

        showWriteWebReview.value = false;

        errorStore.LoadSuccess("留言成功!");

        await errorStore.CloseLoadEle();
        window.location.reload();
      }

      errorStore.CloseEle();
    };

    const CreateDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");

      reviewDate.value = year + "-" + month + "-" + day;
    };

    const ExamInput = () => {
      if (starClick.value === 0) {
        errorStore.SetError("請選擇星星數!");
      } else if (reviewContent.value === "") {
        errorStore.SetError("請輸入回饋內容!");
      } else {
        errorStore.errorType = false;
        errorStore.showErrorMsg = false;
      }
    };

    return {
      showWriteWebReview,
      starTouch,
      starClick,
      reviewContent,
      reviewDate,
      HandleStarTouch,
      HandleStarLeave,
      ClickStart,
      ClickSend,
      CreateDate,
      ExamInput,
    };
  },
};
</script>

<style scoped>
.page {
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
.write-content {
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
.stars-frame {
  display: flex;
  justify-content: center;
  align-items: start;
}
.stars-frame i {
  color: #ffea9d;
  font-size: 28px;
  margin: 10px 10px;
  transition: all 0.3s ease;
}
.stars-frame i:hover {
  color: #f0c42d;
  cursor: pointer;
  transform: scale(1.2);
}
.stars-frame i.starTouch {
  color: #f0c42d;
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
.submit-btn:hover,
.cancel-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.cancel-btn:hover {
  border: 1px solid #849c7d;
}
</style>
