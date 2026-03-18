import { defineStore } from "pinia";
import { ref } from "vue";

export const pickupUiStore = defineStore("pickup", () => {
  const dataList = ref("");
  const showElePage = ref(false);

  const GetPickupData = async () => {
    const response = await fetch("http://localhost:5000/api/get-pickup");
    const data = await response.json();

    return data.data;
  };

  const SendPickupData = async (inputData) => {
    const responsePost = await fetch("http://localhost:5000/api/send-pickup", {
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

  const DeletePickup = async () => {
    const responsePost = await fetch(
      "http://localhost:5000/api/delete-pickup",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: dataList.value }),
      }
    );

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
  };
});
