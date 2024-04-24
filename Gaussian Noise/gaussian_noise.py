import os
import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, stddev=25):
    """
    Add Gaussian noise to an image.
    
    Args:
    - image: Input image
    - mean: Mean of the Gaussian distribution (default is 0)
    - stddev: Standard deviation of the Gaussian distribution (default is 25)
    
    Returns:
    - noisy_image: Image with added Gaussian noise
    """
    # Generate Gaussian noise matrix
    noise = np.zeros(image.shape, np.uint8)
    cv2.randn(noise, mean, stddev)
    
    # Add noise to the image
    noisy_image = cv2.add(image, noise)
    
    return noisy_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store noisy images
output_directory = os.path.join(input_directory, "noisy_images")
os.makedirs(output_directory, exist_ok=True)

# Define parameters for Gaussian noise
mean = 0
stddev = 50

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Add Gaussian noise to the image
        noisy_image = add_gaussian_noise(image, mean, stddev)
        
        # Save the noisy image with appropriate name
        noisy_image_path = os.path.join(output_directory, "noisy_" + filename)
        cv2.imwrite(noisy_image_path, noisy_image)
