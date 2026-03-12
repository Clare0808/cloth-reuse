import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomeView.vue";
import ClothPage from "@/components/ClothPage.vue";
import WebReviewPage from "@/components/WebReviewPage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/cloth",
    name: "ClothPage",
    component: ClothPage,
  },
  {
    path: "/web-review",
    name: "WebReviewPage",
    component: WebReviewPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
