import os
from dotenv import load_dotenv
from llama_cpp import Llama

from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
print("✅ LLAMA_MODEL_PATH =", os.getenv("LLAMA_MODEL_PATH"))



# === Config
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH")
LLAMA_N_CTX = int(os.getenv("LLAMA_N_CTX", 4096))

_llm = None

def get_llama_instance():
    global _llm
    if _llm is None:
        _llm = Llama(
            model_path=LLAMA_MODEL_PATH,
            n_ctx=LLAMA_N_CTX,
            verbose=False,
        )
    return _llm

def handle_llama_prompt(prompt):
    try:
        llm = get_llama_instance()
        result = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Llama.cpp Error: {str(e)}"

