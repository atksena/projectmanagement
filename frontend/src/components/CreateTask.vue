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
          v-model="task.issuesName"
          :items="issuesNameItems"
          label="Issue Type"
          outlined
        ></v-select>
        <v-card-actions
          ><v-spacer></v-spacer>
          <v-btn class="mx-2" color="black" outlined @click="saveTask"
            >Create</v-btn
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
    items: ["Highest", "High", "Medium", "Low"],
    task: {
      summary: null,
      description: null,
      priority: null,
      issuesName: null,
    },
    tasks: [],
    issues: [],
  }),
  computed: {
    issuesNameItems() {
      return this.issues.map((issue) => issue.name);
    },
  },
  methods: {
    resetTask() {
      this.task = {
        summary: null,
        description: null,
        priority: null,
        issuesName: null,
      };
    },
    saveTask() {
      if (this.index !== null) {
        this.tasks[this.index] = this.task;
      } else {
        this.tasks.push(this.task);
      }
      this.resetTask();
      console.log(this.tasks);

      localStorage.setItem("tasks", JSON.stringify(this.tasks));
      fetch("http://localhost", {
        method: "POST",
        body: JSON.stringify(this.tasks),
      });
      this.close();
    },
    close() {
      this.$emit("close");
    },
    getIssueType() {
      this.issues = JSON.parse(localStorage.getItem("issues"));
    },
  },
  created() {
    if (localStorage.getItem("tasks") !== null) {
      this.tasks = JSON.parse(localStorage.getItem("tasks"));
    }
    if (this.currentTask) {
      this.task = { ...this.currentTask };
    }
    if (localStorage.getItem("issues") !== null) {
      this.getIssueType();
    }
  },
};
</script>
