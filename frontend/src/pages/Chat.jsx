import React, { useState } from 'react';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch('/invoke/llm', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          input: {
            prompt: input,
            model: 'llamacpp' // or 'openai'
          }
        }),
      });

      const data = await res.json();
      setMessages((prev) => [...prev, { role: 'assistant', content: data.response }]);
    } catch (err) {
      console.error('Error:', err);
    }

    setInput('');
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>EgyptBot Chat</h2>
      <div style={{ height: '300px', overflowY: 'auto', border: '1px solid #ccc', padding: '10px' }}>
        {messages.map((msg, i) => (
          <div key={i}><strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.content}</div>
        ))}
      </div>
      <input
        type="text"
        placeholder="Ask about Egypt..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Chat;

