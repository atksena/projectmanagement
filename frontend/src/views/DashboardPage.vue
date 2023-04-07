<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row class="clickable">
          <v-col cols="12" md="12">
            <v-card class="ml-5 mr-5">
              <v-container>
                <v-row>
                  <v-col cols="12" sm="5">
                    <v-card outlined>
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title>Tasks</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                          <canvas id="tasks"></canvas>
                        </v-list-item-content>
                      </v-list-item>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-btn text to="/tasks">Task List</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                  <v-col cols="12" sm="5">
                    <v-card outlined>
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title>Issues</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                          <canvas id="issues"></canvas>
                        </v-list-item-content>
                      </v-list-item>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-btn text to="/issueType">Issue List</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Chart from "chart.js/auto";
export default {
  name: "DashboardPage",
  data() {
    return {
      numTasks: null,
      numCompletedTasks: null,
      numIssues: null,
      numIssueTypes: null,
      chartTasks: null,
      chartIssues: null,
    };
  },
  created() {
    this.numTasks = localStorage.getItem("numTasks");
    this.numCompletedTasks = localStorage.getItem("numCompletedTasks");
    this.numIssues = localStorage.getItem("numIssues");
    this.numIssueTypes = localStorage.getItem("numIssueTypes");
  },
  mounted() {
    this.chartTasks = new Chart(document.getElementById("tasks"), {
      type: "doughnut",
      data: {
        labels: ["Completed Tasks", "Incomplete Tasks"],
        datasets: [
          {
            label: "Task Status",
            data: [
              this.numCompletedTasks,
              this.numTasks - this.numCompletedTasks,
            ],
            backgroundColor: ["#007bff", "#6c757d"],
          },
        ],
      },
    });
    this.chartIssues = new Chart(document.getElementById("issues"), {
      type: "doughnut",
      data: {
        labels: ["Issue Types", "Issue Used"],
        datasets: [
          {
            label: "Issue Types",
            data: [this.numIssueTypes, this.numIssues - this.numIssueTypes],
            backgroundColor: ["#007bff", "#6c757d"],
          },
        ],
      },
    });
  },
};
</script>
