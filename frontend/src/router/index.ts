import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";

import DefaultLayout from "../layout/DefaultLayout.vue";

// Import your Pages Here

import Home from "../pages/Home.vue";

// Define Routes Here
const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: DefaultLayout,
    children: [{ path: "", component: Home }],
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
