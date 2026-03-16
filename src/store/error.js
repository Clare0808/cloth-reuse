import { defineStore } from "pinia";
import { ref } from "vue";

export const errorUiStore = defineStore("error", () => {
  const errorText = ref("");
  const errorType = ref("");
  const showErrorMsg = ref(false);
  const showLoader = ref(false);

  const LoadSuccess = (msg) => {
    errorText.value = msg;
    errorType.value = false;

    showErrorMsg.value = true;
    showLoader.value = true;
  };

  const LoadError = (msg) => {
    errorText.value = msg;
    errorType.value = true;

    showErrorMsg.value = true;
    showLoader.value = true;
  };

  const CloseLoadEle = () => {
    return new Promise((resolve) => {
      setTimeout(() => {
        showErrorMsg.value = false;
        showLoader.value = false;

        resolve();
      }, 2000);
    });
  };

  const SetSuccess = (msg) => {
    errorText.value = msg;
    errorType.value = false;

    showErrorMsg.value = true;
  };

  const SetError = (msg) => {
    errorText.value = msg;
    errorType.value = true;

    showErrorMsg.value = true;
  };

  const CloseEle = () => {
    setTimeout(() => {
      showErrorMsg.value = false;
    }, 2000);
  };

  return {
    errorText,
    errorType,
    showErrorMsg,
    showLoader,
    LoadSuccess,
    LoadError,
    CloseLoadEle,
    SetSuccess,
    SetError,
    CloseEle,
  };
});
