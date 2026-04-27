<template>
  <div class="back-review">
    <div class="review-box-outframe">
      <div
        class="review-box-frame"
        v-for="(review, index) in reviewData"
        :key="index"
      >
        <div class="review-box">
          <div class="text-outframe">
            <div class="text-frame">
              <div class="review-stars">
                <div v-for="i in review.star" :key="i">
                  <i class="fa-solid fa-star"></i>
                </div>
              </div>
              <div class="review-info">{{ review.content }}</div>
            </div>
            <div class="text-frame">
              <div class="review-info">{{ review.name }}</div>
              <div class="review-info">{{ review.email }}</div>
              <div class="review-date">{{ review.data }}</div>
            </div>
          </div>
          <div class="btn-frame">
            <i class="fa-solid fa-trash-can" @click="ClickDelete(review)"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { reviewUiStore } from "@/store/review";
import { deleteUiStore } from "@/store/delete";

export default {
  name: "BackWebReviewPage",
  setup() {
    const reviewData = ref([]);

    const reviewStore = reviewUiStore();
    const deleteStore = deleteUiStore();

    const ClickDelete = async (data) => {
      deleteStore.open("review", data.id);
    };

    onMounted(async () => {
      reviewData.value = await reviewStore.GetReviewData();
    });

    return {
      reviewData,
      ClickDelete,
    };
  },
};
</script>

<style scoped>
.back-review {
  width: calc(100% - 290px);
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
}
.review-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.review-box-frame {
  width: 100%;
}
.review-box {
  width: 100%;
  margin: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-outframe {
  width: 100%;
  font-size: 20px;
  border-right: 1px solid #3b5131;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.text-frame {
  width: 100%;
  font-size: 18px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.review-stars {
  color: #f0c42d;
  font-size: 24px;
  display: flex;
  justify-content: start;
  align-items: center;
}
.review-date {
  color: #9d9d9d;
}
.review-info-box-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}
.review-info-box-frame {
  width: 98%;
}
.btn-frame {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.btn-frame i {
  color: #3b5131;
  margin: 10px 0;
}
.btn-frame i:hover {
  color: #849c7d;
  cursor: pointer;
}
</style>
