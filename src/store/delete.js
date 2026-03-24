import { defineStore } from "pinia";

import { errorUiStore } from "./error";
import { loginUiStore } from "./login";
import { reviewUiStore } from "./review";
import { contactUiStore } from "./contact";
import { finishUiStore } from "./finish";
import { clothUiStore } from "./cloth";

export const deleteUiStore = defineStore("delete", {
  state: () => ({
    showCheck: false,
    type: null,
    deleteData: null,
  }),
  actions: {
    open(type, id) {
      this.showCheck = true;
      this.type = type;
      this.deleteData = id;
    },
    cancel() {
      this.showCheck = false;
      this.type = null;
      this.deleteData = null;
    },
    async sendDelete() {
      const errorStore = errorUiStore();
      const loginStore = loginUiStore();
      const reviewStore = reviewUiStore();
      const contactStore = contactUiStore();
      const finishStore = finishUiStore();
      const clothStore = clothUiStore();

      if (this.type === "review") {
        await reviewStore.DeleteReview(this.deleteData);
      } else if (this.type === "contact") {
        await contactStore.DeleteContact(this.deleteData);
      } else if (this.type === "user") {
        await loginStore.removeUser(this.deleteData);
      } else if (this.type === "finish") {
        await finishStore.DeleteFinish(this.deleteData);
      } else if (this.type === "cloth") {
        await clothStore.DeleteCloth(this.deleteData);
      }

      this.cancel();

      errorStore.LoadSuccess("成功刪除!");

      await errorStore.CloseLoadEle();
      window.location.reload();
    },
  },
});
