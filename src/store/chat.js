import { defineStore } from "pinia";
import { ref } from "vue";

export const chatUiStore = defineStore("chat", () => {
  const showElePage = ref(false);
  const chatReceiver = ref("");
  const chatReceiverEmail = ref("");

  return {
    showElePage,
    chatReceiver,
    chatReceiverEmail,
  };
});
