<!-- <script setup>
import { nextTick, ref } from "vue";
import { Panel, VueFlow, useVueFlow } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
import Icon from "../components/Icon.vue";
import ProcessNode from "../components/ProcessNode.vue";
import AnimationEdge from "../components/AnimationEdge.vue";

import { initialEdges, initialNodes } from "../utils/initial-elements";
import { useRunProcess } from "../utils/useRunProcess";
import { useShuffle } from "../utils/useShuffle";
import { useLayout } from "../utils/useLayout";

const nodes = ref(initialNodes);

const edges = ref(initialEdges);

const cancelOnError = ref(true);

const shuffle = useShuffle();

const { graph, layout, previousDirection } = useLayout();

const { run, stop, reset, isRunning } = useRunProcess({ graph, cancelOnError });

const { fitView } = useVueFlow();

async function shuffleGraph() {
  await stop();

  reset(nodes.value);

  edges.value = shuffle(nodes.value);

  nextTick(() => {
    layoutGraph(previousDirection.value);
  });
}

async function layoutGraph(direction) {
  await stop();

  reset(nodes.value);

  nodes.value = layout(nodes.value, edges.value, direction);

  nextTick(() => {
    fitView();
  });
}
</script>

<template>
  <div class="layout-flow">
    <VueFlow
      :nodes="nodes"
      :edges="edges"
      :default-edge-options="{ type: 'animation', animated: true }"
      @nodes-initialized="layoutGraph('LR')"
    >
      <template #node-process="props">
        <ProcessNode
          :data="props.data"
          :source-position="props.sourcePosition"
          :target-position="props.targetPosition"
        />
      </template>

      <template #edge-animation="edgeProps">
        <AnimationEdge
          :id="edgeProps.id"
          :source="edgeProps.source"
          :target="edgeProps.target"
          :source-x="edgeProps.sourceX"
          :source-y="edgeProps.sourceY"
          :targetX="edgeProps.targetX"
          :targetY="edgeProps.targetY"
          :source-position="edgeProps.sourcePosition"
          :target-position="edgeProps.targetPosition"
        />
      </template>

      <Background />

      <Panel class="process-panel" position="top-right">
        <div class="layout-panel">
          <button v-if="isRunning" class="stop-btn" title="stop" @click="stop">
            <Icon name="stop" />
            <span class="spinner" />
          </button>
          <button v-else title="start" @click="run(nodes)">
            <Icon name="play" />
          </button>

          <button title="set horizontal layout" @click="layoutGraph('LR')">
            <Icon name="horizontal" />
          </button>

          <button title="set vertical layout" @click="layoutGraph('TB')">
            <Icon name="vertical" />
          </button>

          <button title="shuffle graph" @click="shuffleGraph">
            <Icon name="shuffle" />
          </button>
        </div>

        <div class="checkbox-panel">
          <label>Cancel on error</label>
          <input v-model="cancelOnError" type="checkbox" />
        </div>
      </Panel>
    </VueFlow>
  </div>
</template>

<style>
.layout-flow {
  background-color: #1a192b;
  height: 100%;
  width: 100%;
}

.process-panel,
.layout-panel {
  display: flex;
  gap: 10px;
}

.process-panel {
  background-color: #2d3748;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
}

