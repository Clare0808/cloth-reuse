<template>
  <div class="page">
    <transition name="slide">
      <div class="func-box" v-if="showLogin">
        <div class="title">登入</div>
        <div class="input-frame">
          <div class="sec-title">E-mail</div>
          <input type="text" v-model.trim="email" />
        </div>
        <div class="input-frame">
          <div class="sec-title">密碼</div>
          <input type="password" v-model.trim="password" />
        </div>
        <div class="btn-frame">
          <div class="local-btn-frame">
            <div class="sign-up-btn" @click="ClickChangeType()">註冊</div>
            <div class="login-btn" @click="ClickLogin()">登入</div>
          </div>
          <div class="text">or</div>
          <div class="google-btn">
            以 <img src="@/assets/img/google.png" /><span class="google"
              >Google</span
            >
            帳號登入
          </div>
        </div>
      </div>
    </transition>
    <transition name="slide">
      <div class="func-box" v-if="showSignUp">
        <div class="title">註冊</div>
        <div class="input-frame">
          <div class="sec-title">E-mail</div>
          <input type="text" v-model.trim="email" />
        </div>
        <div class="input-frame-mix">
          <div class="input-frame">
            <div class="sec-title">名稱</div>
            <input type="text" v-model.trim="name" />
          </div>
          <div class="input-frame">
            <div class="sec-title">電話號碼</div>
            <input type="text" v-model.trim="phone" />
          </div>
        </div>
        <div class="input-frame">
          <div class="sec-title">密碼</div>
          <input type="password" v-model.trim="password" />
        </div>
        <div class="input-frame">
          <div class="sec-title">確認密碼</div>
          <input type="password" v-model.trim="conPassword" />
        </div>
        <div class="btn-frame">
          <div class="local-btn-frame">
            <div class="sign-up-btn" @click="ClickChangeType()">登入</div>
            <div class="login-btn" @click="ClickSignUp()">註冊</div>
          </div>
          <div class="text">or</div>
          <div class="google-btn">
            以 <img src="@/assets/img/google.png" /><span class="google"
              >Google</span
            >
            帳號登入
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
import { errorUiStore } from "@/store/error";

export default {
  name: "LoginPage",
  setup() {
    const showLogin = ref(false);
    const showSignUp = ref(false);

    const email = ref("");
    const name = ref("");
    const phone = ref("");
    const password = ref("");
    const conPassword = ref("");
    const userName = ref("");

    const router = useRouter();

    const loginStore = loginUiStore();
    const errorStore = errorUiStore();

    const ClickChangeType = () => {
      showLogin.value = !showLogin.value;
      showSignUp.value = !showSignUp.value;

      CleanInput();
    };

    const ClickLogin = async () => {
      ExamInputFrame();

      if (!errorStore.errorType) {
        try {
          if (!errorStore.errorType) {
            await loginStore.login({
              email: email.value,
              password: password.value,
            });

            if (loginStore.isAuthenticated) {
              errorStore.LoadSuccess("登入成功!");

              await GetUserInfo();

              localStorage.setItem("userEmail", email.value);
              localStorage.setItem("userName", userName.value);
              localStorage.setItem("inAdmin", loginStore.isAdmin);

              CleanInput();

              await errorStore.CloseLoadEle();
              router.push("/");
            }
          }
        } catch (err) {
          errorStore.SetError(err.message);
        }
      }

      errorStore.CloseEle();
    };

    const ClickSignUp = async () => {
      ExamInputFrame();

      if (!errorStore.errorType) {
        try {
          if (!errorStore.errorType) {
            await loginStore.signup({
              email: email.value,
              name: name.value,
              phone: phone.value,
              password: password.value,
            });

            errorStore.SetSuccess("註冊成功!");

            CleanInput();

            setTimeout(() => {
              ClickChangeType();
            }, 2000);
          }
        } catch (err) {
          errorStore.SetError(err.message);
        }
      }

      errorStore.CloseEle();
    };

    const CleanInput = () => {
      email.value = "";
      name.value = "";
      phone.value = "";
      password.value = "";
      conPassword.value = "";
    };

    const ExamInputFrame = () => {
      if (email.value === "") {
        errorStore.SetError("請輸入E-mail!");
      } else if (name.value === "" && showSignUp.value) {
        errorStore.SetError("請輸入名稱!");
      } else if (phone.value === "" && showSignUp.value) {
        errorStore.SetError("請輸入電話號碼!");
      } else if (password.value === "") {
        errorStore.SetError("請輸入密碼!");
      } else if (conPassword.value === "" && showSignUp.value) {
        errorStore.SetError("請再次輸入密碼!");
      } else if (password.value !== conPassword.value && showSignUp.value) {
        errorStore.SetError("密碼與確認密碼不相符!");
      } else {
        errorStore.errorType = false;
        errorStore.showErrorMsg = false;
      }
    };

    const GetUserInfo = async () => {
      const data = await loginStore.getUserInfo();

      userName.value = data.find((item) => {
        return item.email === email.value;
      }).name;
    };

    onMounted(() => {
      showLogin.value = true;
    });

    return {
      showLogin,
      showSignUp,
      email,
      name,
      phone,
      password,
      conPassword,
      ClickChangeType,
      ClickLogin,
      ClickSignUp,
      CleanInput,
      ExamInputFrame,
      GetUserInfo,
    };
  },
};
</script>

<style scoped>
.page {
  height: 79vh;
  overflow: hidden;
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
  margin-bottom: 20px;
}
.func-box {
  width: 40%;
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 0;
  transform: translate(-50%, -50%);
}
.input-frame {
  width: 100%;
  margin: 10px 0;
}
.input-frame-mix {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, calc(50% - 10px));
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.sec-title {
  font-size: 22px;
  text-align: start;
  margin: 5px 0;
}
input {
  width: 100%;
  height: 20px;
  font-size: 16px;
  font-family: "Pacifico", cursive;
  border: 1px solid #ffffff;
  border-bottom: 1px solid #3b5131;
}
input:focus {
  outline: none;
  border-bottom: 2px solid #3b5131;
}
.local-btn-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.sign-up-btn,
.login-btn {
  width: 100px;
  height: 40px;
  font-size: 20px;
  text-align: center;
  line-height: 40px;
  border-radius: 20px;
  margin: 0px 20px;
  margin-top: 10px;
  transition: all 0.3s ease;
}
.sign-up-btn {
  color: #3b5131;
  background-color: #ffffff;
  border: 1px solid #849c7d;
}
.sign-up-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  border: 1px solid #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.login-btn {
  color: #ffffff;
  background-color: #849c7d;
}
.login-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.text {
  color: #d0d0d0;
  font-size: 18px;
  margin: 10px 0;
}
.google-btn {
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.google-btn img {
  width: 25px;
  height: 25px;
  margin-left: 5px;
}
.google {
  font-family: "Segoe UI", Arial;
  margin: 0 5px;
}
.google-btn:hover {
  cursor: pointer;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 1s ease;
}
.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translate(-50%, -50%) translateY(20px);
}
.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translate(-50%, -50%) translateY(0);
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
</style>
