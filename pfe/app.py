import os
import requests
from flask import Flask

app = Flask(__name__)

# Pull hostname and port from environment vars, with defaults.
MIDDLE_HOST = os.environ.get('MID_HOST', 'middle-service')
MIDDLE_PORT = os.environ.get('MID_PORT', '8080')

@app.route("/")
def index():
    return f"""
    <html>
    <head><title>Python Frontend</title></head>
    <body>
      <h1>Python Server-Side Frontend</h1>
      <p>This page is served by Python/Flask. It makes HTTP requests to the middle service:</p>
      <ul>
        <li>MIDDLE_HOST: {MIDDLE_HOST}</li>
        <li>MIDDLE_PORT: {MIDDLE_PORT}</li>
      </ul>
      <ul>
        <li><a href="/hello">Fetch Hello</a></li>
        <li><a href="/people">Fetch People</a></li>
      </ul>
    </body>
    </html>
    """

@app.route("/hello")
def hello():
    try:
        url = f"http://{MIDDLE_HOST}:{MIDDLE_PORT}/api/hello"
        resp = requests.get(url, timeout=5)
        return f"<h2>Response from {url}:</h2><p>{resp.text}</p>"
    except Exception as e:
        return f"<h2>Error calling {MIDDLE_HOST}:{MIDDLE_PORT}:</h2><p>{e}</p>"

@app.route("/people")
def people():
    try:
        url = f"http://{MIDDLE_HOST}:{MIDDLE_PORT}/api/person"
        resp = requests.get(url, timeout=5)
        data = resp.json()
        items = "".join(f"<li>{p['firstName']} {p['lastName']}</li>" for p in data)
        return f"<h2>People from {url}:</h2><ul>{items}</ul>"
    except Exception as e:
        return f"<h2>Error calling {MIDDLE_HOST}:{MIDDLE_PORT}:</h2><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
