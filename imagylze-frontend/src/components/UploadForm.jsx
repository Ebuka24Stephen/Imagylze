import { useState } from "react";
import { uploadImage } from "../services/api";

export default function UploadForm({ setTask }) {
    const [image, setImage] = useState(null);
    const [width, setWidth] = useState(300);
    const [height, setHeight] = useState(300);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append("image", image);
        formData.append("width", width);
        formData.append("height", height);

        const data = await uploadImage(formData);
        setTask(data);
    };

    return (
        <form onSubmit={handleSubmit} style={styles.form}>
            
            <label style={styles.label}>Upload Image</label>
            <input
                type="file"
                onChange={(e) => setImage(e.target.files[0])}
                style={styles.input}
            />

            <div style={styles.row}>
                
                <div style={styles.field}>
                    <label style={styles.label}>Width</label>
                    <input
                        type="number"
                        value={width}
                        onChange={(e) => setWidth(Number(e.target.value))}
                        style={styles.input}
                    />
                </div>

                <div style={styles.field}>
                    <label style={styles.label}>Height</label>
                    <input
                        type="number"
                        value={height}
                        onChange={(e) => setHeight(Number(e.target.value))}
                        style={styles.input}
                    />
                </div>

            </div>

            <button type="submit" style={styles.button}>
                Upload & Process
            </button>

        </form>
    );
}

const styles = {
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "12px",
    },

    row: {
        display: "flex",
        gap: "12px",
    },

    field: {
        flex: 1,
        display: "flex",
        flexDirection: "column",
        gap: "6px",
    },

    label: {
        fontSize: "12px",
        color: "#6b7280",
    },

    input: {
        padding: "10px",
        borderRadius: "10px",
        border: "1px solid #d1d5db",
        background: "#f9fafb",
        color: "#111827",   // ✅ FIX: makes text visible
        outline: "none",
        fontSize: "14px",
        width: "100%",
    },

    button: {
        marginTop: "8px",
        padding: "10px",
        borderRadius: "10px",
        border: "none",
        background: "#2563eb",
        color: "white",
        fontWeight: "600",
        cursor: "pointer",
    },
};