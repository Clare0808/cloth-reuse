import { defineStore } from "pinia";
import { ref } from "vue";

export const reviewUiStore = defineStore("review", () => {
  const showElePage = ref(false);
  const showCheck = ref(false);
  const deleteData = ref("");

  const SendReview = async (inputData) => {
    const responsePost = await fetch("http://localhost:5000/api/send-review", {
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

  const GetReviewData = async () => {
    const response = await fetch("http://localhost:5000/api/get-review");
    const data = await response.json();

    return data.data;
  };

  const DeleteReview = async (inputData) => {
    const responsePost = await fetch(
      "http://localhost:5000/api/delete-review",
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
    SendReview,
    GetReviewData,
    DeleteReview,
  };
});
