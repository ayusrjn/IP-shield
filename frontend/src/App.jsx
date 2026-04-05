// frontend/src/App.jsx
import { useState } from "react"
import { QueryInput } from "./components/QueryInput"
import { AgentTrace } from "./components/AgentTrace"

export default function App() {
  const [query, setQuery] = useState("")

  return (
    <div style={{ maxWidth: 800, margin: "60px auto", padding: "0 20px" }}>
      <h1 style={{ marginBottom: 8 }}>IP Shield</h1>
      <p style={{ color: "#666", marginBottom: 24 }}>
        Protect your brand, content, and ideas.
      </p>
      <QueryInput onSubmit={setQuery} />
      {query && <AgentTrace query={query} />}
    </div>
  )
}