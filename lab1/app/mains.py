from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Python!"


@app.route("/probe")
def service_probe():
    return "ok_1"


@app.route("/health")
def service_health():
    return "{""status"": ""OK""}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
