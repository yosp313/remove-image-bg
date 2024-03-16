from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/image", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]

    if file.filename == "":
        return "No file selected", 400

    input_image = Image.open(file.stream)
    output_image = remove(input_image, post_process_mask=True)
    image_io = BytesIO()

    output_image.save(image_io, "PNG")
    image_io.seek(0)

    return send_file(
        image_io, mimetype="image/png", as_attachment=True, download_name="_rmbg.png"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
