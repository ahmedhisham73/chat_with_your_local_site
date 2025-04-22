import sys
import time
import json
from flask import Flask, Response, request, jsonify
from prometheus_client import Counter, generate_latest

# ✅ Append LLM service path
sys.path.append("/home/ahmedetsh/Desktop/LLM_MCP/LLM_service")

# ✅ Custom Imports
from tools.summarize import summarize_page
from promptschema_openai import handle_openai_prompt
from promptschema_llama import handle_llama_prompt

app = Flask(__name__)

# ✅ Prometheus Counter
REQUEST_COUNT = Counter('mcp_requests_total', 'Total MCP Requests')

# ===========================================================
# ✅ SSE Keep-Alive Endpoint (for dev)
# ===========================================================
@app.route("/sse", methods=["GET"])
def sse():
    def event_stream():
        yield "data: Connected to MCP Server\n\n"
        while True:
            time.sleep(15)
            yield "data: keep-alive\n\n"
    return Response(event_stream(), headers={
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    })

# ===========================================================
# ✅ Summarization Endpoint
# ===========================================================
@app.route("/invoke/summarize", methods=["POST"])
def invoke_summarize():
    REQUEST_COUNT.inc()
    data = request.get_json(force=True)
    url = data.get("input", {}).get("url", "")
    if not url:
        return jsonify({"error": "Missing URL input"}), 400

    try:
        result = summarize_page(url)
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===========================================================
# ✅ Unified LLM Prompt Handler
# ===========================================================
@app.route("/invoke/llm", methods=["POST"])
def invoke_llm():
    REQUEST_COUNT.inc()
    data = request.get_json(force=True)
    input_data = data.get("input", {})
    prompt = input_data.get("prompt", "").strip()
    model = input_data.get("model", "openai")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        if model == "openai":
            response = handle_openai_prompt(prompt)
            return jsonify({"backend": "openai", "response": response})

        elif model == "llamacpp":
            response = handle_llama_prompt(prompt)
            return jsonify({"backend": "llamacpp", "response": response})

        else:
            return jsonify({"error": f"Unsupported model: {model}"}), 400
    except Exception as e:
        return jsonify({"error": f"Internal error: {str(e)}"}), 500

# ===========================================================
# ✅ Tool Metadata for React dynamic UI
# ===========================================================
@app.route("/tool-metadata.json", methods=["GET"])
def metadata():
    try:
        with open("metadata/tool_metadata.json", "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({"error": f"Failed to load metadata: {str(e)}"}), 500

# ===========================================================
# ✅ Prometheus Metrics
# ===========================================================
@app.route("/metrics", methods=["GET"])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# ===========================================================
# ✅ App Runner
# ===========================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)


