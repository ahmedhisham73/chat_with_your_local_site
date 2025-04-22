# 🔐 Secure Local Chatbot System (Frontend + Backend + Monitoring)

A complete secure local AI-based chatbot system with:

- Frontend built using **React** (no Tailwind)
- Backend services (Auth + MCP for summarization + LLM)
- Full Dockerized deployment with NGINX + TLS + Monitoring

---

## 📁 Features

- ✅ JWT-based Login Authentication
- ✅ Protected Routing (`/page_1`)
- ✅ Responsive Layout (Sidebar + Content + EgyptBot Chatbot)
- ✅ Chatbot supports both **OpenAI** and **LLaMA.cpp**
- ✅ HTTPS with TLS (NGINX reverse proxy)
- ✅ Prometheus + Grafana Monitoring
- ✅ Structured JSON logging (Nginx)
- ✅ No Tailwind or Bootstrap — clean manual CSS

---

## 🏗️ Tech Stack

- React + Vite
- Flask (Auth + MCP)
- OpenAI API + llama.cpp integration
- NGINX (TLS, HTTP2, Reverse Proxy, Rate Limiting)
- Prometheus + Grafana (Monitoring)
- Docker Compose (isolated services, single network)

---

## 🔑 Pages

| Route       | Description                              |
|-------------|------------------------------------------|
| `/login`    | JWT-based login page                     |
| `/page_1`   | Protected page with static Egypt history + EgyptBot |
| `/tools`    | Dynamic tool metadata tester (RAG-friendly)

---

## 🧠 Chatbot Integration

- Located inside `Page1.jsx`
- Supports **model switching** between:
  - `openai`
  - `llamacpp`
- Dynamic prompt sent to unified backend `/invoke/llm`
- Sample JSON payload:
  ```json
  {
    "input": {
      "prompt": "من هو رمسيس الثاني؟",
      "model": "llamacpp"
    }
  }
  ```

---

## ⚙️ Backend Endpoints

### 🔹 `/invoke/llm` (POST)
Unified LLM endpoint

| Field     | Type   | Description          |
|-----------|--------|----------------------|
| prompt    | string | User input           |
| model     | string | "openai" or "llamacpp" |

Returns:
```json
{
  "backend": "llamacpp",
  "response": "..."
}
```

---

### 🔹 `/tool-metadata.json` (GET)
Returns JSON metadata used in `/tools` page for dynamic tool rendering.

### 🔹 `/metrics` (GET)
Exposes Prometheus metrics for `auth_service` and `mcp_service`.

---

## 🧩 Directory Structure

```
LLM_MCP/
├── auth_service/           # Login / JWT
├── mcp_service/            # Summarization & LLM API
├── LLM_service/            # llama.cpp backend, models, logic
├── frontend/               # React app with EgyptBot
├── monitoring/             # Prometheus + Grafana provisioning
├── docker-compose-merged.yml
```

---

## 🔐 Docker & Network

- All services share the `shared_net` (bridge network)
- NGINX acts as HTTPS reverse proxy
- Mounted frontend `dist/` inside NGINX as root
- Rate limiting, gzip compression, and security headers enabled

---

## ⚠️ Notes

- `.env` **is no longer required** in frontend (`REACT_APP_MCP_HOST` was removed)
- API routing now uses `https://localhost/invoke/llm`
- NGINX TLS cert path: `./auth_service/certs/`
- No Tailwind; pure CSS via `Page1.css`

---

## 🚀 Run Locally

```bash
# Build frontend:
cd frontend
npm install
npm run build

# Go back and run all services:
cd ..
docker compose -f docker-compose-merged.yml up --build
```

---

## 🔎 Access

| Component     | URL                    |
|---------------|------------------------|
| Frontend      | https://localhost      |
| Grafana       | http://localhost:3000  |
| Prometheus    | http://localhost:9090  |
| Backend (API) | proxied via NGINX      |

---

## ✅ Default Login (for testing)

| Username | Password   |
|----------|------------|
| `admin`  | `admin123` |

---

## 📜 License

MIT License
