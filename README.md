# 🔐 Secure Local Chatbot System (Frontend + Backend + Monitoring)

A complete secure local AI-based chatbot system with:

- Frontend built using **React** (no Tailwind)
- Backend services (Auth + MCP for summarization)
- Full Dockerized deployment with NGINX + TLS + Monitoring

---

## 📁 Features

- ✅ JWT-based Login Authentication
- ✅ Protected Routing (`/page_1`)
- ✅ Responsive Layout (Sidebar + Content + Chatbot)
- ✅ Info panel (e.g. history, articles...)
- ✅ Chatbot-ready interface for integration
- ✅ HTTPS with TLS (NGINX reverse proxy)
- ✅ Prometheus + Grafana Monitoring
- ✅ Logging in structured JSON format
- ❌ No Tailwind / No Bootstrap — just clean custom CSS

---

## 🏗️ Tech Stack

- React + Vite + Vanilla CSS
- Flask (Auth & MCP microservices)
- NGINX (TLS + Routing + Rate Limiting)
- Prometheus + Grafana (Monitoring)
- Docker Compose (Multi-service deployment)

---

## 📦 MCP Service (Summarization Endpoint)

- Endpoint: `/invoke/summarize`
- Method: `POST`
- Example Payload:
  ```json
  {
    "input": {
      "url": "https://en.wikipedia.org/wiki/History_of_Egypt"
    }
  }
  ```
- Returns JSON summary.

---

## 🔍 Monitoring

- Prometheus scrapes metrics from:
  - `auth_service:5007/metrics`
  - `mcp_service:8787/metrics`
- Metrics exposed via `prometheus_client` in each service
- Grafana preconfigured via provisioning
- Custom metric: `auth_requests_total` defined in Auth service

---

## 🔐 Default Credentials (for testing)

| Username | Password   |
|----------|------------|
| `admin`  | `admin123` |

---

## 🧠 Pages

| Route       | Description                   |
|-------------|-------------------------------|
| `/login`    | Login form with JWT storage   |
| `/page_1`   | Protected page with content + chatbot |

---

## 🧩 Project Structure

```
root/
├── auth_service/               # Flask Auth Service (with metrics)
├── mcp_service/                # Summarization backend (MCP)
├── frontend/                   # React frontend
├── nginx/                      # NGINX config + TLS certs
├── monitoring/                 # Prometheus + Grafana provisioning
├── docker-compose-merged.yml  # Full deployment
```

---

## ⚙️ NGINX Enhancements

- TLS with self-signed certs
- JSON logs (`/var/log/nginx/access.log`)
- Rate Limiting (ready to enable)
- Caching headers for static files
- Secure upstream routing for `/auth/` and `/invoke/`

---

## 🧠 Ahmed Notes

- All services run on a shared Docker bridge network
- JWT tokens stored in `localStorage`
- Frontend React served at `/`
- Backend:
  - Auth service routed via `/auth/`
  - MCP service routed via `/invoke/`
- `/metrics` added for Prometheus scraping in both services

---

## 🚀 Usage

```bash
# Start all services:
docker-compose -f docker-compose-merged.yml up --build

# Visit:
Frontend: https://localhost
Grafana: http://localhost:3000
Prometheus: http://localhost:9090
```

---

## 📜 License

MIT License
