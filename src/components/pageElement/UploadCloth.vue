<template>
  <div class="ele">
    <div class="title">服飾上架</div>
    <div class="info-frame">
      <div class="img-frame">
        <img class="img" :src="tempImage" />
        <i
          class="fa-solid fa-cloud-arrow-up"
          id="cloud"
          @click.prevent="TriggleFileInput"
        ></i>
        <input
          type="file"
          @change="UploadImage"
          ref="fileInput"
          style="display: none"
        />
      </div>
      <div class="text-outframe">
        <div class="text-frame">
          <div class="sec-title">名稱</div>
          <input type="text" v-model.trim="name" />
        </div>
        <div class="text-frame">
          <div class="sec-title">類型</div>
          <div class="type-select-outframe">
            <div
              class="type-select-prompt"
              @click="showSelector = !showSelector"
            >
              {{ typeName }}
            </div>
            <transition name="slide-down">
              <div class="type-select-box" v-if="showSelector">
                <div
                  v-for="(option, index) in OptionsData.slice(1)"
                  :key="index"
                >
                  <div class="type-selector" @click="ClickOption(option.name)">
                    {{ option.name }}
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>
        <div class="text-frame">
          <div class="sec-title">尺寸</div>
          <input type="text" v-model.trim="size" />
        </div>
        <div class="text-frame">
          <div class="sec-title">地點</div>
          <input type="text" v-model.trim="place" />
        </div>
        <div class="text-frame">
          <div class="sec-title">時間</div>
          <input type="text" v-model.trim="time" />
        </div>
        <div class="text-frame">
          <div class="sec-title">衣況描述</div>
          <textarea type="text" v-model.trim="situation"></textarea>
        </div>
      </div>
    </div>
    <div class="btn-frame">
      <div class="no-btn" @click="ClickCancel">取消</div>
      <div class="yes-btn" @click="SendAdd">確定</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { errorUiStore } from "@/store/error";
import { clothUiStore } from "@/store/cloth";

import OptionsDataRaw from "@/assets/data/optionsData.json";

export default {
  setup() {
    const name = ref("");
    const type = ref("");
    const size = ref("");
    const place = ref("");
    const time = ref("");
    const situation = ref("");
    const newId = ref("");

    const fileInput = ref(null);
    const tempImage = ref(null);
    const tempImageName = ref("");
    const showSelector = ref(false);
    const typeName = ref("");

    const errorStore = errorUiStore();
    const clothStore = clothUiStore();

    const OptionsData = ref(OptionsDataRaw);

    const SendAdd = async () => {
      ExamEmptyInput();

      if (!errorStore.errorType) {
        const userEmail = localStorage.getItem("userEmail");
        const userName = localStorage.getItem("userName");

        await clothStore.UploadNewCloth({
          id: newId.value,
          name: name.value,
          situation: situation.value,
          size: size.value,
          image: tempImageName.value,
          pEmail: userEmail,
          pName: userName,
          place: place.value,
          time: time.value,
          type: type.value,
          lock: false,
        });

        clothStore.showElePage = false;

        errorStore.LoadSuccess("收藏成功!");
      }

      await errorStore.CloseEle();
    };

    const CleanInput = () => {
      name.value = "";
      type.value = "";
      size.value = "";
      place.value = "";
      time.value = "";
      situation.value = "";
    };

    const TriggleFileInput = () => {
      fileInput.value.click();
    };

    const UploadImage = async (e) => {
      const fd = new FormData();

      fd.append("name", name.value);
      fd.append("image", e.target.files[0]);

      const data = await clothStore.UploadClothImage(fd);
      tempImage.value = "http://localhost:5000/upload/cloth/" + data;
      tempImageName.value = data;

      ExamImage();
    };

    const ClickCancel = () => {
      clothStore.showElePage = false;
    };

    const ExamEmptyInput = () => {
      if (name.value === "") {
        errorStore.SetError("衣服名稱尚未填入!");
      } else if (type.value === "") {
        errorStore.SetError("衣服類型尚未填入!");
      } else if (size.value === "") {
        errorStore.SetError("衣服尺寸尚未填入!");
      } else if (place.value === "") {
        errorStore.SetError("取衣地點尚未填入!");
      } else if (time.value === "") {
        errorStore.SetError("取衣時間尚未填入!");
      } else if (situation.value === "") {
        errorStore.SetError("衣服狀況尚未填入!");
      } else if (!tempImage.value) {
        errorStore.SetError("衣服圖片尚未上傳!");
      } else {
        errorStore.errorType = false;
        errorStore.showErrorMsg = false;
      }
    };

    const ExamImage = () => {
      const imgEle = document.querySelector(".img");
      const cloudEle = document.querySelector("#cloud");

      if (!tempImage.value) {
        imgEle.style.display = "none";
        cloudEle.style.display = "block";
      } else {
        imgEle.style.display = "block";
        cloudEle.style.display = "none";
      }
    };

    const FindNewId = async () => {
      const response = await fetch("/data/clothData.json");
      const data = await response.json();

      let maxId = -1;

      data.forEach((item) => {
        if (item.id > maxId) {
          maxId = item.id;
        }
      });

      newId.value = maxId + 1;
    };

    const ClickOption = (option) => {
      const filteredData = OptionsData.value.find((item) => {
        return item.name === option;
      });

      type.value = filteredData.label;
      typeName.value = filteredData.name;

      showSelector.value = false;

      const optionEle = document.querySelector(".type-select-prompt");
      optionEle.style.color = "#ffffff";
      optionEle.style.backgroundColor = "#849c7d";
    };

    onMounted(() => {
      CleanInput();

      typeName.value = "請選擇";

      ExamImage();

      FindNewId();
    });

    return {
      name,
      type,
      size,
      place,
      time,
      situation,
      newId,
      fileInput,
      tempImage,
      tempImageName,
      showSelector,
      typeName,
      clothStore,
      OptionsDataRaw,
      OptionsData,
      SendAdd,
      CleanInput,
      TriggleFileInput,
      UploadImage,
      ClickCancel,
      ExamEmptyInput,
      ExamImage,
      FindNewId,
      ClickOption,
    };
  },
};
</script>

