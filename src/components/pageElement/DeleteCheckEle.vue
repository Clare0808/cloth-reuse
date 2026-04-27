<template>
  <div class="check-ele">
    <div class="title">是否要刪除資料?</div>
    <div class="sec-title">注意! 資料刪除後就無法復原!</div>
    <div class="btn-frame">
      <div class="no-btn" @click="deleteStore.showCheck = false">取消</div>
      <div class="yes-btn" @click="SendDelete">確定</div>
    </div>
  </div>
</template>

<script>
import { deleteUiStore } from "@/store/delete";

export default {
  setup() {
    const deleteStore = deleteUiStore();

    const SendDelete = async () => {
      await deleteStore.sendDelete();
    };

    return {
      deleteStore,
      SendDelete,
    };
  },
};
</script>

<style scoped>
.check-ele {
  width: 65%;
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.title {
  font-size: 26px;
  margin-bottom: 10px;
}
.sec-title {
  color: #9d9d9d;
  font-size: 20px;
  margin-top: 10px;
}
.btn-frame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.no-btn,
.yes-btn {
  width: 150px;
  height: 40px;
  font-size: 20px;
  border-radius: 20px;
  line-height: 40px;
  text-align: center;
  margin: 20px 20px 0px 20px;
  transition: all 0.3s ease;
}
.no-btn {
  color: #3b5131;
  background-color: #ffffff;
  border: 1px solid #849c7d;
}
.no-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  border: 1px solid #3b5131;
  cursor: pointer;
}
.yes-btn {
  color: #ffffff;
  background-color: #849c7d;
}
.yes-btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
}
</style>
