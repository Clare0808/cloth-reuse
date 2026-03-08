<template>
  <div class="page">
    <div class="title-frame">
      <div class="title">舊衣回收平台</div>
      <div class="slogan">讓每件衣服再走一段路</div>
      <div class="btn">開始</div>
    </div>
  </div>
</template>

<style scoped>
.page {
  height: 100vh;

  background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url("@/assets/img/background3.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;

  overflow-y: hidden;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title-frame {
  color: #3b5131;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  font-size: 56px;
}
.slogan {
  color: #3b5131;
  font-size: 26px;
  margin-top: 20px;
}
.btn {
  font-size: 22px;
  background-color: #bcbfb1;
  border-radius: 12px;
  margin-top: 30px;
  padding: 10px 20px;
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #d1d4c1;
  cursor: pointer;
  transform: scale(1.2);
}
</style>
