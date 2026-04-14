from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from google import genai

app = Flask(__name__)
CORS(app)

# Crear cliente Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return "Tu chatbot con Gemini está funcionando 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "mensaje" not in data:
            return jsonify({"error": "Falta el campo 'mensaje'"}), 400

        mensaje = data["mensaje"]

        # 🔥 NUEVA FORMA (FUNCIONA SEGURO)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=mensaje
        )

        return jsonify({
            "respuesta": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
