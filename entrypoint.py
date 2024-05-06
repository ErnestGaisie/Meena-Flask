from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and methods

# ENTRY ENDPOINT


@app.route('/')
def hello_world():
    return 'Hello, World!'


# GETTING STATIC DATA
@app.route('/get-static-image/<image_url>', methods=['GET'])
def get_static_image(image_url):
    # Define the image URL
    first_image_url = "http://example.com/path/to/your/image.jpg"
    second_image_url = "http://example.com/path/to/your/image.jpg"

    # Create a response object, including the image URL, a message, and a status code
    response = {
        'status': 'success',
        'message': 'Image retrieved successfully.',
        'image_url': first_image_url
    }

    # Return the response as JSON with a 200 OK status code
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
