import os
import cv2
import numpy as np

def shear_image(image, shear_factor_x=0.2, shear_factor_y=0):
    """
    Shear an image.
    
    Args:
    - image: Input image
    - shear_factor_x: Shearing factor along the x-axis (default is 0.2)
    - shear_factor_y: Shearing factor along the y-axis (default is 0)
    
    Returns:
    - sheared_image: Sheared image
    """
    # Define the transformation matrix
    shear_matrix = np.array([[1, shear_factor_x, 0],
                             [shear_factor_y, 1, 0]])

    # Apply the shearing transformation
    sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
    
    return sheared_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store sheared images
output_directory = os.path.join(input_directory, "sheared_images")
os.makedirs(output_directory, exist_ok=True)

# Define shearing factors
shear_factor_x = 0.2
shear_factor_y = 0.1

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Shear the image
        sheared_image = shear_image(image, shear_factor_x, shear_factor_y)
        
        # Save the sheared image with appropriate name
        sheared_image_path = os.path.join(output_directory, "sheared_" + filename)
        cv2.imwrite(sheared_image_path, sheared_image)
