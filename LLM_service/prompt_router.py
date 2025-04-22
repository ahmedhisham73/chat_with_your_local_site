import os
from dotenv import load_dotenv
from promptschema_openai import handle_openai_prompt
from promptschema_llama import handle_llama_prompt

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "tinyllama")

def route_dual_prompt(prompt):
    openai_response = handle_openai_prompt(prompt)
    llama_response = handle_llama_prompt(prompt)
    llama_model_name = os.path.basename(LLAMA_MODEL_PATH)

    return {
        "openai": {
            "model": OPENAI_MODEL,
            "response": openai_response
        },
        "llamacpp": {
            "model": llama_model_name,
            "response": llama_response
        }
    }


