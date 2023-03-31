import Vue from "vue";
import VueRouter from "vue-router";
import TaskList from "@/views/TaskList.vue";
import IssueTypeList from "@/components/IssueTypeList.vue";
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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
