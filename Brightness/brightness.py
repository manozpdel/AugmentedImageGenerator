import os
import cv2
import numpy as np

def adjust_brightness(image, brightness_factor):
    """
    Adjust the brightness of an image.
    
    Args:
    - image: Input image
    - brightness_factor: Factor to adjust brightness. 
                         1.0 indicates no change, 
                         less than 1.0 decreases brightness, 
                         greater than 1.0 increases brightness.
    
    Returns:
    - adjusted_image: Image with adjusted brightness
    """
    # Apply brightness adjustment
    adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
    
    return adjusted_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store adjusted brightness images
output_directory = os.path.join(input_directory, "adjusted_brightness_images")
os.makedirs(output_directory, exist_ok=True)

# Define the brightness factor
brightness_factor = 25  # Increase or decrease as needed (1.0 for no change)

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Adjust the brightness of the image
        adjusted_image = adjust_brightness(image, brightness_factor)
        
        # Save the adjusted brightness image with appropriate name
        adjusted_image_path = os.path.join(output_directory, "adjusted_brightness_" + filename)
        cv2.imwrite(adjusted_image_path, adjusted_image)
