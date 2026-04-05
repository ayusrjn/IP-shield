// frontend/src/components/QueryInput.jsx
import { useState } from "react"

export function QueryInput({ onSubmit }) {
    const [value, setValue] = useState("")

    return (
        <div style={{ display: "flex", gap: 8 }}>
            <textarea
                value={value}
                onChange={e => setValue(e.target.value)}
                placeholder="Describe what you want to protect — brand name, content, logo..."
                rows={3}
                style={{ flex: 1, padding: 12, borderRadius: 8, border: "1px solid #ddd", fontSize: 14 }}
            />
            <button
                onClick={() => onSubmit(value)}
                style={{ padding: "0 20px", borderRadius: 8, background: "#534AB7", color: "#fff", border: "none", cursor: "pointer" }}
            >
                Analyze
            </button>
        </div>
    )
}