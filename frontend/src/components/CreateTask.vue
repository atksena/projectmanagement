<template>
  <v-card>
    <v-toolbar color="blue-grey lighten-3">
      <v-toolbar-title>Add / Edit Task</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn style="background-color: transparent" depressed @click="close">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Summary"
          name="summary"
          type="text"
          v-model="task.summary"
        />
        <v-textarea
          label="Description"
          name="description"
          type="text"
          v-model="task.description"
        ></v-textarea>
        <v-select
          v-model="task.priority"
          :items="items"
          label="Priority"
          outlined
        ></v-select>
        <v-select
          v-model="task.issue_type"
          :items="issuesNameItems"
          label="Issue Type"
          outlined
          item-value="id"
          item-text="name"
        ></v-select>
        <v-card-actions
          ><v-spacer></v-spacer>
          <v-btn class="mx-2" color="black" outlined @click="saveTask"
            >Add</v-btn
          ></v-card-actions
        >
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "CreateTask",
  props: {
    currentTask: Object,
    index: Number,
  },
  data: () => ({
    items: ["highest", "high", "medium", "low"],
    task: {
      summary: null,
      description: null,
      priority: null,
      issue_type: null,
    },
    tasks: [],
    issuesNameItems: [],
  }),
  methods: {
    saveTask() {
      if (!window.localStorage.getItem("access")) {
        this.$router.push({ name: "LoginPage" });
        return;
      }

      let url = "/api/tasks/create/";
      if (this.currentTask) {
        url = `/api/tasks/update/`;
        this.task.id = this.currentTask.id;
      }
      const _this = this;
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${window.localStorage.getItem("access")}`,
        },
        body: JSON.stringify(this.task),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          return response.json();
        })
        .then((data) => {
          this.tasks.push(data);
          _this.close();
        })
        .catch((error) => {
          console.error(error);
        });
    },

    close() {
      this.$emit("close");
    },
    loadIssuesNameOptions() {
      const access = window.localStorage.getItem("access");
      if (!access) {
        window.location.href = "/loginPage";
        return;
      }
      fetch("/api/issues/list/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
        },
        body: JSON.stringify(this.issues),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          return response.json();
        })
        .then((data) => {
          this.issuesNameItems = data;
        });
    },
  },
  created() {
    this.loadIssuesNameOptions();
    if (this.currentTask) {
      this.task = { ...this.currentTask };
    }
  },
};
</script>
