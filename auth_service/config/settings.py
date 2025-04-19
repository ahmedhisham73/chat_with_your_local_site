from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    os.environ["FLASK_ENV"] = "development"

