import { defineStore } from "pinia";

export const likeUiStore = defineStore("like", () => {
  const GetLikeData = async () => {
    const response = await fetch("http://localhost:5000/api/get-like");
    const data = await response.json();

    return data.data;
  };

  const SendLikeData = async (likeData) => {
    const responsePost = await fetch("http://localhost:5000/api/store-like", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(likeData),
    });

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  const DeleteLike = async (likeData) => {
    const responsePost = await fetch("http://localhost:5000/api/delete-like", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: likeData }),
    });

    if (!responsePost.ok) {
      throw new Error("Network response was not ok");
    }
  };

  return {
    GetLikeData,
    SendLikeData,
    DeleteLike,
  };
});
