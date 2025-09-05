<template>
  <div
    class="grid grid-cols-2 sm:grid-cols-4 gap-6 w-full max-w-5xl mx-auto py-10"
  >
    <div
      class="bg-gradient-to-br from-blue-900/30 to-purple-900/30 rounded-xl p-6 flex flex-col items-center text-center transform transition-all duration-300 hover:scale-105 hover:shadow-2xl"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-12 w-12 mx-auto mb-4 text-blue-600"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="6"></circle>
        <circle cx="12" cy="12" r="2"></circle>
      </svg>
      <p class="text-2xl font-bold text-white">2000</p>
      <p class="text-sm text-gray-300 mt-1">کل مسائل</p>
    </div>
    <div
      class="bg-gradient-to-br from-blue-900/30 to-purple-900/30 rounded-xl p-6 flex flex-col items-center text-center transform transition-all duration-300 hover:scale-105 hover:shadow-2xl"
    >
      <svg
        class="h-12 w-12 mx-auto mb-4 text-green-600"
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M5.09 10.121A5.25 5.25 0 0 1 1 5V3.75C1 2.784 1.784 2 2.75 2h2.364c.236-.586.81-1 1.48-1h10.812c.67 0 1.244.414 1.48 1h2.489c.966 0 1.75.784 1.75 1.75V5a5.25 5.25 0 0 1-4.219 5.149a7.01 7.01 0 0 1-4.644 5.478l.231 3.003l.034.031c.079.065.303.203.836.282c.838.124 1.637.81 1.637 1.807v.75h2.25a.75.75 0 0 1 0 1.5H4.75a.75.75 0 0 1 0-1.5H7v-.75c0-.996.8-1.683 1.637-1.807c.533-.08.757-.217.836-.282l.034-.031l.231-3.003A7.01 7.01 0 0 1 5.09 10.12ZM6.5 2.594V9a5.5 5.5 0 1 0 11 0V2.594a.094.094 0 0 0-.094-.094H6.594a.094.094 0 0 0-.094.094m4.717 13.363l-.215 2.793l-.001.021l-.003.043a1 1 0 0 1-.022.147c-.05.237-.194.567-.553.86c-.348.286-.853.5-1.566.605a.48.48 0 0 0-.274.136a.26.26 0 0 0-.083.188v.75h7v-.75a.26.26 0 0 0-.083-.188a.48.48 0 0 0-.274-.136c-.713-.105-1.218-.32-1.567-.604c-.358-.294-.502-.624-.552-.86a1 1 0 0 1-.025-.19l-.001-.022l-.215-2.793a7 7 0 0 1-1.566 0M19 8.578A3.75 3.75 0 0 0 21.625 5V3.75a.25.25 0 0 0-.25-.25H19ZM5 3.5H2.75a.25.25 0 0 0-.25.25V5A3.75 3.75 0 0 0 5 8.537Z"
        />
      </svg>
      <p class="text-2xl font-bold text-white">۱۲</p>
      <p class="text-sm text-gray-300 mt-1">مسائل حل‌شده</p>
    </div>
    <div
      class="bg-gradient-to-br from-blue-500/20 to-purple-500/20 from-blue-900/30 to-purple-900/30 rounded-xl p-6 flex flex-col items-center text-center transform transition-all duration-300 hover:scale-105 hover:shadow-2xl"
    >
      <svg
        class="h-12 w-12 mx-auto mb-4 text-yellow-600"
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
          stroke-width="1.5"
          d="m12.495 18.587l4.092 2.15a1.044 1.044 0 0 0 1.514-1.106l-.783-4.552a1.05 1.05 0 0 1 .303-.929l3.31-3.226a1.043 1.043 0 0 0-.575-1.785l-4.572-.657A1.04 1.04 0 0 1 15 7.907l-2.088-4.175a1.044 1.044 0 0 0-1.88 0L8.947 7.907a1.04 1.04 0 0 1-.783.575l-4.51.657a1.044 1.044 0 0 0-.584 1.785l3.309 3.226a1.04 1.04 0 0 1 .303.93l-.783 4.55a1.044 1.044 0 0 0 1.513 1.107l4.093-2.15a1.04 1.04 0 0 1 .991 0"
        />
      </svg>
      <p class="text-2xl font-bold text-white">1800</p>
      <p class="text-sm text-gray-300 mt-1">کل امتیازات</p>
    </div>
    <div
      class="bg-gradient-to-br from-blue-900/30 to-purple-900/30 rounded-xl p-6 flex flex-col items-center text-center transform transition-all duration-300 hover:scale-105 hover:shadow-2xl"
    >
      <svg
        class="h-12 w-12 mx-auto mb-4 text-purple-600"
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        aria-hidden="true"
      >
        <path
          d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"
        ></path>
        <circle cx="12" cy="8" r="6"></circle>
      </svg>
      <p class="text-2xl font-bold text-white">#5</p>
      <p class="text-sm text-gray-300 mt-1">رتبه</p>
    </div>
  </div>
</template>
