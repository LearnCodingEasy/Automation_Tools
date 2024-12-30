<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

import { Background } from "@vue-flow/background";
import { Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import { VueFlow, Panel, useVueFlow } from "@vue-flow/core";
import CustomNode from "../components/CustomNode.vue";
import CustomEdge from "../components/CustomEdge.vue";
import vuedraggable from "vuedraggable";

// VueFlow hooks
const { onConnect, addEdges } = useVueFlow();

// Nodes and edges state
const nodes = ref([]);
const edges = ref([]);

// Programs fetched from the database
const programs = ref([]);

// Fetch programs from database
const gatDatabaseList = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/programs/program_list/"
    );
    programs.value = response.data;
  } catch (error) {
    console.error("Error fetching programs:", error);
  }
};

// Function to add a new node with a program
const addNodeWithProgram = (program) => {
  const id = Date.now().toString();
  nodes.value.push({
    id,
    position: { x: Math.random() * 300, y: Math.random() * 300 },
    data: { label: program.name },
  });
};

// Handle drag and drop
const onDragEnd = (event) => {
  const programId = event.dataTransfer.getData("text/plain");
  const program = programs.value.find((p) => p.id === programId);
  if (program) addNodeWithProgram(program);
};

// Initialize the component
onMounted(() => {
  gatDatabaseList();
});
</script>

