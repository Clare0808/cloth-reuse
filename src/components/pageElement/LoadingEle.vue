<template>
  <div class="loader-overlay"></div>
  <div class="loader-frame">
    <div class="loader"></div>
  </div>
</template>

<style scoped>
.loader-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 2;
}
.loader-frame {
  width: 200px;
  height: 200px;
  background-color: #ffffff;
  border-radius: 20px;
  border: 2px solid #849c7d;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 50%;
  left: 50%;
  z-index: 2;
}
.loader {
  border: 8px solid #d3dcba; /* 背景圈 */
  border-top: 8px solid #849c7d; /* 藍色圈 */
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
