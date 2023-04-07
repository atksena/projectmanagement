<template>
  <div>
    <v-dialog
      v-model="showCreateIssue"
      width="1000"
      hide-overlay
      transition="dialog-bottom-transition"
      persistent
    >
      <create-issue
        v-if="showCreateIssue"
        :currentIssue="currentIssue"
        :index="editedIndex"
        @close="closeCreateIssue()"
      ></create-issue>
    </v-dialog>
    <v-app>
      <v-main>
        <v-container>
          <v-card>
            <v-card-title>Issue Type List</v-card-title>
            <v-spacer></v-spacer>
            <v-row class="mb-4">
              <v-card-text class="text--primary">
                <v-simple-table fixed-header height="500px">
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
                          >
                            <v-icon>mdi-delete-empty</v-icon>
                          </v-btn>
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
  name: "IssueType",
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
  watch: {
    numIssues: {
      handler(newLength) {
        localStorage.setItem("numIssues", newLength);
      },
    },
  },
  computed: {
    numIssues() {
      return this.issues.length;
    },
  },
  methods: {
    openCreateIssue() {
      this.showCreateIssue = true;
      this.issuesList();
    },
    closeCreateIssue() {
      this.showCreateIssue = false;
      this.issuesList();
      this.currentIssue = null;
      this.editedIndex = null;
    },
    deleteIssue(index) {
      if (!window.localStorage.getItem("access")) {
        this.$router.push("/loginPage");
        return;
      }
      const issueToDelete = this.issues[index];
      fetch(`/api/issues/delete/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + window.localStorage.getItem("access"),
        },
        body: JSON.stringify({ id: issueToDelete.id }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          this.issues.splice(index, 1);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    editIssue(index) {
      this.editedIndex = index;
      this.currentIssue = { ...this.issues[index] };
      this.showCreateIssue = true;
    },
    issuesList() {
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
          this.issues = data;
        });
    },
  },

  created() {
    this.issuesList();
  },
};
</script>