<style scoped>
.ele {
  width: 65%;
  background-color: #ffffff;
  border: 1px solid #3b5131;
  border-radius: 20px;
  padding: 20px;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.info-frame {
  display: grid;
  grid-template-columns: 30% 70%;
  justify-content: center;
  align-items: center;
}
.img-frame {
  width: 200px;
  height: 200px;
  border: 1px solid #849c7d;
  border-radius: 20px;
  position: relative;
}
img {
  width: 200px;
  height: 200px;
}
#cloud {
  color: #d3dcba;
  font-size: 60px;
  position: absolute;
  bottom: 35%;
  right: 32%;
}
#cloud:hover {
  color: #849c7d;
  cursor: pointer;
}
.text-frame {
  width: 100%;
  font-size: 20px;
  margin: 20px 0;
  display: flex;
  justify-content: start;
  align-items: center;
}
.sec-title {
  width: 100px;
}
input {
  width: 95%;
  font-size: 20px;
  font-family: "Pacifico", cursive;
  text-align: center;
  border: none;
  border-bottom: 1px solid #849c7d;
  padding: 5px;
}
input:focus {
  outline: none;
  border-bottom: 1px solid #3b5131;
}
.type-select-outframe {
  position: relative;
}
.type-select-prompt {
  width: 150px;
  background-color: #ffffff;
  border: 1px solid #849c7d;
  border-radius: 20px;
  padding: 10px;
  position: relative;
  z-index: 3;
  transition: all 0.3s ease;
}
.type-select-prompt:hover {
  color: #ffffff;
  background-color: #849c7d;
  cursor: pointer;
  transform: scale(1.1);
}
.type-select-box {
  width: 150px;
  background-color: #ffffff;
  color: #3b5131;
  border: 1px solid #3b5131;
  border-top: none;
  border-radius: 8px;
  padding: 10px;
  padding-top: 20px;
  position: absolute;
  top: 30px;
  left: 0px;
  z-index: 2;
  transition: all 0.3s ease;
}
.type-selector {
  margin: 5px 0;
}
.type-selector:hover {
  color: #ffffff;
  background-color: #849c7d;
  border-radius: 20px;
  cursor: pointer;
  transform: scale(1.1);
}
textarea {
  width: 95%;
  font-size: 20px;
  font-family: "Pacifico", cursive;
  margin-top: 10px;
  height: 80px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #adadad;
}
textarea:focus {
  outline: none;
  border: 1px solid #849c7d;
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

.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.5s ease;
}
.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
.slide-down-enter-to,
.slide-down-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
