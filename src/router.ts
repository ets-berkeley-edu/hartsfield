import { createRouter, createWebHistory } from 'vue-router'
import auth from './auth'
const Fetchurl = () => import('./views/Fetchurl.vue')

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Fetchurl',
        // Lazy-load components
        component: () => import('@/views/FetchURL.vue'),
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
