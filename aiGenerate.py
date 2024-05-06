import replicate
import urllib.request
import os
from PIL import Image, ImageDraw
import upload
import base64



class AIGenerate:


    def create_mask(self,image_size, mask_coords):
        mask = Image.new('L', image_size, 0)  # Create a blank mask image
        draw = ImageDraw.Draw(mask)
        draw.rectangle(mask_coords, fill=255)  # Draw a white rectangle on the mask
        return mask

    def create_sub_mask(self,mask_coords,image):
        mask = image
        draw = ImageDraw.Draw(mask)
        draw.rectangle(mask_coords, fill=255)  # Draw a white rectangle on the mask
        return mask


    def generate_image_from_image(self,image):
        # Load the empty room image
        imagePath = "empty_room.png"

        
        room_image = image
        room_image_size = room_image.size


        # Define the coordinates for the mask area
        # Adjust these values to specify the area where you want to insert furniture
        mask_coords = (100, 100, 1800, 1800)

        # Create the mask image
        mask_image = self.create_mask(room_image_size,mask_coords)

        # Encode the room image and mask image as Base64 strings
        room_image_bytes = room_image.tobytes()
        room_image_base64 = base64.b64encode(room_image_bytes).decode('utf-8')

        mask_image_bytes = mask_image.tobytes()
        mask_image_base64 = base64.b64encode(mask_image_bytes).decode('utf-8')

        print("Mask image size:", mask_image.size)
        print(room_image_size)

        mask = Image.frombytes('L', room_image_size, mask_image_bytes)  # Adjust the size as needed
        mask.save("mask.png")


        # # Upload Image or use uploaded url for speed and tests
        room_url = upload.upload_image_file(image,"dalle/imagePath")
        mask_url = upload.upload_image("mask.png","dalle/mask_image")

        print(room_url)
        print(mask_url)

        # room_url = "https://storage.googleapis.com/ritapp-384418.appspot.com/dalle/imagePath"
        # mask_url = "https://storage.googleapis.com/ritapp-384418.appspot.com/dalle/mask_image"


        print("\n\n done \n\n")

        input = {
            "image": room_url,
            "mask": mask_url,
            "prompt": "Imagine a spacious living room during the golden hour. The room features a neutral color palette with white walls, a large, soft gray sectional sofa adorned with pastel-colored cushions, and sleek black coffee table. On the walls, abstract art pieces in gold and blue tones complement the natural wooden floor.Leaving the windows as they are",
            "num_inference_steps": 80,
            "negative_prompt":"bad anatomy, worst quality, low quality,modified windows"
        }

        output = replicate.run(
            "stability-ai/stable-diffusion-inpainting:95b7223104132402a9ae91cc677285bc5eb997834bd2349fa486f53910fd68b3",
            input=input
        )

        # Save the output image
        output_image = output[0]
        return output_image
