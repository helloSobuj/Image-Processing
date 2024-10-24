from PIL import Image
def compress_image(input_image_path, output_image_path, quality=60):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, optimize=True, quality=quality)
input_image = "input.jpg"
output_image = "optimized_image.jpg"
compress_image(input_image, output_image)
