from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "X-Forwarded-For": request.headers.get("X-Forwarded-For"),
        "Remote-Addr": request.remote_addr,
        "All-Headers": dict(request.headers)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)