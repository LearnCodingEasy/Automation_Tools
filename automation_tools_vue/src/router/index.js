
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// Authentication
import LoginView from '../views/Authentication/LoginView.vue'

// Account
import ProfileView from '../views/Account/ProfileView.vue'

// 404 catchall Page Not Found
import PageNotFound from "@/components/PageNotFound/PageNotFound.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // 404 Catchall Page Not Found
    {
      path: "/:catchAll(.*)",
      name: "PageNotFound",
      component: PageNotFound
    },
    // Authentication [ Login ]
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    // Account [ Profile ]
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router

        