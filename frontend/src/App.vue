<template>
  <v-app>
    <v-main>
      <v-navigation-drawer
        v-if="loggedIn"
        v-model="drawer"
        :mini-variant.sync="mini"
        permanent
        color="#2C3A47"
        dark
        app
      >
        <v-sheet color="#2C3A47" class="pa-4">
          <v-img :src="require('@/assets/download.png')" class="mb-4"></v-img>
        </v-sheet>
        <v-list shaped class="clickable">
          <template v-for="item in items">
            <v-list-group
              v-if="item.children"
              :key="item.text"
              v-model="item.model"
              :prepend-icon="item['icon-ctr']"
              :append-icon="item.model ? item.icon : item['icon-alt']"
              active-class="blue--text"
            >
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </template>
              <v-list-item
                v-for="(child, i) in item.children"
                :key="i"
                route
                :to="child.route"
                active-class="blue--text"
              >
                <v-list-item-action v-if="child.icon">
                  <v-icon>{{ child.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ child.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
            <v-list-item
              v-else
              :key="item.text"
              active-class="blue--text"
              route
              :to="item.route"
            >
              <v-list-item-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  {{ item.text }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
        <v-btn
          color="#2C3A47"
          fab
          small
          fixed
          bottom
          right
          absolute
          class="clickable"
          style="margin-right: 10px; margin-bottom: 10px"
          @click.stop="mini = !mini"
        >
          <v-icon> mdi-arrow-up </v-icon>
        </v-btn>
      </v-navigation-drawer>
      <v-app-bar app color="#2C3A47" dark>
        <v-spacer />
        <v-toolbar-title class="white--text">{{ username }}</v-toolbar-title>
        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on">
              <v-icon>mdi-account</v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item>
              <v-list-item-title v-on:click="goToLogin"
                >Login</v-list-item-title
              >
            </v-list-item>
            <v-list-item>
              <v-list-item-title v-on:click="logout">Logout</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
      <v-btn
        bottom
        color="#2C3A47"
        dark
        fab
        fixed
        right
        @click="toTop"
        class="clickable"
      >
        <v-icon>mdi-chevron-up</v-icon>
      </v-btn>
    </v-main>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  components: {},
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
    mini: false,
    fab: false,
    showLogin: true,
    username: window.localStorage.getItem("username"),
    items: [
      { icon: "mdi-home", text: "Dashboard", route: "/dashboardPage" },
      {
        icon: "mdi-calendar-check",
        text: "Task List",
        route: "/tasks",
      },
      {
        icon: "mdi-alert-circle-outline",
        text: "Issue Type",
        route: "/issueTYpe",
      },
    ],
  }),
  computed: {
    loggedIn() {
      return window.localStorage.getItem("access") !== null;
    },
  },
  methods: {
    toTop() {
      this.$vuetify.goTo(0);
    },
    goToLogin() {
      this.$router.push("/loginPage");
    },
    logout() {
      window.localStorage.removeItem("access");
      window.localStorage.removeItem("username");
      window.location.href = "/loginPage";
    },
  },
};
</script>
