import os
import cv2

def apply_histogram_equalization(image):
    """
    Apply histogram equalization to an image.
    
    Args:
    - image: Input image
    
    Returns:
    - equalized_image: Image with histogram equalization applied
    """
    # Convert image to grayscale if it's in color
    if len(image.shape) > 2:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)
    
    return equalized_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store equalized images
output_directory = os.path.join(input_directory, "equalized_images")
os.makedirs(output_directory, exist_ok=True)

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Apply histogram equalization to the image
        equalized_image = apply_histogram_equalization(image)
        
        # Save the equalized image with appropriate name
        equalized_image_path = os.path.join(output_directory, "equalized_" + filename)
        cv2.imwrite(equalized_image_path, equalized_image)
