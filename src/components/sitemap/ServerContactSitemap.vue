<template>
  <div class="ele">
    <div class="title">使用導覽</div>
    <div class="box-frame">
      <i class="fa-regular fa-message" id="contact"></i>
      <i class="fa-solid fa-arrow-pointer" id="pointer"></i>
    </div>
    <div class="sec-title">點擊右下角對話框可填寫線上客服表單!</div>
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
.box-frame {
  position: relative;
}
#contact {
  width: 60px;
  height: 60px;
  color: #ffffff;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  background-color: #849c7d;
  border-radius: 50%;
  box-shadow: 0px 0px 3px 3px #d0d0d0;
  margin: 20px 0;
  transition: all 0.3s ease;
}
#pointer {
  color: #849c7d;
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
    color: #3b5131;
    transform: translateX(0px) translateY(0px);
  }
  to {
    transform: translateX(40px) translateY(40px);
  }
}
</style>
