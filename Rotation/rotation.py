import os
import cv2
import numpy as np

def rotate_image(image, angle):
    """
    Rotate an image by a specified angle.
    
    Args:
    - image: Input image
    - angle: Angle (in degrees) by which to rotate the image
    
    Returns:
    - rotated_image: Rotated image
    """
    # Get the dimensions of the image
    (height, width) = image.shape[:2]
    # Calculate the center of the image
    center = (width / 2, height / 2)
    # Perform the rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    return rotated_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store rotated images
output_directory = os.path.join(input_directory, "rotated_images")
os.makedirs(output_directory, exist_ok=True)

# Define the angle by which you want to rotate the images
rotation_angle = 10  # Change this angle as per your requirement

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Rotate the image
        rotated_image = rotate_image(image, rotation_angle)
        
        # Save the rotated image with appropriate name
        rotated_image_path = os.path.join(output_directory, "rotated-" + filename)
        cv2.imwrite(rotated_image_path, rotated_image)
