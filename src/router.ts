import { createRouter, createWebHistory } from 'vue-router'
import DefaultView from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import NotFound from '@/views/NotFound.vue'


const routes = [
  {
    path: '/',
    component: DefaultView,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
      },
    ],
  },
  {
    path: '/',
    component: DefaultView,
    children: [ 
      {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component:  NotFound,
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
