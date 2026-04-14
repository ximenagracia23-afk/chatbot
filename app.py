from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Chatbot funcionando con OpenAI 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "mensaje" not in data:
            return jsonify({"error": "Falta el campo 'mensaje'"}), 400

        mensaje = data["mensaje"]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": mensaje}
            ]
        )

        respuesta = response.choices[0].message.content

        return jsonify({
            "respuesta": respuesta
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
