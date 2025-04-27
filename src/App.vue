<template>
  <div>
    <VuePlotly
      :data="data_ref"
      :layout="layout_ref"
      :config="config"
      ref="plotRef"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import VuePlotly from 'vue3-plotly-ts'
import { rpc } from "pyloid-js"

// 定义响应式变量
const data_ref = ref([])
const layout_ref = ref({})
const config = {
  responsive: true,
}

// 从 rpc 加载数据
onMounted(async () => {
  const json_data = await rpc.call("plot")
  console.log(json_data)
  const { data, layout } = JSON.parse(json_data)
  data_ref.value = data
  layout_ref.value = layout
})
</script>
