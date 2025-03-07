from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__, static_folder="static")
CORS(app)

genai.configure(api_key="AIzaSyACrTOIcxhvw9HGWwJSgJXRbWmnoMSDlZs") ##<< Ganti pakai API GEMINI

@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")  # Menyajikan halaman utama

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("prompt", "")

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(user_input)

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
