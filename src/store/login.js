import { defineStore } from "pinia";
import axios from "axios";

export const loginUiStore = defineStore("login", {
  state: () => ({
    user: null,
    token: localStorage.getItem("token") || null, // 刷新頁面仍保持登入狀態
    isAuthenticated: !!localStorage.getItem("token"), // 轉化成布林值
  }),
  actions: {
    async login(userData) {
      try {
        const response = await axios.get("/api/login");
        const data = response.data;

        this.user = data.data.filter((item) => {
          return item.email === userData.email;
        });

        this.isAuthenticated = true;
      } catch (error) {
        const msg = error.response?.message || "登入失敗!";

        throw new Error(msg);
      }
    },
    async signup(userData) {
      try {
        const response = await axios.post("/api/signup", userData);
        const data = response.data;

        this.user = data.data;
      } catch (error) {
        const msg = error.response?.message || "註冊失敗!";

        throw new Error(msg);
      }
    },
  },
});