<template>
  <main>
    <div class="" style="display: none">
      <div
        class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
        style="height: 90vh"
      >
        <!-- Sidebar with Programs -->
        <div
          class="mobile_item_2 tablet_item_2 laptop_item_2 laptop_lg_item_2 desktop_item_2 desktop_lg_item_2 border_test"
        >
          <div class="p-4 border">
            <h2 class="mt-5">قائمة البرامج</h2>
            <vuedraggable
              v-model="programs"
              item-key="id"
              class="list-group"
              :move="onMove"
              @end="onDragEnd"
            >
              <template v-slot:item="program">
                <div :key="program.id" class="list-group-item">
                  <prime_button
                    icon="pi pi-play"
                    :label="program.name"
                    class="w-full mb-2"
                    @click="addNodeWithProgram(program)"
                  />
                  <!-- Add click handler -->
                </div>
              </template>
            </vuedraggable>
          </div>
        </div>

        <!-- Main VueFlow Area -->
        <div
          class="mobile_item_10 tablet_item_10 laptop_item_10 laptop_lg_item_10 desktop_item_10 desktop_lg_item_10"
        >
          <VueFlow
            v-model:nodes="nodes"
            v-model:edges="edges"
            fit-view-on-init
            class="vue-flow-basic-example vue_flow_node_custom"
            :default-zoom="1.5"
            :min-zoom="0.2"
            :max-zoom="4"
          >
            <Background pattern-color="#f4f5f8" :gap="10" />
            <MiniMap />
            <Controls />
            <template #node-custom="nodeProps">
              <CustomNode v-bind="nodeProps" />
            </template>
            <template #edge-custom="edgeProps">
              <CustomEdge v-bind="edgeProps" />
            </template>
            <Panel>
              <button type="button" @click="addNode">Add a node</button>
              <button type="button" @click="removeNode('1')">
                Remove Node 1
              </button>
              <button type="button" @click="removeNode('2')">
                Remove Node 2
              </button>
            </Panel>
          </VueFlow>
        </div>
      </div>
    </div>
    <div class="" style="display: none">
      <div
        class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
        style="height: 90vh"
      >
        <!-- Sidebar with Programs -->
        <div
          class="mobile_item_2 tablet_item_2 laptop_item_2 laptop_lg_item_2 desktop_item_2 desktop_lg_item_2 border_test"
        >
          <div class="p-4 border">
            <h2 class="mt-5">قائمة البرامج</h2>
            <vuedraggable
              v-model="programsTest"
              item-key="id"
              class="list-group"
              :move="onMove"
              @end="onDragEnd"
            >
              <template v-slot:item="program">
                <div
                  :key="program.id"
                  class="list-group-item"
                  draggable="true"
                  @dragstart="
                    (event) =>
                      event.dataTransfer.setData('text/plain', program.id)
                  "
                >
                  <prime_button
                    icon="pi pi-play"
                    :label="program.name"
                    class="w-full mb-2"
                    @click="addNodeWithProgram(program)"
                  />
                </div>
              </template>
            </vuedraggable>
          </div>
        </div>

        <!-- Main VueFlow Area -->
        <div
          class="mobile_item_10 tablet_item_10 laptop_item_10 laptop_lg_item_10 desktop_item_10 desktop_lg_item_10"
        >
          <VueFlow
            v-model:nodes="nodes"
            v-model:edges="edges"
            fit-view-on-init
            class="vue-flow-basic-example vue_flow_node_custom"
            :default-zoom="1.5"
            :min-zoom="0.2"
            :max-zoom="4"
          >
            <Background pattern-color="#f4f5f8" :gap="10" />
            <MiniMap />
            <Controls />
            <template #node-custom="nodeProps">
              <CustomNode v-bind="nodeProps" />
            </template>
            <template #edge-custom="edgeProps">
              <CustomEdge v-bind="edgeProps" />
            </template>
            <Panel>
              <button type="button" @click="addNode">Add a node</button>
              <button type="button" @click="removeNode('1')">
                Remove Node 1
              </button>
              <button type="button" @click="removeNode('2')">
                Remove Node 2
              </button>
            </Panel>
          </VueFlow>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-12 h-screen">
      <!-- Sidebar with programs -->
      <div class="col-span-2 border p-4">
        <h2 class="text-lg font-bold mb-4">قائمة البرامج</h2>

        <vuedraggable v-model="programs" item-key="id" class="list-group">
          <template v-slot:item="{ element: program }">
            <div
              :key="program.id"
              class="list-group-item p-2 border rounded cursor-pointer"
              draggable="true"
              @dragstart="
                (event) => event.dataTransfer.setData('text/plain', program.id)
              "
            >
              {{ program.name }}
            </div>
          </template>
        </vuedraggable>
      </div>

      <!-- VueFlow workspace -->
      <div class="col-span-10">
        <h1>VueFlow workspace</h1>

        <VueFlow
          v-model:nodes="nodes"
          v-model:edges="edges"
          fit-view-on-init
          class="vue-flow-basic-example vue_flow_node_custom"
          :default-zoom="1.5"
          :min-zoom="0.2"
          :max-zoom="4"
        >
          <Background pattern-color="#f4f5f8" :gap="10" />
          <MiniMap />
          <Controls />
          <template #node-custom="nodeProps">
            <CustomNode v-bind="nodeProps" />
          </template>
          <template #edge-custom="edgeProps">
            <CustomEdge v-bind="edgeProps" />
          </template>
          <Panel>
            <button type="button" @click="addNode">Add a node</button>
            <button type="button" @click="removeNode('1')">
              Remove Node 1
            </button>
            <button type="button" @click="removeNode('2')">
              Remove Node 2
            </button>
          </Panel>
        </VueFlow>
      </div>
    </div>
  </main>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
// For draggable functionality
import vuedraggable from "vuedraggable";

