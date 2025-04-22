import React, { useState, useEffect } from "react";

const Tools = () => {
  const [tools, setTools] = useState([]);
  const [selectedTool, setSelectedTool] = useState(null);
  const [formData, setFormData] = useState({});
  const [response, setResponse] = useState(null);

  useEffect(() => {
    fetch("/tool-metadata.json")
      .then(res => res.json())
      .then(data => setTools(data))
      .catch(err => console.error("Failed to fetch tools:", err));
  }, []);

  const handleSubmit = async () => {
    if (!selectedTool) return;

    const endpoint = selectedTool.endpoint || `/invoke/${selectedTool.name}`;
    const body = { input: formData };

    try {
      const res = await fetch(endpoint, {
        method: selectedTool.method || "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status} - ${text}`);
      }

      const result = await res.json();
      setResponse(result);
    } catch (err) {
      console.error("Error calling tool:", err);
      setResponse({ error: err.message });
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Select a Tool</h2>
      <select
        onChange={(e) => {
          const tool = tools.find(t => t.name === e.target.value);
          setSelectedTool(tool);
          setFormData({});
          setResponse(null);
        }}
      >
        <option value="">-- Choose --</option>
        {tools.map(t => (
          <option key={t.name} value={t.name}>{t.name}</option>
        ))}
      </select>

      {selectedTool && (
        <div style={{ marginTop: 20 }}>
          <h3>Tool: {selectedTool.name}</h3>
          {Object.entries(selectedTool.input_schema.properties).map(([key, config]) => (
            <div key={key} style={{ marginBottom: "10px" }}>
              <label>{key}</label>
              <input
                type="text"
                value={formData[key] || ""}
                onChange={(e) => setFormData({ ...formData, [key]: e.target.value })}
              />
            </div>
          ))}
          <button onClick={handleSubmit}>Submit</button>
        </div>
      )}

      {response && (
        <div style={{ marginTop: 20 }}>
          <h3>Response</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Tools;

