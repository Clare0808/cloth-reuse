<template>
  <div
    class="error-msg"
    :class="{ error: errorStore.errorType, success: !errorStore.errorType }"
  >
    <div class="text">{{ errorStore.errorText }}</div>
  </div>
</template>

<script>
import { errorUiStore } from "@/store/error";

export default {
  setup() {
    const errorStore = errorUiStore();

    return {
      errorStore,
    };
  },
};
</script>

<style scoped>
.error,
.success {
  width: 250px;
  height: 60px;
  font-size: 22px;
  border-radius: 20px;
  text-align: center;
  line-height: 60px;
}
.error {
  color: #c56869;
  background-color: #f3d7d4;
}
.success {
  color: #3b5131;
  background-color: #d3dcba;
}
</style>
