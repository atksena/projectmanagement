<template>
  <v-app>
    <v-main>
      <v-app-bar color="navy" dark>
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
        <v-toolbar-title>Project Management</v-toolbar-title>
      </v-app-bar>

      <v-navigation-drawer v-model="drawer" absolute>
        <v-list nav dense>
          <v-list-item-group
            v-model="group"
            active-class="navy--text text--accent-4"
          >
            <v-list-item>
              <v-list-item-title @click="goToTaskList"
                >Task List</v-list-item-title
              >
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goToIssueType"
                >Issue Type</v-list-item-title
              >
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-main>
    <router-view></router-view>
  </v-app>
</template>

<script>
import TaskList from "@/views/TaskList.vue";
import IssueTypeList from "@/components/IssueTypeList.vue";

export default {
  name: "App",
  // eslint-disable-next-line vue/no-unused-components
  components: { TaskList, IssueTypeList },
  data: () => ({
    drawer: false,
    group: null,
  }),
  methods: {
    goToTaskList() {
      this.$router.push({ path: "/tasks" });
    },
    goToIssueType() {
      this.$router.push({ path: "/issueTYpe" });
    },
  },
};
</script>
