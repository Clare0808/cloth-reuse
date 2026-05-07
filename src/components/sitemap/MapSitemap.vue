<template>
  <div class="ele">
    <div class="title">使用導覽</div>
    <div class="frame">
      <img src="@/assets/img/marker.png" />
      <i class="fa-solid fa-arrow-pointer" id="pointer"></i>
    </div>
    <div class="sec-title">點擊地標可查看詳細資訊!</div>
  </div>
</template>

<style scoped>
.ele {
  width: 60%;
  height: 35%;
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
.frame {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  transition: all 0.3s ease;
}
.frame img {
  width: 80px;
}
#pointer {
  color: #3b5131;
  font-size: 35px;
  position: absolute;
  bottom: 20px;
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
