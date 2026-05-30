export default function ImagePreview({ task }) {
    if (!task || task.status !== "COMPLETED") return null;

    const SERVER_URL = "http://localhost:8000/api";

    return (
        <div
            style={{
                marginTop: "20px",
                padding: "20px",
                borderRadius: "12px",
                background: "#111",
                color: "#fff",
                maxWidth: "420px",
            }}
        >
            

            <a
                href={`${SERVER_URL}/download/${task.id}/`}
                style={{
                    display: "inline-block",
                    marginTop: "10px",
                    padding: "8px 12px",
                    background: "#4f46e5",
                    color: "#fff",
                    borderRadius: "8px",
                    textDecoration: "none",
                }}
            >
                Download Image
            </a>
        </div>
    );
}