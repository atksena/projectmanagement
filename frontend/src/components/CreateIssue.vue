<template>
  <v-card>
    <v-toolbar color="blue-grey lighten-3">
      <v-toolbar-title>Add / Edit Issues Type</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn style="background-color: transparent" depressed @click="close">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field
          label="Name"
          name="name"
          type="text"
          v-model="issue.name"
        />
        <v-textarea
          label="Description"
          name="description"
          type="text"
          v-model="issue.description"
        ></v-textarea>
        <v-card-actions
          ><v-spacer></v-spacer>
          <v-btn class="mx-2" color="black" outlined @click="saveIssueType"
            >Add</v-btn
          ></v-card-actions
        >
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "CreateIssue",
  props: {
    currentIssue: Object,
    index: Number,
  },
  data: () => ({
    issue: {
      name: null,
      description: null,
    },
    issues: [],
  }),
  methods: {
    saveIssueType() {
      if (!window.localStorage.getItem("access")) {
        this.$router.push("/loginPage");
        return;
      }
      let url = "/api/issues/create/";
      if (this.currentIssue) {
        url = `/api/issues/update/`;
        this.issue.id = this.currentIssue.id;
        this.issuesList();
      }
      const _this = this;
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + window.localStorage.getItem("access"),
        },
        body: JSON.stringify(this.issue),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("HTTP error " + response.status);
          }
          return response.json();
        })
        .then((data) => {
          this.issues.push(data);
          this.issuesList();
          _this.close();
        })
        .catch((error) => {
          console.error(error);
        });
    },

    close() {
      this.$emit("close");
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
    if (this.currentIssue) {
      this.issue = { ...this.currentIssue };
    }
  },
};
</script>
