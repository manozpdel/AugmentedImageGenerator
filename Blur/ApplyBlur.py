import os
import cv2

def apply_blur(image, kernel_size):
    """
    Apply Gaussian blur to an image.
    
    Args:
    - image: Input image
    - kernel_size: Size of the Gaussian kernel
    
    Returns:
    - blurred_image: Image with Gaussian blur applied
    """
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    return blurred_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store blurred images
output_directory = os.path.join(input_directory, "blurred_images")
os.makedirs(output_directory, exist_ok=True)

# Define the size of the Gaussian kernel for blur
kernel_size = 3

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Apply blur to the image
        blurred_image = apply_blur(image, kernel_size)
        
        # Save the blurred image with appropriate name
        blurred_image_path = os.path.join(output_directory, "blurred_" + filename)
        cv2.imwrite(blurred_image_path, blurred_image)
