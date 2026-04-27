import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "vue-router";

export const mapUiStore = defineStore("map", () => {
  const mapData = ref("");

  const router = useRouter();

  const ClickMap = (name) => {
    mapData.value = name;

    router.push("/map");
  };

  return {
    mapData,
    ClickMap,
  };
});
