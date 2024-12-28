<script>
import { computed } from "vue";
import {
  BaseEdge,
  EdgeLabelRenderer,
  getBezierPath,
  useVueFlow,
} from "@vue-flow/core";

export default {
  inheritAttrs: false,
  setup(props) {
    const { removeEdges } = useVueFlow();
    const path = computed(() => getBezierPath(props));

    return {
      path,
      removeEdges,
    };
  },
};
</script>
<template>
  <BaseEdge :path="path[0]" />
  <EdgeLabelRenderer>
    <div
      :style="{
        pointerEvents: 'all',
        position: 'absolute',
        transform: `translate(-50%, -50%) translate(${path[1]}px,${path[2]}px)`,
      }"
      class="nodrag nopan"
    >
      <button class="edgebutton" @click="removeEdges(props.id)">×</button>
    </div>
  </EdgeLabelRenderer>
</template>

<style>
.edgebutton {
  border-radius: 999px;
  cursor: pointer;
}
.edgebutton:hover {
  box-shadow: 0 0 0 2px pink, 0 0 0 4px #f05f75;
}
</style>
