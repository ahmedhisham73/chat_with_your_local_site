import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Page1.css";

function Page1() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  return (
    <div className="page-container">
      <header className="header">
        <h1>📚 History of Egypt</h1>
        <button
          onClick={() => {
            localStorage.removeItem("token");
            navigate("/login");
          }}
        >
          Logout
        </button>
      </header>

      <div className="main-content">
        <div className="history-section">
          <h2>Ancient Egyptian Civilization</h2>
          <p>
            Egypt has one of the longest histories of any country, tracing its
            heritage along the Nile Delta back to the 6th–4th millennia BCE. Considered
            a cradle of civilization, Ancient Egypt saw some of the earliest developments
            of writing, agriculture, urbanization, organized religion, and central government.
          </p>
          <p>
            The civilization of ancient Egypt coalesced around 3100 BCE with the political
            unification of Upper and Lower Egypt under the first pharaoh. The culture of Egypt
            flourished for over three millennia and left a legacy that still captivates the world.
          </p>
          <p>
            Key achievements include the pyramids, hieroglyphic writing system, and advances in medicine, engineering, and mathematics.
          </p>
          <p>Read more on <a href="https://en.wikipedia.org/wiki/History_of_Egypt" target="_blank" rel="noreferrer">Wikipedia</a>.</p>
        </div>

        <div className="chatbot-section">
          <h2>🤖 Chat with EgyptBot</h2>
          <div className="chat-window">
            <div className="chat-messages">
              <div className="message bot">Welcome! Ask me anything about Egypt 🇪🇬</div>
              {/* Dynamic messages go here */}
            </div>
            <form className="chat-input">
              <input type="text" placeholder="Type your question..." />
              <button type="submit">Send</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Page1;





