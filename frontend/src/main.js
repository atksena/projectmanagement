import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "@/router";
import { Bar, Line } from "vue-chartjs";
Vue.component("bar-chart", Bar);
Vue.component("line-chart", Line);

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
