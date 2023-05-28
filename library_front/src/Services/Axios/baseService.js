import axios from "axios";

export const BASE_API = axios.create({
    baseURL: "http://" + process.env.HOST + ":8000"
});