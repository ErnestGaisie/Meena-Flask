
import vertexai
from vertexai.preview.vision_models import Image, ImageGenerationModel

# TODO(developer): Update and un-comment below lines
project_id = "elite-matter-421102"
input_file = "out-0.png"
mask_mode = "background"  # 'background', 'foreground', or 'semantic'
output_file = "my-output.png"
# The text prompt describing what you want to see inserted.
prompt = "Improve the quality"
mask_file = "download3.png"

# vertexai.init(project=project_id, location="us-central1")

# model = ImageGenerationModel.from_pretrained("imagegeneration@006")
# base_img = Image.load_from_file(location=input_file)

# images = model.edit_image(
#     base_image=base_img,
#     mask_mode=mask_mode,
#     prompt=prompt,
#     edit_mode="inpainting-insert",
# )

# images[0].save(location=output_file, include_generation_parameters=False)

# # Optional. View the edited image in a notebook.
# # images[0].show()

# print(f"Created output image using {len(images[0]._image_bytes)} bytes")


# ////////////////////////////////////////////////////////////


# vertexai.init(project=project_id, location="us-central1")

# model = ImageGenerationModel.from_pretrained("imagegeneration@006")
# base_img = Image.load_from_file(location=input_file)
# mask_img = Image.load_from_file(location=mask_file)

# images = model.edit_image(
#     base_image=base_img,
#     mask=mask_img,
#     prompt=prompt,
#     edit_mode="inpainting-insert",
# )

# images[0].save(location=output_file, include_generation_parameters=False)

# # Optional. View the edited image in a notebook.
# # images[0].show()

# print(f"Created output image using {len(images[0]._image_bytes)} bytes")


# //////////////////////////////////////////////////////////////
vertexai.init(project=project_id, location="us-central1")

model = ImageGenerationModel.from_pretrained("imagegeneration@002")
base_img = Image.load_from_file(location=input_file)

images = model.edit_image(
    base_image=base_img,
    prompt=prompt,
    # Optional parameters
    seed=1,
    # Controls the strength of the prompt.
    # -- 0-9 (low strength), 10-20 (medium strength), 21+ (high strength)
    guidance_scale=21,
    number_of_images=1,
)
# print(images)
images[0].save(location=output_file, include_generation_parameters=False)

# Optional. View the edited image in a notebook.
# images[0].show()

print(f"Created output image using {len(images[0]._image_bytes)} bytes")
