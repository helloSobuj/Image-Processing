![Image](https://github.com/user-attachments/assets/fee1deca-99ee-41da-8309-136cdad0e57a)


**1. before run this project please open the terminal and run**

   `pip install Pillow`

**2. Replace Placeholders:**

- Update input_image with the path to your image file (e.g., C:/images/my_photo.jpg).
- Modify output_image to your preferred output filename (e.g., compressed_photo.jpg).

**3. Quality Adjustment:**

- The quality parameter in the compress_image function controls the compression level (1-95). Higher values result in larger file sizes and better image quality, while lower values produce smaller files with greater quality loss. Experiment to find the optimal balance for your needs.
- `compress_image(input_image, output_image, quality=80)  # Compress with 80% quality`


**Additional Notes:**

- This script currently works with JPEG images. For other formats, consider exploring Pillow's conversion capabilities.
- Be cautious with very low quality settings, as they can significantly degrade image quality.
