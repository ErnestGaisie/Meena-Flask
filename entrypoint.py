from flask import Flask, jsonify,request
from flask_cors import CORS
import util
import aiGenerate
from PIL import Image

utility = util.Util()

ai = aiGenerate.AIGenerate()

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and methods

# ENTRY ENDPOINT


@app.route('/')
def hello_world():
    return 'Hello, World!'


# UPLOAD IMAGE
# @app.route('/upload', methods=['POST'])
def upload_image():
    # Get the image file from the request
    image_file = request.files['image']

    # Save the image to a file
    image_file.save('uploaded_image.jpg')

    return 'Image uploaded successfully'


# GETTING STATIC DATA
@app.route('/get-static-image/<prompt>', methods=['GET','POST'])
def get_static_image(prompt):
    # Define the image URL
    first_image_url = "First Image"
    second_image_url = "Second Image"

    if prompt == first_image_url:
        response = {
        'status': 'success',
        'message': 'Image retrieved successfully.',
        'image_url': "First Image"
    }
    elif prompt == second_image_url:
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



@app.route("/generate-ai-room",methods = ['GET','POST'])
def generate_image():

    if request.method == 'POST':
        # Get the image file from the request
        image_file = request.files['image']

    #Open Image file
    img = Image.open(image_file)

    

    #preprocess image
    resolved_image = utility.resolveImage(img)
    #generate ai image
    ai_generated = ai.generate_image_from_image(resolved_image)
    #clean up with vertex
    #upload final image
    #return string
    response = {
            'status': 'success',
            'message': 'Image retrieved successfully.',
            'image_url': ai_generated
        }
    
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
