export default function StatusCard({ task }) {
    if (!task) return null;

    return (
        <div>
            <p>Status: {task.status}</p>
        </div>
    );
}