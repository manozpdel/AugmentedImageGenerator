import os
import cv2

def flip_image(image, flip_code):
    """
    Flip an image.
    
    Args:
    - image: Input image
    - flip_code: Flip code to specify the direction of flipping:
                 0 for flipping around the x-axis (vertical flip)
                 >0 for flipping around the y-axis (horizontal flip)
                 <0 for flipping around both axes (horizontal and vertical flip)
    
    Returns:
    - flipped_image: Flipped image
    """
    # Perform the flipping
    flipped_image = cv2.flip(image, flip_code)
    
    return flipped_image

# Path to the directory containing images
input_directory = "cats/"
# Create a directory to store flipped images
output_directory = os.path.join(input_directory, "flipped_images")
os.makedirs(output_directory, exist_ok=True)

# Define flip code: 0 for vertical flip, 1 for horizontal flip
flip_code = 1

# Iterate over all the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Assuming images are PNG or JPG format
        # Load the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)
        
        # Flip the image
        flipped_image = flip_image(image, flip_code)
        
        # Save the flipped image with appropriate name
        flipped_image_path = os.path.join(output_directory, "flipped_" + filename)
        cv2.imwrite(flipped_image_path, flipped_image)
