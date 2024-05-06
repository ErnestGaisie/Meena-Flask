from PIL import Image



def convertImage(image):
    grayscale_image = image.convert("RGBA")
    # grayscale_image.show()
    return grayscale_image


def resizeImage(image_path,w,h):
    image = Image.open(image_path)
    resized_image = image.resize((w,h))
    return resized_image



def resolveImage(image_path):
    img = resizeImage(image_path,1024,1024)
    value = convertImage(img)
    value.save(f"{image_path}_converted.png")


# resolveImage("sample.png")
# # It dey job

