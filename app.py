from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)
@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json["mensaje"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": mensaje
        },
        stream=True
    )

    respuesta_completa = ""

    for linea in response.iter_lines():
        if linea:
            data = json.loads(linea)
            respuesta_completa += data.get("response", "")

    return jsonify({"respuesta": respuesta_completa})

if __name__ == "__main__":
    import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))