import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/")
def home():
    return "Tu chatbot con Gemini está funcionando 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json["mensaje"]

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": mensaje}
                ]
            }
        ]
    }

    response = requests.post(url, json=data)

    respuesta = response.json()

    if "candidates" in respuesta:
    texto = respuesta["candidates"][0]["content"]["parts"][0]["text"]
else:
    texto = str(respuesta)

    return jsonify({"respuesta": texto})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
if __name__ == "__main__":
    import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
