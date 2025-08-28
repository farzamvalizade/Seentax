<template>
  <nav
    class="fixed top-0 left-0 w-full z-50 bg-black text-white flex items-center justify-between px-6 py-3 border-b border-white/10"
  >
    <!-- Logo + Name -->
    <div>
      <RouterLink
        to="/"
        class="flex items-center gap-2 cursor-pointer select-none mx-auto"
      >
        <motion.div :animate="logoAnimate" :transition="logoTransition">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="26"
            height="26"
            viewBox="0 0 16 16"
            fill="white"
          >
            <path
              d="m11.28 3.22l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326a.75.75 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275a.75.75 0 0 1 .734.215m-6.56 0a.75.75 0 0 1 1.042.018a.75.75 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275a.75.75 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"
            />
          </svg>
        </motion.div>
        <p class="font-bold text-lg tracking-tight">سینتکس</p>
      </RouterLink>
    </div>

    <!-- Links -->
    <div class="flex gap-6 text-sm font-medium">
      <motion.div
        v-for="link in links"
        :key="link.to"
        :while-hover="linkHover"
        :transition="linkTransition"
        class="group"
      >
        <RouterLink
          :to="link.to"
          class="relative flex items-center gap-2 px-2 py-1 rounded-md"
        >
          <component :is="link.icon" class="w-4 h-4" />
          <span>{{ link.label }}</span>
          <span
            class="absolute left-0 -bottom-1 h-[2px] w-0 bg-white transition-all duration-200 group-hover:w-full"
          ></span>
        </RouterLink>
      </motion.div>
    </div>

    <!-- Auth buttons -->
    <div class="flex gap-3 text-sm font-semibold">
      <motion.div :while-hover="btnHover" :transition="btnTransition">
        <RouterLink
          to="/login"
          class="px-4 py-1.5 rounded-lg border border-white hover:bg-white hover:text-black transition-colors"
        >
          ورود
        </RouterLink>
      </motion.div>
      <motion.div :while-hover="btnHover" :transition="btnTransition">
        <RouterLink
          to="/sign-up"
          class="px-4 py-1.5 rounded-lg bg-white text-black hover:bg-black hover:text-white border border-white transition-colors"
        >
          ثبت‌نام
        </RouterLink>
      </motion.div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { motion } from "motion-v";
import { RouterLink } from "vue-router";

type Link = { to: string; label: string; icon: any };

const HomeIcon = {
  template: `<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24"><path fill="white" d="M3 11.5L12 3l9 8.5V21a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>`,
};
const ProblemIcon = {
  template: `<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24"><path fill="white" d="M12 2a10 10 0 1 0 .001 20.001A10 10 0 0 0 12 2zm0 5a1.25 1.25 0 1 1 0 2.5A1.25 1.25 0 0 1 12 7zm2 9v2H10v-2h4z"/></svg>`,
};
const LeaderboardIcon = {
  template: `<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24"><path fill="white" d="M5 3h4v18H5zM11 8h4v13h-4zM18 13h4v8h-4z"/></svg>`,
};

const links: Link[] = [
  { to: "/", label: "خانه", icon: HomeIcon },
  { to: "/problems", label: "مسائل", icon: ProblemIcon },
  { to: "/leaderboard", label: "جدول امتیازات", icon: LeaderboardIcon },
];

const logoAnimate = { rotate: 360 };
const logoTransition = { repeat: Infinity, duration: 20, ease: "linear" };

const linkHover = { y: -6, scale: 1.06 };
const linkTransition = { duration: 20, repeat: Infinity, ease: "linear" };

const btnHover = { y: -4, scale: 1.04 };
const btnTransition = { type: "spring", stiffness: 400 };
</script>
