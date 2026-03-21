<template>
  <div class="back-ele">
    <div class="cloth-box-outframe">
      <div
        class="cloth-box-frame"
        v-for="(cloth, index) in dataList"
        :key="index"
      >
        <div class="cloth-box">
          <img :src="cloth.image" />
          <div class="info-frame">
            <div class="text-outframe">
              <div class="text-frame">
                <div class="cloth-info">{{ cloth.name }}</div>
                <div class="cloth-info">{{ cloth.pName }}</div>
                <div class="cloth-info">{{ cloth.email }}</div>
              </div>
              <div class="text-sec-frame">
                <div class="cloth-info"></div>
                <div class="cloth-info">{{ cloth.place }}</div>
                <div class="cloth-info">{{ cloth.time }}</div>
              </div>
              <div class="text-sec-frame">
                <div class="cloth-info"></div>
                <div class="cloth-info">類型: {{ cloth.category }}</div>
                <div class="cloth-info">尺寸: {{ cloth.size }}</div>
              </div>
            </div>
            <div class="btn-frame">
              <i class="fa-solid fa-pencil"></i>
              <i class="fa-solid fa-trash-can"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="add-btn">新增服飾 +</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "BackClothPage",
  setup() {
    const dataList = ref([]);

    const GetDishData = async () => {
      const response = await fetch("/data/clothData.json");
      const data = await response.json();

      dataList.value = data;
    };

    onMounted(async () => {
      await GetDishData();
    });

    return {
      dataList,
      GetDishData,
    };
  },
};
</script>

<style scoped>
.back-ele {
  width: calc(100% - 290px);
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
}
.cloth-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.cloth-box-frame {
  width: 100%;
}
.cloth-box {
  width: 100%;
  margin: 20px 0;
  display: grid;
  grid-template-columns: 12% 88%;
  justify-content: center;
  align-items: center;
}
img {
  width: 100px;
  height: 100px;
}
.info-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-outframe {
  width: 100%;
  font-size: 20px;
  text-align: start;
  margin: 0 20px;
  border-right: 1px solid #3b5131;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.text-frame,
.text-sec-frame {
  width: 100%;
  margin-bottom: 10px;
  text-align: left;
  display: grid;
  grid-template-columns: 30% 30% 35%;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
.text-sec-frame {
  color: #4f4f4f;
  font-size: 16px;
}
.cloth-sec-info {
  font-size: 18px;
}
.btn-frame {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
i {
  color: #3b5131;
  margin: 10px 0;
}
i:hover {
  color: #849c7d;
  cursor: pointer;
}
.add-btn {
  color: #3b5131;
  font-size: 24px;
  margin: 20px;
}
.add-btn:hover {
  color: #849c7d;
  cursor: pointer;
}

.slide-child-enter-active,
.slide-child-leave-active {
  transition: all 1s ease;
}
.slide-child-enter-from,
.slide-child-leave-to {
  opacity: 0;
  transform: translate(-50%, -50%) translateY(20px);
}
.slide-child-enter-to,
.slide-child-leave-from {
  opacity: 1;
  transform: translate(-50%, -50%) translateY(0);
}
</style>
