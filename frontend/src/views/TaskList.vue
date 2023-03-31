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
    <v-dialog v-model="showDeleteDialog">
      <v-card>
        <v-card-title>
          Are you sure you want to delete this task?
        </v-card-title>
        <v-card-actions
          ><v-spacer></v-spacer>
          <v-btn @click="cancelDelete">Cancel</v-btn>
          <v-btn @click="confirmDelete" color="red">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-app>
      <v-main>
        <v-container>
          <v-card>
            <v-card-title>Task List</v-card-title>
            <v-spacer></v-spacer>
            <v-row class="mb-4">
              <v-card-text class="text--primary">
                <v-simple-table fixed-header height="300px">
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
                        :class="priorityClass(task.priority)"
                      >
                        <td>{{ task.summary }}</td>
                        <td>{{ task.description }}</td>
                        <td>{{ task.priority }}</td>
                        <td>{{ task.issuesName }}</td>
                        <td>
                          <v-btn
                            @click="deleteTask(index)"
                            style="border: none; background-color: transparent"
                            class="mx-2"
                            outlined
                            ><v-icon>mdi-delete-empty</v-icon></v-btn
                          >
                          <v-btn
                            @click="editTask(index)"
                            style="border: none; background-color: transparent"
                            class="mx-2"
                            outlined
                          >
                            <v-icon>mdi-pencil</v-icon>
                          </v-btn>
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
  methods: {
    openCreateTask() {
      this.showCreateTask = true;
      this.tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    },
    closeCreateTask() {
      this.showCreateTask = false;
      this.tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      this.currentTask = null;
      this.editedIndex = null;
    },
    deleteTask(index) {
      this.taskToDeleteIndex = index;
      this.showDeleteDialog = true;
    },
    confirmDelete() {
      this.tasks.splice(this.taskToDeleteIndex, 1);
      localStorage.setItem("tasks", JSON.stringify(this.tasks));
      this.showDeleteDialog = false;
      this.taskToDeleteIndex = null;
    },
    cancelDelete() {
      this.showDeleteDialog = false;
      this.taskToDeleteIndex = null;
    },
    editTask(index) {
      this.editedIndex = index;
      this.currentTask = this.tasks[index];
      this.showCreateTask = true;
    },
    priorityClass(priority) {
      return {
        "bd-red": priority === "Highest",
        "bg-orange": priority === "High",
        "bg-yellow": priority === "Medium",
        "bg-green": priority === "Low",
      };
    },
  },
  created() {
    this.tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  },
};
</script>
