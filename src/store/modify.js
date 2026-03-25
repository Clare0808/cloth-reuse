import { defineStore } from "pinia";
import { ref } from "vue";

export const modifyUiStore = defineStore("modify", () => {
  const showBackEle = ref(false);
  const backDataList = ref({});

  const ModifyUserRole = async (inputData) => {
    const responsePost = await fetch("http://localhost:5000/api/modify-user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  return {
    showBackEle,
    backDataList,
    ModifyUserRole,
  };
});
