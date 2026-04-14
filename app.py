from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configurar API Key desde Render
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return "Tu chatbot con Gemini está funcionando 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        mensaje = data.get("mensaje")

        if not mensaje:
            return jsonify({"respuesta": "No enviaste mensaje"})

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(mensaje)

        return jsonify({"respuesta": response.text})

    except Exception as e:
        return jsonify({"respuesta": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
