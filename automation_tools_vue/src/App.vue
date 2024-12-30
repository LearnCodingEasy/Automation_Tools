<script setup>
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";

// import { ref } from 'vue'
//
import { onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const userStore = useUserStore();
userStore.initStore();
const router = useRouter();

onMounted(() => {
  // Perform any necessary operations on component mount
  if (!userStore.user.access) {
    // console.log('User Data: ', userStore.user.access)
    // Replace '/login' with your actual login route
    router.push("/login");
  } else {
    // Set default Authorization header for axios
    axios.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${userStore.user.access}`;
    // console.log('User Data: ', userStore.user)
  }
});

// Log Out
let logout = () => {
  // console.log('User Log out')
  userStore.removeToken();
  // توجيه المستخدم إلى صفحة تسجيل الدخول
  setTimeout(() => {
    router.push("/login").then(() => {});
  }, 10);
};
</script>

<template>
  <div class="wrapper_app">
    <!-- Header Tailwind -->
    <div class="header_wrapper sticky top-0 left-0 right-0">
      <div class="container mx-auto">
        <div class="header_inner">
          <prime_card
            class="header_card px-2"
            v-if="userStore.user.isAuthenticated"
          >
            <!-- <prime_card class="header_card px-2"> -->
            <template #content>
              <header class="header_header">
                <nav class="header_nav">
                  <!-- Tablet Laptop Desktop -->
                  <div class="header_content">
                    <div
                      class="header_content_inner relative flex items-center justify-between"
                    >
                      <div
                        class="header_mobile_menu_button absolute inset-y-0 left-0 flex items-center sm:hidden"
                      >
                        <!-- Mobile menu button-->
                        <button
                          type="button"
                          class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-blue-600 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                          aria-controls="mobile-menu"
                          aria-expanded="false"
                          @click="toggleDropdownMobile"
                          id="header_main_links-menu-button"
                          aria-haspopup="true"
                        >
                          <span class="absolute -inset-0.5"></span>
                          <span class="sr-only">Open main menu</span>
                          <!--
                            Icon when menu is closed.
                            Menu open: "hidden", Menu closed: "block"
                          -->
                          <svg
                            class="block h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                            data-slot="icon"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                            />
                          </svg>
                          <!--
                            Icon when menu is open.
                            Menu open: "block", Menu closed: "hidden"
                          -->
                          <svg
                            class="hidden h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                            data-slot="icon"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M6 18 18 6M6 6l12 12"
                            />
                          </svg>
                        </button>
                      </div>
                      <div
                        class="header_wrapper_links flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
                      >
                        <div
                          class="header_logo_link flex flex-shrink-0 items-center"
                        >
                          <!-- Logo -->
                          <RouterLink to="/" class="logo flex items-center">
                            <img
                              class="h-8 w-8"
                              src="./assets/Images/Messenger_80x80.png"
                              alt="Your Company"
                            />
                            <span class="px-2 font-bold"> Messenger </span>
                          </RouterLink>
                        </div>
                        <div class="header_main_links hidden sm:ml-6 sm:block">
                          <div class="header_main_link flex space-x-4">
                            <RouterLink
                              to="/Desktop"
                              class="rounded-md px-3 py-2 text-md"
                              aria-current="page"
                            >
                              Desktop</RouterLink
                            >
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >Laptop
                            </RouterLink>
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >Tablet
                            </RouterLink>
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >Mobile
                            </RouterLink>
                          </div>
                        </div>
                      </div>
                      <!-- Right -->
                      <div
                        class="header_wrapper_profile_search absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
                      >
                        <!-- input_search -->
                        <div
                          class="header_input_search mobile_none tablet_none"
                        >
                          <prime_input_text
                            class="rounded-md border-black"
                            size="large"
                            placeholder="Search"
                          ></prime_input_text>
                        </div>
                        <!-- Notifications -->
                        <div class="relative mx-2 notifications">
                          <div class="notifications_button">
                            <!-- <button
                              class=" flex bg-gray-800 text-sm focus:outline-none
                              id="user-menu-button"
                              aria-expanded="false"
                              aria-haspopup="true"
                            >
                            </button> -->
                            <button
                              type="button"
                              class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                              @click="toggleDropdownNotifications"
                            >
                              <span class="absolute -inset-1.5"></span>
                              <span class="sr-only">View notifications</span>
                              <span class="notifications_length">
                                <prime_overlay_badge
                                  :value="notifications.length"
                                  size="small"
                                >
                                  <i
                                    class="pi pi-bell"
                                    style="font-size: 1.5rem"
                                  />
                                </prime_overlay_badge>
                              </span>
                            </button>
                          </div>
                          <!-- dropdown -->
                          <div
                            v-if="isDropdownNotificationsOpen"
                            class="absolute right-0 z-10 mt-2 w-96 origin-top-right rounded-md py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none notifications_wrapper"
                            role="menu"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu-button"
                            tabindex="-1"
                          >
                            <div
                              class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12 gap_5 notifications_inner"
                              v-if="notifications.length"
                            >
                              <!-- Start Card -->
                              <prime_card
                                style="width: 100%; overflow: hidden"
                                class="mobile_item_12 tablet_item_12 laptop_item_12 laptop_lg_item_12 desktop_item_12 desktop_lg_item_12 p-2 notifications_inner_button_read_all"
                              >
                                <template #header>
                                  <prime_button @click="markAllAsRead"
                                    >Mark all as read</prime_button
                                  >
                                </template>
                              </prime_card>
                              <!-- End Card -->

                              <!-- Start Card -->
                              <prime_card
                                style="width: 100%; overflow: hidden"
                                class="mobile_item_12 tablet_item_12 laptop_item_12 laptop_lg_item_12 desktop_item_12 desktop_lg_item_12 p-2 notifications_inner_content"
                                v-for="notification in notifications"
                                v-bind:key="notification.id"
                              >
                                <template #header>
                                  <img
                                    :src="
                                      notification.created_by_data.get_avatar
                                    "
                                    class="w-10 h-10 rounded-full cursor-pointer"
                                    alt=""
                                    @click="readNotification(notification)"
                                  />
                                </template>
                                <template #content>
                                  <div
                                    class="notBody text-sm cursor-pointer"
                                    @click="readNotification(notification)"
                                  >
                                    {{ notification.body }}
                                  </div>
                                </template>
                                <template #footer>
                                  <prime_button
                                    severity="success"
                                    class="class_name ml-2 cursor-pointer"
                                    size="small"
                                    @click="readNotification(notification)"
                                  >
                                    <i
                                      class="pi"
                                      :class="
                                        getNotificationIcon(
                                          notification.type_of_notification
                                        )
                                      "
                                    ></i>
                                  </prime_button>
                                </template>
                              </prime_card>
                              <!-- End Card -->
                            </div>
                            <!-- No Notifications -->
                            <div
                              class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
                              v-else
                            >
                              <div
                                class="mobile_item_12 tablet_item_12 laptop_item_12 laptop_lg_item_12 desktop_item_12 desktop_lg_item_12 py-2 px-1"
                              >
                                You don't have any unread notifications!
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- Profile  -->
                        <div class="relative ml-3">
                          <div>
                            <button
                              type="button"
                              class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                              id="user-menu-button"
                              aria-expanded="false"
                              aria-haspopup="true"
                              @click="toggleDropdown"
                            >
                              <span class="absolute -inset-1.5"></span>
                              <span class="sr-only">Open user menu</span>
                              <img
                                v-if="userStore.user.get_avatar !== 'undefined'"
                                :src="userStore.user.get_avatar"
                                class="h-8 w-8 rounded-full"
                                alt=""
                              />
                              <img
                                v-else
                                class="h-8 w-8 rounded-full"
                                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                alt=""
                              />
                            </button>
                          </div>
                          <!-- dropdown -->
                          <div
                            v-if="isDropdownOpen"
                            class="border absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                            role="menu"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu-button"
                            tabindex="-1"
                          >
                            <!-- User Profile -->
                            <div
                              class="div_wrapper_profile flex py-1 items-center cursor-pointer"
                            >
                              <div
                                class="icon_div_wrapper_profile flex justify-center items-center"
                              >
                                <RouterLink
                                  class="flex justify-center items-center"
                                  v-if="userStore.user.id"
                                  :to="{
                                    name: 'profile',
                                    params: { id: userStore.user.id },
                                  }"
                                  @click="closeDropdown"
                                >
                                  <!-- If Image -->
                                  <div class="mr-1">
                                    <span
                                      class="user_img"
                                      v-if="
                                        userStore.user.get_avatar !==
                                        'undefined'
                                      "
                                    >
                                      <img
                                        :src="userStore.user.get_avatar"
                                        class="rounded-full w-8 h-8"
                                        alt=""
                                      />
                                    </span>
                                    <span class="user_icon" v-else>
                                      <i
                                        class="pi pi-user px-2"
                                        shape="circle"
                                      ></i>
                                    </span>
                                  </div>
                                  <!-- If Name -->
                                  <div class="">
                                    <span
                                      class="user_name"
                                      v-if="userStore.user.name"
                                      >{{ userStore.user.name }}</span
                                    >
                                    <span class="user_name" v-else
                                      >Your Profile</span
                                    >
                                  </div>
                                </RouterLink>
                              </div>
                            </div>
                            <!-- Settings -->
                            <div
                              class="div_wrapper_logout flex py-1 items-center cursor-pointer"
                            >
                              <div
                                class="icon_logout flex justify-center items-center"
                                @click="closeDropdown"
                              >
                                <i class="pi pi-cog px-2" shape="circle"></i>
                                <button class="">Settings</button>
                              </div>
                            </div>
                            <!-- Sign Out -->
                            <div
                              class="div_wrapper_logout flex py-1 items-center cursor-pointer"
                              @click="logout"
                            >
                              <div
                                class="icon_logout flex justify-center items-center"
                                @click="closeDropdown"
                              >
                                <i
                                  class="pi pi-sign-out px-2"
                                  shape="circle"
                                ></i>
                                <button class="">Sign out</button>
                              </div>
                            </div>
                            <!-- Toggle Theme -->
                            <div
                              class="flex div_wrapper_toggle_theme cursor-pointer"
                              @click="closeDropdown"
                            >
                              <ThemeSwitcher />
                              <span class="mb-2">Toggle theme</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- Mobile menu, show/hide based on menu state. -->
                  <div
                    class="header_content_mobile sm:hidden"
                    id="mobile-menu"
                    v-if="isDropdownMobileOpen"
                  >
                    <div class="space-y-1 px-2 pb-3 pt-2">
                      <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                      <a
                        href="#"
                        class="block rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white"
                        aria-current="page"
                        >Dashboard</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Team</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Projects</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Calendar</a
                      >
                    </div>
                  </div>
                </nav>
              </header>
            </template>
          </prime_card>
        </div>
      </div>
    </div>
    <prime_toast />

    <RouterView />
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDropdownOpen: false,
      isDropdownMobileOpen: false,
      isDropdownNotificationsOpen: false,
      notifications: [],
      // Object to store user avatars
      userAvatars: {},
      user: {},
    };
  },
  mounted() {
    document.title = "Messenger | Home";
    // this.getNotifications()
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    closeDropdown() {
      this.isDropdownOpen = false;
    },
    toggleDropdownMobile() {
      this.isDropdownMobileOpen = !this.isDropdownMobileOpen;
    },
    closeDropdownMobile() {
      this.isDropdownMobileOpen = false;
    },
    toggleDropdownNotifications() {
      this.isDropdownNotificationsOpen = !this.isDropdownNotificationsOpen;
    },
    closeDropdownNotifications() {
      this.isDropdownNotificationsOpen = false;
    },
    getNotifications() {
      axios
        .get("/api/notifications/")
        .then((response) => {
          // console.log(`Notifications Data`, response)
          this.notifications = response.data;

          // this.notifications.forEach((notification) => {
          //   // const sender = notification.created_by
          //   // const receiver = notification.created_for
          //   // console.log(`المرسل: ${sender.name} ${sender.surname}, البريد: ${sender.email}`)
          //   // console.log(`المستلم: ${receiver.name} ${receiver.surname}, البريد: ${receiver.email}`)
          // })
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    },
    async readNotification(notification) {
      await axios
        .post(`/api/notifications/read/${notification.id}/`)
        .then((response) => {
          console.log("api/notifications/read/", response.data);
          this.$router.push({
            name: "profile",
            params: { id: notification.created_by },
          });
          this.getNotifications();
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    },
    getNotificationIcon(type) {
      const icons = {
        new_friendrequest: "pi-user-plus",
        accepted_friendrequest: "pi-check",
        post_comment: "pi-comment",
        post_like: "pi-thumbs-up-fill",
        message: "pi-envelope",
      };
      return icons[type] || "pi-bell";
    },
  },
};
</script>

<style lang="scss"></style>
