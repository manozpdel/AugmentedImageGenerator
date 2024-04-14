import os
import cv2
import numpy as np

def scale_image(image, scale_width=1.0, scale_height=1.0):
    """
    Scale an image by specified factors for width and height.
    
    Args:
    - image: Input image
    - scale_width: Scaling factor for the width (default is 1.0)
    - scale_height: Scaling factor for the height (default is 1.0)
    
    Returns:
    - scaled_image: Scaled image
    """
    # Get the dimensions of the image
    (height, width) = image.shape[:2]
    
    # Scale the width and height
    new_width = int(width * scale_width)
    new_height = int(height * scale_height)
    
    # Perform the scaling
    scaled_image = cv2.resize(image, (new_width, new_height))
    
    return scaled_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store scaled images
output_directory = os.path.join(input_directory, "scaled_images")
os.makedirs(output_directory, exist_ok=True)

# Define the scaling factors for width and height
scale_width = 1.2      # Use range 0.8 to 1.2 accroding to your wish
scale_height = 0.8     # Use range 0.8 to 1.2 accroding to your wish

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Scale the image
        scaled_image = scale_image(image, scale_width, scale_height)
        
        # Save the scaled image with appropriate name
        scaled_image_path = os.path.join(output_directory, "scaled-" + filename)
        cv2.imwrite(scaled_image_path, scaled_image)
