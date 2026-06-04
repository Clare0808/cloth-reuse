import { defineStore } from "pinia";
import { ref } from "vue";

export const clothUiStore = defineStore("cloth", () => {
  const showElePage = ref(false);
  const showModifyPage = ref(false);
  const modifyList = ref({});

  const getErrorMessage = async (response) => {
    const fallback = `${response.status} ${response.statusText}`;

    try {
      const data = await response.json();
      return data.message || data.error || fallback;
    } catch {
      return fallback;
    }
  };

  const UploadNewCloth = async (inputData) => {
    const responsePost = await fetch("/api/upload-cloth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });

    if (!responsePost.ok) {
      throw new Error(await getErrorMessage(responsePost));
    }
  };

  const UploadClothImage = async (inputData) => {
    const res = await fetch("/api/upload-cloth-image", {
      method: "POST",
      body: inputData,
    });

    if (!res.ok) {
      throw new Error(await getErrorMessage(res));
    }

    const data = await res.json();

    return data.data;
  };

  const DeleteCloth = async (inputData) => {
    const responsePost = await fetch("/api/delete-cloth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: inputData }),
    });

    if (!responsePost.ok) {
      throw new Error(await getErrorMessage(responsePost));
    }
  };

  const ModifyCloth = async (inputData) => {
    const responsePost = await fetch("/api/modify-cloth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    });

    if (!responsePost.ok) {
      throw new Error(await getErrorMessage(responsePost));
    }
  };

  return {
    showElePage,
    showModifyPage,
    modifyList,
    UploadNewCloth,
    UploadClothImage,
    DeleteCloth,
    ModifyCloth,
  };
});
