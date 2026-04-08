from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Secure DevSecOps App"})

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        result = float(data["a"]) + float(data["b"])
    except ValueError:
        return jsonify({"error": "Inputs must be numbers"}), 400

    return jsonify({"result": result})
