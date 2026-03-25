<template>
  <div class="back-ele">
    <div class="user-box-outframe">
      <div
        class="user-box-frame"
        v-for="(user, index) in userData"
        :key="index"
      >
        <div class="user-box">
          <div class="text-outframe">
            <div class="text-frame">
              <div class="user-info">{{ user.name }}</div>
              <div class="user-info">{{ user.email }}</div>
              <div class="user-info">{{ user.phone }}</div>
              <div class="user-info">角色</div>
            </div>
          </div>
          <div class="btn-frame">
            <i class="fa-solid fa-trash-can" @click="ClickDelete(user)"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { loginUiStore } from "@/store/login";
import { deleteUiStore } from "@/store/delete";

export default {
  name: "BackUserPage",
  setup() {
    const userData = ref([]);

    const loginStore = loginUiStore();
    const deleteStore = deleteUiStore();

    const ClickDelete = async (data) => {
      deleteStore.open("user", data.id);
    };

    onMounted(async () => {
      userData.value = await loginStore.getUserInfo();
    });

    return {
      userData,
      ClickDelete,
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
.user-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.user-box-frame {
  width: 100%;
}
.user-box {
  width: 100%;
  margin: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-outframe {
  width: 100%;
  font-size: 20px;
  border-right: 1px solid #3b5131;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.text-frame {
  width: 100%;
  font-size: 18px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.review-stars {
  color: #f0c42d;
  font-size: 24px;
  display: flex;
  justify-content: start;
  align-items: center;
}
.review-date {
  color: #9d9d9d;
}
.user-info-box-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}
.user-info-box-frame {
  width: 98%;
}
.btn-frame {
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.btn-frame i {
  color: #3b5131;
  margin: 10px 0;
}
.btn-frame i:hover {
  color: #849c7d;
  cursor: pointer;
}
</style>
