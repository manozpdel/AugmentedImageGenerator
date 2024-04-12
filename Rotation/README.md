## Image Rotation Script

This Python script facilitates image rotation by a specified angle using the OpenCV library. 

### Description:
The script defines a function `rotate_image(image, angle)` designed to rotate images. It traverses a directory containing images (PNG or JPG format), applies the specified rotation angle to each image, and stores the rotated images in an output directory.

### Usage:
1. Insert the images to be rotated into the designated input directory (`cats/` in this script).
2. Execute the script. It establishes a directory called `rotated_images` within the input directory (if it does not exist), and it saves the rotated images there.
3. You can tailor the rotation angle by adjusting the `rotation_angle` variable in the script. The default rotation angle is set to 10 degrees.

### Requirements:
- Python 3.x
- OpenCV library (`cv2`)
- NumPy library (`numpy`)

### Example:
```python
# Define the angle by which you want to rotate the images
rotation_angle = 10  # Adjust as per your requirement from -10 to 10 degree
```

### Note:
- Ensure the input directory contains images in PNG or JPG format.
- The script overwrites existing files with the same name in the output directory.

Feel free to customize the script to suit your specific needs.

