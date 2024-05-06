import uuid
import requests
from PIL import Image
from io import BytesIO

class Util:

    def load_image_url(self,image_url):
        response = requests.get(image_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the image using PIL's Image module
            img = Image.open(BytesIO(response.content))
            
            # Now you can work with the image, for example, display it
            return img
        else:
            print("Failed to fetch the image. Status code:", response.status_code)


    
    def resolveImage(self,image):
        img = self._resizeImage(image,1024,1024)
        value = self._convertImage(img)
        # value.save(f"output_converted.png")
        return value


    ############### SUB METHODS  ###############
    def _convertImage(self,image):
        grayscale_image = image.convert("RGBA")
        # grayscale_image.show()
        return grayscale_image


    def _resizeImage(self,image,w,h):
        # image = Image.open(image_path)
        resized_image = image.resize((w,h))
        return resized_image
    ############################################

    def generate_random_image_path(base_path="dalle/", extension=".png"):
        random_filename = str(uuid.uuid4())  # Generates a random UUID
        return f"{base_path}{random_filename}{extension}"



