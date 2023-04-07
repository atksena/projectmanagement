import Vue from "vue";
import VueRouter from "vue-router";
import TaskList from "@/views/TaskList.vue";
import IssueTypeList from "@/components/IssueTypeList.vue";
import LoginPage from "@/components/LoginPage.vue";
import DashboardPage from "@/views/DashboardPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/tasks",
    component: TaskList,
  },
  {
    path: "/issueType",
    component: IssueTypeList,
  },
  {
    path: "/loginPage",
    component: LoginPage,
  },

  {
    path: "/dashboardPage",
    component: DashboardPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
