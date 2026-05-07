<template>
  <div class="ele">
    <div class="title">使用導覽</div>
    <div class="cloth-frame">
      <img src="@/assets/img/cloth1.jpg" />
      <div class="cloth-info-frame">
        <div class="cloth-name">白色T-shirt</div>
        <div class="cloth-size">L</div>
      </div>
      <i class="fa-solid fa-arrow-pointer" id="pointer"></i>
    </div>
    <div class="sec-title">點擊服飾可查看詳細資訊!</div>
  </div>
</template>

<style scoped>
.ele {
  width: 60%;
  height: 70%;
  background-color: #ffffff;
  border-radius: 12px;
  border: 1px solid #3b5131;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.cloth-frame {
  width: 300px;
  background-color: #ffffff;
  border: 1px solid #849c7d;
  border-radius: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  transition: all 0.3s ease;
}
.cloth-frame img {
  width: 250px;
}
.cloth-info-frame {
  width: 95%;
  font-size: 24px;
  margin-top: 10px;
  padding-top: 15px;
  border-top: 1px solid #849c7d;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.cloth-size {
  color: #849c7d;
}
#pointer {
  color: #3b5131;
  font-size: 35px;
  position: absolute;
  bottom: 60px;
  right: 0px;
  animation: movePointer 1.5s infinite alternate;
}
.sec-title {
  font-size: 22px;
  color: #272727;
  margin-top: 20px;
}

@keyframes movePointer {
  from {
    color: #849c7d;
    transform: translateX(0px) translateY(0px);
  }
  to {
    transform: translateX(40px) translateY(40px);
  }
}
</style>
