"""
	•	Description: Overlays a transparent shirt image on an input image and saves the result.
	•	Usage:
	•	Input: An image file (JPG or PNG) to be overlaid.
	•	Output: An image file (JPG or PNG) with the shirt overlay applied.
	•	Requirements:
	•	The shirt.png overlay file must be in the same directory as the script.
"""

import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for exactly two command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check file extensions and validate that they match
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()
    valid_extensions = {".jpg", ".jpeg", ".png"}

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Error: Input and output files must be .jpg, .jpeg, or .png")
        sys.exit(1)
    
    if input_ext != output_ext:
        print("Error: Input and output files must have the same extension")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.isfile(input_path):
        print(f"Error: The file {input_path} does not exist.")
        sys.exit(1)

    try:
        # Open the shirt overlay image
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size

        # Open the input image and resize/crop it to match the shirt size
        with Image.open(input_path) as input_image:
            input_image = ImageOps.fit(input_image, shirt_size)

            # Overlay the shirt image on top of the resized input image
            input_image.paste(shirt, (0, 0), shirt)

            # Save the result to the output file
            input_image.save(output_path)
            print(f"Image saved as {output_path}")

    except FileNotFoundError:
        print("Error: shirt.png not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()