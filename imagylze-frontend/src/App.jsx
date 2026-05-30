import { useEffect, useState } from "react";
import UploadForm from "./components/UploadForm";
import StatusCard from "./components/StatusCard";
import ImagePreview from "./components/ImagePreview";
import { getTask } from "./services/api";

function App() {
    const [task, setTask] = useState(null);

    useEffect(() => {
        if (!task || task.status === "COMPLETED") return;

        const interval = setInterval(async () => {
            const updated = await getTask(task.id);
            setTask(updated);

            if (updated.status === "COMPLETED") {
                clearInterval(interval);
            }
        }, 2000);

        return () => clearInterval(interval);
    }, [task]);

    return (
        <div style={styles.page}>
            
            <div style={styles.container}>

                {/* Header */}
                <div style={styles.header}>
                    <h1 style={styles.title}>Imagylze</h1>
                    <p style={styles.subtitle}>
                        Upload images. Resize instantly. Powered by Celery.
                    </p>
                </div>

                {/* Main Card */}
                <div style={styles.card}>
                    <UploadForm setTask={setTask} />

                    <div style={styles.divider} />

                    <StatusCard task={task} />
                    <ImagePreview task={task} />
                </div>

                {/* Footer */}
                <p style={styles.footer}>
                    PNG • JPEG • Async Processing • Django + Celery
                </p>

            </div>

        </div>
    );
}

export default App;

const styles = {
    page: {
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#f6f9fc",
        fontFamily: "Arial, sans-serif",
    },

    container: {
        width: "420px",
        textAlign: "center",
    },

    header: {
        marginBottom: "20px",
    },

    title: {
        fontSize: "40px",
        fontWeight: "700",
        color: "#1e3a8a",
        marginBottom: "6px",
        letterSpacing: "0.5px",
    },

    subtitle: {
        fontSize: "14px",
        color: "#6b7280",
    },

    card: {
        background: "#ffffff",
        border: "1px solid #e5e7eb",
        borderRadius: "16px",
        padding: "20px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.05)",
    },

    divider: {
        height: "1px",
        background: "#e5e7eb",
        margin: "15px 0",
    },

    footer: {
        marginTop: "12px",
        fontSize: "12px",
        color: "#9ca3af",
    },
};