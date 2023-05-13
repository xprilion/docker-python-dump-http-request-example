import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    if request.scheme == 'https':
        return 'Hello, World! You are connected over HTTPS!'
    else:
        return 'Hello, World! You are connected over HTTP!'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))