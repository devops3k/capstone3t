import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Read environment variables for middle service
MIDDLE_HOST = os.environ.get('MID_HOST', 'middle-service')
MIDDLE_PORT = os.environ.get('MID_PORT', '8080')

@app.route("/")
def index():
    # Just render our Bootstrap page
    return render_template("index.html", middle_host=MIDDLE_HOST, middle_port=MIDDLE_PORT)

@app.route("/fetchHello")
def fetch_hello():
    # Server-side call to the middle service
    url = f"http://{MIDDLE_HOST}:{MIDDLE_PORT}/api/hello"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return jsonify({"message": resp.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/fetchPeople")
def fetch_people():
    # Server-side call to /api/person
    url = f"http://{MIDDLE_HOST}:{MIDDLE_PORT}/api/person"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.text  # It's already JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
