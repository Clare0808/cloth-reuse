import { defineStore } from "pinia";
import { ref } from "vue";

export const contactUiStore = defineStore("contact", () => {
  const showElePage = ref(false);

  const SendContact = async (inputData) => {
    const responsePost = await fetch("http://localhost:5000/api/send-contact", {
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

  const GetContactData = async () => {
    const response = await fetch("http://localhost:5000/api/get-contact");
    const data = await response.json();

    return data.data;
  };

  return {
    showElePage,
    SendContact,
    GetContactData,
  };
});