export default {
  setup() {
    const form = ref({ name: "", path: "" });
    const programs = ref([]);

    return { form, programs, submitForm };
  },
  data() {
    return {
      statusOptions: [
        { name: "NEWWINDOW", code: "--new-window" },
        { name: "CURRENTWINDOW", code: "current window" },
        { name: "IN_MAKING", code: "In Making" },
      ],
      name: "",
      program_path: "",
      command_line_args: "",
      window_type: "NEWWINDOW",
      errors: [],
      programs: [],
      nodes: [], // Nodes array for VueFlow
      edges: [], // Edges array for VueFlow
    };
  },

  methods: {
    gatDatabaseList() {
      fetch("http://127.0.0.1:8000/api/programs/program_list/")
        .then((response) => response.json())
        .then((data) => {
          this.programs = data;
          console.log(data);
        })
        .catch((error) => console.error("Fetch error:", error));
    },
    submitForm() {
      this.errors = [];
      let formData = new FormData();
      // Name
      if (this.name == "") {
        this.$toast.add({
          severity: "error",
          summary: "Type Script Title",
          detail: "Your Script Title is missing",
          life: 3000,
        });
        this.errors.push("Type Script Title");
      } else if (this.title !== "") {
        formData.append("name", this.name);
      }
      // Program Path
      if (!this.program_path.trim()) {
        this.errors.push("Program Path is required");
        this.$toast.add({
          severity: "error",
          summary: "Program Path Missing",
          detail: "Please enter a valid program path.",
          life: 3000,
        });
      } else {
        formData.append("program_path", this.program_path);
      }

      // Command Line Args
      if (this.command_line_args.trim()) {
        formData.append("command_line_args", this.command_line_args);
      }

      // Window Type
      formData.append("window_type", this.window_type);

      // All Is Good
      if (this.errors.length === 0) {
        axios
          .post("/api/programs/program_create/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            console.log("Data Is Send To Django: ", response.data);
            this.$toast.add({
              severity: "success",
              summary: "Script Done",
              detail: "Good Script Youtube Adding.",
              life: 3000,
            });
          })
          .catch((error) => {
            console.log("error", error);
            console.log("error", error);

            // console.log("error.response.data", error.response.data);
            this.$toast.add({
              severity: "error",
              summary: `Type Script Error`,
              detail: `Error = ${error.response}`,
              life: 3000,
            });
          });
      }
    },
    async runProgram(id) {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/programs/run/${id}/`
        );
        alert(response.data.message);
      } catch (error) {
        console.error(error);
        alert("Failed to run program.");
      }
    },
    async openVscode() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/programs/open_vscode/`
        );
        alert(response.data.message);
      } catch (error) {
        console.error(error);
        alert("Failed to run program.");
      }
    },
  },

  mounted() {
    this.gatDatabaseList();
  },
};
</script>

<style>
/* Use a purple theme for our custom node */
.vue_flow_node_custom {
  background: purple;
  color: white;
  border: 1px solid purple;
  border-radius: 4px;
  box-shadow: 0 0 0 1px purple;
  padding: 8px;
}
.style_tow {
  background: rgb(38, 0, 128);
  color: white;
  border: 1px solid rgb(38, 0, 128);
  border-radius: 4px;
  box-shadow: 0 0 0 1px rgb(38, 0, 128);
  padding: 8px;
}
</style>

<!--
Vue
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install primevue primeicons
npm install @primevue/forms
npm install @primevue/themes
npm install quill
npm install -D sass@latest
npm install axios
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
npm install -D vite-plugin-pwa
npm i prismjs
npm i vue-prism-component
npm i swiper
npm install @vue-flow/core
npm install @vue-flow/background
npm install @vue-flow/controls
npm install @vue-flow/minimap
npm install lodash
npm install @dagrejs/dagre
npm install vuedraggable@next

