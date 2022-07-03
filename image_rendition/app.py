import io
from PIL import Image
from flask import Flask, jsonify, request, send_file


from flask import Flask, jsonify, request


app = Flask(__name__)


def convertImage(image, outputFormat):
    imageObject = Image.open(image)
    if imageObject.format != outputFormat:
        imageIO = io.BytesIO()
        imageObject.save(imageIO, outputFormat)
        imageIO.seek(0)
        return imageIO


@app.route('/rendition', methods=['POST'])
def get_file():
    image = request.files['image']
    convertedIO = convertImage(image, 'PNG')
    return send_file(convertedIO, mimetype='image/png')

app.run(port=5000)