from pathlib import Path

from flask import Flask, abort, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/profile")
def profile():
    return send_from_directory(BASE_DIR, "profile.html")


@app.get("/services")
def services():
    return send_from_directory(BASE_DIR, "services.html")


@app.get("/<path:filename>")
def assets(filename):
    if filename not in {"styles.css", "script.js"}:
        abort(404)
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    app.run(debug=True)
