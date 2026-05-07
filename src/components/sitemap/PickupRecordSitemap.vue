<template>
  <div class="ele">
    <div class="title">使用導覽</div>
    <div class="box-frame">
      <i class="fa-solid fa-shirt"></i>
      <i class="fa-solid fa-heart"></i>
      <i class="fa-solid fa-user" id="user"></i>
    </div>
    <div class="sec-title">取衣紀錄可在使用者中心中查看!</div>
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
  box-shadow: 0px 0px 3px 3px #d0d0d0;
  margin: 20px 0;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  transition: all 0.3s ease;
}
.box-frame i {
  margin: 0 20px;
}
#user {
  animation: shake 0.8s infinite alternate;
}
.sec-title {
  font-size: 22px;
  color: #272727;
  margin-top: 20px;
}

@keyframes shake {
  0% {
    transform: translateY(0px);
  }
  40% {
    transform: translateY(-10px) scale(1.4);
  }
  50% {
    transform: translateY(-10px) rotate(5deg) scale(1.4);
  }
  75% {
    transform: translateY(-10px) rotate(-5deg) scale(1.4);
  }
  100% {
    color: #849c7d;
    transform: translateY(-10px) rotate(0deg) scale(1.4);
  }
}
</style>
