<template>
  <div>
    <v-dialog
      v-model="showCreateIssue"
      width="1000"
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <create-issue
        v-if="showCreateIssue"
        :currentTask="currentIssue"
        :index="editedIndex"
        @close="closeCreateIssue()"
      ></create-issue>
    </v-dialog>
    <v-dialog v-model="showDeleteDialog">
      <v-card>
        <v-card-title>
          Are you sure you want to delete this task?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancelDelete">Cancel</v-btn>
          <v-btn @click="confirmDelete" color="red">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-app>
      <v-main>
        <v-container>
          <v-card>
            <v-card-title>Issue Type List</v-card-title>
            <v-spacer></v-spacer>
            <v-row class="mb-4">
              <v-card-text class="text--primary">
                <v-simple-table fixed-header height="300px">
                  <template v-slot:default>
                    <thead>
                      <tr>
                        <th class="text-left">Name</th>
                        <th class="text-left">Description</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(issue, index) in issues" :key="index">
                        <td>{{ issue.name }}</td>
                        <td>{{ issue.description }}</td>
                        <td>
                          <v-btn
                            @click="deleteIssue(index)"
                            style="border: none; background-color: transparent"
                            class="mx-2"
                            outlined
                            ><v-icon>mdi-delete-empty</v-icon></v-btn
                          >
                          <v-btn
                            @click="editIssue(index)"
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
                @click="openCreateIssue()"
                >Add Issue Type</v-btn
              ></v-footer
            >
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </div>
</template>
<script>
import CreateIssue from "@/components/CreateIssue.vue";

export default {
  // eslint-disable-next-line vue/no-unused-components
  components: { CreateIssue },
  name: "IssueTYpe",
  data() {
    return {
      showDeleteDialog: false,
      issueToDeleteIndex: null,
      showCreateIssue: false,
      currentIssue: null,
      editedIndex: null,
      issues: [],
    };
  },
  methods: {
    openCreateIssue() {
      this.showCreateIssue = true;
      this.issues = JSON.parse(localStorage.getItem("issues")) || [];
    },
    closeCreateIssue() {
      this.showCreateIssue = false;
      this.issues = JSON.parse(localStorage.getItem("issues")) || [];
      this.currentIssue = null;
      this.editedIndex = null;
    },
    deleteIssue(index) {
      this.issueToDeleteIndex = index;
      this.showDeleteDialog = true;
    },
    confirmDelete() {
      this.issues.splice(this.issueToDeleteIndex, 1);
      localStorage.setItem("issues", JSON.stringify(this.issues));
      this.showDeleteDialog = false;
      this.issueToDeleteIndex = null;
    },
    cancelDelete() {
      this.showDeleteDialog = false;
      this.issueToDeleteIndex = null;
    },
    editIssue(index) {
      this.editedIndex = index;
      this.currentIssue = this.issues[index];
      this.showCreateIssue = true;
    },
  },
  created() {
    this.issues = JSON.parse(localStorage.getItem("issues")) || [];
  },
};
</script>
