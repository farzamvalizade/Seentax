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
            fill="#1b71ea"
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
        :while-hover="linkHover"
        :transition="linkTransition"
        class="group"
      >
        <RouterLink
          to="/"
          class="relative flex items-center gap-2 px-2 py-1 rounded-md"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 24 24"
          >
            <path
              fill="none"
              stroke="#f4efef"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 12L12 1l11 11m-2-2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V10m6 12v-8h6v8"
            />
          </svg>
          <span>خانه</span>
          <span
            class="absolute left-0 -bottom-1 h-[2px] w-0 bg-white transition-all duration-200 group-hover:w-full"
          ></span>
        </RouterLink>
      </motion.div>
      <motion.div
        :while-hover="linkHover"
        :transition="linkTransition"
        class="group"
      >
        <RouterLink
          to="/"
          class="relative flex items-center gap-2 px-2 py-1 rounded-md"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M4 13c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0 4c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0-8c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m4 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1m0 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1M7 8c0 .55.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1m-3 5c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0 4c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0-8c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m4 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1m0 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1M7 8c0 .55.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1"
            />
          </svg>
          <span>مسائل</span>
          <span
            class="absolute left-0 -bottom-1 h-[2px] w-0 bg-white transition-all duration-200 group-hover:w-full"
          ></span>
        </RouterLink> </motion.div
      ><motion.div
        :while-hover="linkHover"
        :transition="linkTransition"
        class="group"
      >
        <RouterLink
          to="/"
          class="relative flex items-center gap-2 px-2 py-1 rounded-md"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M5.09 10.121A5.25 5.25 0 0 1 1 5V3.75C1 2.784 1.784 2 2.75 2h2.364c.236-.586.81-1 1.48-1h10.812c.67 0 1.244.414 1.48 1h2.489c.966 0 1.75.784 1.75 1.75V5a5.25 5.25 0 0 1-4.219 5.149a7.01 7.01 0 0 1-4.644 5.478l.231 3.003l.034.031c.079.065.303.203.836.282c.838.124 1.637.81 1.637 1.807v.75h2.25a.75.75 0 0 1 0 1.5H4.75a.75.75 0 0 1 0-1.5H7v-.75c0-.996.8-1.683 1.637-1.807c.533-.08.757-.217.836-.282l.034-.031l.231-3.003A7.01 7.01 0 0 1 5.09 10.12ZM6.5 2.594V9a5.5 5.5 0 1 0 11 0V2.594a.094.094 0 0 0-.094-.094H6.594a.094.094 0 0 0-.094.094m4.717 13.363l-.215 2.793l-.001.021l-.003.043a1 1 0 0 1-.022.147c-.05.237-.194.567-.553.86c-.348.286-.853.5-1.566.605a.48.48 0 0 0-.274.136a.26.26 0 0 0-.083.188v.75h7v-.75a.26.26 0 0 0-.083-.188a.48.48 0 0 0-.274-.136c-.713-.105-1.218-.32-1.567-.604c-.358-.294-.502-.624-.552-.86a1 1 0 0 1-.025-.19l-.001-.022l-.215-2.793a7 7 0 0 1-1.566 0M19 8.578A3.75 3.75 0 0 0 21.625 5V3.75a.25.25 0 0 0-.25-.25H19ZM5 3.5H2.75a.25.25 0 0 0-.25.25V5A3.75 3.75 0 0 0 5 8.537Z"
            />
          </svg>
          <span>جدول امتیازات</span>
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
          class="flex items-center px-4 py-1.5 rounded-lg border border-white hover:bg-white hover:text-black transition-colors"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M13 21q-.425 0-.712-.288T12 20t.288-.712T13 19h6V5h-6q-.425 0-.712-.288T12 4t.288-.712T13 3h6q.825 0 1.413.588T21 5v14q0 .825-.587 1.413T19 21zm-1.825-8H4q-.425 0-.712-.288T3 12t.288-.712T4 11h7.175L9.3 9.125q-.275-.275-.275-.675t.275-.7t.7-.313t.725.288L14.3 11.3q.3.3.3.7t-.3.7l-3.575 3.575q-.3.3-.712.288T9.3 16.25q-.275-.3-.262-.712t.287-.688z"
            />
          </svg>
          ورود
        </RouterLink>
      </motion.div>
      <motion.div :while-hover="btnHover" :transition="btnTransition">
        <RouterLink
          to="/sign-up"
          class="flex items-center px-4 py-1.5 rounded-lg bg-white text-black hover:bg-black hover:text-white border border-white transition-colors"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 11h3m0 0h3m-3 0v3m0-3V8m-3 11v-1.25c0-2.071-1.919-3.75-4.286-3.75H7.286C4.919 14 3 15.679 3 17.75V19m9-11a3 3 0 1 1-6 0a3 3 0 0 1 6 0"
            />
          </svg>
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
  name: "HomeIcon",
};

