from flask import Flask, request, jsonify
from promptschema_openai import handle_openai_prompt
from promptschema_llama import handle_llama_prompt

app = Flask(__name__)

@app.route("/llm/openai", methods=["POST"])
def call_openai():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = handle_openai_prompt(prompt)
    return jsonify({
        "backend": "openai",
        "response": response
    })

@app.route("/llm/llama", methods=["POST"])
def call_llama():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = handle_llama_prompt(prompt)
    return jsonify({
        "backend": "llamacpp",
        "response": response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7005)


