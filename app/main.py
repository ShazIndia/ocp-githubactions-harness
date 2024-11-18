from flask import Flask, jsonify
from models import Developer, Manager
from config import get_secret

app = Flask(__name__)

@app.route("/")
def home():
    dev = Developer("Alice", "Python")
    mgr = Manager("Bob", 5)
    return jsonify({
        "developer": dev.work(),
        "manager": mgr.work(),
        "secret": get_secret("api_key")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
