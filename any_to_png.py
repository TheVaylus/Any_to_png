import os
import imghdr
from PIL import Image

def convert_to_png(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and imghdr.what(input_path):
            # Open the image using Pillow
            image = Image.open(input_path)

            # Construct the output path with a .png extension
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

            # Convert and save the image as PNG
            image.save(output_path, 'PNG')

            print(f"Converted {filename} to PNG")

    print("Conversion completed.")

#define the path of the input and output folders
input_folder = 'images'
output_folder = 'png'
convert_to_png(input_folder, output_folder)
