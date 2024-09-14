import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
// import axios from "axios";

const app = createApp(App);

app.use(router);
// app.use(axios, {
//     baseUrl: "http://127.0.0.1:5000",
// });

app.mount("#app");