const ProblemIcon = {
  template: `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
	<path fill="currentColor" d="M4 13c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0 4c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0-8c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m4 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1m0 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1M7 8c0 .55.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1m-3 5c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0 4c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m0-8c.55 0 1-.45 1-1s-.45-1-1-1s-1 .45-1 1s.45 1 1 1m4 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1m0 4h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1s.45 1 1 1M7 8c0 .55.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1H8c-.55 0-1 .45-1 1" />
</svg>`,
};
const LeaderboardIcon = {
  template: `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
	<path fill="currentColor" d="M5.09 10.121A5.25 5.25 0 0 1 1 5V3.75C1 2.784 1.784 2 2.75 2h2.364c.236-.586.81-1 1.48-1h10.812c.67 0 1.244.414 1.48 1h2.489c.966 0 1.75.784 1.75 1.75V5a5.25 5.25 0 0 1-4.219 5.149a7.01 7.01 0 0 1-4.644 5.478l.231 3.003l.034.031c.079.065.303.203.836.282c.838.124 1.637.81 1.637 1.807v.75h2.25a.75.75 0 0 1 0 1.5H4.75a.75.75 0 0 1 0-1.5H7v-.75c0-.996.8-1.683 1.637-1.807c.533-.08.757-.217.836-.282l.034-.031l.231-3.003A7.01 7.01 0 0 1 5.09 10.12ZM6.5 2.594V9a5.5 5.5 0 1 0 11 0V2.594a.094.094 0 0 0-.094-.094H6.594a.094.094 0 0 0-.094.094m4.717 13.363l-.215 2.793l-.001.021l-.003.043a1 1 0 0 1-.022.147c-.05.237-.194.567-.553.86c-.348.286-.853.5-1.566.605a.48.48 0 0 0-.274.136a.26.26 0 0 0-.083.188v.75h7v-.75a.26.26 0 0 0-.083-.188a.48.48 0 0 0-.274-.136c-.713-.105-1.218-.32-1.567-.604c-.358-.294-.502-.624-.552-.86a1 1 0 0 1-.025-.19l-.001-.022l-.215-2.793a7 7 0 0 1-1.566 0M19 8.578A3.75 3.75 0 0 0 21.625 5V3.75a.25.25 0 0 0-.25-.25H19ZM5 3.5H2.75a.25.25 0 0 0-.25.25V5A3.75 3.75 0 0 0 5 8.537Z" />
</svg>`,
};

const links: Link[] = [
  { to: "/", label: "خانه", icon: HomeIcon },
  { to: "/problems", label: "مسائل", icon: ProblemIcon },
  { to: "/leaderboard", label: "جدول امتیازات", icon: LeaderboardIcon },
];

const logoAnimate = { rotate: 360, scale: [1, 1.1, 1] };
const logoTransition = { repeat: Infinity, duration: 15, ease: "linear" };

const linkHover = { y: -6, scale: 1.06 };
const linkTransition = { type: "spring", stiffness: 400, damping: 20 };

const btnHover = { y: -4, scale: 1.04 };
const btnTransition = { type: "spring", stiffness: 400 };
</script>
