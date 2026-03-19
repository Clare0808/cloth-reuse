import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomeView.vue";
import ClothPage from "@/components/ClothPage.vue";
import WebReviewPage from "@/components/WebReviewPage.vue";
import LikePage from "@/components/LikePage.vue";
import UserPage from "@/components/UserPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import MapPage from "@/components/MapPage.vue";
import PickupPage from "@/components/PickupPage.vue";
import ProblemPage from "@/components/ProblemPage.vue";

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
  {
    path: "/like",
    name: "LikePage",
    component: LikePage,
  },
  {
    path: "/user",
    name: "UserPage",
    component: UserPage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/map",
    name: "MapPage",
    component: MapPage,
  },
  {
    path: "/pickup",
    name: "PickupPage",
    component: PickupPage,
  },
  {
    path: "/problem",
    name: "ProblemPage",
    component: ProblemPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