.process-panel button {
  border: none;
  cursor: pointer;
  background-color: #4a5568;
  border-radius: 8px;
  color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.process-panel button {
  font-size: 16px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.checkbox-panel {
  display: flex;
  align-items: center;
  gap: 10px;
}

.process-panel button:hover,
.layout-panel button:hover {
  background-color: #2563eb;
  transition: background-color 0.2s;
}

.process-panel label {
  color: white;
  font-size: 12px;
}

.stop-btn svg {
  display: none;
}

.stop-btn:hover svg {
  display: block;
}

.stop-btn:hover .spinner {
  display: none;
}

.spinner {
  border: 3px solid #f3f3f3;
  border-top: 3px solid #2563eb;
  border-radius: 50%;
  width: 10px;
  height: 10px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style> -->
<!-- <script setup>
import { nextTick, ref } from "vue";
import { Panel, VueFlow, useVueFlow } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
// import { AnimationEdge } from "@vue-flow/animation-edge";
import AnimationEdge from "../components/AnimationEdge.vue";

import Icon from "../components/Icon.vue";
import ProcessNode from "../components/ProcessNode.vue";

import { initialEdges, initialNodes } from "../utils/initial-elements";
import { useRunProcess } from "../utils/useRunProcess";
import { useShuffle } from "../utils/useShuffle";
import { useLayout } from "../utils/useLayout";

const nodes = ref(initialNodes);
const edges = ref(initialEdges);
const cancelOnError = ref(true);

const shuffle = useShuffle();
const { graph, layout, previousDirection } = useLayout();
const { run, stop, reset, isRunning } = useRunProcess({ graph, cancelOnError });
const { fitView } = useVueFlow();

async function shuffleGraph() {
  await stop();
  reset(nodes.value);
  edges.value = shuffle(nodes.value);
  nextTick(() => {
    layoutGraph(previousDirection.value);
  });
}

async function layoutGraph(direction) {
  await stop();
  reset(nodes.value);
  nodes.value = layout(nodes.value, edges.value, direction);
  nextTick(() => {
    fitView();
  });
}
</script>

<template>
  <div class="layout-flow">
    <VueFlow
      :nodes="nodes"
      :edges="edges"
      :default-edge-options="{ type: 'animation', animated: true }"
      @nodes-initialized="layoutGraph('LR')"
    >
      <template #node-process="props">
        <ProcessNode
          :data="props.data"
          :source-position="props.sourcePosition"
          :target-position="props.targetPosition"
        />
      </template>

      <template #edge-animation="edgeProps">
        <AnimationEdge
          :id="edgeProps.id"
          :source="edgeProps.source"
          :target="edgeProps.target"
          :source-x="edgeProps.sourceX"
          :source-y="edgeProps.sourceY"
          :targetX="edgeProps.targetX"
          :targetY="edgeProps.targetY"
          :source-position="edgeProps.sourcePosition"
          :target-position="edgeProps.targetPosition"
          animated
        />
      </template>

      <Background />

      <Panel class="process-panel" position="top-right">
        <div class="layout-panel">
          <button v-if="isRunning" class="stop-btn" title="stop" @click="stop">
            <Icon name="stop" />
            <span class="spinner" />
          </button>
          <button v-else title="start" @click="run(nodes)">
            <Icon name="play" />
          </button>
          <button title="set horizontal layout" @click="layoutGraph('LR')">
            <Icon name="horizontal" />
          </button>
          <button title="set vertical layout" @click="layoutGraph('TB')">
            <Icon name="vertical" />
          </button>
          <button title="shuffle graph" @click="shuffleGraph">
            <Icon name="shuffle" />
          </button>
        </div>
        <div class="checkbox-panel">
          <label>Cancel on error</label>
          <input v-model="cancelOnError" type="checkbox" />
        </div>
      </Panel>
    </VueFlow>
  </div>
</template>

<style>
.layout-flow {
  background-color: #1a192b;
  height: 100%;
  width: 100%;
}

.process-panel,
.layout-panel {
  display: flex;
  gap: 10px;
}

.process-panel {
  background-color: #2d3748;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
}

.process-panel button {
  border: none;
  cursor: pointer;
  background-color: #4a5568;
  border-radius: 8px;
  color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.process-panel button {
  font-size: 16px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.checkbox-panel {
  display: flex;
  align-items: center;
  gap: 10px;
}

.process-panel button:hover,
.layout-panel button:hover {
  background-color: #2563eb;
  transition: background-color 0.2s;
}

.process-panel label {
  color: white;
  font-size: 12px;
}

.stop-btn svg {
  display: none;
}

.stop-btn:hover svg {
  display: block;
}

.stop-btn:hover .spinner {
  display: none;
}

.spinner {
  border: 3px solid #f3f3f3;
  border-top: 3px solid #2563eb;
  border-radius: 50%;
  width: 10px;
  height: 10px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style> -->

<!--  -->

<!-- <script setup>
import { ref } from "vue";
import { VueFlow, useVueFlow } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
import { ControlButton, Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import Icon from "../components/Icon.vue";
import { initialEdges, initialNodes } from "../utils/initial-elements";

/**
 * `useVueFlow` provides:
 * 1. a set of methods to interact with the VueFlow instance (like `fitView`, `setViewport`, `addEdges`, etc)
 * 2. a set of event-hooks to listen to VueFlow events (like `onInit`, `onNodeDragStop`, `onConnect`, etc)
 * 3. the internal state of the VueFlow instance (like `nodes`, `edges`, `viewport`, etc)
 */
const { onInit, onNodeDragStop, onConnect, addEdges, setViewport, toObject } =
  useVueFlow();

const nodes = ref(initialNodes);

const edges = ref(initialEdges);

// our dark mode toggle flag
const dark = ref(false);

/**
 * This is a Vue Flow event-hook which can be listened to from anywhere you call the composable, instead of only on the main component
 * Any event that is available as `@event-name` on the VueFlow component is also available as `onEventName` on the composable and vice versa
 *
 * onInit is called when the VueFlow viewport is initialized
 */
onInit((vueFlowInstance) => {
  // instance is the same as the return of `useVueFlow`
  vueFlowInstance.fitView();
});

/**
 * onNodeDragStop is called when a node is done being dragged
 *
 * Node drag events provide you with:
 * 1. the event object
 * 2. the nodes array (if multiple nodes are dragged)
 * 3. the node that initiated the drag
 * 4. any intersections with other nodes
 */
onNodeDragStop(({ event, nodes, node }) => {
  console.log("Node Drag Stop", { event, nodes, node });
});

/**
 * onConnect is called when a new connection is created.
 *
 * You can add additional properties to your new edge (like a type or label) or block the creation altogether by not calling `addEdges`
 */
onConnect((connection) => {
  addEdges(connection);
});

/**
 * To update a node or multiple nodes, you can
 * 1. Mutate the node objects *if* you're using `v-model`
 * 2. Use the `updateNode` method (from `useVueFlow`) to update the node(s)
 * 3. Create a new array of nodes and pass it to the `nodes` ref
 */
function updatePos() {
  nodes.value = nodes.value.map((node) => {
    return {
      ...node,
      position: {
        x: Math.random() * 400,
        y: Math.random() * 400,
      },
    };
  });
}

/**
 * toObject transforms your current graph data to an easily persist-able object
 */
function logToObject() {
  console.log(toObject());
}

/**
 * Resets the current viewport transformation (zoom & pan)
 */
function resetTransform() {
  setViewport({ x: 0, y: 0, zoom: 1 });
}

function toggleDarkMode() {
  dark.value = !dark.value;
}
</script>

<template>
  <VueFlow
    :nodes="nodes"
    :edges="edges"
    :class="{ dark }"
    class="basic-flow"
    :default-viewport="{ zoom: 1.5 }"
    :min-zoom="0.2"
    :max-zoom="4"
  >
    <Background pattern-color="#aaa" :gap="16" />

    <MiniMap />

    <Controls position="top-left">
      <ControlButton title="Reset Transform" @click="resetTransform">
        <Icon name="reset" />
      </ControlButton>

      <ControlButton title="Shuffle Node Positions" @click="updatePos">
        <Icon name="update" />
      </ControlButton>

      <ControlButton title="Toggle Dark Mode" @click="toggleDarkMode">
        <Icon v-if="dark" name="sun" />
        <Icon v-else name="moon" />
      </ControlButton>

      <ControlButton title="Log `toObject`" @click="logToObject">
        <Icon name="log" />
      </ControlButton>
    </Controls>
  </VueFlow>
</template> -->
<!--
<script setup>
import { h, ref } from "vue";
import { Background } from "@vue-flow/background";
import { Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import { VueFlow, useVueFlow } from "@vue-flow/core";
import CustomNode from "../components/CustomNode.vue";
import CustomEdge from "../components/CustomEdge.vue";

const { onConnect, addEdges } = useVueFlow();

const nodes = ref([
  { id: "1", type: "input", label: "Node 1", position: { x: 250, y: 5 } },
  { id: "2", type: "output", label: "Node 2", position: { x: 100, y: 100 } },
  { id: "3", type: "custom", label: "Node 3", position: { x: 400, y: 100 } },
]);

const edges = ref([
  { id: "e1-2", source: "1", target: "2", type: "custom" },
  { id: "e1-3", source: "1", target: "3", animated: true },
]);

onConnect((params) => {
  addEdges([params]);
});
</script>

<template>
  <div style="height: 100vh">
    <VueFlow
      v-model:nodes="nodes"
      v-model:edges="edges"
      fit-view-on-init
      class="vue-flow-basic-example"
      :default-zoom="1.5"
      :min-zoom="0.2"
      :max-zoom="4"
    >
      <Background pattern-color="#aaa" :gap="8" />

      <MiniMap />

      <Controls />

      <template #node-custom="nodeProps">
        <CustomNode v-bind="nodeProps" />
      </template>

      <template #edge-custom="edgeProps">
        <CustomEdge v-bind="edgeProps" />
      </template>
    </VueFlow>
  </div>
</template> -->

<!-- <script setup>
import { ref } from "vue";
import { Background } from "@vue-flow/background";
import { Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import { VueFlow, useVueFlow } from "@vue-flow/core";
import CustomNode from "../components/CustomNode.vue";
import CustomEdge from "../components/CustomEdge.vue";

// VueFlow hooks and initial state
const { onConnect, addEdges } = useVueFlow();

const nodes = ref([
  { id: "1", type: "input", label: "Node 1", position: { x: 250, y: 5 } },
  { id: "2", type: "output", label: "Node 2", position: { x: 100, y: 100 } },
  { id: "3", type: "custom", label: "Node 3", position: { x: 400, y: 100 } },
]);

const edges = ref([
  { id: "e1-2", source: "1", target: "2", type: "custom" },
  { id: "e1-3", source: "1", target: "3", animated: true },
]);

// Automatically add new edges on connection
onConnect((params) => {
  addEdges([params]);
});
</script>

<template>
  <div class="">
    <div style="height: 100vh; position: relative; margin-bottom: 15rem">
      <VueFlow
        v-model:nodes="nodes"
        v-model:edges="edges"
        fit-view-on-init
        class="vue-flow-basic-example"
        :default-zoom="1.5"
        :min-zoom="0.2"
        :max-zoom="4"
      >

        <Background pattern-color="#eee" :gap="8" />


        <MiniMap />


        <Controls />


        <template #node-custom="nodeProps">
          <CustomNode v-bind="nodeProps" />
        </template>


        <template #edge-custom="edgeProps">
          <CustomEdge v-bind="edgeProps" />
        </template>
      </VueFlow>
    </div>
    <h1>Header1</h1>
  </div>
</template> -->
<script setup>
import { ref, onMounted } from "vue";

import { Background } from "@vue-flow/background";
import { Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import { VueFlow, Panel, useVueFlow } from "@vue-flow/core";
import CustomNode from "../components/CustomNode.vue";
import CustomEdge from "../components/CustomEdge.vue";

// استخدام دوال VueFlow hooks وحالة البداية
const { onConnect, addEdges } = useVueFlow();

const nodes = ref([
  {
    id: "1",
    type: "input",
    position: { x: 0, y: 0 },
    data: { label: "Node 1" },
  },
  {
    id: "2",
    position: { x: 0, y: 30 },
    data: { label: "Node 2" },
  },
  {
    id: "3",
    position: { x: 0, y: 60 },
    data: { label: "Node 3" },
  },
  {
    id: "4",
    type: "output",
    position: { x: 0, y: 90 },
    data: { label: "Node 4" },
  },
]);

const edges = ref([
  {
    id: "e1->3",
    source: "1",
    target: "3",
  },
  {
    id: "e1->2",
    source: "1",
    target: "2",
  },
]);
const elements = ref([
  { id: "1", type: "input", label: "Node 1", position: { x: 0, y: 0 } },
  { id: "2", label: "Node 2", position: { x: 0, y: 30 } },
  { id: "3", label: "Node 3", position: { x: 0, y: 60 } },
  { id: "4", type: "output", label: "Node 4", position: { x: 0, y: 90 } },
  { id: "e1-3", source: "1", target: "3" },
  { id: "e1-2", source: "1", target: "2", animated: true },
]);

// تنفيذ الوظيفة عند الاتصال بين العقدة والروابط
onConnect((params) => {
  addEdges([params]); // إضافة روابط جديدة عند الاتصال
});
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
</script>

<template>
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
        <!-- Add  -->
        <Panel>
          <button type="button" @click="addNode">Add a node</button>
          <button type="button" @click="removeNode('1')">Remove Node 1</button>
          <button type="button" @click="removeNode('2')">Remove Node 2</button>
        </Panel>
      </VueFlow>
    </div>

    <!-- محتوى إضافي أو عناوين -->
    <h1>Header 1</h1>
    <div class="">
      <VueFlow class="style_tow" v-model="elements" />
    </div>
  </div>
</template>
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
npm install @vue-flow/core
npm install @vue-flow/background
npm install @vue-flow/controls
npm install @vue-flow/minimap
npm install lodash
npm install @dagrejs/dagre
npm install vuedraggable@next
-->

<!--
Adding Nodes to the Graph
Removing Nodes from the Graph

-->
