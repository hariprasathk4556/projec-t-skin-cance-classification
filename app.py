from flask import Flask, render_template, request, jsonify
from pathlib import Path
import uuid

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024
UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED = {"png", "jpg", "jpeg", "webp"}

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/upload")
def upload():
    file = request.files.get("image")
    if not file or not file.filename:
        return jsonify({"error": "No image selected"}), 400
    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ALLOWED:
        return jsonify({"error": "Please upload JPG, PNG or WEBP"}), 400
    name = f"{uuid.uuid4().hex}.{ext}"
    path = UPLOAD_DIR / name
    file.save(path)
    return jsonify({"url": "/" + str(path).replace("\\", "/")})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
