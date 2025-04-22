import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Page1.css";

function Page1() {
  const navigate = useNavigate();
  const [model, setModel] = useState("openai");
  const [messages, setMessages] = useState([
    { from: "bot", text: "Welcome! Ask me anything about Egypt 🇪🇬" },
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = { from: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const response = await fetch("/invoke/llm", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: { prompt: input, model } }),
      });

      if (!response.ok) throw new Error("Failed to fetch");

      const data = await response.json();
      const botMsg = { from: "bot", text: data.response || "No response." };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [...prev, { from: "bot", text: "⚠️ Error contacting server." }]);
    }

    setInput("");
  };

  return (
    <div className="page-container">
      <header className="header">
        <h1>📚 History of Egypt</h1>
        <button onClick={() => {
          localStorage.removeItem("token");
          navigate("/login");
        }}>
          Logout
        </button>
      </header>

      <div className="main-content">
        <div className="history-section">
          <h2>Ancient Egyptian Civilization</h2>
          <p>
            Egypt’s history is one of the richest and most influential in the world, spanning thousands of years and shaping much of human civilization. The story begins in prehistoric times along the fertile banks of the Nile River, where early communities settled and developed agriculture. This agricultural foundation gave rise to one of the world’s earliest and most enduring civilizations: Ancient Egypt. Around 3100 BCE, Upper and Lower Egypt were unified under the first pharaoh, Narmer (also known as Menes), marking the start of the dynastic period.

Ancient Egypt thrived for over three millennia, leaving behind incredible achievements in architecture, mathematics, astronomy, and medicine. The construction of the pyramids—especially the Great Pyramid of Giza—stands as a testament to their engineering genius. The Egyptians also developed a complex system of writing known as hieroglyphics and practiced a deeply spiritual religion centered around gods, the afterlife, and divine kingship. The most well-known pharaohs, such as Ramses II, Akhenaten, and Tutankhamun, played vital roles in both domestic affairs and foreign relations.

Following centuries of internal prosperity and occasional periods of fragmentation, Egypt was eventually conquered by foreign powers. First came the Persians in the 6th century BCE, followed by Alexander the Great in 332 BCE, who established the city of Alexandria. After his death, Egypt was ruled by the Ptolemaic dynasty, a Greek-speaking line of monarchs. The last of the Ptolemies was the famous Queen Cleopatra VII, who attempted to resist Roman domination but ultimately failed, leading to Egypt becoming a province of the Roman Empire in 30 BCE.

Egypt remained under Roman and later Byzantine control until the Arab-Muslim conquest in 641 CE. This marked a significant cultural and religious transformation, as Islam became the dominant faith and Arabic replaced Greek and Coptic as the primary language. The Islamic period introduced new architectural styles, scholarship, and trade networks. Cairo, founded in 969 CE by the Fatimid dynasty, became a center of Islamic learning and culture and remains the capital of Egypt to this day.

In the modern era, Egypt experienced Ottoman rule (beginning in the 16th century) and later became a British protectorate in the 19th century. The desire for independence grew steadily, culminating in the 1952 revolution led by the Free Officers Movement and Gamal Abdel Nasser. This ended the monarchy and established a republic. Nasser's policies included land reforms, nationalization of the Suez Canal, and a pan-Arab ideology that positioned Egypt as a leader in the Arab world.

Today, Egypt is a republic with a dynamic, if sometimes turbulent, political landscape. It has faced challenges such as authoritarianism, economic pressures, and popular uprisings like the 2011 revolution during the Arab Spring. Despite these challenges, Egypt remains a pivotal player in the Middle East and Africa, with a legacy that continues to captivate scholars and tourists alike. From the towering pyramids to the bustling streets of Cairo, Egypt’s history is a story of resilience, innovation, and enduring cultural identity....
            <a href="https://en.wikipedia.org/wiki/History_of_Egypt" target="_blank" rel="noreferrer">Read more</a>
          </p>
        </div>

        <div className="chatbot-section">
          <h2>🤖 Chat with EgyptBot</h2>

          <div className="model-select">
            <label htmlFor="model">Choose Model:</label>
            <select id="model" value={model} onChange={(e) => setModel(e.target.value)}>
              <option value="openai">OpenAI</option>
              <option value="llamacpp">LLaMA.cpp</option>
            </select>
          </div>

          <div className="chat-window">
            <div className="chat-messages">
              {messages.map((msg, i) => (
                <div key={i} className={`message ${msg.from}`}>{msg.text}</div>
              ))}
            </div>
            <form className="chat-input" onSubmit={sendMessage}>
              <input
                type="text"
                placeholder="Type your question..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
              />
              <button type="submit">Send</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Page1;


