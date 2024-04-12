from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Configuración de la URL base y el endpoint para la generación de imágenes
API_URL = "https://api.openai.com/v1/images/generations"


@app.route("/generate_image", methods=["POST"])
def generate_image():
    try:
        # Obtener el prompt del usuario desde el formulario
        text_prompt = request.form["text"]
        # Opciones adicionales pueden ser pasadas mediante formularios
        model = request.form.get("model", "dall-e-3")
        size = request.form.get("size", "1024x1024")
        quality = request.form.get("quality", "standard")
        style = request.form.get("style", "vivid")

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        }

        data = {
            "prompt": text_prompt,
            "model": model,
            "n": 1,
            "size": size,
            "quality": quality,
            "style": style,
        }

        response = requests.post(API_URL, headers=headers, json=data)

        if response.status_code == 200:
            image_data = response.json()
            return jsonify({"status": "success", "images": image_data["data"]}), 200
        else:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Failed to generate image",
                        "details": response.text,
                    }
                ),
                response.status_code,
            )

    except Exception as e:
        # return jsonify({"status": "error", "message": str(e)}), 500
        return jsonify({"status": "success", "images": image_data["data"]}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
