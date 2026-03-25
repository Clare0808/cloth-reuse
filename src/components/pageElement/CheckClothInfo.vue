<template>
  <div class="ele">
    <div class="title">詳細資訊</div>
    <div class="info-box">
      <img :src="selectedCloth.image" />
      <div class="cloth-info-frame">
        <div class="title-frame">
          <div class="cloth-name">{{ selectedCloth.name }}</div>
          <div class="icon-box">
            <i
              class="fa-solid fa-heart"
              @click="ClickHeart"
              :class="{ inLikeCSS: inLike }"
            ></i>
            <i
              class="fa-solid fa-map"
              @click="mapStore.ClickMap(selectedCloth.name)"
            ></i>
          </div>
        </div>
        <div class="cloth-info">類型: {{ type }}</div>
        <div class="cloth-info">尺寸: {{ selectedCloth.size }}</div>
        <div class="cloth-dis">服飾狀況: {{ selectedCloth.description }}</div>
        <div class="cloth-info">提供者: {{ selectedCloth.pName }}</div>
        <div class="cloth-info">取衣地點: {{ selectedCloth.place }}</div>
        <div class="cloth-info">取衣時間: {{ selectedCloth.time }}</div>
      </div>
    </div>
    <div class="btn" @click="ClickPickup">我要取衣</div>
  </div>
</template>

<script>
import { ref, watch } from "vue";

import { errorUiStore } from "@/store/error";
import { likeUiStore } from "@/store/like";
import { mapUiStore } from "@/store/map";
import { pickupUiStore } from "@/store/pickup";

import { selectedCloth, showElePage } from "../../components/ClothPage.vue";

import OptionData from "@/assets/data/optionsData.json";

export default {
  setup() {
    const errorStore = errorUiStore();
    const likeStore = likeUiStore();
    const mapStore = mapUiStore();
    const pickupStore = pickupUiStore();

    const type = ref("");
    const selectedList = ref({});
    const inLike = ref(false);

    const ClickHeart = async () => {
      const data = await likeStore.GetLikeData();

      const existData = data.find((item) => {
        return item.name === selectedList.value.name;
      });

      if (existData) {
        showElePage.value = false;

        errorStore.SetError("已經在收藏清單!");
      } else {
        await likeStore.SendLikeData({
          name: selectedList.value.name,
          type: type.value,
          size: selectedList.value.size,
          situation: selectedList.value.description,
          time: selectedList.value.time,
          place: selectedList.value.place,
          pEmail: selectedList.value.email,
          pName: selectedCloth.value.pName,
          image: selectedList.value.image,
        });

        showElePage.value = false;

        errorStore.LoadSuccess("收藏成功!");
      }

      await errorStore.CloseLoadEle();
    };

    const TransformType = (list) => {
      type.value = OptionData.find((item) => {
        return item.label === list.category;
      }).name;
    };

    const ClickPickup = async () => {
      const userEmail = localStorage.getItem("userEmail");
      const userName = localStorage.getItem("userName");

      await pickupStore.SendPickupData({
        rEmail: userEmail,
        rName: userName,
        name: selectedList.value.name,
        type: type.value,
        size: selectedList.value.size,
        situation: selectedList.value.description,
        time: selectedList.value.time,
        place: selectedList.value.place,
        pEmail: selectedCloth.value.email,
        pName: selectedCloth.value.pName,
        image: selectedList.value.image,
      });

      await pickupStore.ModifyFile(selectedList.value.name);

      showElePage.value = false;

      errorStore.LoadSuccess("取衣申請成功!");

      await errorStore.CloseLoadEle();
      window.location.reload();
    };

    watch(selectedCloth, async (newVal) => {
      selectedList.value = newVal;

      TransformType(newVal);

      const data = await likeStore.GetLikeData();

      const existData = data.find((item) => {
        return item.name === selectedList.value.name;
      });

      if (existData) {
        inLike.value = true;
      } else {
        inLike.value = false;
      }
    });

    return {
      selectedCloth,
      showElePage,
      OptionData,
      type,
      selectedList,
      inLike,
      mapStore,
      ClickHeart,
      TransformType,
      ClickPickup,
    };
  },
};
</script>

<style scoped>
.ele {
  width: 65%;
  background-color: #ffffff;
  border-radius: 12px;
  border: 1px solid #3b5131;
  padding: 20px;
  padding-bottom: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  color: #3b5131;
  font-size: 35px;
  font-weight: bold;
  margin: 20px 0;
}
.info-box {
  width: 100%;
  text-align: left;
  display: flex;
  grid-template-columns: 35% 65%;
  gap: 30px;
  justify-content: center;
  align-items: center;
}
.cloth-info-frame {
  width: 100%;
}
img {
  width: 280px;
}
.title-frame {
  width: 100%;
  border-bottom: 1px solid #3b5131;
  padding: 10px 0;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title-frame i {
  color: #d3dcba;
  font-size: 22px;
  transition: all 0.3s ease;
}
.title-frame i:hover {
  color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}
.cloth-name {
  font-size: 30px;
}
.icon-box i {
  margin: 0 10px;
}
.cloth-info,
.cloth-dis {
  font-size: 20px;
  margin: 10px 0;
}
.btn {
  width: 150px;
  height: 40px;
  color: #ffffff;
  font-size: 20px;
  background-color: #849c7d;
  border-radius: 12px;
  line-height: 40px;
  text-align: center;
  margin-top: 30px;
  transition: all 0.3s ease;
}
.btn:hover {
  color: #ffffff;
  background-color: #3b5131;
  cursor: pointer;
  transform: scale(1.1);
}

.title-frame i.inLikeCSS {
  color: #3b5131;
}
</style>
