<template>
  <div>
    <v-dialog
      v-model="showCreateTask"
      width="1000"
      hide-overlay
      transition="dialog-bottom-transition"
      persistent
    >
      <create-task
        v-if="showCreateTask"
        :currentTask="currentTask"
        :index="editedIndex"
        @close="closeCreateTask()"
      ></create-task>
    </v-dialog>
    <v-app>
      <v-main>
        <v-container>
          <v-card>
            <v-card-title>Task List</v-card-title>
            <v-spacer></v-spacer>
            <v-row class="mb-4">
              <v-card-text class="text--primary">
                <v-simple-table fixed-header height="700px">
                  <template v-slot:default>
                    <thead>
                      <tr>
                        <th class="text-left">Summary</th>
                        <th class="text-left">Description</th>
                        <th class="text-left">Priority</th>
                        <th class="text-left">Issue Type</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(task, index) in tasks"
                        :key="index"
                        :class="task.priority"
                      >
                        <td>{{ task.summary }}</td>
                        <td>{{ task.description }}</td>
                        <td>{{ task.priority }}</td>
                        <td>{{ task.issue_type__name }}</td>
                        <td>
                          <v-btn
                            @click="deleteTask(index)"
                            style="border: none; background-color: transparent"
                            class="mx-2"
                            outlined
                          >
                            <v-icon>mdi-delete-empty</v-icon></v-btn
                          >
                          <v-btn
                            @click="editTask(task)"
                            style="border: none; background-color: transparent"
                            class="mx-2"
                            outlined
                          >
                            <v-icon>mdi-pencil-outline</v-icon>
                          </v-btn>
                        </td>
                        <td>
                          <input type="checkbox" v-model="task.completed" />
                        </td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-card-text>
            </v-row>
            <v-footer>
              <v-spacer></v-spacer>
              <v-btn
                class="mx-2"
                color="black"
                dark
                outlined
                @click="openCreateTask()"
                >Add Task</v-btn
              ></v-footer
            >
          </v-card>
        </v-container>
      </v-main>
      <router-view></router-view>
    </v-app>
  </div>
</template>
<script>
import CreateTask from "@/components/CreateTask.vue";

export default {
  components: { CreateTask },
  name: "TaskList",
  data() {
    return {
      showDeleteDialog: false,
      taskToDeleteIndex: null,
      showCreateTask: false,
      currentTask: null,
      editedIndex: null,
      tasks: [],
    };
  },
  watch: {
    tasks: {
      handler(newTasks) {
        localStorage.setItem("tasks", JSON.stringify(newTasks));
      },
      deep: true,
    },
    numTasks: {
      handler(value) {
        localStorage.setItem("numTasks", value);
      },
      immediate: true,
    },
    numCompletedTasks: {
      handler(value) {
        localStorage.setItem("numCompletedTasks", value);
      },
      immediate: true,
    },
    numIssueTypes: {
      handler(value) {
        localStorage.setItem("numIssueTypes", value);
      },
      immediate: true,
    },
  },
  computed: {
    numTasks() {
      return this.tasks.length;
    },
    numCompletedTasks() {
      return this.tasks.filter((task) => task.completed).length;
    },
    // eslint-disable-next-line vue/return-in-computed-property
    numIssueTypes() {
      let issueTypes = [];
      for (let i = 0; i < this.tasks.length; i++) {
        issueTypes.push(this.tasks[i].issue_type__name);
      }
      let uniqueIssueTypes = new Set(issueTypes);
      let numIssueTypes = uniqueIssueTypes.size;
      return numIssueTypes;
    },
  },
  methods: {
    openCreateTask() {
      this.showCreateTask = true;
    },
    closeCreateTask() {
      this.showCreateTask = false;
      this.taskList();
      this.currentTask = null;
      this.editedIndex = null;
    },
    deleteTask(index) {
      if (!window.localStorage.getItem("access")) {
        this.$router.push("/loginPage");
        return;
      }

      const taskToDelete = this.tasks[index];
      fetch(`/api/tasks/delete/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + window.localStorage.getItem("access"),
        },
        body: JSON.stringify({ id: taskToDelete.id }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          this.tasks.splice(index, 1);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    editTask(task, index) {
      this.currentTask = { ...task };
      this.editedIndex = index;
      this.showCreateTask = true;
    },
    taskList() {
      const access = window.localStorage.getItem("access");
      if (!access) {
        window.location.href = "/loginPage";
        return;
      }

      fetch("/api/tasks/list/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
        },
        body: JSON.stringify(this.tasks),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          return response.json();
        })
        .then((data) => {
          this.tasks = data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    const tasks = localStorage.getItem("tasks");
    if (tasks) {
      this.tasks = JSON.parse(tasks);
    } else {
      this.taskList();
    }
  },
};
</script>
