from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image
import io

app = Flask(__name__)
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

@app.route("/describe", methods=["POST"])
def describe():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400
            
        # Получаем файл и читаем как PIL Image
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400
            
        image = Image.open(io.BytesIO(file.read()))
        
        # Генерируем описание
        result = captioner(image)
        return jsonify({"description": result[0]["generated_text"]})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)