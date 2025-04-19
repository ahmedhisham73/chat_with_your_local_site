from flask import Flask, Response, request, jsonify
import time, json
from tools.summarize import summarize_page
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# ✅ Prometheus Counter
REQUEST_COUNT = Counter('mcp_requests_total', 'Total MCP Requests')

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

@app.route("/invoke/summarize", methods=["POST"])
def invoke():
    REQUEST_COUNT.inc()  
    data = request.get_json()
    url = data.get("input", {}).get("url", "")
    result = summarize_page(url)
    return jsonify({"output": result})

@app.route("/tool-metadata.json", methods=["GET"])
def metadata():
    with open("metadata/tool_metadata.json") as f:
        return jsonify(json.load(f))

# ✅ Prometheus Metrics endpoint
@app.route("/metrics", methods=["GET"])
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)

