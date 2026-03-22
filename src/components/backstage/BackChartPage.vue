<template>
  <div class="back-chart">
    <div class="container">
      <div class="option-frame">
        <div class="sec-title" @click="HandleCanvas('star')">使用者評價</div>
        <div class="sec-title" @click="HandleCanvas('reuse')">總衣物回收量</div>
      </div>
      <div class="data-flame">
        <transition name="fade">
          <canvas ref="reviewCanvas" v-show="showStar"></canvas>
        </transition>
        <transition name="fade">
          <canvas ref="reuseCanvas" v-show="showReuse"></canvas>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, nextTick } from "vue";
import { Chart, registerables } from "chart.js";

import { reviewUiStore } from "@/store/review";
import { finishUiStore } from "@/store/finish";

Chart.register(...registerables); // 註冊 Chart.js

export default {
  name: "BackChartPage",
  setup() {
    const reviewData = ref([]);
    const reviewCanvas = ref(null);
    const reuseData = ref([]);
    const reuseCanvas = ref(null);

    let reviewChart = null;
    let reuseChart = null;

    const showStar = ref(false);
    const showReuse = ref(false);

    const reviewStore = reviewUiStore();
    const finishStore = finishUiStore();

    const GetReviewData = async () => {
      const data = await reviewStore.GetReviewData();

      for (let i = 1; i <= 5; i++) {
        const tempList = {};

        tempList.label = String(i);
        tempList.amount = 0;

        reviewData.value.push(tempList);
      }

      for (const review of data) {
        for (const item of reviewData.value) {
          if (review.star === Number(item.label)) {
            item.amount += 1;
          }
        }
      }
    };

    const GetReuseData = async () => {
      const data = await finishStore.GetFinishData();

      for (const item of data) {
        const tempTime = item.time.substring(0, 7);

        let existing = reuseData.value.find(
          (item) => item.time.substring(0, 7) === tempTime
        );

        if (!existing) {
          reuseData.value.push({ time: tempTime, total: 0 });
        }
      }

      for (const item of data) {
        const tempTime = item.time.substring(0, 7);

        let existing = reuseData.value.find(
          (item) => item.time.substring(0, 7) === tempTime
        );

        if (existing) {
          existing.total += 1;
        }
      }
    };

    const HandleCanvas = async (type) => {
      if (type === "star") {
        showStar.value = true;
        showReuse.value = false;

        if (!reviewChart) {
          await GetReviewData();

          await nextTick();

          reviewChart = new Chart(reviewCanvas.value, {
            type: "bar",
            data: {
              labels: reviewData.value.map((item) => item.label),
              datasets: [
                {
                  label: "數量",
                  data: reviewData.value.map((item) => item.amount),
                  backgroundColor: "#849c7d",
                },
              ],
            },
            options: {
              responsive: false,
              scales: {
                y: {
                  beginAtZero: true,
                  ticks: {
                    stepSize: 1, // 每格間距為 1，確保都是整數
                  },
                },
              },
            },
          });
        }
      } else if (type === "reuse") {
        showStar.value = false;
        showReuse.value = true;

        if (!reuseChart) {
          await GetReuseData();

          await nextTick();

          reuseChart = new Chart(reuseCanvas.value, {
            type: "line",
            data: {
              labels: reuseData.value.map((item) => item.time),
              datasets: [
                {
                  label: "數量",
                  data: reuseData.value.map((item) => item.total),
                  backgroundColor: "#849c7d",
                  borderColor: "#3b5131",
                },
              ],
            },
            options: {
              responsive: false,
              scales: {
                y: {
                  beginAtZero: true,
                  ticks: {
                    stepSize: 10, // 每格間距為 1，確保都是整數
                  },
                },
              },
            },
          });
        }
      }
    };

    return {
      reviewData,
      reviewCanvas,
      reuseData,
      reuseCanvas,
      showStar,
      showReuse,
      GetReviewData,
      GetReuseData,
      HandleCanvas,
    };
  },
};
</script>

<style scoped>
.back-chart {
  width: calc(100% - 290px);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
}
.option-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.sec-title {
  width: 120px;
  color: #3b5131;
  font-size: 20px;
  border: 1px solid #3b5131;
  border-radius: 20px;
  margin: 20px;
  padding: 10px;
  transition: all 0.3s ease;
}
.sec-title:hover {
  color: #ffffff;
  background-color: #849c7d;
  border: 1px solid #849c7d;
  cursor: pointer;
  transform: scale(1.1);
}
canvas {
  width: 900px;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.8s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}
</style>
