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
    first_image_url = "First Image"
    second_image_url = "Second Image"

    if image_url == first_image_url:
        response = {
        'status': 'success',
        'message': 'Image retrieved successfully.',
        'image_url': "First Image"
    }
    elif image_url == second_image_url:
        response = {
        'status': 'success',
        'message': 'Image retrieved successfully.',
        'image_url': "Second Image"
    }
    else:
        # Create a response object, including the image URL, a message, and a status code
        response = {
            'status': 'success',
            'message': 'Image retrieved successfully.',
            'image_url': "AI Image"
        }

    # Return the response as JSON with a 200 OK status code
    return jsonify(response), 200






if __name__ == '__main__':
    app.run(debug=True)
