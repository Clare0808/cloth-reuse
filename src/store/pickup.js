import { defineStore } from "pinia";
import { ref } from "vue";

export const pickupUiStore = defineStore("pickup", () => {
  const dataList = ref("");
  const showElePage = ref(false);

  const GetPickupData = async () => {
    const response = await fetch("https://cloth-reuse.onrender.com/api/get-pickup");
    const data = await response.json();

    return data.data;
  };

  const SendPickupData = async (inputData) => {
    const responsePost = await fetch("https://cloth-reuse.onrender.com/api/send-pickup", {
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

  const DeletePickup = async (data) => {
    const responsePost = await fetch(
      "https://cloth-reuse.onrender.com/api/delete-pickup",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: data }),
      }
    );

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  const ModifyFile = async (data) => {
    const responsePost = await fetch("https://cloth-reuse.onrender.com/api/modify-file", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: data }),
    });

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  return {
    dataList,
    showElePage,
    GetPickupData,
    SendPickupData,
    DeletePickup,
    ModifyFile,
  };
});
