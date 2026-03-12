<template>
  <div class="ele">
    <div class="title">詳細資訊</div>
    <div class="info-box">
      <img :src="selectedCloth.image" />
      <div class="cloth-info-frame">
        <div class="cloth-name">{{ selectedCloth.name }}</div>
        <div class="cloth-info">類型: {{ selectedCloth.size }}</div>
        <div class="cloth-info">尺寸: {{ selectedCloth.size }}</div>
        <div class="cloth-info">服飾狀況: {{ selectedCloth.description }}</div>
        <div class="cloth-info">取衣地點: {{ selectedCloth.place }}</div>
        <div class="cloth-info">取衣時間: {{ selectedCloth.time }}</div>
      </div>
    </div>
    <div class="btn">我要取衣</div>
  </div>
</template>

<script>
import { selectedCloth, showElePage } from "../../components/ClothPage.vue";

export default {
  setup() {
    return {
      selectedCloth,
      showElePage,
    };
  },
};
</script>

<style scoped>
.ele {
  width: 65%;
  background-color: #ffffff;
  border-radius: 12px;
  border: 1px solid #3b5131;
  padding: 20px;
  padding-bottom: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.info-box {
  width: 100%;
  text-align: left;
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  width: 300px;
  margin-right: 50px;
}
.cloth-name {
  font-size: 30px;
  border-bottom: 1px solid #3b5131;
  margin-bottom: 20px;
  padding-bottom: 10px;
}
.cloth-info {
  font-size: 20px;
  margin: 10px 0;
}
.btn {
  width: 150px;
  height: 40px;
  color: #ffffff;
  font-size: 20px;
  background-color: #849c7d;
  border-radius: 12px;
  line-height: 40px;
  text-align: center;
  margin-top: 30px;
  transition: all 0.3s ease;
}
.btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
</style>
