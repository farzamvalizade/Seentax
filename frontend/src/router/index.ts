import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";

// Import your Pages Here

import Home from "../pages/Home.vue";

// Define Routes Here
const routes: RouteRecordRaw[] = [{ path: "/", component: Home }];

export default createRouter({
  history: createWebHistory(),
  routes,
});
