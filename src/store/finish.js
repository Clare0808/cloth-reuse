import { defineStore } from "pinia";
import { ref } from "vue";

export const finishUiStore = defineStore("finish", () => {
  const dataList = ref("");
  const showElePage = ref(false);

  const GetFinishData = async () => {
    const response = await fetch(
      "https://cloth-reuse.onrender.com/api/get-finish"
    );
    const data = await response.json();

    return data.data;
  };

  const SendFinishData = async (inputData) => {
    const responsePost = await fetch(
      "https://cloth-reuse.onrender.com/api/send-finish",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(inputData),
      }
    );

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  const DeleteFinish = async (inputData) => {
    const responsePost = await fetch(
      "https://cloth-reuse.onrender.com/api/delete-review",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: inputData }),
      }
    );

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  return {
    dataList,
    showElePage,
    GetFinishData,
    SendFinishData,
    DeleteFinish,
  };
});
