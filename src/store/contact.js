import { defineStore } from "pinia";
import { ref } from "vue";

export const contactUiStore = defineStore("contact", () => {
  const showElePage = ref(false);
  const showCheck = ref(false);
  const deleteData = ref("");

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

  const DeleteContact = async (inputData) => {
    const responsePost = await fetch(
      "http://localhost:5000/api/delete-contact",
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
    showElePage,
    showCheck,
    deleteData,
    SendContact,
    GetContactData,
    DeleteContact,
  };
});
