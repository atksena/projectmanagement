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
            >Create</v-btn
          ></v-card-actions
        >
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
export default {
  name: "CreateIssue",
  props: {
    currentIssue: Object,
    index: Number,
  },
  data: () => ({
    issue: {
      id: null,
      name: null,
      description: null,
    },
    issues: [],
  }),
  methods: {
    resetIssue() {
      this.issue = {
        name: null,
        description: null,
      };
    },
    saveIssueType() {
      if (this.issue.id === null) {
        this.issue.id = uuidv4();
      }
      if (this.index !== null) {
        this.issues[this.index] = this.issue;
      } else {
        this.issues.push(this.issue);
      }
      this.resetIssue();
      console.log(this.issues);

      localStorage.setItem("issues", JSON.stringify(this.issues));
      this.close();
    },
    close() {
      this.$emit("close");
    },
  },
  created() {
    if (localStorage.getItem("issues") !== null) {
      this.issues = JSON.parse(localStorage.getItem("issues"));
    }
    if (this.currentIssue) {
      this.issue = { ...this.currentIssue };
    }
  },
};
</script>
