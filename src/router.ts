import { createRouter, createWebHistory } from 'vue-router'
import DefaultVue from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'


const routes = [
  {
    path: '/',
    component: DefaultVue,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
