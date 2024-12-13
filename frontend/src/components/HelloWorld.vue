<template>
  <div class="hello">
    <h1>API Status: {{ apiStatus }}</h1>
    <p>本プロジェクトはDjangoとVueで構成されています</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { onMounted } from "vue";

const apiStatus = ref("None");
onMounted(() => {
  axios
    .get("/api/v1/sample")
    .then((res) => {
      apiStatus.value = res.data;
    })
    .catch((e) => {
      apiStatus.value = "Failed";
      console.log(e);
    });
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

a {
  color: #42b983;
}
</style>
