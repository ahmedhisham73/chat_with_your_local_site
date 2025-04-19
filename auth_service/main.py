import os
import sys
from dotenv import load_dotenv

from flask import Flask, Response
from prometheus_client import Counter, generate_latest


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

from controllers.auth_controller import auth_bp


app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")


REQUEST_COUNT = Counter('auth_requests_total', 'Total Auth Requests')

# ✅ Endpoint لـ Prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)

