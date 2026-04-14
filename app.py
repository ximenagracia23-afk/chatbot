from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configurar API Key desde variables de entorno
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Ruta principal (para probar en el navegador)
@app.route("/")
def home():
    return "Tu chatbot con Gemini está funcionando 🚀"

# Ruta del chatbot
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        # Validar entrada
        if not data or "mensaje" not in data:
            return jsonify({"error": "Falta el campo 'mensaje'"}), 400

        mensaje = data["mensaje"]

        # Modelo de Gemini
        model = genai.GenerativeModel("gemini-pro")

        # Generar respuesta
        response = model.generate_content(mensaje)

        return jsonify({
            "respuesta": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# Puerto para Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
