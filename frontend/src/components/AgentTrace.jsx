// frontend/src/components/AgentTrace.jsx
import { useEffect, useState } from "react"

export function AgentTrace({ query }) {
    const [events, setEvents] = useState([])

    useEffect(() => {
        if (!query) return
        setEvents([])

        // SSE — this is what shows the agent "thinking" live
        fetch("http://localhost:8000/api/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        }).then(res => {
            const reader = res.body.getReader()
            const decoder = new TextDecoder()

            function read() {
                reader.read().then(({ done, value }) => {
                    if (done) return
                    const text = decoder.decode(value)
                    const lines = text.split("\n").filter(l => l.startsWith("data: "))
                    lines.forEach(line => {
                        const event = JSON.parse(line.slice(6))
                        setEvents(prev => [...prev, event])
                    })
                    read()
                })
            }
            read()
        })
    }, [query])

    return (
        <div style={{ marginTop: 24, fontFamily: "monospace", fontSize: 13 }}>
            {events.map((e, i) => (
                <div key={i} style={{
                    marginBottom: 8, padding: 10, borderRadius: 6,
                    background: e.type === "tool_call" ? "#EEEDFE"
                        : e.type === "tool_result" ? "#E1F5EE"
                            : e.type === "final" ? "#FAEEDA"
                                : "#f5f5f5"
                }}>
                    {e.type === "tool_call" && (
                        <span>Calling <strong>{e.tool}</strong> with {JSON.stringify(e.input)}</span>
                    )}
                    {e.type === "tool_result" && (
                        <span>Result from <strong>{e.tool}</strong>: {JSON.stringify(e.result)}</span>
                    )}
                    {e.type === "final" && (
                        <pre style={{ whiteSpace: "pre-wrap" }}>{e.content}</pre>
                    )}
                </div>
            ))}
        </div>
    )
}