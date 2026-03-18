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
        const response = await axios.post("/api/login", userData);
        const data = response.data;

        this.token = data.token;
        this.isAuthenticated = true;

        localStorage.setItem("token", this.token);

        return response;
      } catch (error) {
        const msg = error.response?.data?.message || "登入失敗!";

        throw new Error(msg);
      }
    },
    async signup(userData) {
      try {
        const response = await axios.post("/api/signup", userData);

        return response;
      } catch (error) {
        const msg = error.response?.data?.message || "註冊失敗!";

        throw new Error(msg);
      }
    },
    async logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;

      localStorage.removeItem("token");
    },
    async getUserInfo() {
      const response = await axios.get("/api/get-user-info");
      const data = response.data;

      return data.data;
    },
  },
});
