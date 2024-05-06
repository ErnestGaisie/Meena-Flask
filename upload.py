import os
import firebase_admin
from firebase_admin import credentials, storage
from PIL import Image

# Path to your Firebase Admin SDK private key
cred_path = 'ritapp-384418-firebase-adminsdk-6ozsd-d4140b321e.json'

# Initialize the app with a service account
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ritapp-384418.appspot.com'
})

# Function to upload a file to Firebase Storage


def upload_image(image_path, file_name):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_filename(image_path)
    blob.make_public()
    # Returns the public URL
    return blob.public_url

def upload_image_file(image:Image,file_name):
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    # Create a temporary file to save the image
    temp_file_path = 'temp_image.png'
    image.save(temp_file_path)
    
    blob.upload_from_filename(temp_file_path)
    blob.make_public()

    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
    # Returns the public URL
    return blob.public_url


# Uncomment below for testing

# Path to the image you want to upload
# image_path = 'roomDecor.png'
# file_name = 'dalle/roomDecor2.jpg'  # Name and path in Firebase Storage

# # # Call the function to upload the image
# public_url = upload_image(image_path, file_name)
# print(f"Uploaded image accessible at {public_url}")
