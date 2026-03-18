import { defineStore } from "pinia";

export const reviewUiStore = defineStore("review", () => {
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

  return {
    SendReview,
    GetReviewData,
  };
});