Django
python -m venv automation_tools_virtual_environment
automation_tools_virtual_environment\\Scripts\\activate
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install pillow
django-admin startproject automation_tools_django
python manage.py startapp user_account
python manage.py startapp program
python manage.py startapp workflow
python manage.py createsuperuser
-->
<!--
<div class="" style="display: none">
      <div
        class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
        style="height: 90vh"
      >
        <div
          class="mobile_item_3 tablet_item_3 laptop_item_3 laptop_lg_item_3 desktop_item_3 desktop_lg_item_3 p-4 border"
        >
          <h2 class="mt-5">قائمة البرامج</h2>
          <ul>
            <li v-for="program in programs" :key="program.id">
              <prime_button
                icon="pi pi-plus"
                :label="program.name"
                class="class_name"
                @click="runProgram(program.id)"
              />
            </li>
          </ul>
        </div>
        <div
          class="mobile_item_9 tablet_item_9 laptop_item_9 laptop_lg_item_9 desktop_item_9 desktop_lg_item_9 p-4 border"
        >
          <div>
            <h2>إضافة برنامج جديد</h2>
            <form @submit.prevent="submitForm">
              <div class="">
                <label for="programPath">Program Name:</label>

                <prime_input_text
                  v-model="name"
                  placeholder="Program Name"
                  class="mb-3"
                />
              </div>
              <!-- <prime_input_text
            v-model="formAddProgram.program_path"
            placeholder="مسار البرنامج"
            class="mb-3"
          />
          <div>
            <label for="programPath">Program Path:</label>
            <prime_input_text
              type="text"
              v-model="program_path"
              placeholder="Program Path"
              id="programPath"
              required
            />
          </div>

          <div>
            <label for="commandLineArgs">Command Line Args:</label>
            <prime_input_text
              type="text"
              v-model="command_line_args"
              placeholder="Command Line Args [.]"
              id="commandLineArgs"
            />
          </div>

          <!-- <div>
        <label for="windowType">Window Type:</label>
        <select v-model="window_type" id="windowType">
          <option value="new">New Window</option>
          <option value="current">Current Window</option>
        </select>
      </div>
          <Status List
          <div class="card flex justify-center">
            <prime_list_box
              v-model="window_type"
              :options="statusOptions"
              optionLabel="name"
              checkmark
              :highlightOnSelect="false"
              class="w-full md:w-56"
            />
          </div>

           <button label="" type="submit">إضافة البرنامج</button>
          <div class="send">
            <prime_button
              @click="submitForm"
              label="Submit"
              severity="success"
              icon="pi pi-send"
              iconPos="right"
            ></prime_button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div>
    <div style="height: 100vh; position: relative; margin-bottom: 15rem">
      <VueFlow
        v-model:nodes="nodes"
        v-model:edges="edges"
        fit-view-on-init
        class="vue-flow-basic-example vue_flow_node_custom"
        :default-zoom="1.5"
        :min-zoom="0.2"
        :max-zoom="4"
      >
        <Background pattern-color="#f4f5f8" :gap="10" />
        <MiniMap />
        <Controls />
        <template #node-custom="nodeProps">
          <CustomNode v-bind="nodeProps" />
        </template>
        <template #edge-custom="edgeProps">
          <CustomEdge v-bind="edgeProps" />
        </template>
        <Panel>
          <button type="button" @click="addNode">Add a node</button>
          <button type="button" @click="removeNode('1')">
            Remove Node 1
          </button>
          <button type="button" @click="removeNode('2')">
            Remove Node 2
          </button>
        </Panel>
      </VueFlow>
    </div>

    <h1>Header 1</h1>
    <div class="">
      <VueFlow class="style_tow" v-model="elements" />
    </div>
  </div>
  <hr />
  <hr />
  <hr />
  <div class="">
    <div
      class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
      style="height: 90vh"
    >
      <div
        class="mobile_item_3 tablet_item_3 laptop_item_3 laptop_lg_item_3 desktop_item_3 desktop_lg_item_3 p-4 border"
      >
        <h2 class="mt-5">قائمة البرامج</h2>
        <ul>
          <li v-for="program in programs" :key="program.id">
            <prime_button
              icon="pi pi-play"
              :label="program.name"
              class="w-full mb-2"
              @click="runProgram(program.id)"
            />
          </li>
        </ul>
      </div>

      <div
        class="mobile_item_9 tablet_item_9 laptop_item_9 laptop_lg_item_9 desktop_item_9 desktop_lg_item_9 p-4 border"
      ></div>
    </div>
  </div>
  <hr />
  <hr />
  <hr />
  <div class="">
    <div
      class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
      style="height: 90vh"
    >
      <div
        class="mobile_item_3 tablet_item_3 laptop_item_3 laptop_lg_item_3 desktop_item_3 desktop_lg_item_3 p-4 border"
      >
        <h2 class="mt-5">قائمة البرامج</h2>
        <ul>
          <li v-for="program in programs" :key="program.id">
            <prime_button
              icon="pi pi-play"
              :label="program.name"
              class="w-full mb-2"
              @click="runProgram(program.id)"
            />
          </li>
        </ul>
      </div>

      <div
        class="mobile_item_9 tablet_item_9 laptop_item_9 laptop_lg_item_9 desktop_item_9 desktop_lg_item_9 p-4 border"
      >
        <VueFlow
          v-model:nodes="nodes"
          v-model:edges="edges"
          fit-view-on-init
          class="vue-flow-basic-example vue_flow_node_custom"
          :default-zoom="1.5"
          :min-zoom="0.2"
          :max-zoom="4"
        >
          <Background pattern-color="#f4f5f8" :gap="10" />
          <MiniMap />
          <Controls />
          <template #node-custom="nodeProps">
            <CustomNode v-bind="nodeProps" />
          </template>
          <template #edge-custom="edgeProps">
            <CustomEdge v-bind="edgeProps" />
          </template>
          <Panel>
            <button type="button" @click="addNode">Add a node</button>
            <button type="button" @click="removeNode('1')">
              Remove Node 1
            </button>
            <button type="button" @click="removeNode('2')">
              Remove Node 2
            </button>
          </Panel>
        </VueFlow>
      </div>
    </div>
  </div>
  <hr />
  <hr />
  <hr />
  <div class="">
    <div
      class="w-full mobile_grid_12 tablet_grid_12 laptop_grid_12 laptop_lg_grid_12 desktop_grid_12 desktop_lg_grid_12"
      style="height: 90vh"
    >
      <div
        class="mobile_item_3 tablet_item_3 laptop_item_3 laptop_lg_item_3 desktop_item_3 desktop_lg_item_3 p-4 border"
      >
        <h2 class="mt-5">قائمة البرامج</h2>
        <ul>
          <li v-for="program in programs" :key="program.id">
            <prime_button
              icon="pi pi-play"
              :label="program.name"
              class="w-full mb-2"
              @click="runProgram(program.id)"
              @dblclick="removeProgram(program.id)"
            />
          </li>
        </ul>
      </div>

      <div
        class="mobile_item_9 tablet_item_9 laptop_item_9 laptop_lg_item_9 desktop_item_9 desktop_lg_item_9 p-4 border"
      >
        <VueFlow
          v-model:nodes="nodes"
          v-model:edges="edges"
          fit-view-on-init
          class="vue-flow-basic-example vue_flow_node_custom"
          :default-zoom="1.5"
          :min-zoom="0.2"
          :max-zoom="4"
        >
          <Background pattern-color="#f4f5f8" :gap="10" />
          <MiniMap />
          <Controls />
          <template #node-custom="nodeProps">
            <CustomNode v-bind="nodeProps" />
          </template>
          <template #edge-custom="edgeProps">
            <CustomEdge v-bind="edgeProps" />
          </template>
          <Panel>
            <button type="button" @click="addNode">Add a node</button>
            <button type="button" @click="removeNode('1')">
              Remove Node 1
            </button>
            <button type="button" @click="removeNode('2')">
              Remove Node 2
            </button>
          </Panel>
        </VueFlow>
      </div>
    </div>
  </div>
  <hr />
  <hr />
  <hr />
  <div>
    <div class="w-full" style="height: 90vh">
      <div class="p-4 border">
        <VueFlow
          v-model:nodes="nodes"
          v-model:edges="edges"
          fit-view-on-init
          :default-zoom="1.5"
          :min-zoom="0.2"
          :max-zoom="4"
        >
          <Background pattern-color="#f4f5f8" :gap="10" />
          <MiniMap />
          <Controls />
          <template #node-custom="nodeProps">
            <CustomNode v-bind="nodeProps" />
          </template>
          <template #edge-custom="edgeProps">
            <CustomEdge v-bind="edgeProps" />
          </template>
          <Panel>
            <button type="button" @click="addNode">Add a node</button>
            <button type="button" @click="removeNode('1')">
              Remove Node 1
            </button>
            <button type="button" @click="removeNode('2')">
              Remove Node 2
            </button>
          </Panel>
        </VueFlow>
      </div>
    </div>
  </div>
</div>
-->

<!--
// Add
function addNode() {
  const id = Date.now().toString();

  nodes.value.push({
    id,
    position: { x: 150, y: 50 },
    data: { label: `Node ${id}` },
  });
}
// remove
function removeNode(id) {
  nodes.value = nodes.value.filter((node) => node.id !== id);
}
const elements = ref([
  { id: "1", type: "input", label: "Node 1", position: { x: 0, y: 0 } },
  { id: "2", label: "Node 2", position: { x: 0, y: 30 } },
  { id: "3", label: "Node 3", position: { x: 0, y: 60 } },
  { id: "4", type: "output", label: "Node 4", position: { x: 0, y: 90 } },
  { id: "e1-3", source: "1", target: "3" },
  { id: "e1-2", source: "1", target: "2", animated: true },
]);

-->
