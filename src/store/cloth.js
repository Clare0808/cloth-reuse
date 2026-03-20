import { defineStore } from "pinia";
import { ref } from "vue";

export const clothUiStore = defineStore("cloth", () => {
  const showElePage = ref(false);

  const UploadNewCloth = async (inputData) => {
    const responsePost = await fetch("http://localhost:5000/api/upload-cloth", {
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

  const UploadClothImage = async (inputData) => {
    const res = await fetch("/api/upload-cloth-image", {
      method: "POST",
      body: inputData,
    });

    const data = await res.json();

    return data.data;
  };

  return {
    showElePage,
    UploadNewCloth,
    UploadClothImage,
  };
});
