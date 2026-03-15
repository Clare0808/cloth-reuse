<template>
  <div>
    <div id="map"></div>

    <div class="search-frame">
      <div class="search-box">
        <input
          type="text"
          v-model.trim="inputText"
          @keydown.enter.exact="FilteredResult"
        />
        <i
          class="fa-solid fa-search"
          id="search-icon"
          @click="FilteredResult"
        ></i>
      </div>
      <div class="result-outframe">
        <div v-for="(result, index) in filteredData" :key="index">
          <div class="result-box" @click="ClickSearchResult(result.name)">
            <div class="search-result">{{ result.name }}</div>
            <div class="search-info">{{ result.city }} {{ result.town }}</div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="overlay"
      v-show="showSelected"
      @click="showSelected = false"
    ></div>
    <transition name="y-slide">
      <div class="info-outframe" v-if="showSelected">
        <div class="info-title">{{ selectedRestaurant.name }}</div>
        <div class="info-box">
          <i class="fa-solid fa-location-dot" id="info-icon"></i>
          <div class="info">
            {{ selectedRestaurant.city }} {{ selectedRestaurant.town }}
          </div>
        </div>
        <div class="info">{{ selectedRestaurant.description }}</div>
        <div class="info-box">
          <i class="fa-solid fa-clock" id="info-icon"></i>
          <div class="info">{{ selectedRestaurant.opentime }}</div>
        </div>
        <div class="info-box">
          <i class="fa-solid fa-phone" id="info-icon"></i>
          <div class="info">{{ selectedRestaurant.phone }}</div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

import { listClick } from "./pageElement/CheckClothInfo.vue";

export default {
  name: "MapPage",
  setup() {
    const map = ref(null);
    const showSelected = ref(false);
    const selectedRestaurant = ref({});
    const inputText = ref("");
    const filteredData = ref([]);
    const markerList = ref({});
    const placeData = ref([]);

    let L;

    const GetPlaceData = async () => {
      const response = await fetch("/data/clothPlaceData.json");
      const data = await response.json();

      placeData.value = data;
    };

    const FilteredResult = () => {
      filteredData.value = placeData.value.filter((rest) => {
        return rest.name.includes(inputText.value);
      });
    };

    const ClickSearchResult = (name) => {
      let marker = markerList.value[name];

      const result = placeData.value.find((r) => r.name === name);

      if (!marker) {
        const latlng = L.latLng(result.lat, result.lng);
        marker = L.marker(latlng).addTo(map.value).bindPopup(result.name);

        markerList.value[name] = marker;
      }

      map.value.flyTo(marker.getLatLng(), 16); // 平滑移動到 marker
      marker.openPopup();
    };

    onMounted(async () => {
      await GetPlaceData();

      L = await import("leaflet"); // 動態載入，避免 SSR
      await import("leaflet/dist/leaflet.css");

      map.value = L.map("map", {
        zoomAnimation: false, // 關閉縮放動畫避免 zoom 時出現 leaflet 錯誤
      }).setView([25.033, 121.5654], 13);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "&copy; OpenStreetMap contributors",
      }).addTo(map.value);

      // 建立一個 LayerGroup 來管理標記
      const markersLayer = L.layerGroup().addTo(map.value);

      // 更新標記函式
      function MakeMark() {
        markersLayer.clearLayers();
        markerList.value = {};
        const bounds = map.value.getBounds(); // 取得目前地圖範圍

        placeData.value.forEach((r) => {
          if (r.lat && r.lng) {
            const latlng = L.latLng(r.lat, r.lng);
            if (bounds.contains(latlng)) {
              const myIcon = L.icon({
                iconUrl: require("../assets/img/marker.png"), // 圖片路徑
                iconSize: [27, 40], // marker 大小
                iconAnchor: [20, 40], // marker 底部對齊點
                popupAnchor: [0, -40], // popup 顯示位置
              });

              const marker = L.marker(latlng, { icon: myIcon })
                .addTo(markersLayer)
                .bindPopup(r.name);

              markerList.value[r.name] = marker;

              marker.on("click", () => {
                showSelected.value = true;

                selectedRestaurant.value = r;
              });
            }
          }
        });
      }

      MakeMark(); // 初始載入

      map.value.on("moveend", MakeMark); // 每次地圖移動結束後更新標記

      // 從 ListPage 點擊過來
      if (listClick && listClick.value) {
        ClickSearchResult(listClick.value);

        listClick.value = "";
      }
    });

    return {
      listClick,
      map,
      showSelected,
      selectedRestaurant,
      inputText,
      filteredData,
      markerList,
      placeData,
      GetPlaceData,
      FilteredResult,
      ClickSearchResult,
    };
  },
};
</script>

<style scoped>
#map {
  height: calc(100vh - 84px);
  width: 100vw;
  position: relative;
  bottom: 0;
  left: 0;
  z-index: 1;
}
.search-frame {
  height: calc(100vh - 84px);
  width: 25%;
  background-color: #ffffff;
  padding: 20px;
  padding-right: 20px;
  position: fixed;
  top: 80px;
  right: 0px;
  z-index: 99;
}
input {
  height: 30px;
  width: 230px;
  background-color: #ffffff;
  border: 2px solid #849c7d;
  border-radius: 8px;
  margin-right: 40px;
  padding: 0 10px;
}
input:focus {
  outline: none;
  border: 2px solid #3b5131;
}
#search-icon {
  color: #849c7d;
  font-size: 20px;
  position: absolute;
  top: 28px;
  right: 30px;
  transition: all 0.3s ease;
}
#search-icon:hover {
  cursor: pointer;
  transform: scale(1.2);
}
.result-outframe {
  overflow-y: auto;
  max-height: calc(80vh - 20px);
  margin-top: 20px;
  padding-right: 10px;
}
.result-box {
  border: 1px solid #3b5131;
  border-radius: 8px;
  margin: 20px 0;
  padding: 10px;
}
.result-box:hover {
  color: #ffffff;
  background-color: #849c7d;
  cursor: pointer;
}
.result-box:hover .search-info {
  color: #ffffff;
}
.search-result {
  text-align: left;
}
.search-info {
  color: #9d9d9d;
  text-align: right;
  margin-top: 10px;
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 99;
}
.info-outframe {
  background-color: #ffffff;
  border: 2px solid #3b5131;
  border-radius: 8px;
  padding: 20px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
}
.info-title {
  font-size: 26px;
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 1px solid #3b5131;
}
.info-box {
  display: flex;
  justify-content: start;
  align-items: center;
}
#info-icon {
  color: #849c7d;
  margin-right: 10px;
}
.info {
  margin: 5px 0;
}

.y-slide-enter-active,
.y-slide-leave-active {
  transition: all 1s ease;
}
.y-slide-enter-from,
.y-slide-leave-to {
  transform: translateY(100%) translate(-50%, -50%);
  opacity: 0;
}
.y-slide-enter-to,
.y-slide-leave-from {
  transform: translateY(0) translate(-50%, -50%);
  opacity: 1;
}
</style>
