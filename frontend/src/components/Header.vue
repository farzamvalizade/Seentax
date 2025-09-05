<template>
  <div
    class="bg-[#0d1117] flex flex-col items-center justify-center text-center px-4"
  >
    <h1
      class="text-2xl md:text-4xl font-bold bg-gradient-to-r from-blue-500 to-blue-300 bg-clip-text text-transparent mb-4"
    >
      مهارت‌های برنامه‌نویسی خود را تقویت کنید
    </h1>

    <p class="text-sm md:text-lg text-gray-400 mb-8 max-w-2xl mx-auto">
      مسائل چالش‌برانگیز برنامه‌نویسی را حل کنید، دانش الگوریتم‌های خود را بهبود
      دهید و با توسعه‌دهندگان سراسر جهان رقابت کنید.
    </p>

    <Motion
      tag="button"
      :whileTap="{ x: 8, scale: 0.95 }"
      class="flex items-center gap-2 px-6 py-3 rounded-2xl bg-blue-600 text-white font-semibold shadow-lg hover:bg-blue-500 transition-colors"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="20"
        height="20"
        viewBox="0 0 15 15"
        class="inline-block"
      >
        <path
          fill="currentColor"
          d="M8.293 2.293a1 1 0 0 1 1.414 0l4.5 4.5a1 1 0 0 1 0 1.414l-4.5 4.5a1 1 0 0 1-1.414-1.414L11 8.5H1.5a1 1 0 0 1 0-2H11L8.293 3.707a1 1 0 0 1 0-1.414"
        />
      </svg>
      شروع کنید
    </Motion>
  </div>
</template>

<script setup>
import { Motion } from "motion-v";
</script>
