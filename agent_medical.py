# 📁 文件: medical_agent/agent_medical.py
from flask import Flask, request, jsonify
from health_logic import get_health_advice

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    symptom = data.get("symptom", "")
    if not symptom:
        return jsonify({"error": "symptom is required"}), 400

    advice = get_health_advice(symptom)
    return jsonify({"role": "medical", "advice": advice})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)