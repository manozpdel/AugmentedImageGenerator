import os
import cv2
import numpy as np
import random

def random_crop(image, crop_height, crop_width):
    """
    Randomly crop an image.
    
    Args:
    - image: Input image
    - crop_height: Height of the cropped region
    - crop_width: Width of the cropped region
    
    Returns:
    - cropped_image: Cropped image
    """
    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Generate random coordinates for cropping
    top = random.randint(0, max(0, height - crop_height))
    left = random.randint(0, max(0, width - crop_width))
    bottom = min(height, top + crop_height)
    right = min(width, left + crop_width)
    
    # Perform cropping
    cropped_image = image[top:bottom, left:right]
    
    return cropped_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store cropped images
output_directory = os.path.join(input_directory, "cropped_images")
os.makedirs(output_directory, exist_ok=True)

# Define crop dimensions
crop_height = 50
crop_width = 50

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Randomly crop the image
        cropped_image = random_crop(image, crop_height, crop_width)
        
        # Save the cropped image with appropriate name
        cropped_image_path = os.path.join(output_directory, "cropped_" + filename)
        cv2.imwrite(cropped_image_path, cropped_image)
