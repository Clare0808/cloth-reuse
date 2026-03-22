<template>
  <div class="back-ele">
    <div class="contact-box-outframe">
      <div
        class="contact-box-frame"
        v-for="(contact, index) in contactData"
        :key="index"
      >
        <div class="contact-box">
          <div class="text-outframe">
            <div class="text-frame">
              <div class="contact-info">{{ contact.name }}</div>
              <div class="contact-info">{{ contact.email }}</div>
              <div class="contact-date">{{ contact.time }}</div>
            </div>
            <div class="text-frame">
              <div class="contact-info">{{ contact.content }}</div>
            </div>
          </div>
          <div class="btn-frame">
            <i class="fa-solid fa-trash-can" @click="ClickDelete(contact)"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { contactUiStore } from "@/store/contact";
import { deleteUiStore } from "@/store/delete";

export default {
  name: "BackContactPage",
  setup() {
    const contactData = ref([]);

    const contactStore = contactUiStore();
    const deleteStore = deleteUiStore();

    const ClickDelete = async (data) => {
      deleteStore.open("contact", data.id);
    };

    onMounted(async () => {
      contactData.value = await contactStore.GetContactData();
    });

    return {
      contactData,
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
.contact-box-outframe {
  width: 95%;
  padding-right: 40px;
  overflow-y: auto;
}
.contact-box-frame {
  width: 100%;
}
.contact-box {
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
.contact-stars {
  color: #f0c42d;
  font-size: 24px;
  display: flex;
  justify-content: start;
  align-items: center;
}
.contact-date {
  color: #9d9d9d;
}
.contact-info-box-outframe {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: end;
}
.contact-info-box-frame {
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
