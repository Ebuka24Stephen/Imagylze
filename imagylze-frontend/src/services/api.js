import axios from "axios";

const BASE_URL = "http://localhost:8000/api/";

export const uploadImage = async (formData) => {
    const res = await axios.post(`${BASE_URL}upload/`, formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });
    return res.data;
};

export const getTask = async (id) => {
    const res = await axios.get(`${BASE_URL}upload/${id}/`);
    return res.data;
};